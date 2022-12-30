from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.mixins.OpenablePageMixin import OpenablePageMixin


class LaptopNotebookPage(BasePage, OpenablePageMixin):
    PRODUCT_BLOCK = (By.XPATH, "//div[contains(@class, 'product-layout')]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[contains(@class, 'product-layout')]//button")
    ALERT_BADGE = (By.CSS_SELECTOR, ".alert")

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.path = "laptop-notebook"

    @property
    def get_product_name(self):
        item = self.element(self.PRODUCT_BLOCK)
        return item.find_element(By.TAG_NAME, "h4").text

    @property
    def add_to_cart(self):
        return self.element(self.ADD_TO_CART_BUTTON)

    @property
    def alert_badge(self):
        return self.element(self.ALERT_BADGE)
