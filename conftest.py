import pytest

import allure

import os

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture(scope="function")
def authenticated_driver(driver):
    from pages.auth_page import AuthPage
    from locators.urls import Urls

    test_email = os.getenv("TEST_EMAIL")
    test_password = os.getenv("TEST_PASSWORD")

    if test_email is None or test_password is None:
        pytest.skip("TEST_EMAIL или TEST_PASSWORD не установлены в .env файле")

    # Открываем страницу логина
    driver.get(f"{Urls.BASE_URL}/login")
    
    auth_page = AuthPage(driver)
    auth_page.login(test_email, test_password)
    
    # После логина открываем главную страницу (конструктор)
    driver.get(f"{Urls.BASE_URL}")
    
    yield driver