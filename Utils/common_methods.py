from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class WaitForElement:
    @staticmethod
    def wait(driver, id, time_out=100):
        try:
            WebDriverWait(driver, time_out).until(
                lambda driver: driver.find_element(*id))
        except TimeoutException:
            print('Not able to find ID:' + id)

class CaptureScreen:
    @staticmethod
    def capture(driver, filename, platform):
        """Captures a screenshot of the current page"""
        if platform == 'WEB':
            driver.save_screenshot("Screenshots/Web"+filename+".png")
        else:
            driver.get_screenshot_as_file("Screenshots/Android"+filename+".png")

# def captureScreen(driver, filename):
#     """Captures a screenshot of the current page"""
#     driver.save_screenshot("Screenshots/"+filename+".png")