import allure
from pages.base_page import BasePage
from locators.auth_locators import AuthLocators
from locators.urls import Urls


class AuthPage(BasePage):

    def login(self, email, password):
        with allure.step(f"Залогинить пользователя: {email}"):
            login_url = f"{Urls.BASE_URL}/login"
            
            with allure.step("Перейти на страницу логина"):
                self.go_to_url(login_url)
            
            with allure.step("Заполнить и отправить форму логина"):
                self._enter_email(email)
                self._enter_password(password)
                self._click_login_button()
            
            with allure.step("Ждём перенаправления на конструктор"):
                self.wait_for_url_contains("/constructor")

    def _enter_email(self, email):
        with allure.step("Ввести email"):
            email_field = self.find_element(AuthLocators.EMAIL_INPUT)
            email_field.clear()
            email_field.send_keys(email)

    def _enter_password(self, password):
        with allure.step("Ввести пароль"):
            password_field = self.find_element(AuthLocators.PASSWORD_INPUT)
            password_field.clear()
            password_field.send_keys(password)

    def _click_login_button(self):
        with allure.step("Кликнуть кнопку входа"):
            login_button = self.find_clickable_element(AuthLocators.LOGIN_BUTTON)
            login_button.click()

    def logout(self):
        with allure.step("Выход из аккаунта"):
            with allure.step("Открыть меню профиля"):
                profile_button = self.find_clickable_element(AuthLocators.PROFILE_BUTTON)
                profile_button.click()
            
            with allure.step("Нажать 'Выход'"):
                logout_button = self.find_clickable_element(AuthLocators.LOGOUT_BUTTON)
                logout_button.click()
            
            with allure.step("Ждём перенаправления на логин"):
                self.wait_for_url_contains("/login")

    def is_logged_in(self):
        with allure.step("Проверить залогинен ли пользователь"):
            return self.is_element_visible(AuthLocators.PROFILE_BUTTON)