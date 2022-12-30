from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ShoppingCartElement(BasePage):
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    SHOPPING_CART_TABLE = (By.XPATH, "//div[@id='cart']//tbody")

    @property
    def cart_button(self):
        return self.element(self.CART_BUTTON)

    @property
    def get_product_name(self):
        table = self.element(self.SHOPPING_CART_TABLE)
        row = table.find_elements(By.TAG_NAME, "td")
        if len(row) > 2:
            return row[1].text
        return ""

    @property
    def delete_from_cart_button(self):
        table = self.element(self.SHOPPING_CART_TABLE)
        row = table.find_elements(By.TAG_NAME, "td")
        if len(row) > 2:
            return row[-1]
        return None
