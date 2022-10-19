from enum import Enum

from selenium import webdriver as wd
from appium import webdriver as ad
from appium.options.android import UiAutomator2Options
from Drivers.capabilities import AppDesiredCapabilities


class Platform(Enum):
    WEB = 1
    ANDROID = 2
    iOS = 3


class Driver():
    def __init__(self, platform):
        self.platform = platform
        self.driver = None

    android_options = UiAutomator2Options().load_capabilities(AppDesiredCapabilities.android_desired_cap)

    def get_driver(self):
        if self.platform == Platform.WEB:
            self.driver = wd.Chrome()
        elif self.platform == Platform.ANDROID:
            self.driver = ad.Remote("http://hub.browserstack.com/wd/hub", options=self.android_options)
        elif self.platform == Platform.iOS:
            self.driver = ad.Remote()
        return self.driver
