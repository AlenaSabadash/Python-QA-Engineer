from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductsListPage(BasePage):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-danger")
    PRODUCTS_TABLE = (By.TAG_NAME, "tbody")

    @property
    def add_new(self):
        return self.element(self.ADD_BUTTON)

    @property
    def delete_product(self):
        return self.element(self.DELETE_BUTTON)

    def get_product_name(self):
        table = self.element(self.PRODUCTS_TABLE)
        row = table.find_elements(By.TAG_NAME, "td")
        if len(row) > 2:
            return row[2].text
        return ""

    @property
    def checkbox(self):
        table = self.element(self.PRODUCTS_TABLE)
        return table.find_element(By.TAG_NAME, "input")
