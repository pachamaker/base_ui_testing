"""
Example of file with locators for search page
"""
from selenium.webdriver.common.by import By

from . import Locator


class SearchLocators(object):
    @property
    def search_input(self):
        return Locator('sfdiv', By.ID)

    @property
    def result_stats(self):
        return Locator('resultStats', By.ID)
    
    @property
    def result_not_found(self):
        return Locator('//div[@class="mnr-c"]')
