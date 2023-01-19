
import time

from pytest_bdd import scenario, given, when, then,  parsers
from selenium import webdriver


@scenario('publish_article.feature', 'Go to the page')
def test_publish():
    pass

@given("Our driver")
def step_impl(request):
    driver = webdriver.Chrome()
    request.driver = driver


@when("I navigate to the page")
def step_impl(request):
    client = request.driver
    client.get(request.url)
    time.sleep(5)


@then("Werify the page content")
def step_impl(request):
    request.driver.close()
    print("done")

@given(parsers.re("Customized URL '(?P<name_0>.*)'"))
def first_user(request, name_0):
    request.url = name_0