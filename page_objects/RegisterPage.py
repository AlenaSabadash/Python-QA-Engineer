import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    PRIVACY_POLICY = (By.NAME, "agree")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")

    @allure.step("Регистрация нового пользователя: {first_name}, {last_name}, {email}, {telephone}, {password}")
    def register(self, first_name, last_name, email, telephone, password):
        self._input(self.element(self.FIRST_NAME), first_name)
        self._input(self.element(self.LAST_NAME), last_name)
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.TELEPHONE), telephone)
        self._input(self.element(self.PASSWORD), password)
        self._input(self.element(self.PASSWORD_CONFIRM), password)
        self.element(self.PRIVACY_POLICY).click()
        self.element(self.REGISTER_BUTTON).click()

        return self
