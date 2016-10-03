from __future__ import absolute_import

from .page_object import PageObject
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException


class AmazonProductPage(PageObject):

    def __init__(self):
        url = "https://www.amazon.com/Sony-DSCW800-Digital-Camera-Black/dp/B00I8BIBCW"
        super(AmazonProductPage, self).__init__(url)

    def add_to_cart(self):
        wait = ui.WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element_by_id("submit.add-to-cart"))
        element.click()

    def dismiss_protection_plan_popover(self):
        wait = ui.WebDriverWait(self.driver, 10)
        try:
            element = wait.until(lambda driver: self.driver.find_element_by_id("siNoCoverage-announce"))
            element.click()
        except TimeoutException:
            pass
