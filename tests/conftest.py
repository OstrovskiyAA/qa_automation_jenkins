import allure
import pytest
from selene import browser, be, have
@pytest.fixture(scope="function")
def open():
    browser.open('https://demoqa.com/automation-practice-form')
