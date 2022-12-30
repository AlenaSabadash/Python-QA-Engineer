import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CustomersFilterElement(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")

    @allure.step("Фильтр пользователей по email: {email}")
    def filter(self, email):
        self._input(self.element(self.EMAIL_INPUT), email)
        self.click(self.element(self.FILTER_BUTTON))
        return self
