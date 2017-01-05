# -*- coding: utf-8 -*-
"""
Example of file with Page for test on main page of google.ru
"""
from pages import BasePage
from pages.locators.search import SearchLocators
from settings import URL


class SearchPage(BasePage):
    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)
        self.locators = SearchLocators()

    def open(self, query):
        self.open_page('%s/#q=%s' % (URL, query))

    # Validators
    def is_result_found(self):
        result_stats = self.find_element(self.locators.result_stats)
        return self.is_displayed(result_stats)

    def is_result_not_found(self):
        result_not_found = self.find_element(self.locators.result_not_found)
        return self.is_displayed(result_not_found) and u'ничего не найдено' in result_not_found.text
