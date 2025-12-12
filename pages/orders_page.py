import allure
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException
)
from pages.base_page import BasePage
from locators import OrdersFeedLocators, Urls

class OrdersPage(BasePage):
    """Страница ленты заказов"""
    
    def open_feed(self):
        """Открыть ленту заказов"""
        with allure.step("Открыть ленту заказов"):
            self.go_to_url(Urls.FEED)
    
    def _parse_counter_text(self, text: str) -> int:
        """Парсить число из текста"""
        with allure.step(f"Парсить число из текста: {text}"):
            digits = "".join(ch for ch in text if ch.isdigit())
            if not digits:
                raise ValueError(f"Не удалось извлечь число: {text!r}")
            return int(digits)
    
    def get_completed_all_time_count(self) -> int:
        """Получить счётчик завершённых заказов (всё время)"""
        with allure.step("Получить счётчик завершённых заказов (всё время)"):
            try:
                counter_element = self.find_visible_element(OrdersFeedLocators.COMPLETED_ALL_TIME)
                count_text = counter_element.text.strip()
                value = self._parse_counter_text(count_text)
                allure.attach(f"Значение счётчика: {value}", "counter_value", allure.attachment_type.TEXT)
                return value
            except (NoSuchElementException, TimeoutException, ValueError) as e:
                allure.attach(str(e), "error", allure.attachment_type.TEXT)
                return 0
    
    def get_completed_today_count(self) -> int:
        """Получить счётчик завершённых заказов (сегодня)"""
        with allure.step("Получить счётчик завершённых заказов (сегодня)"):
            try:
                counter_element = self.find_visible_element(OrdersFeedLocators.COMPLETED_TODAY)
                count_text = counter_element.text.strip()
                value = self._parse_counter_text(count_text)
                allure.attach(f"Значение счётчика: {value}", "counter_value", allure.attachment_type.TEXT)
                return value
            except (NoSuchElementException, TimeoutException, ValueError) as e:
                allure.attach(str(e), "error", allure.attachment_type.TEXT)
                return 0
    
    def find_order_in_work_section(self, order_number: str) -> bool:
        """Найти заказ в разделе 'В работе'"""
        with allure.step(f"Найти заказ {order_number} в разделе 'В работе'"):
            try:
                clean_target = "".join(ch for ch in order_number if ch.isdigit())
                self.wait_for_element_visible(OrdersFeedLocators.IN_WORK_ORDERS)
                order_elements = self.find_all_elements(OrdersFeedLocators.IN_WORK_ORDERS)
                
                for elem in order_elements:
                    text = elem.text.strip()
                    clean_text = "".join(ch for ch in text if ch.isdigit())
                    if clean_target == clean_text or clean_target in clean_text:
                        allure.attach(f"Найден заказ: {clean_target}", "found_order", allure.attachment_type.TEXT)
                        return True
                
                allure.attach(f"Заказ {clean_target} не найден", "order_not_found", allure.attachment_type.TEXT)
                return False
            except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
                allure.attach(str(e), "error", allure.attachment_type.TEXT)
                return False
    
    def get_in_work_order_numbers(self) -> list:
        """Получить все номера заказов в работе"""
        with allure.step("Получить все номера заказов в работе"):
            try:
                self.wait_for_element_visible(OrdersFeedLocators.IN_WORK_ORDERS)
                order_elements = self.find_all_elements(OrdersFeedLocators.IN_WORK_ORDERS)
                order_numbers = []
                seen = set()
                
                for elem in order_elements:
                    text = elem.text.strip()
                    clean_num = "".join(ch for ch in text if ch.isdigit())
                    if clean_num and len(clean_num) >= 4 and clean_num not in seen:
                        order_numbers.append(clean_num)
                        seen.add(clean_num)
                
                allure.attach(f"Найденные номера: {', '.join(order_numbers)}", "order_numbers", allure.attachment_type.TEXT)
                return order_numbers
            except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
                allure.attach(str(e), "error", allure.attachment_type.TEXT)
                return []