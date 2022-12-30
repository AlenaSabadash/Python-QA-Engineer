import allure
import pytest

from page_objects.LaptopNotebookPage import LaptopNotebookPage
from page_objects.MainPage import MainPage
from page_objects.elements.ShoppingCartElement import ShoppingCartElement
from test_data.enum.currency import CurrencyEnum
from tests.opencart.spec import SUCCESS_TEXT, EMPTY_CART_TEXT


@allure.title("Тест смены валюты")
@pytest.mark.parametrize(
    "currency",
    [
        CurrencyEnum.EUR,
        CurrencyEnum.GBP,
        CurrencyEnum.USD,
    ],
)
def test_change_currency(browser, base_url, currency):
    main_page = MainPage(browser, base_url).open()
    main_page.currency_dropdown.click()
    main_page.currency_item(currency.name).click()
    assert currency.value in main_page.currency_dropdown.text


@allure.title("Проверка добавления товара в корзину")
def test_add_item_to_cart(browser, base_url):
    page = LaptopNotebookPage(browser, base_url).open()
    page.add_to_cart.click()

    assert SUCCESS_TEXT in page.alert_badge.text


@allure.title("Проверка что в корзину добавился нужный товар")
def test_check_item_in_cart(browser, base_url):
    with allure.step("Добавляем товар в корзину"):
        page = LaptopNotebookPage(browser, base_url).open()
        product_name = page.get_product_name
        page.add_to_cart.click()

    with allure.step("Клик по кнопке просмотра корзины"):
        page_element = ShoppingCartElement(browser)
        page_element.cart_button.click()

    with allure.step("Проверка наличия товара '{product_name}' в корзине"):
        assert product_name == page_element.get_product_name


@allure.title("Проверка что товар удалился из корзины")
def test_delete_item_from_cart(browser, base_url):
    with allure.step("Добавляем товар в корзину"):
        page = LaptopNotebookPage(browser, base_url).open()
        page.add_to_cart.click()

    with allure.step("Клик по кнопке удаления товара из корзины"):
        page_element = ShoppingCartElement(browser)
        page_element.cart_button.click()
        if hasattr(page_element.delete_from_cart_button, "click"):
            page_element.delete_from_cart_button.click()

    assert EMPTY_CART_TEXT in page_element.cart_button.text
