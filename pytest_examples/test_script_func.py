# import pytest
# tests using pure python
from func_test import our_func


def test_funct_2():
    assert our_func(1, 2, 3) != 3


def test_funct_3():
    assert our_func(5, 6, 2) == 12


def test_funct_4():
    assert our_func(5, 5, 2) == 2


def test_funct_1():
    assert our_func(1, 2, 3) == 6