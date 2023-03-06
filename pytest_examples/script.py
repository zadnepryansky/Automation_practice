import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page_objects import PageObject as PO
from page_objects import WikipediaPage


@pytest.fixture(scope="function")
def driver():
    url = "https://wikipedia.org"
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    time.sleep(1)
    yield driver
    time.sleep(1)
    driver.quit()


def test_web_test(driver):
    element = driver.find_element(By.XPATH, PO.field_locator)
    element.send_keys(PO.expected_text)
    element_2 = driver.find_element(By.XPATH, PO.search_locator)
    element_2.click()


def test_web_test_1(driver):
    element = driver.find_element(By.XPATH, PO.field_locator)
    element.send_keys(PO.expected_text)
    element_2 = driver.find_element(By.XPATH, PO.italian_nanduage)
    element_2.click()


def test_web_test_2(driver):
    page = WikipediaPage(driver)
    page.search("completely new search")

