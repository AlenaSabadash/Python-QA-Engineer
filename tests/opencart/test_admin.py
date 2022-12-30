import pytest
import allure

from page_objects.AlertElement import AlertElement
from page_objects.AdminAuthPage import AdminAuthPage
from page_objects.ProductCreatePage import ProductCreatePage
from page_objects.ProductsListPage import ProductsListPage
from page_objects.elements.MenuElement import MenuElement
from page_objects.elements.ProductFilterElement import ProductFilterElement
from test_data.models.users import get_user


@allure.title("Тест добавления нового продукта в каталог")
@pytest.mark.parametrize(
    "product_name,meta_tag,model",
    [
        ("test_product", "test_tag", "test_model"),
        ("test_product2", "test_tag2", "test_model2"),
        ("test_product3", "test_tag3", "test_model3"),
        ("test_product4", "test_tag4", "test_model4"),
        ("test_product5", "test_tag5", "test_model5"),
    ],
)
def test_add_product(browser, base_url, product_name, meta_tag, model):
    AdminAuthPage(browser, base_url).open().login(*get_user())
    menu_element = MenuElement(browser)
    menu_element.catalog_menu.click()
    menu_element.products_submenu.click()

    ProductsListPage(browser).add_new.click()
    ProductCreatePage(browser).create(product_name, meta_tag, model)
    ProductFilterElement(browser).filter(product_name)
    assert ProductsListPage(browser).get_product_name() == product_name


@allure.title("Тест удаления продукта из каталога")
@pytest.mark.parametrize(
    "product_name,meta_tag,model",
    [
        ("test_product", "test_tag", "test_model"),
        ("test_product2", "test_tag2", "test_model2"),
        ("test_product3", "test_tag3", "test_model3"),
        ("test_product4", "test_tag4", "test_model4"),
        ("test_product5", "test_tag5", "test_model5"),
    ],
)
def test_delete_product(browser, base_url, product_name, meta_tag, model):
    with allure.step("Логинимся под админом и переходим в каталог товаров"):
        AdminAuthPage(browser, base_url).open().login(*get_user())
        menu_element = MenuElement(browser)
        menu_element.catalog_menu.click()
        menu_element.products_submenu.click()

    with allure.step("Ищем товар {product_name} и удаляем из каталога"):
        products_list_page = ProductsListPage(browser)
        ProductFilterElement(browser).filter(product_name)
        products_list_page.checkbox.click()
        products_list_page.delete_product.click()

    with allure.step("Принимаем алерт"):
        products_list_page.alert.accept()

    assert "Success" in AlertElement(browser).this.text
