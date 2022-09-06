from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class AlertElement(BasePage):
    THIS = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS = (By.LINK_TEXT, "Success")

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.this = self.element(self.THIS)

    @property
    def success(self):
        return self.element(self.SUCCESS)
