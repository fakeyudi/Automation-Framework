from _pytest.fixtures import fixture

from Tests.Web.base_test import WebBaseTest
from Pages.Web.login_modal import LoginModal


class TestLoginModal(WebBaseTest):

    def setup(self):
        super().setUp()
        self.login_modal = LoginModal(self.driver)

    def teardown(self):
        super().tearDown()

    # def test_login_modal(self):
    #     self.login_modal.verify_login_modal_title()
    #     self.login_modal.verify_login_modal_close_button()
    #     self.login_modal.verify_login_modal_email_field()
    #     self.login_modal.verify_login_modal_password_field()

    def test_login_modal_title(self):
        self.login_modal.verify_login_modal_title()

    def test_login_modal_close_button(self):
        self.login_modal.verify_login_modal_close_button()

    def test_login_modal_email_field(self):
        self.login_modal.verify_login_modal_email_field()

    def test_login_modal_password_field(self):
        self.login_modal.verify_login_modal_password_field()
