# GitHub Issue Sync Process for Roo Code

## Overview
This document defines the lightweight process for keeping Roo Code's task tracking in sync with GitHub issues, following the minimal mapping approach.

## Core Principles
  1. **Single Source of Truth**: Roo Code's todo list (managed via `update_todo_list`) tracks work progress
  2. **Lightweight Mapping**: `plans/GITHUB_ISSUE_MAP.md` provides static links between task descriptions and GitHub issue numbers
  3. **Strong Commit Linkage**: All commits and changes reference the related GitHub issue ID (e.g., `Fixes #123`)
  4. **Minimal Overhead**: Only the mapping file requires occasional updates; no status syncing needed

## Sync Process Details

### 1. Work Identification & Issue Creation
**Trigger**: When Roo Code needs to identify next work items
**Process**:
1. Roo Code reviews `plans/GITHUB_ISSUE_MAP.md` for items with empty GitHub Issue # column
2. For each unmapped high-priority task:
   - Create GitHub issue using standard template (see below)
   - Copy task description from mapping file
   - Add appropriate labels (`type: task`, `phase: 2`, etc.)
   - Submit issue and note the assigned issue number
   - Update mapping file with the GitHub issue number
   - Commit the mapping file update with a reference to the new issue (e.g., `refs #<issue_number>: Add mapping for new task`)
3. Roo Code adds item to todo list as `[ ]` (pending) or `[-]` (in progress) if starting immediately
   - Commit the todo list update with a reference to the issue (e.g., `refs #<issue_number>: Start work on <task_description>`)

### 2. Standard GitHub Issue Template
All Roo Code-created issues should follow this format:
```markdown
## Task Description
[Copy task description from GITHUB_ISSUE_MAP.md]

## Acceptance Criteria
- [ ] Measurable outcome 1
- [ ] Measurable outcome 2
- [ ] ...

## Priority
[high/medium/low]

## Estimated Effort
[1-5 scale]

## Area
[testing/documentation/infrastructure/etc.]

## Related Roo Code Tracking
This issue is tracked in Roo Code's todo list via:
[plans/GITHUB_ISSUE_MAP.md](./GITHUB_ISSUE_MAP.md)
```

### 3. Work Execution & Progress Tracking
**During Work**:
- All progress tracking happens in Roo Code's todo list via `update_todo_list`
- Status transitions: `[ ]` (pending) → `[-]` (in progress) → `[x]` (completed)
- Mapping file remains unchanged during work (unless task description changes)
- No need to update GitHub issue status during work (avoids duplication)

### 4. Completion Handling
**When Roo Code marks todo item as `[x]`**:
1. Optionally add a comment to the GitHub issue:
   ```
   Work completed by Roo Code. See implementation in [branch/commit reference].
   Ready for review.
   ```
2. Issue can be closed via:
   - GitHub UI (manual)
   - GitHub API (if available and automated)
   - Left open for manual review/closure by human
3. Mapping file status column remains `[ ]` (it's a static link, not a status tracker)

### 5. Issue Updates from GitHub
**Periodically** (or when notified):
1. Roo Code checks for updates to assigned GitHub issues
2. If issue description or acceptance criteria changed significantly:
   - Update task description in `GITHUB_ISSUE_MAP.md`
   - Update corresponding todo item if needed
3. New comments or labels don't require mapping file updates

## Workflow Examples

### Starting New Work
**Before**:
```markdown
# GITHUB_ISSUE_MAP.md
| Write unit tests for cognify_init.py | | [ ] |
```

**After creating issue #10**:
```markdown
# GITHUB_ISSUE_MAP.md
| Write unit tests for cognify_init.py | 10 | [ ] |
```

**Roo Code todo list**:
```markdown
[-] Write unit tests for cognify_init.py (GitHub Issue #10)
```

### During Work
**Roo Code todo list updates** (no mapping file changes):
```markdown
[-] Write unit tests for cognify_init.py (GitHub Issue #10)  # In progress
[ ] Write unit tests for verify_openhands.py (GitHub Issue #11)  # Pending
[ ] Create comprehensive README.md (GitHub Issue #12)  # Pending
```

### Upon Completion
**Roo Code todo list**:
```markdown
[x] Write unit tests for cognify_init.py (GitHub Issue #10)
[-] Write unit tests for verify_openhands.py (GitHub Issue #11)
[ ] Create comprehensive README.md (GitHub Issue #12)
```

**GitHub Issue #10** gets optional comment but mapping file unchanged:
```markdown
# GITHUB_ISSUE_MAP.md
| Write unit tests for cognify_init.py | 10 | [ ] |
| Write unit tests for verify_openhands.py | 11 | [ ] |
| Create comprehensive README.md | 12 | [ ] |
```

## Benefits of This Approach
- **No status sync overhead**: Avoids constant updates between systems
- **Clear audit trail**: Mapping file shows permanent links
- **Flexible completion**: Issues can be closed manually after review
- **Minimal files**: Only one additional markdown file needed
- **Preserves Roo Code's native tracking**: Todo list remains primary

## Implementation Notes
- The mapping file is the only artifact that needs updates when:
  - New work is identified (add issue number)
  - Task descriptions change significantly (update description)
- All other tracking happens in Roo Code's native todo list system
- GitHub issue status is informational; Roo Code relies on its own todo list for work state