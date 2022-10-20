from Drivers.driver_class import Driver, Platform

class WebBaseTest:
    def setUp(self):
        self.driver = Driver(Platform.WEB).get_driver()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

class AndroidBaseTest:
    def setUp(self):
        self.driver = Driver(Platform.ANDROID).get_driver()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()