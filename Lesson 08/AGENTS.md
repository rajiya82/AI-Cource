Purpose
- Short, high-signal instructions for an OpenCode agent working in this repository. Only include items an agent would likely miss.

Quick facts
- This repo is a collection of Jupyter notebooks and a few small Python scripts (lesson materials). Most work should avoid touching notebooks unless asked.
- Python runtime hint: a compiled bytecode file in Lesson 08 uses cpython-313, so prefer Python 3.13 if available. Verify with `python --version`.

How to run the one-off script
- Script: Lesson 08/weather.py
- Run (PowerShell / Windows):
  python "Lesson 08\weather.py"
- The script depends on the requests package. Install with:
  python -m pip install requests

Notebooks
- There are many .ipynb files with outputs and accompanying .html exports. Do not modify notebooks' outputs or metadata by hand — that creates large noisy diffs.
- If you must change notebook code, prefer creating/patching a .py script instead, or use nbformat/nbconvert to programmatically modify and re-run. To execute a notebook headless:
  python -m pip install nbconvert ipykernel
  jupyter nbconvert --to notebook --execute "Lesson 08/LU08 Notebook.ipynb" --output executed.ipynb

Dependencies & environment
- There is no top-level requirements file or pyproject.toml. Inspect each folder for needed packages; for the weather script only `requests` is required.
- Use `python -m pip install --user <pkg>` or a virtualenv. Quote paths that contain spaces.

VCS and commits
- This repo has a .git directory. NEVER run destructive git commands (no hard resets, no forced pushes) unless the user explicitly asks.
- Do NOT create commits unless the user explicitly requests it. If asked to commit, include a succinct commit message that explains why and what changed.

Files and directories to avoid
- Do not edit or remove .git/* files. They are repository internals.
- Avoid modifying the generated .html notebook exports unless instructed.

Where to look first
- Lesson folders (Lesson 01..08) and their notebooks/scripts — these are the sources of truth for behavior.
- The small script Lesson 08/weather.py is the only standalone executable script; open it to understand runtime assumptions.

If something is unclear
- Ask the user one simple question before making commits or broad edits (e.g., "May I commit these changes?" or "Should I modify notebooks or create .py scripts instead?").

Minimal editing rules for agents
- Prefer the smallest correct change. If changing a notebook, prefer extracting logic to a .py and leaving the .ipynb untouched unless the user requests notebook edits.
