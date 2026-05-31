"""Core conversion logic for camel2snake."""

from __future__ import annotations


def camel_to_snake(camel_string: str | None) -> str | None:
    """Convert a camelCase string to snake_case (lowercase with underscores).

    An underscore is inserted before every uppercase letter (except the first
    character), and the result is lowercased. Consecutive uppercase letters
    (acronyms) are treated as individual characters, so ``XMLHttpRequest``
    becomes ``x_m_l_http_request``.

    Args:
        camel_string: Input string in camel case. ``None`` and empty strings
            are returned unchanged.

    Returns:
        The string converted to snake case (or the original falsy value).
    """
    if not camel_string:
        return camel_string

    result: list[str] = []
    for i, char in enumerate(camel_string):
        if char.isupper():
            if i > 0:
                result.append("_")
            result.append(char.lower())
        else:
            result.append(char)

    return "".join(result)
