# Setup Guide for SciCode-Nexus

This guide will help you set up the SciCode-Nexus system on your local machine for development and testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [Git](https://git-scm.com/downloads)
- [VS Code](https://code.visualstudio.com/) (optional, but recommended for MCP integration)

## Step 1: Clone the Repository

```bash
git clone https://github.com/ndjones/scicode-nexus.git
cd scicode-nexus
```

## Step 2: Set Up the Environment

### Create a Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory with the following variables (you can copy from `.env.example` if provided):

```env
# Example .env file
GITHUB_TOKEN=your_github_personal_access_token
OPENAI_API_KEY=your_openai_api_key  # If using OpenAI models
# Add any other required API keys or configuration
```

> **Note**: The `.env` file is already in `.gitignore` to keep your secrets safe.

## Step 3: Set Up Directory Structure

The system expects the following directories to exist:
- `src/` - for source code
- `papers/` - for academic/research documents

These directories are created during the bootstrap process, but you can create them manually if needed:

```bash
mkdir -p src papers
```

## Step 4: Configure Docker Compose

The `docker-compose.yml` file defines the services for the system. Review it to ensure the ports and configurations are suitable for your environment.

## Step 5: Start the Services

Use Docker Compose to start all required services:

```bash
docker-compose up -d
```

This will start:
- **Onyx** on port 8000
- **Cognee** on port 8001 (with MCP endpoint at http://localhost:8001/mcp)
- **OpenHands** on port 8080
- **PostgreSQL with pgvector** on port 5432

You can check the status of the services with:

```bash
docker-compose ps
```

## Step 6: Run Bootstrap Scripts

### Initialize the Cognee Knowledge Base

The `cognify_init.py` script triggers the Entity-Contrast-Learning (ECL) pipeline on the `src/` and `papers/` directories.

```bash
python cognify_init.py
```

### Verify OpenHands Connectivity

The `verify_openhands.py` script checks that the OpenHands service is reachable and responding.

```bash
python verify_openhands.py
```

## Step 7: Configure VS Code MCP Integration (Optional)

If you are using VS Code, the `.vscode/mcp_config.json` file is already configured to connect to the Cognee-MCP server at `http://localhost:8001/mcp`.

You may need to install the appropriate MCP extension in VS Code to use this feature.

## Step 8: Running Tests

To run the test suite for bootstrap validation:

```bash
python tests/run_tests.py
```

## Troubleshooting

### Common Issues

1. **Docker services not starting**
   - Check Docker is running and you have sufficient resources.
   - Look at the logs: `docker-compose logs [service-name]`

2. **Python import errors**
   - Ensure you are in the virtual environment and dependencies are installed.

3. **Connection refused errors**
   - Verify the services are up and running on the expected ports.
   - Check firewall settings.

4. **Permission issues**
   - On Linux, you might need to use `sudo` for Docker commands or add your user to the docker group.

## Getting Help

If you encounter issues not covered in this guide, please:
- Check the existing GitHub issues
- Open a new issue with detailed information about the problem
- Reach out to the maintainers

## Next Steps

After setting up, you can:
- Explore the Phase 2 design document ([PLAN_PHASE2.md](./PLAN_PHASE2.md)) for planned features.
- Look at the test files in the `tests/` directory to understand how the system is validated.
- Begin contributing by following the [Contributing Guidelines](contributing.md).

Happy coding!