from Pages.Android.base_page import BasePage
from Resources.Android.locators import LanguagePageLocators
from Utils.common_methods import CaptureScreen


class LanguagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_language_page_title(self):
        pass

    def select_english_language(self):
        try:
            self.click(LanguagePageLocators.language_eng)
        except:
            CaptureScreen.capture(self.driver, "language_page_error")

    def select_continue_button(self):
        try:
            self.click(LanguagePageLocators.language_continue_button)
        except:
            CaptureScreen.capture(self.driver, "language_page_continue_button_error")