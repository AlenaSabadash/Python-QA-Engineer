from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ProductFilterElement(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")

    def filter(self, product_name):
        self._input(self.element(self.PRODUCT_NAME), product_name)
        self.click(self.element(self.FILTER_BUTTON))
        return self
