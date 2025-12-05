import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Urls

TEST_EMAIL = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"
LOGIN_URL = "https://stellarburgers.education-services.ru/login"

def login_via_login_page(driver, email, password):
    
    wait = WebDriverWait(driver, 10)
    
    
    with allure.step("Перейти на страницу логина"):
        driver.get(LOGIN_URL)
    
   
    with allure.step("Ждём загрузки формы логина"):
        email_input = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//input[@type='text'][@name='name']"
            ))
        )
    
    with allure.step(f"Вводим email: {email}"):
        email_input.clear()
        email_input.send_keys(email)
    
    
    with allure.step("Вводим пароль"):
        password_input = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//input[@type='password'][@name='Пароль']"
            ))
        )
        password_input.clear()
        password_input.send_keys(password)
    
    
    with allure.step("Нажимаем кнопку 'Войти'"):
        login_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти')]"
            ))
        )
        login_button.click()
    
    
    with allure.step("Ждём перенаправления на конструктор"):
        wait.until(EC.url_changes(LOGIN_URL))
        wait.until(
            EC.url_matches(f".*{Urls.MAIN}.*")
        )


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
  
    login_via_login_page(driver, TEST_EMAIL, TEST_PASSWORD)
    return driver