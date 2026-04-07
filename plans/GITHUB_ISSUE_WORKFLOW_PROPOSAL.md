# Minimal GitHub Issue Workflow for Phase 2

## Objective
  Adopt GitHub issues for incremental task tracking while minimizing overhead and duplication. Roo Code's todo list remains the primary source of truth, with lightweight mapping to GitHub issues.
  ## Core Principles
  1. **Single Source of Truth**: Roo Code's todo list (managed via `update_todo_list`) tracks work progress
  2. **Lightweight Mapping**: `plans/GITHUB_ISSUE_MAP.md` provides static links between task descriptions and GitHub issue numbers
  3. **Strong Commit Linkage**: All commits and changes reference the related GitHub issue ID (e.g., `Fixes #123`)
  4. **Minimal Overhead**: Only the mapping file requires occasional updates; no status syncing needed

## Current State
- Roo Code uses todo list (via `update_todo_list`) for task tracking
- Phase 2 plan exists in PLAN_PHASE2.md with 5 initial tasks
- GitHub repository exists but issues not yet used for task tracking

## Minimal Proposed Changes

### 1. Single Mapping File
Create `plans/GITHUB_ISSUE_MAP.md` with simple format:
```markdown
# GitHub Issue Mapping for Roo Code Tasks

| Roo Code Task Description | GitHub Issue # | Status |
|---------------------------|----------------|--------|
| Write unit tests for cognify_init.py | 1 | [ ] |
| Write unit tests for verify_openhands.py | 2 | [ ] |
| Create comprehensive README.md | 3 | [ ] |
| Configure Onyx connectors | 4 | [ ] |
| Improve docker-compose.yml | 5 | [ ] |
| Create OpenHands task trigger mechanism | 6 | [ ] |
```

### 2. Workflow Integration
#### When Starting Work:
1. Roo Code checks `GITHUB_ISSUE_MAP.md` for unmapped high-priority items
2. For each unmapped item, create GitHub issue using standard template
3. Update mapping file with issue number and commit with reference (e.g., `refs #<issue_number>: Add mapping for new task`)
4. Roo Code adds item to todo list as `[-]` (in progress) and commits with reference (e.g., `refs #<issue_number>: Start work on <task_description>`)

#### During Work:
- Progress tracked exclusively in Roo Code's todo list (updated via `update_todo_list`)
- Mapping file only stores static links (issue number ↔ task description)
- No need to update mapping file during work unless task description changes

#### Upon Completion:
1. Roo Code marks todo item as `[x]` and commits with reference (e.g., `refs #<issue_number>: Complete work on <task_description>`)
2. Optionally add comment to GitHub issue referencing completion and commit SHA
3. Issue closed via GitHub UI or API (if available)

### 3. Minimal Documentation Updates
#### PLAN_PHASE2.md
Add a section referencing the mapping file:
```markdown
## Task Tracking
Detailed task breakdown and GitHub issue mapping maintained in:
[plans/GITHUB_ISSUE_MAP.md](./GITHUB_ISSUE_MAP.md)
```

#### No changes needed to specs directory - keep as reference only

### 4. Benefits of Minimal Approach
- **Single source of truth**: Roo Code todo list for progress tracking
- **Low overhead**: Only one additional file to maintain
- **No duplication**: Avoids syncing status between multiple places
- **Clear traceability**: Direct link from task description to GitHub issue
- **Easy to audit**: Simple table format shows coverage

### 5. Implementation Steps
1. Create `plans/GITHUB_ISSUE_MAP.md` with initial mapping
2. Add reference to PLAN_PHASE2.md
3. Create GitHub issues for initial Phase 2 tasks
4. Update mapping file with issue numbers
5. Use todo list for daily work tracking

### 6. Example
**Before work:**
```markdown
| Write unit tests for cognify_init.py | 1 | [ ] |
```

**After starting work (todo list updated and committed):**
```markdown
[-] Write unit tests for cognify_init.py (GitHub Issue #1)
```
Commit: `refs #1: Start work on Write unit tests for cognify_init.py`

**Mapping file updated and committed:**
```markdown
| Write unit tests for cognify_init.py | 1 | [ ] |
```
Commit: `refs #1: Add mapping for Write unit tests for cognify_init.py`

**Upon completion (todo list updated and committed):**
```markdown
[x] Write unit tests for cognify_init.py (GitHub Issue #1)
```
Commit: `refs #1: Complete work on Write unit tests for cognify_init.py`

**Mapping file unchanged** - still shows `[ ]` in status column (it's a static link, not a status tracker)

## Addressing User Concerns
- **Where Roo Code stores plans**: In the todo list (via `update_todo_list`)
- **Integration**: Mapping file links todo items to GitHub issues without duplication
- **Consistency**: Only mapping file needs occasional updates; specs/plans remain reference
- **Minimal assets**: Only one new markdown file required
- **Strong commit linkage**: All commits reference the related GitHub issue ID