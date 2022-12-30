import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminAuthPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.path = "admin"

    @allure.step("Логин пользователя {username}")
    def login(self, username, password):
        self._input(self.element(self.USERNAME_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def open(self):
        self._open(f"{self.url}/{self.path}")
        return self
