import pytest


def setup():
    print("Basic setup into module")


def teardown():
    print("Basic teardown into module")


# def setup_module(module):
#     print('module setup')
#
#
# def teardown_function(function):
#     print('function setup')


def setup_function(function):
    print('Function setup')


def teardown_function(function):
    print('function teardown')

@pytest.mark.smoke
def test_number_3_4():
    print('test 3*4')
    pytest.data = 345        # We can use pytest.test_data to sharing another tests
    assert 3 * 4 == 12


def test_strings_a_3():
    local_data = pytest.data
    print("test a*3")
    assert local_data == 345
    # assert 'a' * 3 == "aaa"
