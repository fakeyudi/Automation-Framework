from selenium import webdriver

def captureScreen(driver, filename):
    """Captures a screenshot of the current page"""
    driver.save_screenshot("Screenshots/"+filename+".png")