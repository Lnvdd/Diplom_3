from pages.base_page import BasePage
from pages.locators import OrdersFeedLocators
from selenium.webdriver.common.by import By
import time
import allure


class OrdersPage(BasePage):
    def open_feed(self):
        self.open("/feed")
        self.find_visible_element(OrdersFeedLocators.COMPLETED_ALL_TIME)

    def _parse_counter_text(self, text: str) -> int:
        digits = "".join(ch for ch in text if ch.isdigit())
        if not digits:
            raise ValueError(f"Не удалось извлечь число из текста счётчика: {text!r}")
        return int(digits)

    def get_completed_all_time_count(self) -> int:
        with allure.step("Получить счётчик 'Выполнено за всё время'"):
            try:
                count_elem = self.find_visible_element(OrdersFeedLocators.COMPLETED_ALL_TIME)
                count_text = count_elem.text.strip()
                value = self._parse_counter_text(count_text)
                allure.attach(f"Значение счётчика: {value}", name="counter_value", attachment_type=allure.attachment_type.TEXT)
                return value
            except Exception as e:
                allure.attach(str(e), name="error", attachment_type=allure.attachment_type.TEXT)
                raise

    def get_completed_today_count(self) -> int:
        with allure.step("Получить счётчик 'Выполнено за сегодня'"):
            try:
                count_elem = self.find_visible_element(OrdersFeedLocators.COMPLETED_TODAY)
                count_text = count_elem.text.strip()
                value = self._parse_counter_text(count_text)
                allure.attach(f"Значение счётчика: {value}", name="counter_value", attachment_type=allure.attachment_type.TEXT)
                return value
            except Exception as e:
                allure.attach(str(e), name="error", attachment_type=allure.attachment_type.TEXT)
                raise

    def find_order_in_work_section(self, order_number: str) -> bool:
        with allure.step(f"Найти заказ {order_number} в разделе 'В работе'"):
            try:
                clean_target = "".join(ch for ch in order_number if ch.isdigit())
                time.sleep(2)
                
                order_elements = self.driver.find_elements(*OrdersFeedLocators.IN_WORK_ORDERS)
                
                for elem in order_elements:
                    text = elem.text.strip()
                    clean_text = "".join(ch for ch in text if ch.isdigit())
                    
                    if clean_target == clean_text or clean_target in clean_text:
                        allure.attach(f"Найден заказ: {clean_target}", name="found_order", attachment_type=allure.attachment_type.TEXT)
                        return True
                
                allure.attach(f"Заказ {clean_target} не найден", name="order_not_found", attachment_type=allure.attachment_type.TEXT)
                return False
            except Exception as e:
                allure.attach(str(e), name="error", attachment_type=allure.attachment_type.TEXT)
                return False

    def get_in_work_order_numbers(self) -> list:
        with allure.step("Получить все номера заказов"):
            try:
                time.sleep(1)
                order_elements = self.driver.find_elements(*OrdersFeedLocators.IN_WORK_ORDERS)
                
                order_numbers = []
                seen = set()
                
                for elem in order_elements:
                    text = elem.text.strip()
                    clean_num = "".join(ch for ch in text if ch.isdigit())
                    
                    if clean_num and len(clean_num) >= 4 and clean_num not in seen:
                        order_numbers.append(clean_num)
                        seen.add(clean_num)
                
                allure.attach(f"Найденные номера: {', '.join(order_numbers)}", name="order_numbers", attachment_type=allure.attachment_type.TEXT)
                return order_numbers
            except Exception as e:
                allure.attach(str(e), name="error", attachment_type=allure.attachment_type.TEXT)
                return []