# Detailed Implementation Plan for Plans and Specs Directory Structure

## Overview
This plan outlines the steps to reorganize the repository by creating dedicated `plans/` and `specs/` directories to better coordinate agent behaviour with OpenHands and improve overall project organization.

## Phase 1: Preparation

### 1.1 Backup Current State
- Ensure all current files are committed to git
- Create a backup branch: `git checkout -b backup-before-restructure`

### 1.2 Review Current Documentation
- Verify content of `PLAN_PHASE1.md` and `PLAN_PHASE2.md`
- Review `ARCHITECTURAL_DESIGN.md` for any references to plan files
- Check `CONTRIBUTING.md` for documentation references
- Examine `docs/` files for internal links to plan documents

## Phase 2: Directory Creation and File Migration

### 2.1 Create New Directories
```bash
mkdir plans
mkdir specs
```

### 2.2 Migrate Existing Plan Files
```bash
mv PLAN_PHASE1.md plans/phase1.md
mv PLAN_PHASE2.md plans/phase2.md
```

### 2.3 Create Initial Specification Files
Create the following files in the `specs/` directory:

#### specs/api-spec.md
```markdown
# API Specification

## Overview
This document defines the APIs for all services in the SciCode-Nexus system.

## Services
- onyx: Search and indexing service
- cognee: Knowledge management and ECL processing
- openhands: Autonomous agent framework
- db: Shared data persistence

## Endpoints
[To be defined]

## Data Models
[To be defined]

## Authentication
[To be defined]

## Error Handling
[To be defined]
```

#### specs/agent-coordination-spec.md
```markdown
# Agent Coordination Specification

## Overview
This document defines how agents interact with the OpenHands framework and coordinate tasks.

## OpenHands Integration
- MCP (Model Context Protocol) integration points
- Agent skill definitions
- Task delegation mechanisms

## Communication Protocols
- Message formats
- Response handling
- Error propagation

## Coordination Patterns
- Sequential task execution
- Parallel processing
- Feedback loops
```

#### specs/data-model-spec.md
```markdown
# Data Model Specification

## Overview
This document defines the data models and schemas used throughout the system.

## Knowledge Graph Schema
- Entities and relationships
- Attributes and properties
- Temporal aspects

## Shared State
- Session data
- User preferences
- System configuration

## Data Transfer Objects
- API request/response models
- Internal service communication models
```

#### specs/mcp-integration-spec.md
```markdown
# MCP Integration Specification

## Overview
This document defines the Model Context Protocol integration details.

## MCP Server Configuration
- Endpoint definitions
- Security considerations
- Context provisioning

## MCP Client Usage
- How services consume MCP contexts
- Context update mechanisms
- Subscription patterns

## Extension Points
- Custom context providers
- Skill integration hooks
```

## Phase 3: Reference Updates

### 3.1 Update Internal Links
Search and update references to the moved plan files:
- In `CONTRIBUTING.md`: Update references to PLAN_PHASE1.md and PLAN_PHASE2.md
- In `docs/setup.md`: Update references to plan files
- In `ARCHITECTURAL_DESIGN.md`: Update any references
- In any other markdown files

### 3.2 Update CONTRIBUTING.md
Add documentation about the new directory structure:
- Explain the purpose of `plans/` and `specs/` directories
- Update development setup instructions if needed
- Add guidelines for creating new plan and spec files

## Phase 4: Validation and Cleanup

### 4.1 Verify Links
- Check that all internal links in markdown files still work
- Validate that external links are still valid
- Ensure no broken references remain

### 4.2 Run Tests
- Execute the test suite to ensure nothing is broken
- Verify that the system still functions correctly after the reorganization

### 4.3 Create Directory READMEs
Create README files in each new directory to explain their purpose:

#### plans/README.md
```markdown
# Plans Directory

This directory contains planning documents that outline the project roadmap, milestones, and high-level objectives.

## Naming Convention
- Use descriptive names with underscores (e.g., `phase1.md`, `feature-plan.md`)
- Files should be in markdown format

## Contents
- Phase-based development plans
- Release planning
- Strategic objectives
```

#### specs/README.md
```markdown
# Specs Directory

This directory contains technical specifications that define implementation details, interfaces, and data models.

## Naming Convention
- Use descriptive names with hyphens (e.g., `api-spec.md`, `data-model-spec.md`)
- Files should be in markdown format

## Contents
- API specifications
- Agent coordination protocols
- Data model definitions
- Integration specifications
```

## Phase 5: Finalization

### 5.1 Commit Changes
```bash
git add plans/ specs/
git add CONTRIBUTING.md docs/setup.md docs/index.md docs/features.md docs/roadmap.md ARCHITECTURAL_DESIGN.md
git add PLANS_AND_SPECS_PROPOSAL.md DETAILED_IMPLEMENTATION_PLAN.md
git commit -m "Reorganize documentation: create plans/ and specs/ directories, migrate plan files, update references"
```

### 5.2 Create Pull Request
- Open a pull request against the main branch
- Request review from team members
- Address any feedback

### 5.3 Post-Merge Cleanup
- Remove backup branch after successful merge
- Update any local development instructions
- Communicate changes to the team

## Timeline Estimate
- Phase 1 (Preparation): 15 minutes
- Phase 2 (Directory Creation and Migration): 30 minutes
- Phase 3 (Reference Updates): 45 minutes
- Phase 4 (Validation and Cleanup): 30 minutes
- Phase 5 (Finalization): 15 minutes
- **Total Estimated Time**: 2 hours

## Risk Mitigation
- **Risk**: Broken internal links
  - **Mitigation**: Use search tools to find all references before moving files
- **Risk**: Confusion among team members
  - **Mitigation**: Clear communication and updated CONTRIBUTING.md
- **Risk**: Loss of document history
  - **Mitigation**: Use git move operations to preserve history

## Success Criteria
- All plan files are accessible in the new `plans/` directory
- All specification files are created in the new `specs/` directory
- No broken internal links in markdown files
- Tests continue to pass
- Team members can easily locate planning and specification documents