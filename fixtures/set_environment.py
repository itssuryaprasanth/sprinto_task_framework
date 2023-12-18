import pytest

from wrappers.browser_driver import BrowserDriver
from utilities.custom_logger import CustomLogger

log = CustomLogger()


class Environment:
    def __init__(self):
        self.driver = ""

    def get_driver(self):
        return self.driver

    def set_driver(self, driver):
        self.driver = driver


@pytest.fixture()
def create_environment():
    driver = BrowserDriver()
    env = Environment()
    env.set_driver(driver=driver)
    return env
