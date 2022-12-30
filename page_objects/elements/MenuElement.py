from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MenuElement(BasePage):
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog a")
    PRODUCTS_SUBMENU = (By.LINK_TEXT, "Products")
    CUSTOMERS_MENU = (By.CSS_SELECTOR, "#menu-customer a")
    CUSTOMERS_SUBMENU = (By.XPATH, "//ul[@id='collapse5']//a")

    @property
    def catalog_menu(self):
        return self.element(self.CATALOG_MENU)

    @property
    def customers_menu(self):
        return self.element(self.CUSTOMERS_MENU)

    @property
    def products_submenu(self):
        return self.element(self.PRODUCTS_SUBMENU)

    @property
    def customers_submenu(self):
        return self.element(self.CUSTOMERS_SUBMENU)
