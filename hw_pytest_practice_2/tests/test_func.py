from hw_pytest_practice_2.func import add
import pytest

error = []


@pytest.mark.parametrize("a, b, expected_result", [(10, 20, 30),
                                                       (20, 40, 60),
                                                       (11, 22, 33)])
def test_add(a, b, expected_result):
    result = add(a, b)
    assert result == expected_result



