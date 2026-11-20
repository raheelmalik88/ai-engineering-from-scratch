# Phase 0, lesson 6: Python environments

Run every command from the course folder (`~/ai-engineering-from-scratch`).

## Exercise 1: run the setup check

```bash
bash phases/00-setup-and-tooling/06-python-environments/code/env_setup.sh
```

Result: all checks passed. It reused the course environment `.venv` (Python 3.12.13, NumPy 2.5.4, PyTorch 2.15.0).

## Exercise 2: two environments, two NumPy versions

`old-numpy/` has its own `.venv` with NumPy 1.26.4. The course `.venv` has NumPy 2.5.4.

```bash
scratch/python-environments/old-numpy/.venv/bin/python -c "import numpy; print(numpy.__version__)"
.venv/bin/python -c "import numpy; print(numpy.__version__)"
```

The first prints 1.26.4, the second 2.5.4. Installing into one environment does not touch the other.

## Exercise 3: a pyproject.toml for PyTorch + the Anthropic SDK

`torch-and-claude/pyproject.toml` lists `torch` and `anthropic`. Installed into a fresh environment with:

```bash
cd scratch/python-environments/torch-and-claude
uv venv --managed-python --python 3.12
uv pip install --python .venv/bin/python -e .
.venv/bin/python -c "import torch, anthropic; print(torch.__version__, anthropic.__version__)"
```

Both imported (torch 2.15.0, anthropic 2.11.0). PyTorch printed a warning that NumPy is missing: the environment only holds what the file lists, and NumPy isn't listed.

## Exercise 4: a global install, on purpose

With no environment active, `python3` is miniconda's Python. `python3 -m pip install --user pyjokes` put the package in:

```
/Users/raheelmalik/.local/lib/python3.12/site-packages
```

That folder is shared by every project that uses that Python, which is the problem environments solve. `python3 -m pip uninstall pyjokes` removed it, and `pip show pyjokes` then said "not found".

The two `.venv` folders are not in git (the course `.gitignore` skips `.venv/`). Rebuild them with the commands above.
