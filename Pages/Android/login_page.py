from Pages.Android.base_page import BasePage
from Resources.Android.locators import LoginPageLocators
from Utils.common_methods import CaptureScreen, WaitForElement
from Drivers.driver_class import Driver, Platform


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_login_fields(self):
        try:
            WaitForElement.wait(self.driver, LoginPageLocators.login_button).is_displayed()
        except:
            CaptureScreen.capture(self.driver, "login_page_fields_error", 'MOBILE')

    def select_cancel_login(self):
        try:
            self.click(LoginPageLocators.login_cancel_button)
        except:
            CaptureScreen.capture(self.driver, "login_page_cancel_error", 'MOBILE')
