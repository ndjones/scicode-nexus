# Phase 2: The Collaborator (The Hands) - Design Document

## Overview
This document outlines the design for Phase 2 of the SciCode-Nexus project, focusing on integrating OpenHands with Cognee-MCP for self-building capabilities. The goal is to establish a test-driven approach with Git workflow integration, enabling OpenHands to autonomously improve the system through self-building tasks.

## 1. Git Workflow Strategy

### Repository Setup
- Create GitHub repository: `scicode-nexus` (placeholder or user-created)
- Set up remote origin: `git remote add origin https://github.com/username/scicode-nexus.git`
- Push initial commit: `git push -u origin main`

### Branching Strategy
- **Main Branch**: Production-ready code only
- **Develop Branch**: Integration branch for features
- **Feature Branches**: `feature/short-description` for new features
- **Task Branches**: `task/openhands-task-id` for OpenHands-generated tasks
- **Hotfix Branches**: `hotfix/description` for urgent fixes

### Pull Request Workflow
1. Create feature branch from `develop`
2. Implement changes with tests
3. Run test suite locally
4. **Validate git status**: Ensure all changes are accounted for, no unintended modifications
5. Commit changes with descriptive message
6. Push branch and open PR against `develop`
7. Require at least one approval
8. Squash and merge into `develop`
9. Regularly merge `develop` into `main` for releases

### Git Validation Practices
- Before committing: Run `git status` to review changes
- Use `git diff` to review modifications before staging
- Ensure `.gitignore` is properly configured to exclude unnecessary files
- Validate that only intended files are staged for commit
- After pushing: Verify that the remote repository reflects the latest changes

### GitHub Actions (Future)
- CI pipeline on PRs to `develop` and `main`
- Automated testing on push
- Docker image building and pushing

## 2. Test-Driven Development Approach

### Test Philosophy
- Write tests before implementation (Red-Green-Refactor)
- Focus on bootstrap artifacts first
- Ensure services start correctly
- Validate script functionality
- Test OpenHands-Cognee-MCP integration

### Test Categories

#### Bootstrap Validation Tests
1. **Dependency Installation Test**
   - Verify `pip install -r requirements.txt` succeeds
   - Check all required packages are installed

2. **Docker Services Test**
   - Verify `docker-compose up -d` starts all services
   - Check health of onyx, cognee, openhands, and db services
   - Validate port exposures (8000, 8001, 8080, 5432)

3. **Cognify Initialization Test**
   - Test `cognify_init.py` runs successfully after deps installed
   - Verify ECL pipeline completes on /src and /papers directories
   - Check for proper error handling when directories missing

4. **OpenHands Connectivity Test**
   - Test `verify_openhands.py` connects to localhost:8080
   - Validate response status code 200
   - Test timeout and connection error handling

#### OpenHands Task Tests
1. **Unit Test Generation**
   - Generated tests for bootstrap scripts achieve >80% coverage
   - Tests pass in CI environment

2. **Documentation Quality**
   - README.md includes setup, usage, and architecture sections
   - Documentation builds without errors (if using static site generator)

3. **Onyx Connector Configuration**
   - Slack and GitHub connector configs are valid
   - Connectors can be imported without syntax errors

4. **Docker Compose Improvements**
   - Health checks added for all services
   - Resource limits defined
   - Logging configurations optimized

### Test Implementation
- Use pytest for Python testing
- Use docker-py or subprocess for Docker service tests
- Use requests library for API testing
- Tests located in `tests/` directory
- Test runner script: `run_tests.py`

## 3. OpenHands-Cognee-MCP Integration Details

### Current Configuration
- MCP server configured in `.vscode/mcp_config.json`
- Points to `http://localhost:8001/mcp` (Cognee service)
- Type: HTTP transport

### Integration Mechanism
1. **Context Retrieval**
   - OpenHands agents query Cognee-MCP for project context
   - Queries include: code structure, documentation, recent changes
   - Uses standard MCP protocol over HTTP

2. **Knowledge Storage**
   - OpenHands stores learned patterns in Cognee
   - Entity-Contrast-Learning pipeline improves context over time
   - Enables cumulative learning across sessions

3. **MCP Client Integration**
   - OpenHands extended with MCP client capability
   - Uses standard MCP SDK or direct HTTP calls
   - Implements retry logic and connection pooling

### Data Flow
```
OpenHands Agent → MCP Client → Cognee-MCP Server → Cognee Knowledge Base
                                    ↑
                                    ← Stores learned patterns
```

### Security Considerations
- MCP communication limited to localhost in development
- In production, use API keys or tokens for authentication
- Validate all inputs to prevent injection attacks

## 4. Initial Self-Building Tasks for OpenHands

### Task Definition Format
Based on OpenHands task specification:
```yaml
task_id: unique-identifier
title: Concise task description
description: Detailed explanation of what needs to be done
acceptance_criteria:
  - Criteria 1: Measurable outcome
  - Criteria 2: Testable condition
  - Criteria 3: Quality standard
priority: high/medium/low
estimated_effort: relative scale (1-5)
dependencies: [list of task_ids]
```

### Task 1: Generate Unit Tests for Bootstrap Scripts
**Title**: Create comprehensive unit tests for cognify_init.py and verify_openhands.py

**Description**: 
Write pytest test suites that validate the functionality of the bootstrap scripts. Tests should cover success cases, error conditions, and edge cases.

**Acceptance Criteria**:
- [ ] Test suite for cognify_init.py covers directory validation, import handling, and ECL pipeline execution
- [ ] Test suite for verify_openhands.py covers successful connection, connection errors, timeouts, and non-200 responses
- [ ] Tests achieve minimum 80% code coverage
- [ ] All tests pass in CI environment
- [ ] Test files follow naming convention: `test_*.py`

**Priority**: High
**Estimated Effort**: 3

### Task 2: Create Project Documentation (README.md)
**Title**: Create comprehensive README.md for the SciCode-Nexus project

**Description**:
Create a well-structured README that introduces the project, explains its purpose, provides setup instructions, usage examples, and architecture overview.

**Acceptance Criteria**:
- [ ] Project title and description
- [ ] Prerequisites and installation instructions
- [ ] Quick start guide
- [ ] Usage examples for bootstrap scripts
- [ ] Architecture overview with diagrams
- [ ] API references (if applicable)
- [ ] Contribution guidelines
- [ ] License information
- [ ] Badges for build status, coverage, etc.

**Priority**: High
**Estimated Effort**: 2

### Task 3: Configure Onyx Connectors for Slack and GitHub
**Title**: Set up Onyx connectors for Slack and GitHub integration

**Description**:
Configure Onyx to index content from Slack workspace and GitHub repository for enhanced search capabilities within the system.

**Acceptance Criteria**:
- [ ] Slack connector configuration file created
- [ ] GitHub connector configuration file created
- [ ] Configuration includes necessary authentication parameters (placeholders for secrets)
- [ ] Connectors validate without syntax errors
- [ ] Documentation on how to configure actual credentials

**Priority**: Medium
**Estimated Effort**: 2

### Task 4: Improve docker-compose.yml
**Title**: Enhance docker-compose.yml with health checks, resource limits, and logging

**Description**:
Improve the Docker Compose configuration to make services more robust and observable in production environments.

**Acceptance Criteria**:
- [ ] Health checks added for all services (onyx, cognee, openhands, db)
- [ ] Resource limits (memory, CPU) defined for each container
- [ ] Logging configurations optimized (drivers, options)
- [ ] Restart policies defined
- [ ] Network configurations improved
- [ ] Volume configurations validated

**Priority**: Medium
**Estimated Effort**: 3

### Task 5: Create OpenHands Task Trigger Mechanism
**Title**: Develop script to assign tasks to OpenHands API

**Description**:
Create a mechanism to programmatically assign tasks to OpenHands, enabling automated self-building workflows.

**Acceptance Criteria**:
- [ ] Script that reads task definitions from YAML/JSON files
- [ ] Script that assigns tasks to OpenHands via API
- [ ] Handles task status polling and result retrieval
- [ ] Includes error handling and retry logic
- [ ] Supports batch task assignment
- [ ] Logging of task assignment and completion

**Priority**: High
**Estimated Effort**: 4

## 5. Mechanism to Trigger OpenHands Tasks

### Task Assignment Script
Create `trigger_openhands_task.py` that:
1. Reads task definitions from `tasks/` directory
2. Authenticates with OpenHands API (if required)
3. Posts tasks to OpenHands task endpoint
4. Polls for task completion
5. Retrieves and stores results
6. Handles failures and retries

### Task Queue System
- Tasks stored as YAML files in `tasks/pending/`
- Moving to `tasks/processing/` when assigned
- Moving to `tasks/completed/` or `tasks/failed/` based on outcome
- Metadata includes timestamps, agent ID, results

### Integration with Self-Building Loop
1. System identifies improvement opportunity
2. Task definition created and placed in pending queue
3. Trigger script assigns task to OpenHands
4. OpenHands works on task using Cognee-MCP for context
5. Results stored and validated
6. Successful results merged via PR workflow
7. Lessons learned stored in Cognee for future reference

## 6. Acceptance Criteria for Phase 2 Completion

### Git Workflow
- [ ] GitHub repository created and connected
- [ ] Branching strategy documented and followed
- [ ] PR workflow established with required approvals
- [ ] Git validation practices implemented (status checks, commit verification)

### Test-Driven Development
- [ ] Test suites written for bootstrap scripts
- [ ] Tests passing locally and in CI
- [ ] Coverage thresholds met

### OpenHands-Cognee-MCP Integration
- [ ] OpenHands can successfully query Cognee-MCP
- [ ] Context retrieval returns relevant project information
- [ ] Learned patterns stored in Cognee

### Self-Building Tasks
- [ ] At least 3 of the 5 initial self-building tasks completed
- [ ] Generated unit tests passing
- [ ] README.md created and comprehensive
- [ ] Onyx connectors configured
- [ ] Docker-compose improvements implemented
- [ ] Task trigger mechanism functional

### Documentation
- [ ] PLAN_PHASE2.md created (this document)
- [ ] All design decisions documented
- [ ] Future work outlined

## 7. Risks and Mitigations

### Risk 1: OpenHands API Changes
- **Mitigation**: Abstract API calls behind interface layer
- **Mitigation**: Version API interactions

### Risk 2: MCP Connection Failures
- **Mitigation**: Implement retry with exponential backoff
- **Mitigation**: Fallback to local context when MCP unavailable
- **Mitigation**: Health checks for MCP service

### Risk 3: Test Flakiness
- **Mitigation**: Use deterministic test data
- **Mitigation**: Mock external services where appropriate
- **Mitigation**: Test isolation and cleanup

### Risk 4: Resource Exhaustion
- **Mitigation**: Define resource limits in docker-compose
- **Mitigation**: Monitor container resource usage
- **Mitigation**: Implement graceful degradation

## 8. Next Steps
 
1. User creates GitHub repository and provides URL
2. Implement test-driven approach for bootstrap validation
3. Develop OpenHands-Cognee-MCP integration mechanism
4. Create initial self-building tasks in OpenHands format
5. Build task trigger mechanism
6. Write PLAN_PHASE2.md (this document)
7. Switch to code mode to implement the plan
 
## Task Tracking
Detailed task breakdown and GitHub issue mapping maintained in:
[plans/GITHUB_ISSUE_MAP.md](./GITHUB_ISSUE_MAP.md)
 
---
*Document created as part of SciCode-Nexus Phase 2 planning*