# Git Compliance Requirements by Mode

## Overview
These requirements ensure clean git status after tasks in each mode of the Roo Code system. Following these practices maintains repository integrity and enables smooth handoffs between modes.

## Orchestrator Mode Requirements

### When to Commit, Stash, or Discard Changes
- **Commit**: When completing a workflow coordination task that updates tracking files (GITHUB_ISSUE_MAP.md, todo list via update_todo_list)
- **Stash**: When switching between different workflow patterns or need to preserve experimental coordination approaches
- **Discard**: When coordination experiments fail and need to revert to clean state

### Handling Untracked Files
- Track all workflow mapping files (GITHUB_ISSUE_MAP.md, todo list updates)
- Review untracked files before committing to ensure only intended workflow artifacts are included
- Add workflow-related temporary files to .gitignore if they should not be versioned

### Mode-Specific Git Practices
- Ensure all workflow tracking files are committed before handing off to other modes
- Validate that issue mapping commits include proper refs to GitHub issues
- Keep workflow coordination commits atomic and descriptive

### Verifying Clean Git Status
- Run `git status` to confirm only expected workflow files are modified
- Verify commit messages reference related GitHub issues when applicable
- Ensure no uncommitted changes remain in tracking files before task completion

## Architect Mode Requirements

### When to Commit, Stash, or Discard Changes
- **Commit**: When completing architectural decisions, creating/modifying design documents, or updating technical specifications
- **Stash**: When exploring alternative architectural approaches or need to preserve work-in-progress designs
- **Discard**: When architectural experiments prove unsuitable and need to revert to baseline

### Handling Untracked Files
- Track all specification and design documents in specs/ and plans/ directories
- Review architectural sketches, diagrams, and notes before committing
- Ensure temporary design files are properly ignored via .gitignore

### Mode-Specific Git Practices
- Commit architectural documents with clear rationale in commit messages
- Ensure design documents are self-contained and understandable without additional context
- Group related architectural changes in single commits when they address the same concern

### Verifying Clean Git Status
- Run `git status` to confirm only intended design/documents are modified
- Verify that architectural decisions are properly documented before committing
- Ensure no stray design files or temporary diagrams remain uncommitted

## Code Mode Requirements (Primary Focus)

### When to Commit, Stash, or Discard Changes
- **Commit**: 
  - After completing a discrete code implementation task
  - When passing tests for implemented functionality
  - Before switching to another mode or requesting review
  - When implementing a complete feature or bug fix
- **Stash**: 
  - When needing to switch contexts urgently (e.g., addressing critical feedback)
  - When experimenting with alternative implementations
  - Before pulling upstream changes to avoid conflicts
- **Discard**: 
  - When code experiments fail and need to reset to clean state
  - When implementing spikes or proofs of concept that won't be kept
  - When code doesn't meet quality standards and needs to be rewritten

### Handling Untracked Files
- Track all source code files that are part of the implementation
- Review generated files (if any) to determine if they should be committed
- Ensure build artifacts, dependencies, and IDE-specific files are properly ignored
- Commit new files that are part of the feature implementation

### Mode-Specific Git Practices
- **Pre-commit verification**: 
  - Run `git status` to review all changes
  - Use `git diff` to review modifications before staging
  - Ensure only intended files are staged for commit
  - Run relevant tests to confirm functionality
- **Commit hygiene**:
  - Make commits atomic and focused on single concerns
  - Write clear, descriptive commit messages following project conventions
  - Reference related issues or tasks when applicable (e.g., "refs #123: Implement feature X")
  - Include both code and necessary tests in the same commit when possible
- **Pre-handoff requirements**:
  - Ensure no uncommitted code remains before handing off to another mode
  - All tests should pass for committed code
  - Code should follow project coding standards (PEP 8 for Python)
  - Documentation updates should accompany code changes when appropriate

### Verifying Clean Git Status
- Run `git status` and confirm working tree is clean or only contains intentional uncommitted work
- Use `git diff --cached` to review staged changes before committing
- Run `git diff` to review unstaged changes
- Verify that `.gitignore` is properly configured to exclude unnecessary files
- Ensure that only files related to the current task are modified

## Debug Mode Requirements

### When to Commit, Stash, or Discard Changes
- **Commit**: 
  - After fixing a bug and verifying the fix with tests
  - When implementing diagnostic code that should be preserved (with plans to remove later)
  - When completing a debugging session that results in code improvements
- **Stash**: 
  - When needing to preserve current debugging state to investigate alternative hypotheses
  - When switching between different debugging approaches
  - Before pulling changes to see if issue persists in updated code
- **Discard**: 
  - When diagnostic code was added temporarily and needs to be removed
  - When debugging experiments fail to reproduce or fix the issue
  - When reverting to known good state after unsuccessful debugging attempts

### Handling Untracked Files
- Track debugging scripts, test reproductions, and diagnostic tools that should be preserved
- Review log files, core dumps, and temporary debug outputs before committing (usually should not be committed)
- Ensure debugging artifacts are properly ignored unless they have lasting value

### Mode-Specific Git Practices
- Keep debugging commits focused and minimal
- Clearly mark temporary debugging code with comments indicating it should be removed
- Commit fixes with clear problem/solution descriptions in commit messages
- When adding temporary diagnostic code, plan for its removal in follow-up commits

### Verifying Clean Git Status
- Run `git status` to confirm only intended debugging changes remain
- Verify that temporary debugging code is either committed (with removal planned) or discarded
- Ensure no unnecessary log files or debug outputs are left in working directory
- Confirm that debugging sessions don't leave the repository in a corrupted state

## Ask Mode Requirements

### When to Commit, Stash, or Discard Changes
- **Commit**: 
  - When completing information gathering tasks that result in documentation updates
  - When creating examples or tutorials based on inquiries
  - When updating FAQs or knowledge base entries
- **Stash**: 
  - When needing to preserve research state while seeking additional information
  - When exploring multiple answer paths before settling on final response
- **Discard**: 
  - When research proves the initial question was based on false premises
  - When gathered information doesn't lead to actionable outcomes
  - When experimental responses need to be cleared

### Handling Untracked Files
- Track research notes, information gathering results, and documentation updates
- Review temporary information files before committing to ensure only relevant knowledge is preserved
- Ensure cached data, temporary research files, and intermediate analysis are properly ignored

### Mode-Specific Git Practices
- Commit information updates with clear context about what was learned or clarified
- Ensure documentation commits are self-explanatory and useful to future readers
- Group related information updates when they address the same topic or question

### Verifying Clean Git Status
- Run `git status` to confirm only intended information/documentation files are modified
- Verify that research notes don't contain sensitive or temporary information
- Ensure that knowledge base updates are accurate and properly formatted
- Confirm that no unnecessary research artifacts remain in working directory

## Cross-Mode Git Practices

### Pre-Task Preparation
- At start of task in any mode, consider running `git status` to understand baseline state
- Ensure working from appropriate branch for the type of work being performed
- Consider creating task-specific branch when appropriate for longer-running tasks

### Post-Task Validation
- Before completing task and switching modes, always verify clean git status appropriate to the mode's requirements
- Ensure that any mode-specific handoff requirements are met (especially Code mode's requirement for no uncommitted code)
- Document any intentional exceptions to clean git status in task tracking or commit messages

### Emergency Procedures
- When needing to urgently switch contexts, consider stashing changes with descriptive message
- When work needs to be preserved but isn't ready for commit, use stashing with clear labels
- Regularly apply stashed changes or commit them to avoid accumulation of stale work

## Implementation Notes

These requirements should be integrated into mode-specific instructions as concise guidelines. The focus is on maintaining repository integrity while enabling productive work in each mode.

Key principles across all modes:
1. Intentionality: All changes should be purposeful and reviewed before committing
2. Traceability: Commit messages should explain why changes were made
3. Cleanliness: Working directories should be left in predictable states
4. Collaboration: Git practices should enable smooth handoffs between modes and human reviewers