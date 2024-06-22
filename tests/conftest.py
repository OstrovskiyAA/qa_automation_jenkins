import allure
import pytest
from selene import browser, be, have

from utils import attach


@pytest.fixture(scope="function")
def open():
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    browser.quit()