from selenium.webdriver.common.by import By


class Locator(object):
    def __init__(self, path, by=By.XPATH):
        self.by = by
        self.path = path
