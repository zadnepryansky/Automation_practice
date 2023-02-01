import time

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(300)

element_path = '//*[@id="W0wltc"]/div'
driver.get("https://google.com")

element = driver.find_element(By.XPATH, element_path)

text_eleent = element.text

element.click()

search_bar = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

search_bar.send_keys("Wikipedia")

search_bar.send_keys(Keys.RETURN)

wiki_link = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3'

wiki_header_class = 'central-textlogo-wrapper'


driver.find_element(By.XPATH, wiki_link).click()

expected_element = driver.find_element(By.CLASS_NAME, wiki_header_class)

print(expected_element.text)


print(expected_element.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[1]/h1/strong').get_attribute("data-jsl10n"))
print(driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[1]/h1/strong').get_attribute("data-jsl10n"))


driver.quit()