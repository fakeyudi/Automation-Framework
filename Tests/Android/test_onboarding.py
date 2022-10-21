from Tests.base_test import AndroidBaseTest
from Pages.Android.language_page import LanguagePage
from Pages.Android.login_page import LoginPage


class TestOnboarding(AndroidBaseTest):

    def setup(self):
        super().setUp()
        self.language_page = LanguagePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def teardown(self):
        super().tearDown()

    def test_onboarding(self):
        self.language_page.verify_language_page_title()
        self.language_page.select_english_language()
        self.language_page.select_continue_button()
        self.login_page.verify_login_fields()
        self.login_page.select_cancel_login()
