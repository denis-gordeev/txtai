"""
Client module
"""

import time

# Conditional import
try:
    from sqlalchemy import StaticPool, Text, cast, create_engine, insert, text as textsql
    from sqlalchemy.orm import Session, aliased

    from .schema import Base, Batch, Document, Object, Section, SectionBase, Score

    ORM = True
except ImportError:
    ORM = False

from .rdbms import RDBMS


class Client(RDBMS):
    """
    Database client instance. This class connects to an external database using SQLAlchemy. It supports any database
    that is supported by SQLAlchemy (PostgreSQL, MariaDB, etc) and has JSON support.
    """

    def __init__(self, config):
        """
        Creates a new Database.

        Args:
            config: database configuration parameters
        """

        super().__init__(config)

        if not ORM:
            raise ImportError('SQLAlchemy is not available - install "database" extra to enable')

    def reindexstart(self):
        # Working table name
        name = f"rebuild{round(time.time() * 1000)}"

        # Create working table metadata
        type("Rebuild", (SectionBase,), {"__tablename__": name})
        Base.metadata.tables[name].create(self.connection.bind)

        return name

    def reindexend(self, name):
        # Remove table object from metadata
        Base.metadata.remove(Base.metadata.tables[name])

    def jsonprefix(self):
        # JSON column prefix
        return "cast("

    def jsoncolumn(self, name):
        # Alias documents table
        d = aliased(Document, name="d")

        # Build JSON column expression for column
        return str(cast(d.data[name], Text).compile(dialect=self.connection.bind.dialect, compile_kwargs={"literal_binds": True}))

    def createtables(self):
        # Create tables
        Base.metadata.create_all(self.connection.bind)

        # Clear existing data - table schema is created upon connecting to database
        for table in ["sections", "documents", "objects"]:
            self.cursor.execute(f"DELETE FROM {table}")

    def finalize(self):
        # Flush cached objects
        self.connection.flush()

    def insertdocument(self, uid, data, tags, entry):
        self.connection.add(Document(id=uid, data=data, tags=tags, entry=entry))

    def insertobject(self, uid, data, tags, entry):
        self.connection.add(Object(id=uid, object=data, tags=tags, entry=entry))

    def insertsection(self, index, uid, text, tags, entry):
        # Save text section
        self.connection.add(Section(indexid=index, id=uid, text=text, tags=tags, entry=entry))

    def createbatch(self):
        # Create temporary batch table, if necessary
        Base.metadata.tables["batch"].create(self.connection.bind, checkfirst=True)

    def insertbatch(self, indexids, ids, batch):
        if indexids:
            self.connection.execute(insert(Batch), [{"indexid": i, "batch": batch} for i in indexids])
        if ids:
            self.connection.execute(insert(Batch), [{"id": str(uid), "batch": batch} for uid in ids])

    def createscores(self):
        # Create temporary scores table, if necessary
        Base.metadata.tables["scores"].create(self.connection.bind, checkfirst=True)

    def insertscores(self, scores):
        # Average scores by id
        self.connection.execute(insert(Score), [{"indexid": i, "score": sum(s) / len(s)} for i, s in scores.items()])

    def connect(self, path=None):
        # Create engine using database URL
        engine = create_engine(self.config["content"], poolclass=StaticPool, echo=False)

        # Create database session
        return Session(engine)

    def getcursor(self):
        return Cursor(self.connection)

    def rows(self):
        return self.cursor

    def addfunctions(self):
        return


class Cursor:
    """
    Implements basic compatability with the Python DB-API.
    """

    def __init__(self, connection):
        self.connection = connection
        self.result = None

    def __iter__(self):
        return self.result

    def execute(self, statement):
        """
        Executes statement.

        Args:
            statement: statement to execute
        """

        if isinstance(statement, str):
            statement = textsql(statement)

        self.result = self.connection.execute(statement)

    def fetchall(self):
        """
        Fetches all rows from the current result.

        Returns:
            all rows from current result
        """

        return self.result.all() if self.result else None

    def fetchone(self):
        """
        Fetches first row from current result.

        Returns:
            first row from current result
        """

        return self.result.first() if self.result else None

    @property
    def description(self):
        """
        Returns columns for current result.

        Returns:
            list of columns
        """

        return [(key,) for key in self.result.keys()] if self.result else None
