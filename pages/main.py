"""
Example of file with Page for test on main page of google.ru
"""
from pages import BasePage
from pages.locators.main import MainLocators
from settings import URL


class MainPage(BasePage):
    URL_PATH = '/'

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.locators = MainLocators()

    def open(self):
        self.open_page('%s%s' % (URL, self.URL_PATH))

    def click_on_logo(self):
        self.click(self.locators.logo)

    def click_search_button(self):
        self.click(self.locators.search_button)

    def type_in_search(self, text):
        self.input_text(self.locators.search_field, text)

    # Validators
    def is_logo_visible(self):
        return self.is_displayed(self.find_element(self.locators.logo))

    def is_search_enabled(self):
        self.is_displayed(self.find_element(self.locators.search_field)) and True

    def is_text_in_search(self, text):
        search = self.find_element(self.locators.search_field)
        return self.is_displayed(search) and text in search.text
