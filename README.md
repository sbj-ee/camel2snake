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
