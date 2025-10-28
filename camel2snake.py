def camel_to_snake(camel_string):
    """
    Convert camel case string to snake case (lowercase with underscores).
    
    Args:
        camel_string (str): Input string in camel case
        
    Returns:
        str: String in snake case format
    """
    if not camel_string:
        return camel_string
    
    result = []
    for i, char in enumerate(camel_string):
        if char.isupper():
            # Add underscore before capital letters (except first character)
            if i > 0:
                result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    
    return ''.join(result)


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "camelCase",
        "CamelCase",
        "CAMELCase",
        "camelCASE",
        "CamelCASEString",
        "XMLHttpRequest",
        "iPhone",
        "URLShortener",
        "myVariableName",
        "ABC",
        "abc",
        ""
    ]
    
    print("Camel Case to Snake Case Converter")
    print("-" * 40)
    
    for test in test_cases:
        result = camel_to_snake(test)
        print(f"{test!r:20} -> {result!r}")


# Alternative one-liner using regular expressions (uncomment to use)
"""
import re

def camel_to_snake_regex(camel_string):
    # Insert underscore before capital letters and convert to lowercase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
"""
