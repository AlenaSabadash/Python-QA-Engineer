import allure
import pytest

from page_objects.AdminAuthPage import AdminAuthPage
from page_objects.AlertElement import AlertElement
from page_objects.AuthPage import AuthPage
from page_objects.CustomersPage import CustomersPage
from page_objects.RegisterPage import RegisterPage
from page_objects.RegisterSuccessPage import RegisterSuccessPage
from page_objects.elements.CustomersFilterElement import CustomersFilterElement
from page_objects.elements.MenuElement import MenuElement
from test_data.models.users import get_customer, get_user
from tests.opencart.spec import (
    SUCCESS_LOGIN_URL,
    SUCCESSFULLY_CREATED_ACCOUNT,
    ERROR_ON_ACCOUNT_CREATION,
    ERROR_ON_LOGIN,
    SUCCESS_TEXT,
)

test_user = get_customer()


@allure.title("Тест нельзя зарегистрироваться без галочки privacy policy")
@pytest.mark.parametrize(
    "first_name, last_name, email, telephone, password",
    [
        (
            test_user.first_name,
            test_user.last_name,
            test_user.email,
            test_user.telephone,
            test_user.password,
        ),
    ],
)
def test_register_new_user(browser, base_url, first_name, last_name, email, telephone, password):
    with allure.step(f"Регистрации нового пользователя: {first_name}, {last_name}, {email}, {telephone}, {password}"):
        user_data = (first_name, last_name, email, telephone, password)
        register_page = (
            RegisterPage(browser, base_url)
            .open()
            .register(
                *user_data,
                privacy_policy=False,
            )
        )
    assert ERROR_ON_ACCOUNT_CREATION in register_page.alert_text.text


@allure.title("Тест регистрации нового пользователя")
@pytest.mark.parametrize(
    "first_name, last_name, email, telephone, password",
    [
        (
            test_user.first_name,
            test_user.last_name,
            test_user.email,
            test_user.telephone,
            test_user.password,
        ),
    ],
)
def test_register_new_user(browser, base_url, first_name, last_name, email, telephone, password):
    with allure.step(f"Регистрации нового пользователя: {first_name}, {last_name}, {email}, {telephone}, {password}"):
        user_data = first_name, last_name, email, telephone, password
        RegisterPage(browser, base_url).open().register(*user_data)
    assert SUCCESSFULLY_CREATED_ACCOUNT in RegisterSuccessPage(browser).success.text


@allure.title("Тест авторизации пользователя в магазине")
def test_user_login(browser, base_url):
    AuthPage(browser, base_url).open().login(test_user.username, test_user.password)
    assert browser.current_url == SUCCESS_LOGIN_URL


@allure.title("Тест обычный пользователь не может залогиниться в админку")
@pytest.mark.parametrize(
    "first_name, last_name, email, telephone, password",
    [
        (
            test_user.first_name,
            test_user.last_name,
            test_user.email,
            test_user.telephone,
            test_user.password,
        ),
    ],
)
def test_non_admin_login(browser, base_url, first_name, last_name, email, telephone, password):
    page = AuthPage(browser, base_url).open().login(email, password)
    assert page.alert_badge.text == ERROR_ON_LOGIN


@allure.title("Тест удаления аккаунта пользователя")
@pytest.mark.parametrize(
    "first_name, last_name, email, telephone, password",
    [
        (
            test_user.first_name,
            test_user.last_name,
            test_user.email,
            test_user.telephone,
            test_user.password,
        ),
    ],
)
def test_user_delete(browser, base_url, first_name, last_name, email, telephone, password):
    with allure.step("Логинимся под админом"):
        AdminAuthPage(browser, base_url).open().login(*get_user())
        menu_element = MenuElement(browser)
        menu_element.customers_menu.click()
        menu_element.customers_submenu.click()

    with allure.step("Ищем пользователя {email} в таблице"):
        customers_filter_element = CustomersFilterElement(browser)
        customers_filter_element.filter(email)

    with allure.step("Удаляем найденного пользователя: {email}"):
        customers_page = CustomersPage(browser)
        customers_page.select_all.click()
        customers_page.delete_users.click()

    with allure.step("Принимаем алерт"):
        menu_element.alert.accept()

    assert SUCCESS_TEXT in AlertElement(browser).this.text
