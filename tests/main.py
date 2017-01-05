"""
Example of file with tests
"""
import pytest

from pages.main import MainPage
from pages.search import SearchPage


@pytest.allure.feature('Check main page on google.com')
class TestGoogle(object):
    @pytest.mark.categories(component='logo', suite='smoke')
    @pytest.allure.story('Check google logo')
    def test_logo(self, driver):
        page = MainPage(driver)
        with pytest.allure.step('Open google.ru'):
            page.open()

        with pytest.allure.step('Check logo'):
            assert page.is_logo_visible(), 'Logo does not visible'

    @pytest.mark.categories(component='search', suite='smoke')
    @pytest.allure.story('Check google search')
    def test_search(self, driver):
        page = MainPage(driver)
        with pytest.allure.step('Open google.ru'):
            page.open()

        with pytest.allure.step('Input something to search string'):
            page.type_in_search('Google')

        with pytest.allure.step('Click on Search button'):
            last_url = page.current_url
            page.click_search_button()

            with pytest.allure.step('Check that search page was open'):
                page = SearchPage(driver)
                next_url = page.current_url

                assert last_url != next_url, 'Transition was not occured'
                assert page.is_result_found(), 'Result was not found'
