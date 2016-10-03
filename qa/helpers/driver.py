from selenium import webdriver


class DriverFactory(object):

    def __init__(self, browser_name):
        self.browser_name = browser_name

    def create_webdriver_chrome(self):
        wd = webdriver.Chrome()
        return wd

    def create(self):
        fn = getattr(self, "create_webdriver_{}".format(self.browser_name))
        return fn()
