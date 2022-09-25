from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterSuccessPage(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")

    @property
    def success(self):
        return self.element(self.CONTENT)
