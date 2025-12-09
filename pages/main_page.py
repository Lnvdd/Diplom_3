import re
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage
from locators import (
    HeaderLocators,
    IngredientLocators,
    BasketLocators,
    ModalLocators,
    OrdersFeedLocators,
    Urls
)


class MainPage(BasePage):

    def open_main(self):
        with allure.step("Открыть главную страницу"):
            self.go_to_url(Urls.MAIN)

    def click_constructor_tab(self):
        with allure.step("Кликнуть на вкладку Конструктор"):
            self.click_element(HeaderLocators.CONSTRUCTOR_TAB)

    def click_orders_feed_tab(self):
        with allure.step("Кликнуть на вкладку Лента заказов"):
            self.click_element(HeaderLocators.ORDERS_FEED_TAB)

    def get_current_url(self):
        with allure.step("Получить текущий URL"):
            return self.driver.current_url

    def is_constructor_tab_visible(self) -> bool:
        with allure.step("Проверить видимость вкладки Конструктор"):
            return self.is_element_visible(HeaderLocators.CONSTRUCTOR_TAB)

    def is_element_visible(self, locator):
        with allure.step("Проверить видимость элемента"):
            return self.wait_for_element_visible(locator)

    def is_element_invisible(self, locator):
        with allure.step("Проверить невидимость элемента"):
            return self.wait_for_element_invisible(locator)

    def click_ingredient(self, ingredient_name):
        with allure.step(f"Кликнуть на ингредиент '{ingredient_name}'"):
            ingredient_img_xpath = f"//img[@alt='{ingredient_name}']"
            element = self.find_clickable_element((By.XPATH, ingredient_img_xpath))
            element.click()

    def close_modal(self):
        with allure.step("Закрыть модальное окно"):
            close_button_xpath = "//button[contains(@class, 'Modal_modal__close')]"
            self.click_element((By.XPATH, close_button_xpath))

    def drag_ingredient_to_basket(self, ingredient_name):
        with allure.step(f"Перетащить ингредиент '{ingredient_name}' в корзину"):
            ingredient_xpath = f"//p[contains(text(), '{ingredient_name}')]"
            basket_locator = BasketLocators.BURGER_BASKET
            self.drag_and_drop((By.XPATH, ingredient_xpath), basket_locator)

    def get_ingredient_counter(self, ingredient_name) -> int:
        with allure.step(f"Получить счётчик ингредиента '{ingredient_name}'"):
            try:
                ingredient_xpath = f"//p[contains(text(), '{ingredient_name}')]"
                self.find_element((By.XPATH, ingredient_xpath))
                counter_xpath = f"//p[contains(text(), '{ingredient_name}')]/following-sibling::span"
                counter_elem = self.find_element((By.XPATH, counter_xpath))
                counter_text = counter_elem.text.strip()
                counter_value = int(''.join(filter(str.isdigit, counter_text))) if counter_text else 0
                return counter_value
            except (NoSuchElementException, TimeoutException, ValueError) as e:
                allure.attach(str(e), "error", allure.attachment_type.TEXT)
                return 0

    def submit_order(self):
        with allure.step("Оформить заказ"):
            button = self.find_clickable_element(BasketLocators.ORDER_SUBMIT_BTN)
            button.click()

    def submit_order_and_get_number(self) -> str:
        with allure.step("Оформить заказ и получить номер"):
            button = self.find_clickable_element(BasketLocators.ORDER_SUBMIT_BTN)
            button.click()
            self.find_visible_element(ModalLocators.ORDER_DETAILS_MODAL)
            
            with allure.step("Ждём загрузки нормального номера заказа"):
                order_number_text = self.find_visible_element(ModalLocators.ORDER_NUMBER_MODAL).text.strip()
                order_number = re.sub(r'[^\d]', '', order_number_text)
                allure.attach(f"Номер заказа: {order_number}", "order_number", allure.attachment_type.TEXT)
                return order_number