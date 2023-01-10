# Conftest collecting all fixture for all tests

import subprocess
import pytest


def collect():
    return 42


@pytest.fixture(scope='function')   # Before all tests
def docker():
    port = 3456
    subprocess.run(f"docker run -d --name selenium_chrome -p"
                   f"{port}:4444 -v "
                   f"/dev/shm:/dev/shm selenium/standalone-chrome",
                   shell=True, check=True)
    yield
    subprocess.run("docker rm --force selenium_chrome", shell=True, check=True)


@pytest.fixture(autouse=True)
def fix_one():
    print("setup")
    yield
    print("Teardown")


@pytest.fixture()
def fix_special():
    data = collect()
    print("special setup")


@pytest.fixture(scope="module", autouse=True)
def th():
    yield
    print("shutdown docker infrastructure")

