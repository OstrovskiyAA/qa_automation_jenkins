import allure
import pytest
from selene import browser, be, have
from selenium import webdriver
from utils import attach
from selenium.webdriver.chrome.options import Options
#Без селенида:
# @pytest.fixture(scope="function")
# def open():
    # browser.open('https://demoqa.com/automation-practice-form')
    # yield
    # attach.add_html(browser)
    # attach.add_logs(browser)
    # attach.add_screenshot(browser)
    # browser.quit()

    # С селенидом:
@pytest.fixture(scope="function")
def open_selenoid():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
    command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
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
