import requests
import logging
from assertpy import assert_that
import pytest

logger = logging.getLogger("Our_logger")
# logger.setLevel(30)  # level of logging (10 it is debug), (20 it is warning)

url_0 = "https://www.aqa.science/"

response = requests.get(url_0).json()

logger.warning(f"{response}")


@pytest.fixture(autouse=True, scope="module")
def change_data():
    return {}


def test_get(change_data):
    response = requests.get(url_0)
    assert response.text == '{"users":"https://www.aqa.science/users/",' \
                            '"groups":"https://www.aqa.science/groups/"}'
    data = response.json()

    assert_that(data).contains_key("users", "groups")

    users_link = data["users"]
    group_link = data["groups"]
    change_data['user_link'] = users_link
    print(users_link, group_link)


def test_get_users(change_data):
    user_link = change_data["user_link"]
    response = requests.get(user_link)
    print(response.json())


