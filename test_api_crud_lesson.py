import json

import requests
import logging
from assertpy import assert_that
import pytest

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)

logger = logging.getLogger()

url_0 = "https://www.aqa.science/"

response = requests.get(url_0).json()
print(type(response))

login = "admin"
pwd = "admin123"


@pytest.fixture(autouse=True, scope="module")
def change_data():
    return {}


def test_get(change_data):
    response = requests.get(url_0)
    assert response.text == '{"users":"https://www.aqa.science/users/",' \
                            '"groups":"https://www.aqa.science/groups/"}'

    data = response.json()
    logger.info(f"json converted to internal {type(data)}")
    assert_that(data).contains_key("users", "groups")
    change_data.update(data)


def test_get_users(change_data):
    user_link = change_data["users"]
    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(user_link, auth=(login, pwd)).json()

    assert_that(response).contains_key(*expected_keys)

    print(response)


def test_get_users_2(change_data):
    next_url = "https://www.aqa.science/users/?page=2"

    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(next_url, auth=(login, pwd)).json()

    assert_that(response).contains_key(*expected_keys)

    with open("result.json", "w+") as f:
        json.dump(response, f)


def test_post_users(change_data):
    post_data = {
            "username": "FGHJKL",
            "email": "dddddd@ggggggk.com",
            "groups": []
    }
    user_link = change_data["users"]
    response = requests.post(user_link, post_data, auth=(login, pwd)).json()

    created_user_url = response['url']
    change_data["created_user_url"] = created_user_url
    # assert_that(response).contains_key(*expected_keys)

    with open("result.json", "w+") as f:
        json.dump(response, f)


def test_delete_users(change_data):
    user_link = change_data["created_user_url"]
    response = requests.delete(user_link, auth=(login, pwd))

    print(response.text)