from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import HeaderLocators, IngredientLocators, BasketLocators, OrdersFeedLocators, ModalLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import re
import allure


class MainPage(BasePage):
    def open_main(self):
        with allure.step("Открыть главную страницу"):
            self.driver.get("https://stellarburgers.education-services.ru")
            time.sleep(2)

    def open_feed(self):
        with allure.step("Открыть ленту заказов"):
            self.driver.get("https://stellarburgers.education-services.ru/feed")

    def click_constructor_tab(self):
        with allure.step("Кликнуть на вкладку 'Конструктор'"):
            self.driver.find_element(*HeaderLocators.CONSTRUCTOR_TAB).click()

    def click_orders_feed_tab(self):
        with allure.step("Кликнуть на вкладку 'Лента Заказов'"):
            self.driver.find_element(*HeaderLocators.ORDERS_FEED_TAB).click()
            self.wait.until(EC.visibility_of_element_located(OrdersFeedLocators.COMPLETED_ALL_TIME))

    def click_ingredient(self, ingredient_name):
        with allure.step(f"Кликнуть на ингредиент '{ingredient_name}'"):
            xpath = f"//p[contains(text(), '{ingredient_name}')]"
            self.driver.find_element(By.XPATH, xpath).click()

    def close_modal(self):
        with allure.step("Закрыть модальное окно"):
            self.driver.find_element(*IngredientLocators.MODAL_CLOSE_BTN).click()

    def close_order_modal(self):
        with allure.step("Закрыть модальное окно заказа"):
            self.driver.find_element(*ModalLocators.ORDER_CLOSE_BTN).click()
            time.sleep(1)

    def drag_ingredient_to_basket(self, ingredient_name):
        with allure.step(f"Добавить '{ingredient_name}' в корзину"):
            time.sleep(2)
            ingredient_xpath = f"//p[contains(text(), '{ingredient_name}')]"
            ingredient = self.wait.until(EC.presence_of_element_located((By.XPATH, ingredient_xpath)))
            basket = self.wait.until(EC.presence_of_element_located(BasketLocators.BURGER_BASKET))
            time.sleep(0.5)
            actions = ActionChains(self.driver)
            actions.move_to_element(ingredient).pause(0.3).drag_and_drop(ingredient, basket).perform()
            time.sleep(1)

    def submit_order(self):
        with allure.step("Оформить заказ"):
            button = self.wait.until(EC.element_to_be_clickable(BasketLocators.ORDER_SUBMIT_BTN))
            button.click()
            time.sleep(3)

    def submit_order_and_get_number(self):
        with allure.step("Оформить заказ и получить номер"):
            button = self.wait.until(EC.element_to_be_clickable(BasketLocators.ORDER_SUBMIT_BTN))
            button.click()
            time.sleep(2)
            wait_for_modal = WebDriverWait(self.driver, 10)
            modal = wait_for_modal.until(EC.presence_of_element_located(ModalLocators.ORDER_DETAILS_MODAL))
            order_number_elem = self.driver.find_element(*ModalLocators.ORDER_NUMBER_MODAL)
            max_attempts = 20
            attempt = 0
            order_number = None
            
            while attempt < max_attempts:
                order_number_text = order_number_elem.text.strip()
                order_number = re.sub(r'[^\d]', '', order_number_text)
                
                if order_number and order_number != "9999":
                    allure.attach(f"Номер заказа: {order_number}", name="order_number", attachment_type=allure.attachment_type.TEXT)
                    return order_number
                
                time.sleep(0.5)
                attempt += 1
                
                try:
                    order_number_elem = self.driver.find_element(*ModalLocators.ORDER_NUMBER_MODAL)
                except:
                    pass
            
            return order_number