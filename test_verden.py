# open wikipedia
# find page for First world war
# Find Verden apearanc on page
# additional Find on page 11.11.18
# additionally find time
import logging
import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from page_obj import Config, Wikipedia

# create logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler("test.log")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handler
ch.setFormatter(formatter)

# add file_handler to logger
logger.addHandler(ch)


expected = Wikipedia(Config.url)



# first_heading_id = "firstHeading"
# search_result = driver.find_element(By.ID, first_heading_id)
# logger.debug(f'Found result is {search_result.text}')
# assert search_result.text == 'Результаты поиска'
#time.sleep(10)
@pytest.fixture(scope='function')
def init_step():
    driver = webdriver.Chrome()
    yield driver
    logger.info('Test finished')
    driver.close()


@pytest.fixture(scope='function')
def landing_page(init_step):
    driver = init_step
    logger.info('Test started')
    driver.get(expected.url)
    search_filed = driver.find_element(By.ID, expected.search_field_id)
    search_filed.send_keys(expected.info)
    search_filed.send_keys(Keys.ENTER)
    return driver


@pytest.mark.first
@pytest.mark.all
def test_pattern(landing_page):
    logger.info('Started test pattern')
    driver = landing_page
    first_heading_id = "firstHeading"
    search_result = driver.find_element(By.ID, first_heading_id)
    logger.debug(f'Found result is {search_result.text}')
    assert search_result.text == 'World War I'
    driver.get(expected.url)
    search_filed = driver.find_element(By.ID, expected.search_field_id)
    search_filed.send_keys('expected.info')
    search_filed.send_keys(Keys.ENTER)
    search_result = driver.find_element(By.ID, first_heading_id)
    logger.debug(f'Found result is {search_result.text}')
    assert search_result.text != 'World War I'


@pytest.mark.second
def test_pattern0(landing_page):
    logger.info('Test pattern0 started')
    driver = landing_page
    first_heading_id = "firstHeading"
    search_result = driver.find_element(By.ID, first_heading_id)
    logger.debug(f'Found result is {search_result.text}')
    assert search_result.text == 'World War I'