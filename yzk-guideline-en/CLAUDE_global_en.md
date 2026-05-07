# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" -> "Write tests for invalid inputs, then make them pass"
- "Fix the bug" -> "Write a test that reproduces it, then make it pass"
- "Refactor X" -> "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```text
1. [Step] -> verify: [check]
2. [Step] -> verify: [check]
3. [Step] -> verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Project Documentation

**When working on a concrete project, first ensure a project-level `CLAUDE.md` exists.**

If the project does not yet have a `CLAUDE.md` document, create a project-level documentation file first.

When initializing that document, it must include:
- If you modify code files in this project, update this Markdown document at the same time.
- A concise code overview for the project, such as what core functionality the project implements.
- The project's directory structure tree; every folder or file in the tree must be followed by `#` and a one-sentence summary of that directory or file.
- The generated document should use English.

If the project already has a `CLAUDE.md` document, supplement the existing document with the code overview and directory structure tree.

## 6. Subdirectory Documentation

**When creating a subdirectory, create that directory's own `CLAUDE.md` first.**

If you create a subdirectory such as `Util`, `Constant`, or `Database`, first create a `CLAUDE.md` document inside that directory.

If you are working in an existing project and discover that a subdirectory does not yet have a `CLAUDE.md`, add one before continuing to modify code in that directory.

When initializing that directory's `CLAUDE.md`, the document must include:
- If you modify code files in this directory, update this Markdown document at the same time.
- A concise code overview for this directory, such as what functionality the code in this directory implements.
- The structure tree for this directory; every folder or file in the tree must be followed by `#` and a one-sentence summary of that directory or file.
- The generated document should use English.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
