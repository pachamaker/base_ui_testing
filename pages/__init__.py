from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import Locator
from settings import IMPLICITLY_WAIT


class BasePage(object):
    """ Base class, should be inherit by pages """
    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    def find_element(self, locator, element=None):
        """ Method for find one element with waiter, if element not found in DOM, from root or from WebElement
        :param locator: Locator
        :param element: WebElement or None
        :return: WebElement
        """
        try:
            root = element or self.driver
            return WebDriverWait(root, IMPLICITLY_WAIT).until(EC.presence_of_element_located((locator.by,
                                                                                              locator.path)))

        except NoSuchElementException:
            return

    def find_elements(self, locator, element=None):
        """ Method for finding list of elements, from root or from WebElement
        :param locator: Locator
        :param element: WebElement or None
        :return: list of WebElements
        """
        root = element or self.driver
        return root.find_elements(by=locator.by, value=locator.path)

    def open_page(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def input_text(self, locator, text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def is_displayed(self, element):
        """ Check if WebElement is displayed on page
        :param element: WebElement or Locator
        :return: boolean
        """
        if isinstance(element, Locator):
            element = self.find_element(element)

        return element.is_displayed() if element else False
