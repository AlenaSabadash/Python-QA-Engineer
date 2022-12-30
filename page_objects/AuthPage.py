import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AuthPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value="Login"]')
    ALERT_BADGE = (By.CSS_SELECTOR, ".alert")

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.path = "index.php?route=account/login"

    @allure.step("Логин пользователя {username}")
    def login(self, username, password):
        self._input(self.element(self.EMAIL_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    @property
    def alert_badge(self):
        return self.element(self.ALERT_BADGE)

    def open(self):
        self._open(f"{self.url}/{self.path}")
        return self
