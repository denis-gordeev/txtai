#

<p align="center">
    <img src="https://raw.githubusercontent.com/neuml/txtai/master/logo.png"/>
</p>

<p align="center">
    <b>All-in-one embeddings database</b>
</p>

<p align="center">
    <a href="https://github.com/neuml/txtai/releases">
        <img src="https://img.shields.io/github/release/neuml/txtai.svg?style=flat&color=success" alt="Version"/>
    </a>
    <a href="https://github.com/neuml/txtai">
        <img src="https://img.shields.io/github/last-commit/neuml/txtai.svg?style=flat&color=blue" alt="GitHub last commit"/>
    </a>
    <a href="https://github.com/neuml/txtai/issues">
        <img src="https://img.shields.io/github/issues/neuml/txtai.svg?style=flat&color=success" alt="GitHub issues"/>
    </a>
    <a href="https://join.slack.com/t/txtai/shared_invite/zt-1cagya4yf-DQeuZbd~aMwH5pckBU4vPg">
        <img src="https://img.shields.io/badge/slack-join-blue?style=flat&logo=slack&logocolor=white" alt="Join Slack"/>
    </a>
    <a href="https://github.com/neuml/txtai/actions?query=workflow%3Abuild">
        <img src="https://github.com/neuml/txtai/workflows/build/badge.svg" alt="Build Status"/>
    </a>
    <a href="https://coveralls.io/github/neuml/txtai?branch=master">
        <img src="https://img.shields.io/coverallsCoverage/github/neuml/txtai" alt="Coverage Status">
    </a>
</p>

txtai is an all-in-one embeddings database for semantic search, LLM orchestration and language model workflows.

![architecture](images/architecture.png#gh-light-mode-only)
![architecture](images/architecture-dark.png#gh-dark-mode-only)

Embeddings databases are a union of vector indexes (sparse and dense), graph networks and relational databases. This enables vector search with SQL, topic modeling, retrieval augmented generation and more.

Embeddings databases can stand on their own and/or serve as a powerful knowledge source for large language model (LLM) prompts.

Summary of txtai features:

- 🔎 Vector search with SQL, object storage, topic modeling, graph analysis and multimodal indexing
- 📄 Create embeddings for text, documents, audio, images and video
- 💡 Pipelines powered by language models that run LLM prompts, question-answering, labeling, transcription, translation, summarization and more
- ↪️️ Workflows to join pipelines together and aggregate business logic. txtai processes can be simple microservices or multi-model workflows.
- ⚙️ Build with Python or YAML. API bindings available for [JavaScript](https://github.com/neuml/txtai.js), [Java](https://github.com/neuml/txtai.java), [Rust](https://github.com/neuml/txtai.rs) and [Go](https://github.com/neuml/txtai.go).
- ☁️ Run local or scale out with container orchestration

txtai is built with Python 3.8+, [Hugging Face Transformers](https://github.com/huggingface/transformers), [Sentence Transformers](https://github.com/UKPLab/sentence-transformers) and [FastAPI](https://github.com/tiangolo/fastapi). txtai is open-source under an Apache 2.0 license.
