# Plans and Specs Directory Structure Proposal

## Current State Analysis

The repository currently contains:
- Planning documents in root: `PLAN_PHASE1.md`, `PLAN_PHASE2.md`
- Architectural documentation: `ARCHITECTURAL_DESIGN.md`
- Contributing guidelines: `CONTRIBUTING.md`
- User documentation in `docs/` directory: features, index, roadmap, setup
- Test files in `tests/` directory
- Core implementation files: `cognify_init.py`, `verify_openhands.py`
- Configuration: `docker-compose.yml`, `requirements.txt`, `.gitignore`

## Proposed Directory Structure

To better organize planning and specification documents for coordinating agent behaviour with OpenHands, I propose the following structure:

```
/
├── .gitignore
├── cognify_init.py
├── CONTRIBUTING.md
├── docker-compose.yml
├── requirements.txt
├── verify_openhands.py
├── .vscode/
├── docs/
│   ├── features.md
│   ├── index.md
│   ├── roadmap.md
│   └── setup.md
├── plans/
│   ├── phase1.md
│   ├── phase2.md
│   ├── phase3.md
│   └── phase4.md
├── specs/
│   ├── api-spec.md
│   ├── agent-coordination-spec.md
│   ├── data-model-spec.md
│   └── mcp-integration-spec.md
└── tests/
    ├── run_tests.py
    ├── test_cognify_init.py
    └── test_verify_openhands.py
```

## Rationale

### Plans Directory (`plans/`)
- Move existing `PLAN_PHASE1.md` and `PLAN_PHASE2.md` to `plans/phase1.md` and `plans/phase2.md`
- Create additional plan files for future phases as needed
- Plans focus on roadmap, milestones, and high-level objectives
- Naming convention: descriptive, lowercase with underscores

### Specs Directory (`specs/`)
- Technical specifications for implementation details
- API specifications for service interfaces
- Agent coordination protocols for OpenHands integration
- Data model definitions for knowledge graph and shared state
- MCP (Model Context Protocol) integration details
- Naming convention: descriptive, lowercase with hyphens

### Documentation Directory (`docs/`)
- Retain existing user-facing documentation
- Focus on end-user guides, feature explanations, and setup instructions
- Maintain separation between internal planning/specs and user documentation

## Migration Steps

1. Create `plans/` directory
2. Move `PLAN_PHASE1.md` to `plans/phase1.md`
3. Move `PLAN_PHASE2.md` to `plans/phase2.md`
4. Create `specs/` directory
5. Create initial specification files in `specs/`:
   - `api-spec.md` - Define service APIs and endpoints
   - `agent-coordination-spec.md` - Define how agents interact with OpenHands
   - `data-model-spec.md` - Define knowledge graph schema and data structures
   - `mcp-integration-spec.md` - Define MCP server/client interactions
6. Update any references to the moved plan files
7. Consider adding a README.md in each new directory explaining its purpose

## Benefits

1. **Better Organization**: Separates concerns between planning, specifications, and user documentation
2. **Scalability**: Easy to add new plan and spec files as the project grows
3. **Clarity**: Clear distinction between different types of documentation
4. **Agent Coordination**: Provides structured locations for OpenHands agents to find planning and specification information
5. **Maintainability**: Easier to locate specific types of information

## Implementation Notes

- All moved/renamed files should maintain their existing content initially
- Future updates should follow the new structure
- Consider creating templates for plan and spec files to ensure consistency
- Update CONTRIBUTING.md to reflect the new directory structure
- Ensure any scripts or documentation referencing the old paths are updated