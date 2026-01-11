# camel2snake

A simple Python utility to convert camelCase strings to snake_case.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
# No external dependencies required
```

## Usage

```python
from camel2snake import camel_to_snake

camel_to_snake("camelCase")      # "camel_case"
camel_to_snake("CamelCase")      # "camel_case"
camel_to_snake("myVariableName") # "my_variable_name"
camel_to_snake("XMLHttpRequest") # "x_m_l_http_request"
```

## Running as a Script

```bash
python camel2snake.py
```

This runs the built-in test cases and displays conversion results.

## Running Tests

```bash
pytest tests/ -v
```

## How It Works

The function iterates through each character and inserts an underscore before uppercase letters (except at the start), then converts everything to lowercase.

Note: Consecutive uppercase letters (like acronyms) are treated as individual characters, so `XMLHttpRequest` becomes `x_m_l_http_request` rather than `xml_http_request`.
