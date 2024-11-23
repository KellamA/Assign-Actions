# tests/test_app.py

import pytest
from src.app import add_numbers

def test_add_numbers_positive():
    """
    Test case to check addition of positive numbers.
    """
    assert add_numbers(3, 5) == 8

def test_add_numbers_negative():
    """
    Test case to check addition of negative numbers.
    """
    assert add_numbers(-3, -5) == -8

def test_add_numbers_mixed():
    """
    Test case to check addition of a positive and a negative number.
    """
    assert add_numbers(3, -5) == -2
