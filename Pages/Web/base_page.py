from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be visible"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Wait for an element to be clickable"""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_invisible(self, locator, timeout=10):
        """Wait for an element to be invisible"""
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_element_to_be_present(self, locator, timeout=10):
        """Wait for an element to be present"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_selected(self, locator, timeout=10):
        """Wait for an element to be selected"""
        return WebDriverWait(self.driver, timeout).until(EC.element_located_to_be_selected(locator))

    def wait_for_element_to_be_deselected(self, locator, timeout=10):
        """Wait for an element to be deselected"""
        return WebDriverWait(self.driver, timeout).until(EC.element_located_selection_state_to_be(locator, False))

    def wait_for_element_to_be_stale(self, locator, timeout=10):
        """Wait for an element to be stale"""
        return WebDriverWait(self.driver, timeout).until(EC.staleness_of(locator))

    def wait_for_element_to_be_located(self, locator, timeout=10):
        """Wait for an element to be located"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_located_and_clickable(self, locator, timeout=10):
        """Wait for an element to be located and clickable"""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_located_and_selected(self, locator, timeout=10):
        """Wait for an element to be located and selected"""
        return WebDriverWait(self.driver, timeout).until(EC.element_located_to_be_selected(locator))

    def click(self, locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title