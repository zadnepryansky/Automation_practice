import pytest
import requests

url_1 = "https://jsonplaceholder.typicode.com/posts"
url_2 = "https://api.chucknorris.io/jokes/random"

errors = []


def add_data(data):
    with open('Output_log.txt', 'a+') as f:
        f.write(f"{data}\n")


def test_one(save_data):
    response = requests.get(url_1)
    stat_code = response.status_code
    assert stat_code == 200, errors.append(stat_code)


@pytest.mark.view_data
def test_two():
    response = requests.get(url_2)
    check = response.json()
    check_info = check.get("value")
    assert "Chuck" or 'CHUCK' in check_info, errors.append('no joke :(')
    add_data(check_info)


def test_three():
    response = requests.get(url_1)
    check = response.text
    assert len(check) > 0, errors.append('Response url_2 is empty')


@pytest.mark.add
def test_four():
    data = {'title': ' new_title', 'body': 'new_body'}
    response = requests.post(url_1, json=data)
    stat_code = response.status_code
    datatest = response.text
    assert stat_code == 201, errors.append(stat_code)


performance_error = []


def test_performance():
    response = requests.get(url_1)
    assert response.elapsed.total_seconds() < 1, \
        performance_error.append(f' Time is {response.elapsed.total_seconds()}')


