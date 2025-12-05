import re
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators import (
    HeaderLocators, 
    ModalLocators, 
    IngredientLocators, 
    BasketLocators,
    OrdersFeedLocators,
    Urls
)


class order_number_loaded:

    def __init__(self, locator):
        self.locator = locator
    
    def __call__(self, driver):
        
        try:
            element = driver.find_element(*self.locator)
            text = element.text.strip()
            order_number = re.sub(r'[^\d]', '', text)
            if order_number and order_number != "9999":
                return element
            return False
        except Exception:
            return False


class MainPage(BasePage):
    """Главная страница приложения"""

    def open_main(self):
        """Открыть главную страницу"""
        with allure.step("Открыть главную страницу"):
            self.driver.get(Urls.MAIN)
            self.wait.until(EC.visibility_of_element_located(HeaderLocators.CONSTRUCTOR_TAB))

    def click_constructor_tab(self):
        """Кликнуть на вкладку 'Конструктор'"""
        with allure.step("Кликнуть на вкладку 'Конструктор'"):
            self.click_element(HeaderLocators.CONSTRUCTOR_TAB)

    def click_orders_feed_tab(self):
        """Кликнуть на вкладку 'Лента Заказов'"""
        with allure.step("Кликнуть на вкладку 'Лента Заказов'"):
            self.click_element(HeaderLocators.ORDERS_FEED_TAB)
            self.wait.until(EC.visibility_of_element_located(OrdersFeedLocators.COMPLETED_ALL_TIME))

    def click_ingredient(self, ingredient_name):
        """Кликнуть на ингредиент по названию"""
        with allure.step(f"Кликнуть на ингредиент '{ingredient_name}'"):
            xpath = f"//p[contains(text(), '{ingredient_name}')]"
            self.driver.find_element(By.XPATH, xpath).click()
            self.wait.until(EC.visibility_of_element_located(IngredientLocators.MODAL_WINDOW))

    def close_modal(self):
        """Закрыть модальное окно ингредиента"""
        with allure.step("Закрыть модальное окно"):
            self.click_element(IngredientLocators.MODAL_CLOSE_BTN)
            self.wait.until(EC.invisibility_of_element_located(IngredientLocators.MODAL_WINDOW))

    def close_order_modal(self):
        """Закрыть модальное окно заказа"""
        with allure.step("Закрыть модальное окно заказа"):
            close_button = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[contains(@class, 'Modal_modal__close')]"
                ))
            )
            close_button.click()
            self.wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL))

    def drag_ingredient_to_basket(self, ingredient_name):
        """Добавить ингредиент в корзину методом drag-and-drop"""
        with allure.step(f"Добавить '{ingredient_name}' в корзину"):
            ingredient_xpath = f"//p[contains(text(), '{ingredient_name}')]"
            ingredient = self.wait.until(
                EC.presence_of_element_located((By.XPATH, ingredient_xpath))
            )
            basket = self.wait.until(
                EC.presence_of_element_located(BasketLocators.BURGER_BASKET)
            )
            
            actions = ActionChains(self.driver)
            actions.move_to_element(ingredient).pause(0.3).drag_and_drop(
                ingredient, basket
            ).perform()
            self.wait.until(EC.element_to_be_clickable(BasketLocators.ORDER_SUBMIT_BTN))

    def submit_order(self):
        """Оформить заказ (без получения номера)"""
        with allure.step("Оформить заказ"):
            button = self.find_clickable_element(BasketLocators.ORDER_SUBMIT_BTN)
            button.click()
            self.wait.until(order_number_loaded(ModalLocators.ORDER_NUMBER_MODAL))

    def submit_order_and_get_number(self) -> str:
        with allure.step("Оформить заказ и получить номер"):
            button = self.find_clickable_element(BasketLocators.ORDER_SUBMIT_BTN)
            button.click()
            self.wait.until(EC.presence_of_element_located(ModalLocators.ORDER_DETAILS_MODAL))
        
            with allure.step("Ждём загрузки нормального номера заказа (не 9999)"):
                order_number_elem = self.wait.until(order_number_loaded(ModalLocators.ORDER_NUMBER_MODAL))
            
            order_number_text = order_number_elem.text.strip()
            order_number = re.sub(r'[^\d]', '', order_number_text)
            
            allure.attach(
                f"Номер заказа: {order_number}",
                name="order_number",
                attachment_type=allure.attachment_type.TEXT
            )
            
            return order_number

    def is_constructor_tab_visible(self) -> bool:
        return self.is_element_visible(HeaderLocators.CONSTRUCTOR_TAB)