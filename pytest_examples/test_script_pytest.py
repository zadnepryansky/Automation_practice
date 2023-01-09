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


def test_number_3_4(request):
    print('test 3*4')
    request.data = 345
    assert 3 * 4 == 12


def test_strings_a_3(request):
    local_data = request.data
    print("test a*3")
    assert 'a' * 3 == "aaa"
