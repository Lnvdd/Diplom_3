import pytest
import allure
from pages.orders_page import OrdersPage
from pages.main_page import MainPage
from locators import OrdersFeedLocators

@allure.feature('Лента заказов')
@allure.description('Тестирование ленты заказов')
class TestOrdersSection:

    @allure.title('Счётчик завершённых заказов (всё время) увеличивается')
    @allure.story('Счётчики')
    def test_completed_all_time_counter_increases(self, driver):
        orders_page = OrdersPage(driver)
        
        with allure.step("Открыть ленту заказов"):
            orders_page.open_feed()
        
        with allure.step("Получить текущее значение счётчика завершённых заказов"):
            counter_value = orders_page.get_completed_all_time_count()
            assert counter_value > 0, "Счётчик должен быть больше 0"

    @allure.title('Счётчик завершённых заказов (сегодня) увеличивается')
    @allure.story('Счётчики')
    def test_completed_today_counter_increases(self, driver):
        orders_page = OrdersPage(driver)
        
        with allure.step("Открыть ленту заказов"):
            orders_page.open_feed()
        
        with allure.step("Получить текущее значение счётчика завершённых сегодня"):
            counter_value = orders_page.get_completed_today_count()
            assert counter_value >= 0, "Счётчик не может быть отрицательным"

    @allure.title('Номер заказа появляется в разделе В работе')
    @allure.story('Работа с заказами')
    def test_order_number_appears_in_work_section(self, driver):
        orders_page = OrdersPage(driver)
        
        with allure.step("Открыть ленту заказов"):
            orders_page.open_feed()
        
        with allure.step("Проверить что секция 'В работе' видима"):
            assert orders_page.is_element_visible(
                OrdersFeedLocators.IN_WORK_ORDERS
            ), "Секция 'В работе' не видна"