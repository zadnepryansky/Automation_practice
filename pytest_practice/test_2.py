import requests
from test_1 import url_1

performance_error = []


def test_performance(run):
    response = requests.get(url_1)
    assert response.elapsed.total_seconds() < 1, \
        performance_error.append(f' Time is {response.elapsed.total_seconds()}')
