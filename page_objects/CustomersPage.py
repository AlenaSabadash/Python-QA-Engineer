import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.mixins.OpenablePageMixin import OpenablePageMixin


class CustomersPage(BasePage):
    TABLE_CHECKBOX_INPUT = (By.XPATH, "//table//td//input")
    DELETE_BUTTON = (By.XPATH, "//button[@data-original-title='Delete']")

    @property
    def select_all(self):
        return self.element(self.TABLE_CHECKBOX_INPUT)

    @property
    def delete_users(self):
        return self.element(self.DELETE_BUTTON)
