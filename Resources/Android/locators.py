from appium.webdriver.common.mobileby import MobileBy

class LanguagePageLocators:
    """Locators for the language screen"""
    language_eng = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout"
                                    "/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout["
                                    "4]/android.widget.RelativeLayout")
    language_continue_button = (MobileBy.ID, "com.flipkart.android:id/select_btn")

class LoginPageLocators:
    """Locators for the login screen"""
    login_button = (MobileBy.ID, "com.flipkart.android:id/btn_mlogin")
    login_title = (MobileBy.ID, "com.flipkart.android:id/login_title")
    username = (MobileBy.ID, "com.flipkart.android:id/mobileNo")
    password = (MobileBy.ID, "com.flipkart.android:id/et_password")
    login_cancel_button = (MobileBy.ID, "com.flipkart.android:id/btn_cancel")