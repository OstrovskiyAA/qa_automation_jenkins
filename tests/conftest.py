import os

import allure
from dotenv import dotenv_values, load_dotenv
import pytest
from selene import browser, be, have
from selenium import webdriver
from utils import attach
from selenium.webdriver.chrome.options import Options
#Без селеноида:
# @pytest.fixture(scope="function")
# def open():
    # browser.open('https://demoqa.com/automation-practice-form')
    # yield
    # attach.add_html(browser)
    # attach.add_logs(browser)
    # attach.add_screenshot(browser)
    # browser.quit()

    # С селеноидом:
DEFAULT_BROWSER_VERSION ='100'
def pytest_addoption(parser):
    parser.addoption(
        '--vbrowser',
        help='Версия браузера',
        choices=['100', '99'],
        default='100'
    )
@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()
@pytest.fixture(scope="function")
def open_selenoid(request):
    browser_version = request.config.getoption('--vbrowser')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.open('https://demoqa.com/automation-practice-form')
    yield browser
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    # Только для селеноида:
    attach.add_video(browser)
    browser.quit()
