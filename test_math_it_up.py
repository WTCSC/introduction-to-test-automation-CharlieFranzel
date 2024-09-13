import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  assert math_it_up.is_even(3) == False
  assert math_it_up.is_even(20)
  assert math_it_up.is_even(0)

def test_is_odd():
  assert math_it_up.is_odd(3)
  assert math_it_up.is_odd(20) == False
  assert math_it_up.is_odd(0) == False

def test_mean():
  assert math_it_up.mean([2,3,5,2]) == 3
  assert math_it_up.mean([89, 31, 48, 11, 9, 68, 95, 3, 2, 41]) == 39.7

def test_median():
  assert math_it_up.median([12, 1, 172, 14, 86, 12.2]) == 13.1
  assert math_it_up.median([2, 3, 5, 6, 8, 1, 3]) == 3
def test_mode():
  assert math_it_up.mode([1, 1, 1, 0, 2, 3, 3]) == [1]
  assert math_it_up.mode([2, 2, 3, 3, 4, 5]) == [2, 3]