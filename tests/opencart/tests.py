import pytest
import allure

from page_objects.AlertElement import AlertElement
from page_objects.AuthPage import AuthPage
from page_objects.MainPage import MainPage
from page_objects.ProductCreatePage import ProductCreatePage
from page_objects.ProductsListPage import ProductsListPage
from page_objects.RegisterPage import RegisterPage
from page_objects.RegisterSucsessPage import RegisterSuccessPage
from page_objects.elements.MenuElement import MenuElement
from page_objects.elements.ProductFilterElement import ProductFilterElement
from test_data.enum.currency import CurrencyEnum
from test_data.users import get_user


@allure.title("Тест добавления нового продукта в каталог")
@pytest.mark.parametrize(
    "product_name,meta_tag,model",
    [
        ("test_product", "test_tag", "test_model"),
    ],
)
def test_add_product(browser, base_url, product_name, meta_tag, model):
    AuthPage(browser, base_url).open().login(*get_user())
    menu_element = MenuElement(browser)
    menu_element.catalog_menu.click()
    menu_element.products_submenu.click()

    ProductsListPage(browser).add_new.click()
    ProductCreatePage(browser).create(product_name, meta_tag, model)
    ProductFilterElement(browser).filter(product_name)
    assert ProductsListPage(browser).get_product_name() == product_name


@allure.title("Тест удаления продукта из каталога")
def test_delete_product(browser, base_url):
    AuthPage(browser, base_url).open().login(*get_user())
    menu_element = MenuElement(browser)
    menu_element.catalog_menu.click()
    menu_element.products_submenu.click()

    products_list_page = ProductsListPage(browser)
    products_list_page.checkbox.click()
    products_list_page.delete_product.click()
    with allure.step("Принимаем алерт"):
        products_list_page.alert.accept()

    assert "Success" in AlertElement(browser).this.text


@allure.title("Тест регистрации нового пользователя")
@pytest.mark.parametrize(
    "first_name, last_name, email, telephone, password",
    [
        ("first_name", "last_name", "email@mail.ru", "89878967898", "1234"),
    ],
)
def test_register_new_user(browser, base_url, first_name, last_name, email, telephone, password):
    main_page = MainPage(browser, base_url).open()
    main_page.my_account.click()
    main_page.register.click()

    RegisterPage(browser).register(first_name, last_name, email, telephone, password)

    assert "Your Account Has Been Created!" in RegisterSuccessPage(browser).success.text


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
