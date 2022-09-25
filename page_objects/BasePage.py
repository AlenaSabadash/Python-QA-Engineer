import logging
import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__init_logger()

    def __init_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step("Клик по элементу: {element}")
    def click(self, element):
        self.logger.info(f"Клик по элементу: {element}")
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value):
        self.logger.info(f"Клик по элементу: {element}")
        self.click(element)
        self.logger.info(f"Заполение значения: {value}")
        element.clear()
        element.send_keys(value)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        self.logger.info(f"Поиск элемента {child_locator} внутри элемента {parent_locator}")
        return self.element(parent_locator).find_element(*child_locator)

    def element(self, locator: tuple):
        try:
            self.logger.info(f"Поиск элемента по локатору {locator}")
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Элемент по локатору {locator} не найден")
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def elements(self, locator: tuple):
        try:
            self.logger.info(f"Поиск элементов по локатору {locator}")
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Элементы по локатору {locator} не найден")
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    @property
    def alert(self):
        try:
            self.logger.info(f"Поиск алерта на странице")
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            return self.driver.switch_to.alert
        except TimeoutException:
            self.logger.error(f"Алерт на странице не найден")
            raise AssertionError(f"Не дождался видимости элемента alert")

    def verify_product_item(self, product_name):
        self.logger.info(f"Проверка наличия продукта с текстом {product_name}")
        return self.element((By.LINK_TEXT, product_name))

    @allure.step("Открытие по адресу {url}")
    def _open(self, url):
        self.driver.get(url)
