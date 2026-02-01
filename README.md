# [WIP] Using ML on AIS Data

## **Python 3.12.6**

This project requires a compatible version of python to run ydata-profiling. 


## Install and Run with `uv`
```bash
# Install the uv Project Manager

    # With Homebrew (MacOS)
    brew install uv 

    # With Powershell (Windows)
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    # With Curl (Linux)
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Load Dependencies with uv
uv sync

# Run a Python file with uv
uv run python <file.py>

# Run __main__.py
uv run python src

# Add Dependencies with uv
uv add [--dev] <package_name>...
```

## Install Juypter Git Filter: _`nbstripout`_

```bash
# Ensure nbstripout is installed
uv sync --group dev

# Add Git Filter to .git/
uv run nbstripout --install

# Verification
git config --get filter.nbstripout.clean
```