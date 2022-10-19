from Tests.Web.base_test import WebBaseTest
from Pages.Web.login_modal import LoginModal


class TestLoginModal(WebBaseTest):
    def setUp(self):
        super().setUp()
        self.login_modal = LoginModal(self.driver)

    def test_login_modal_title(self):
        self.login_modal.verify_login_modal_title()

    def test_login_modal_close_button(self):
        self.login_modal.verify_login_modal_close_button()

    def test_login_modal_email_field(self):
        self.login_modal.verify_login_modal_email_field()

    def test_login_modal_password_field(self):
        self.login_modal.verify_login_modal_password_field()
