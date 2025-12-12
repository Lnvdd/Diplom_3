import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.auth_locators import AuthLocators

class AuthPage(BasePage):
    """Страница логина"""
    
    def _enter_email(self, email):
        """Ввести email"""
        with allure.step(f"Ввести email: {email}"):
            email_input = self.find_clickable_element(AuthLocators.EMAIL_INPUT)
            email_input.clear()
            email_input.send_keys(email)
    
    def _enter_password(self, password):
        """Ввести пароль"""
        with allure.step("Ввести пароль"):
            password_input = self.find_clickable_element(AuthLocators.PASSWORD_INPUT)
            password_input.clear()
            password_input.send_keys(password)
    
    def _click_login_button(self):
        """Кликнуть кнопку логина"""
        with allure.step("Кликнуть кнопку 'Войти'"):
            self.click_element(AuthLocators.LOGIN_BUTTON)
    
    def login(self, email, password):
        """Залогинить пользователя"""
        with allure.step(f"Залогинить пользователя: {email}"):
            with allure.step("Заполнить и отправить форму логина"):
                self._enter_email(email)
                self._enter_password(password)
                self._click_login_button()
            
            with allure.step("Ждём загрузки страницы после логина"):
                self.wait.until(EC.invisibility_of_element_located(AuthLocators.LOGIN_BUTTON))