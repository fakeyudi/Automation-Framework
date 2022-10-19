from enum import Enum
from selenium import webdriver

class platform(Enum):
    WEB = 1
    ANDROID = 2
    iOS = 3

class Driver():
    def __init__(self, platform):
        self.platform = platform
        self.driver = None

    def get_driver(self):
        if self.platform == platform.WEB:
            self.driver = webdriver.Chrome()
        elif self.platform == platform.ANDROID:
            self.driver = webdriver.Remote()
        elif self.platform == platform.iOS:
            self.driver = webdriver.Remote()
        return self.driver