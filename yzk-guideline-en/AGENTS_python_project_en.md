# AGENTS.md

## The Current Project Is A Python Automation Project

**Always use the current directory's `.venv` and keep dependency declarations in sync.**

- When working on a Python project, always use the `.venv` virtual environment in the current directory.
- If the current directory does not yet contain a `.venv`, create and activate it before installing dependencies, running scripts, or executing tests.
- After installing any dependency, always update `requirements.txt`.
- If you change dependency versions or remove dependencies, update `requirements.txt` as well so it stays aligned with the actual environment.

## Python Coding And Documentation Rules

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

## The Following Section Is Updated Dynamically By The Agent (Project Overview And Structure Tree)
