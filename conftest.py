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
    
    test_email = os.getenv("TEST_EMAIL")
    test_password = os.getenv("TEST_PASSWORD")
    
    assert test_email is not None, "TEST_EMAIL не установлен в .env"
    assert test_password is not None, "TEST_PASSWORD не установлен в .env"
    
    auth_page = AuthPage(driver)
    auth_page.login(test_email, test_password)
    
    yield driver