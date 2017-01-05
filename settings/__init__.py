"""
Parent file with settings, can be override by local_settings
"""
# Link to selenium-hub like 'http://127.0.0.1:4444/wd/hub'
REMOTE = False
SELENIUM_HUB = None
DESIRED_CAPABILITIES = {
    'browserName': 'chrome',
    'version': '',
    'platform': 'ANY',
    'javascriptEnabled': True
}
IMPLICITLY_WAIT = 10
PAGE_TIMEOUT = 30

URL = 'http://google.ru'


try:
    from .local_settings import *
except ImportError:
    pass
