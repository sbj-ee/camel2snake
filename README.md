# camel2snake

A simple Python utility (library **and** CLI) to convert camelCase strings to snake_case.

## Installation

```bash
pip install camel2snake
```

Or install the latest from source:

```bash
pip install git+https://github.com/sbj-ee/camel2snake.git
```

## Usage

### As a library

```python
from camel2snake import camel_to_snake

camel_to_snake("camelCase")      # "camel_case"
camel_to_snake("CamelCase")      # "camel_case"
camel_to_snake("myVariableName") # "my_variable_name"
camel_to_snake("XMLHttpRequest") # "x_m_l_http_request"
```

### As a command

```bash
# convert arguments (one result per line)
camel2snake camelCase myVariableName
# camel_case
# my_variable_name

# or pipe from stdin (one string per line)
printf 'fooBar\nBazQux\n' | camel2snake
# foo_bar
# baz_qux

camel2snake --version
```

## How It Works

The function iterates through each character and inserts an underscore before
uppercase letters (except at the start), then converts everything to lowercase.

Note: Consecutive uppercase letters (like acronyms) are treated as individual
characters, so `XMLHttpRequest` becomes `x_m_l_http_request` rather than
`xml_http_request`.

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"   # editable install with test deps
pytest -v                 # run the test suite
```

## Releasing to PyPI

Publishing is automated via `.github/workflows/publish.yml` using
[PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (OIDC) — no
API tokens are stored.

**One-time setup** (on PyPI, once you have an account):

1. On PyPI → *Your projects* → *Publishing*, add a trusted publisher:
   - Owner: `sbj-ee`  ·  Repository: `camel2snake`  ·  Workflow: `publish.yml`  ·  Environment: `pypi`
   - (Optionally do the same on [TestPyPI](https://test.pypi.org/) with environment `testpypi`.)
2. In this repo → *Settings → Environments*, create environments named `pypi`
   (and `testpypi`), optionally adding yourself as a required reviewer.

**To release:**

1. Bump `version` in `pyproject.toml` and `__version__` in
   `src/camel2snake/__init__.py`.
2. Create a GitHub Release (tag e.g. `v0.1.0`). The workflow builds, runs
   `twine check`, and publishes to PyPI automatically.

**Dry run:** trigger the workflow manually (*Actions → Publish to PyPI → Run
workflow*) with target `testpypi` to publish to TestPyPI first.
