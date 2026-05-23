---
name: git-workflow
description: A Git skill for repository management tasks such as status checks, staging, committing, branching, pushing, pulling, and inspecting remotes. Use this skill when the user asks to perform or explain Git operations in the current repository.
---

# Git Workflow

## Overview

This Skill helps with Git repository workflows in the current workspace. It is intended for tasks such as:

- checking repository status
- staging and committing files
- pushing and pulling changes
- creating, switching, and merging branches
- inspecting remotes and branch tracking
- recovering from simple merge conflicts
- using Git in environments where the CLI may not be on PATH

## Instructions

1. Always identify the repository root before running Git commands.
   - Use `git status --short --branch` to determine the current branch and changed files.

2. For file changes, prefer precise staging:
   - `git add <file>` to stage a specific file
   - `git add -p` to stage hunks interactively when appropriate

3. Commit with a clear message:
   - `git commit -m "<summary>"`
   - If the working tree is clean and no commit is needed, explain that no commit is necessary.

4. Push or pull from the configured remote:
   - `git push origin <branch>`
   - `git pull origin <branch>`
   - If the branch is tracking a remote, `git push` and `git pull` are sufficient.

5. For branch operations:
   - Create a branch: `git checkout -b <branch-name>` or `git switch -c <branch-name>`
   - Switch branches: `git checkout <branch-name>` or `git switch <branch-name>`
   - Merge a branch: `git merge <source-branch>`
   - Rebase when needed: `git rebase <base-branch>`

6. Inspect remotes and refs when necessary:
   - `git remote -v` to show configured fetch/push URLs
   - `git branch --all` to list local and remote branches
   - `git log --oneline --decorate --graph` to inspect commit history

7. If the shell environment cannot run `git` directly, detect the executable path and use the full path when available.
   - On Windows, prefer `C:\Progra~1\Git\cmd\git.exe` if `git` is not on PATH.

8. Do not perform destructive operations without confirmation.
   - Avoid `git reset --hard`, `git clean -fd`, or `git push --force` unless explicitly requested by the user.

## Examples

- "Check repo status and summarize what changed."
- "Commit the README update and push it to origin master."
- "Create a new branch named feature/update-readme and switch to it."
- "Show me the configured remotes and current branch tracking info."
- "Help me resolve a merge conflict in `start.py`."

## Best Practices

- Keep commands minimal and explicit.
- Prefer safe Git operations unless the user explicitly asks for recovery or rewriting history.
- If the repository is not clean, describe the changes and ask whether to stage and commit them.
- When possible, use the repository's existing remote and branch configuration rather than hardcoding remote names.
