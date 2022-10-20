from Pages.Web.base_page import BasePage
from Resources.Web.locators import LoginModalLocators
from Utils.common_methods import CaptureScreen


class LoginModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.flipkart.com/")

    def verify_login_modal_title(self):
        try:
            if self.wait_for_element(LoginModalLocators.login_title).text == "Login":
                assert True
            else:
                raise AssertionError
        except AssertionError:
            CaptureScreen.capture(self.driver, "login_modal_title_error")

    def verify_login_modal_close_button(self):
        try:
            if self.wait_for_element(LoginModalLocators.close_button).is_displayed():
                assert True
            else:
                raise AssertionError
        except AssertionError:
            CaptureScreen.capture(self.driver, "login_modal_close_button_error")

    def verify_login_modal_email_field(self):
        try:
            if self.wait_for_element(LoginModalLocators.username).is_displayed():
                assert True
            else:
                raise AssertionError
        except AssertionError:
            CaptureScreen.capture(self.driver, "login_modal_email_field_error")

    def verify_login_modal_password_field(self):
        try:
            if self.wait_for_element(LoginModalLocators.password).is_displayed():
                assert True
            else:
                raise AssertionError
        except AssertionError:
            CaptureScreen.capture(self.driver, "login_modal_password_field_error")
