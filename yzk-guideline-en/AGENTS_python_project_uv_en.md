# AGENTS.md

## The Current Project Uses uv To Manage Python

**Always use the current directory's `.venv`, and treat `pyproject.toml` and `uv.lock` as the source of truth for dependencies.**

- When working on a Python project, prefer the `.venv` virtual environment in the current directory that is managed by `uv`.
- If the current directory does not yet contain `.venv`, create it with `uv venv` before installing dependencies, running scripts, or executing tests.
- When adding, removing, or changing dependencies, prefer `uv` commands such as `uv add` and `uv remove`. Do not mutate the installed environment manually in a way that bypasses dependency declarations.
- Use `pyproject.toml` as the dependency declaration and `uv.lock` as the locked resolution. Whenever dependencies change, keep both files in sync.
- Prefer `uv run` for project commands. Use `uv sync` when the local environment must be aligned with the lockfile.
- Unless the project explicitly requires exported compatibility files, do not treat `requirements.txt` as the primary dependency manifest or the only source of truth for the environment state.

## Python Coding And Documentation Rules

This is a strict project template intended for long-lived Python automation projects or projects maintained by multiple people or Agents. One-off scripts, test helpers, and exploratory scripts may simplify boilerplate when doing so does not reduce readability or maintainability.

- When creating or updating a Python module, the file header must follow this format. `File:` must not be hardcoded to a specific filename and should be replaced with the current module filename:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: current_module_filename.py
Author:
Date:
Version: 1.0.0
Description:
"""
```

- When creating a new method, add the following section-style comment immediately above the method definition. Do not hardcode a person's name here; replace it with the current method name or processing topic:

```python
# ------------------------------------------------------------
# Fill in the method name or processing topic here
# ------------------------------------------------------------
```

- Every function or method must include a docstring with at least a short summary, `Args:`, and `Returns:`. The recommended format is:

```python
"""
Brief description of the method

Args:

Returns:
"""
```

- All functions and methods must explicitly declare parameter types and return types.
- If a function has many parameters or a complex return structure, the docstring must clearly describe the meaning, constraints, default values, and return structure.

## AI-Maintained Dynamic Section

<!-- AI-DYNAMIC-SECTION:START -->
This section is reserved for AI-maintained project overview and structure tree content for a concrete project. When appending content, edit only this section and do not change the general Python rules above.
<!-- AI-DYNAMIC-SECTION:END -->
