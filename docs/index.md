# SciCode-Nexus

SciCode-Nexus is an autonomous research assistant system that integrates multiple AI agents and knowledge management tools to facilitate scientific discovery and code development.

## Overview

The system combines:
- **Cognee**: A knowledge management system for Entity-Contrast-Learning (ECL) pipeline
- **OpenHands**: An autonomous AI agent for code development and task execution
- **Onyx**: A search and indexing service for enhanced information retrieval
- **Custom orchestration scripts** for bootstrap and verification

## Key Components

1. **Bootstrap Scripts**
   - `cognify_init.py`: Triggers ECL pipeline on source and paper directories
   - `verify_openhands.py`: Verifies connectivity to OpenHands API

2. **Services** (orchestrated via Docker Compose)
   - **Onyx**: Search and indexing service (port 8000)
   - **Cognee**: Knowledge management service with MCP endpoint (port 8001)
   - **OpenHands**: Autonomous AI agent service (port 8080)
   - **Database**: PostgreSQL with pgvector extension (port 5432)

3. **Development Tools**
   - VSCode MCP configuration for Cognee integration
   - Test suite for bootstrap validation
   - GitHub Actions CI/CD pipeline (planned)

## Getting Started

See [Setup Guide](setup.md) for installation and configuration instructions.

## Contributing

See [Contributing Guidelines](contributing.md) for information on how to contribute to the project.

## Features

See [Features Overview](features.md) for current capabilities.

## Roadmap

See [Roadmap](roadmap.md) for planned enhancements and future work.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Cognee](https://github.com/cognee-labs/cognee)
- Powered by [OpenHands](https://github.com/All-Hands-AI/OpenHands)
- Search capabilities via [Onyx](https://github.com/onyx-ai/onyx)