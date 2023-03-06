from selenium.webdriver.common.by import By

class PageObject:

    field_locator = """//*[@id="searchInput"]"""

    expected_text = "automation"

    search_locator = """//*[@id="search-form"]/fieldset/button/i"""

    italian_nanduage = """//*[@id="js-link-box-it"]/strong"""




# page_url = https://www.wikipedia.org/
class WikipediaPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_field = driver.find_element(By.CSS_SELECTOR, "input[id='searchInput']")
        self.i_search_input_button = self.driver.find_elements(By.CSS_SELECTOR, "i[data-jsl10n='search-input-button']")

    def search(self, value):
        self.search_field.send_keys(value)
        self.i_search_input_button[0].click()

    def i_search_input_button(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "i[data-jsl10n='search-input-button']")

    def strong_italiano(self):
        return self.driver.find_elements(By.TAG_NAME, "strong")
