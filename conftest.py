import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--url", default="http://localhost")
    parser.addoption("--status_code", default=200, type=int)


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def base_status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = Service(executable_path=os.path.join(drivers, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        service = Service(executable_path=os.path.join(drivers, "yandexdriver"))
        options.binary_location = "/usr/bin/yandex-browser"
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.join(drivers, "geckodriver"))
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)

    return driver
