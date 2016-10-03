class Window(object):

    def __init__(self, driver):
        self.driver = driver
        self._page = None

    @property
    def page(self):
        return self._page

    def visit(self, page_object):
        self._page = page_object
        page_object._driver = self.driver
        if self._page.url is not None:
            self.driver.get(self._page.url)
        else:
            pass
