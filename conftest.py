import pytest
import os
import logging
import allure

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--url", default="http://localhost")
    parser.addoption("--status_code", default=200, type=int)
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def base_status_code(request):
    return request.config.getoption("--status_code")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode) as f:
                if "browser" in item.fixturenames:
                    web_driver = item.funcargs["browser"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))


@pytest.fixture
def logger(request):
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.now()))

    return logger


@pytest.fixture
def browser(request, logger):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    executor = request.config.getoption("--executor")

    if executor == "local":
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
        driver = webdriver.Remote(
            command_executor="http://{}:4444/wd/hub".format(executor),
            desired_capabilities={"browserName": browser},
        )

    driver.log_level = logger.level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser, driver.capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.now()))

    request.addfinalizer(fin)

    return driver
