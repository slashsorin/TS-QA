from __future__ import absolute_import

from .page_object import PageObject
import selenium.webdriver.support.ui as ui


class AddedToBasketPage(PageObject):

    def __init__(self):
        url = None
        super(AddedToBasketPage, self).__init__(url)

    def is_confirmed(self):
        wait = ui.WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element_by_id("huc-v2-order-row-confirm-text"))
        return element.text == "Added to Cart"

    def view_shopping_basket(self):
        self.driver.find_element_by_id("hlb-view-cart-announce").click()
