from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    REGISTER = (By.LINK_TEXT, "Register")
    CURRENCY = (By.CSS_SELECTOR, "#form-currency")
    EURO = (By.NAME, "EUR")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".search-arrow__button")

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.path = "index.php?route=common/home"

    @property
    def my_account(self):
        return self.element(self.MY_ACCOUNT)

    @property
    def register(self):
        return self.element(self.REGISTER)

    @property
    def currency_dropdown(self):
        return self.element(self.CURRENCY)

    @property
    def submit_button(self):
        return self.element(self.SUBMIT_BUTTON)

    def currency_item(self, name):
        return self.element((By.NAME, name))

    def open(self):
        self._open(f"{self.url}/{self.path}")
        return self
