# air-claw

An autonomous research assistant system powered by Docker, Python, and AI agents.

## Overview

air-claw is a development project designed to create an autonomous research assistant system. It leverages Docker containers for service isolation, Python for backend logic, and integrates various AI agents and knowledge management systems to provide intelligent research capabilities.

## Project Structure

```
air-claw/
├── .gitignore
├── .vscode/
├── cognify_init.py
├── CONTRIBUTING.md
├── docker-compose.yml
├── requirements.txt
├── README.md
├── docs/
│   ├── features.md
│   ├── index.md
│   ├── roadmap.md
│   └── setup.md
├── plans/
│   ├── DETAILED_IMPLEMENTATION_PLAN.md
│   ├── PLAN_PHASE1.md
│   ├── PLAN_PHASE2.md
│   ├── PLANS_AND_SPECS_PROPOSAL.md
│   └── README.md
├── specs/
│   ├── AGENT_COORDINATION.md
│   ├── API.md
│   ├── ARCHITECTURAL_DESIGN.md
│   ├── DATA_MODEL.md
│   ├── MCP_INTEGRATION.md
│   └── README.md
└── tests/
    ├── run_tests.py
    ├── test_cognify_init.py
    ├── test_verify_openhands.py
    └── verify_openhands.py
```

## Technologies Used

- **Docker & Docker Compose**: Container orchestration for services
- **Python 3.8+**: Core programming language
- **PostgreSQL with pgvector**: Database for vector storage and retrieval
- **Cognee**: Knowledge management and MCP integration
- **Onyx**: Backend service
- **OpenHands**: AI agent framework
- **Various Python packages**: As listed in `requirements.txt`

## Setup Instructions

Follow these steps to set up the air-claw development environment:

### Prerequisites

Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [Git](https://git-scm.com/downloads)
- [VS Code](https://code.visualstudio.com/) (optional, but recommended for MCP integration)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd air-claw
```

### Step 2: Set Up the Environment

#### Create a Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Example .env file
GITHUB_TOKEN=your_github_personal_access_token
OPENAI_API_KEY=your_openai_api_key  # If using OpenAI models
# Add any other required API keys or configuration
```

> **Note**: The `.env` file is already in `.gitignore` to keep your secrets safe.

### Step 3: Set Up Directory Structure

The system expects the following directories to exist:
- `src/` - for source code
- `papers/` - for academic/research documents

These directories are created during the bootstrap process, but you can create them manually if needed:

```bash
mkdir -p src papers
```

### Step 4: Configure Docker Compose

Review the `docker-compose.yml` file to ensure the ports and configurations are suitable for your environment.

### Step 5: Start the Services

Use Docker Compose to start all required services:

```bash
docker-compose up -d
```

This will start:
- **Onyx** on port 8000
- **Cognee** on port 8001 (with MCP endpoint at http://localhost:8001/mcp)
- **OpenHands** on port 3000
- **PostgreSQL with pgvector** on port 5432

You can check the status of the services with:

```bash
docker-compose ps
```

### Step 6: Run Bootstrap Scripts

#### Initialize the Cognee Knowledge Base

The `cognify_init.py` script triggers the Entity-Contrast-Learning (ECL) pipeline on the `src/` and `papers/` directories.

```bash
python cognify_init.py
```

#### Verify OpenHands Connectivity

The `verify_openhands.py` script checks that the OpenHands service is reachable and responding.

```bash
python verify_openhands.py
```

### Step 7: Configure VS Code MCP Integration (Optional)

If you are using VS Code, the `.vscode/mcp_config.json` file is already configured to connect to the Cognee-MCP server at `http://localhost:8001/mcp`.

You may need to install the appropriate MCP extension in VS Code to use this feature.

### Step 8: Running Tests

To run the test suite for bootstrap validation:

```bash
python tests/run_tests.py
```

## How to Contribute

We welcome contributions from the community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for detailed information on how to contribute to air-claw.

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Any relevant logs or error messages
- Information about your environment (OS, Python version, etc.)

### Suggesting Features

Feature requests are welcome! Please open an issue to discuss your idea before starting work.

### Contributing Code

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a branch for your changes
4. Make your changes in your branch
5. Run tests to ensure your changes don't break existing functionality
6. Commit your changes with a clear and descriptive commit message
7. Push your branch to your fork
8. Open a pull request against the `main` branch

## Documentation

Additional documentation can be found in the `docs/` directory:
- [Setup Guide](docs/setup.md) - Detailed setup instructions
- [Features](docs/features.md) - Planned and implemented features
- [Roadmap](docs/roadmap.md) - Future development plans
- [Index](docs/index.md) - Documentation overview

Technical specifications are available in the `specs/` directory:
- [Architectural Design](specs/ARCHITECTURAL_DESIGN.md)
- [API Specifications](specs/API.md)
- [Data Models](specs/DATA_MODEL.md)
- [Agent Coordination](specs/AGENT_COORDINATION.md)
- [MCP Integration](specs/MCP_INTEGRATION.md)

Implementation plans are available in the `plans/` directory:
- [Phase 1 Plan](plans/PLAN_PHASE1.md)
- [Phase 2 Plan](plans/PLAN_PHASE2.md)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to all contributors who have helped shape air-claw.