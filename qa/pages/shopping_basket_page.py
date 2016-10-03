from __future__ import absolute_import

from .page_object import PageObject
import selenium.webdriver.support.ui as ui


class ShoppingBasketPage(PageObject):

    def __init__(self):
        url = None
        super(ShoppingBasketPage, self).__init__(url)

    def is_product_displayed(self):
        wait = ui.WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver
                             .find_element_by_css_selector("#activeCartViewForm > div.sc-list-body > div"))
        return element.get_attribute("data-item-count") == '1'
