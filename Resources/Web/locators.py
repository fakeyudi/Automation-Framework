from selenium.webdriver.common.by import By


class LoginModalLocators:
    """Locators for the login modal"""
    username = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    password = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
    login_button = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button")
    login_title = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/span/span")
    close_button = (By.XPATH, "/html/body/div[2]/div/div/button")