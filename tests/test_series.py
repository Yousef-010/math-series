import pytest
from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci_zeros():
    """
    This function tests the fibonacci function by 0
    """
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    """
    This function tests the fibonacci function by 1
    """
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_else():
    """
    This function tests the fibonacci function by ever number grater than 1
    """
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


#--------------------------------------------------------------------------

def test_lucas_zero():
    """
    This function tests the lucas function  by 0 and return 2
    """
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    """
    This function tests the lucas function  by 1 and return 1
    """
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_else():
    """
    This function tests the lucas function  by every number else
    """
    actual = lucas(5)
    expected = 11
    assert actual == expected

# -------------------------------------------------------------------------------------------


def test_sum_series_zero():
    """
    This function tests the lucas function  by 0 and return the first index
    """
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_one():
    """
    This function tests the lucas function  by 1 and return the second index
    """
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_else():
    """
    This function tests the lucas function  by every number and return the index value based on sum_series
    """
    actual = sum_series(5)
    expected = 5
    assert actual == expected
