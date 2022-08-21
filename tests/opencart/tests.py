import pytest
from enum import Enum
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageUrl(str, Enum):
    catalog = "index.php?route=product/category&path={}"
    product = "index.php?route=product/product&path={}&product_id={}"
    admin = "admin"
    register = "index.php?route=account/register"


class CatalogPath(Enum):
    desktops = 20
    laptops_n_notebooks = 18
    components = 25
    tablets = 57


def test_check_main(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, "#logo")
    browser.find_element(By.CSS_SELECTOR, "#search")
    browser.find_element(By.CSS_SELECTOR, "#header-cart")


@pytest.mark.parametrize(
    "category,path",
    [
        ("desktops", CatalogPath.desktops.value),
        ("laptops & notebooks", CatalogPath.laptops_n_notebooks.value),
        ("components", CatalogPath.components.value),
        ("tablets", CatalogPath.tablets.value),
    ],
)
def test_check_catalog(browser, base_url, category, path):
    browser.get(f"{base_url}/{PageUrl.catalog.format(path)}")
    browser.find_element(By.CSS_SELECTOR, "#column-left")
    browser.find_element(By.CSS_SELECTOR, "#form-currency")
    browser.find_element(By.CSS_SELECTOR, "#wishlist-total")
    browser.find_element(By.CSS_SELECTOR, "#menu")
    title_element = browser.find_element(By.CSS_SELECTOR, "#content").find_element(By.TAG_NAME, "h2")
    assert title_element.text.lower() == category.lower()


def test_check_product(browser, base_url):
    browser.get(f"{base_url}/{PageUrl.product.format(20, 42)}")
    browser.find_element(By.CSS_SELECTOR, "#button-cart")
    browser.find_element(By.CSS_SELECTOR, "#content")
    browser.find_element(By.CSS_SELECTOR, "#form-currency")
    browser.find_element(By.CSS_SELECTOR, "#wishlist-total")
    browser.find_element(By.CSS_SELECTOR, "#search")


def test_check_admin(browser, base_url):
    browser.get(f"{base_url}/{PageUrl.admin}")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    browser.find_element(By.CSS_SELECTOR, "#footer")
    browser.find_element(By.CSS_SELECTOR, "#container")
    browser.find_element(By.CSS_SELECTOR, "#header")


def test_check_register(browser, base_url):
    browser.get(f"{base_url}/{PageUrl.register}")
    browser.find_element(By.CSS_SELECTOR, "#input-firstname")
    browser.find_element(By.CSS_SELECTOR, "#input-lastname")
    browser.find_element(By.CSS_SELECTOR, "#input-email")
    browser.find_element(By.CSS_SELECTOR, "#input-password")
    browser.find_element(By.CSS_SELECTOR, "#input-newsletter-yes")
    browser.find_element(By.CSS_SELECTOR, "#input-newsletter-no")
