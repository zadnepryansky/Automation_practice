import json
import requests
import logging
from assertpy import assert_that
import pytest

# create logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

ch = logging.FileHandler("test.log")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handler
ch.setFormatter(formatter)

# add file_handler to logger
logger.addHandler(ch)

url = "https://www.aqa.science/"

response = requests.get(url).json()
print(type(response))

login = "admin"
pwd = "admin123"


# fixture for the test
@pytest.fixture(autouse=True, scope="module")
def change_data():
    return {}


# test to get response and ensure that needed keys are presented in response
def test_get(change_data):
    response = requests.get(url)
    assert response.text == '{"users":"https://www.aqa.science/users/",' \
                            '"groups":"https://www.aqa.science/groups/"}'

    data = response.json()
    logger.info(f"json converted to internal {type(data)}")
    assert_that(data).contains_key("users", "groups")
    # save dict to change data for use it in next tests
    change_data.update(data)


# test to get response from users and check that response contains expected keys
def test_get_users(change_data):
    user_link = change_data["users"]
    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(user_link, auth=(login, pwd)).json()

    # check that expected keys are presented in response
    # * to unpack list
    assert_that(response).contains_key(*expected_keys)


# test check that response from page contains expected keys
def test_get_users_2(change_data):
    next_url = "https://www.aqa.science/users/?page=2"
    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(next_url, auth=(login, pwd)).json()
    assert_that(response).contains_key(*expected_keys)
    # save data in json
    with open("result.json", "w+") as f:
        json.dump(response, f)


# test check that user can be created
def test_post_users(change_data):
    post_data = {
        "username": "SOMETHING",
        "email": "dddddd@k.com",
        "groups": []
    }
    expected_keys = ["username", "email", "groups"]
    user_link = change_data["users"]
    response = requests.post(user_link, post_data, auth=(login, pwd)).json()
    created_user_url = response['url']
    change_data["created_user_url"] = created_user_url
    assert_that(response).contains_key(*expected_keys)
    # save data in json
    with open("result.json", "w+") as f:
        json.dump(response, f)


# test check that user be able to change used PUT
def test_put_users(change_data):
    put_data = {
        "username": "SOMETHING",
        "email": "own@gmail.com",
        "groups": []
    }
    user_link = change_data["created_user_url"]
    response = requests.put(user_link, put_data, auth=(login, pwd)).json()
    # check that user mail is update
    assert_that(response).contains_value("own@gmail.com")


# test check that user be able to delete
def test_delete_users(change_data):
    # use old link
    user_link = change_data["created_user_url"]
    # delete user
    response = requests.delete(user_link, auth=(login, pwd))


# test to update user
def test_post_user_2(change_data):
    post_data = {
        "username": "John",
        "email": "smith@gmail.com",
        "groups": []
    }
    expected_values = ["John", "smith@gmail.com"]
    user_link = change_data["users"]
    response = requests.post(user_link, post_data, auth=(login, pwd)).json()
    created_user_url = response['url']
    change_data["created_new_user_url"] = created_user_url
    # check user
    assert_that(response).contains_value(*expected_values)


# test to delete user_2
def test_delete_user_2(change_data):
    user_link = change_data["created_new_user_url"]
    response = requests.delete(user_link, auth=(login, pwd))

