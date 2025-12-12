import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.ingredient_locators import Ingredients, IngredientLocators
from locators import (
    HeaderLocators,
    ModalLocators,
    IngredientLocators,
    BasketLocators,
    OrdersFeedLocators,
    Urls
)

class MainPage(BasePage):
    """Главная страница приложения"""
    
    def open_main(self):
        """Открыть главную страницу"""
        with allure.step("Открыть главную страницу"):
            self.open(Urls.MAIN)
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
            locator = self.get_locator_with_text(
                IngredientLocators.INGREDIENT_BY_NAME_XPATH,
                ingredient_name
            )
            self.click_element(locator)
            self.wait.until(EC.visibility_of_element_located(IngredientLocators.MODAL_WINDOW))
    
    def close_modal(self):
        """Закрыть модальное окно ингредиента"""
        with allure.step("Закрыть модальное окно"):
            self.click_element(IngredientLocators.MODAL_CLOSE_BTN)
            self.wait.until(EC.invisibility_of_element_located(IngredientLocators.MODAL_WINDOW))
    
    def close_order_modal(self):
        """Закрыть модальное окно заказа"""
        with allure.step("Закрыть модальное окно заказа"):
            self.click_element(ModalLocators.ORDER_CLOSE_BTN)
            self.wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL))
    
    def drag_ingredient_to_basket(self, ingredient_name):
        """Добавить ингредиент в корзину методом drag-and-drop"""
        with allure.step(f"Добавить '{ingredient_name}' в корзину"):
            locator = self.get_locator_with_text(
                IngredientLocators.INGREDIENT_BY_NAME_XPATH, 
                ingredient_name
            )
            ingredient = self.wait.until(EC.presence_of_element_located(locator))
            basket = self.wait.until(EC.presence_of_element_located(BasketLocators.BURGER_BASKET))
            self.actions.move_to_element(ingredient).pause(0.3).drag_and_drop(ingredient, basket).perform()
            self.wait.until(EC.element_to_be_clickable(BasketLocators.ORDER_SUBMIT_BTN))
    
    def submit_order(self):
        """Оформить заказ (без получения номера)"""
        with allure.step("Оформить заказ"):
            button = self.find_clickable_element(BasketLocators.ORDER_SUBMIT_BTN)
            button.click()
            self.wait_for_order_number(ModalLocators.ORDER_NUMBER_MODAL)
    
    def submit_order_and_get_number(self) -> str:
        """Оформить заказ и получить номер"""
        with allure.step("Оформить заказ и получить номер"):
            button = self.find_clickable_element(BasketLocators.ORDER_SUBMIT_BTN)
            button.click()
            self.wait.until(EC.presence_of_element_located(ModalLocators.ORDER_DETAILS_MODAL))
            with allure.step("Ждём загрузки нормального номера заказа (не 9999)"):
                order_number = self.wait_for_order_number(ModalLocators.ORDER_NUMBER_MODAL)
                allure.attach(
                    f"Номер заказа: {order_number}",
                    name="order_number",
                    attachment_type=allure.attachment_type.TEXT
                )
            return order_number
    
    def is_constructor_tab_visible(self) -> bool:
        """Проверить видимость вкладки Конструктор"""
        return self.is_element_visible(HeaderLocators.CONSTRUCTOR_TAB)
    
    def get_ingredient_counter(self, ingredient_name) -> int:
        """Получить значение счётчика ингредиента"""
        with allure.step(f"Получить счётчик для '{ingredient_name}'"):
            locator = self.get_locator_with_text(
                IngredientLocators.INGREDIENT_COUNTER_BY_NAME_XPATH,
                ingredient_name
            )
            text = self.get_element_text(locator)
            return int(text)