"""
Example of file with locators for main page
"""
from selenium.webdriver.common.by import By

from . import Locator


class MainLocators(object):
    """
    Main page google locators
    """
    @property
    def logo(self):
        return Locator('hplogo', By.ID)
    
    @property
    def search_field(self):
        return Locator('//div[@class="lst-c"]//input[@id="lst-ib"]')

    @property
    def search_button(self):
        return Locator('btnG', By.NAME)
