import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import AuthLocators, ModalLocators, Urls, HeaderLocators

TEST_EMAIL = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"

def login(driver, email, password):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ModalLocators.ORDER_MODAL)
    )
    time.sleep(1)
    
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(AuthLocators.LOGIN_EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(0.5)
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(AuthLocators.LOGIN_PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(0.5)
  
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AuthLocators.LOGIN_BUTTON)
    )
    button.click()
    time.sleep(2)

def login_and_go_to_main(driver, base_url, main_login_btn, email, password):
    driver.get(base_url)
    time.sleep(2)
    
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(main_login_btn)
    )
    login_btn.click()
    time.sleep(2)
    
    login(driver, email, password)
    
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(ModalLocators.ORDER_MODAL)
    )
    time.sleep(2)


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

    login_and_go_to_main(
        driver,
        base_url=Urls.MAIN,
        main_login_btn=HeaderLocators.MAIN_LOGIN_BTN,
        email=TEST_EMAIL,
        password=TEST_PASSWORD
    )
    return driver