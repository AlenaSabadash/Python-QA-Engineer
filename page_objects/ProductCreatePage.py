import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductCreatePage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    MODEL = (By.CSS_SELECTOR, "#input-model")
    TAB_DATA = (By.CSS_SELECTOR, "a[href='#tab-data']")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")

    @allure.step("Создание нового продукта: {product_name}, {meta_tag}, {model}")
    def create(self, product_name, meta_tag, model):
        self._input(self.element(self.PRODUCT_NAME), product_name)
        self._input(self.element(self.META_TAG_TITLE), meta_tag)
        self.click(self.element(self.TAB_DATA))
        self._input(self.element(self.MODEL), model)
        self.click(self.element(self.SAVE_BUTTON))
        return self
