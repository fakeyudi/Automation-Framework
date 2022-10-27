import os
import sys

sys.path.insert(0, os.path.abspath("../../.."))

from pytest_bdd import scenarios, given, when, then
from Drivers.driver_class import Driver, Platform
from Pages.Android.language_page import LanguagePage
from Pages.Android.login_page import LoginPage


scenarios('../../../Tests/Features/AppTest.feature')

@given(u'Launch the App')
def launch_app(context):
    context.driver = Driver(Platform.ANDROID).get_driver()
    context.driver.implicitly_wait(30)

@then(u'I should select English')
def select_english(context):
    language_page = LanguagePage(context.driver)
    language_page.verify_language_page_title()
    language_page.select_english_language()
    language_page.select_continue_button()

@then(u'I should close Login')
def close_login(context):
    login_page = LoginPage(context.driver)
    # login_page.verify_login_fields()
    login_page.select_cancel_login()

@then(u'I should click on Mobile')
def click_mobile(context):
    pass

@when(u'I select iPhone')
def select_iphone(context):
    pass

@then(u'Close the App')
def close_app(context):
    context.driver.quit()