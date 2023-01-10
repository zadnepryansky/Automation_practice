import pytest
import requests
# Particular test using fixture


# @pytest.fixture(scope='function')             # 'function' = where fixture were call
@pytest.fixture(scope='module')                 # 'module' = all file
def fixt():
    print('Started')
    yield {'initial': []}                       # pytest.test_data in test_script_pytest
    print('Test ended')


@pytest.fixture  # 'module' = all file
def fixt_new():
    print('start test')
    yield
    print('finish test')


def test_one(fixt, fixt_new):
    response = requests.get("https://google.com")
    fixt["test_data"] = response.text
    assert response.status_code == 200


def test_second(fixt, fixt_new):
    print('second test')
    assert len(fixt["test_data"]) > 0