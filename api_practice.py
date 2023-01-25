import requests
import logging
from assertpy import assert_that

logger = logging.getLogger("Our_logger")
# logger.setLevel(30)  # level of logging (10 it is debug), (20 it is warning)

url_0 = "https://www.aqa.science/"

response = requests.get(url_0).json()

logger.warning(f"{response}")


def test_get():
    response = requests.get(url_0)
    assert response.text == '{"users":"https://www.aqa.science/users/",' \
                            '"groups":"https://www.aqa.science/groups/"}'
    data = response.json()

    assert_that(data).contains_key("users", "groups")

    users_link = data["users"]
    group_link = data["groups"]

    print(users_link, group_link)


