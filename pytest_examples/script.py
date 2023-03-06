import time
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page_objects import PageObject as PO
from page_objects import WikipediaPage

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


@pytest.fixture(scope="module", autouse=True)
def docker_setup():
    subprocess.run(f"docker run -d --name selenium_chrome -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome",
                   shell=True, check=True)
    time.sleep(5)
    yield
    subprocess.run("docker rm --force selenium_chrome", shell=True, check=True)


@pytest.fixture(scope="function")
def driver():
    url = "https://wikipedia.org"
    driver = webdriver.Remote(command_executor=f'http://localhost:4444/wd/hub')
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
