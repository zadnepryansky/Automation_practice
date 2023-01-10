# import pytest
# tests_hw using pure python
import pytest

from func_test import our_func


# def test_funct_2():
#     assert our_func(1, 2, 3) != 3
#
#
# def test_funct_3():
#     assert our_func(5, 6, 2) == 12
#
#
# def test_funct_4():
#     assert our_func(5, 5, 2) == 2


test_data = [(10, 5, 3, 8),
             (5, 6, 2, 13),
             (5, 5, 2, 2),
             (100, 200, 0, 300)]


@pytest.mark.parametrize("value, value_1, value_2, result", test_data)  # add some cases
def test_funct_1(value, value_1, value_2, result):
    assert our_func(value, value_1, value_2) == result
