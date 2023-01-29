import pytest


@pytest.fixture
def run():
    print("Test is run")


@pytest.fixture
def save_data():
    with open('Test.log', 'w+') as f:
        f.write("Test data")


