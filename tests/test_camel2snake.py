"""Tests for camel_to_snake function."""

import pytest
from camel2snake import camel_to_snake


class TestCamelToSnake:
    """Test cases for camel case to snake case conversion."""

    def test_simple_camel_case(self):
        """Test standard camelCase conversion."""
        assert camel_to_snake("camelCase") == "camel_case"

    def test_pascal_case(self):
        """Test PascalCase (leading capital) conversion."""
        assert camel_to_snake("CamelCase") == "camel_case"

    def test_consecutive_capitals_beginning(self):
        """Test consecutive capitals at start."""
        assert camel_to_snake("CAMELCase") == "c_a_m_e_l_case"

    def test_consecutive_capitals_end(self):
        """Test consecutive capitals at end."""
        assert camel_to_snake("camelCASE") == "camel_c_a_s_e"

    def test_mixed_consecutive_capitals(self):
        """Test mixed consecutive capitals."""
        assert camel_to_snake("CamelCASEString") == "camel_c_a_s_e_string"

    def test_acronym_in_middle(self):
        """Test acronym in the middle of string."""
        assert camel_to_snake("XMLHttpRequest") == "x_m_l_http_request"

    def test_lowercase_prefix(self):
        """Test string with lowercase prefix before capital."""
        assert camel_to_snake("iPhone") == "i_phone"

    def test_acronym_prefix(self):
        """Test acronym as prefix."""
        assert camel_to_snake("URLShortener") == "u_r_l_shortener"

    def test_long_variable_name(self):
        """Test typical variable name."""
        assert camel_to_snake("myVariableName") == "my_variable_name"

    def test_all_capitals(self):
        """Test all uppercase string."""
        assert camel_to_snake("ABC") == "a_b_c"

    def test_all_lowercase(self):
        """Test all lowercase (no change needed)."""
        assert camel_to_snake("abc") == "abc"

    def test_empty_string(self):
        """Test empty string returns empty string."""
        assert camel_to_snake("") == ""

    def test_single_lowercase_letter(self):
        """Test single lowercase letter."""
        assert camel_to_snake("a") == "a"

    def test_single_uppercase_letter(self):
        """Test single uppercase letter."""
        assert camel_to_snake("A") == "a"

    def test_two_words(self):
        """Test simple two-word camelCase."""
        assert camel_to_snake("firstName") == "first_name"

    def test_three_words(self):
        """Test three-word camelCase."""
        assert camel_to_snake("getFirstName") == "get_first_name"

    def test_none_input(self):
        """Test None input returns None."""
        assert camel_to_snake(None) is None

    def test_numbers_in_string(self):
        """Test string with numbers (numbers preserved)."""
        assert camel_to_snake("test123Value") == "test123_value"

    def test_leading_number(self):
        """Test string starting with numbers."""
        assert camel_to_snake("123testValue") == "123test_value"


class TestEdgeCases:
    """Edge case tests."""

    def test_already_snake_case(self):
        """Test string already in snake_case is modified (uppercase removed)."""
        assert camel_to_snake("snake_case") == "snake_case"

    def test_mixed_separators(self):
        """Test string with existing underscores."""
        assert camel_to_snake("some_CamelCase") == "some__camel_case"

    def test_whitespace(self):
        """Test string with whitespace (preserved)."""
        assert camel_to_snake("camel Case") == "camel _case"

    def test_special_characters(self):
        """Test string with special characters (preserved)."""
        assert camel_to_snake("camel-Case") == "camel-_case"
