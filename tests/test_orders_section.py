import pytest
import allure
from pages.main_page import MainPage
from pages.orders_page import OrdersPage


@allure.feature('Лента Заказов')
@allure.description('Тестирование функциональности раздела "Лента заказов"')
class TestOrdersSection:

    @allure.title('Счётчик "Выполнено за все время" увеличивается при создании заказа')
    @allure.story('Счётчики')
    def test_completed_all_time_counter_increases(self, authenticated_driver):
        """Проверить что счётчик 'за всё время' растёт после создания заказа"""
        driver = authenticated_driver
        orders_page = OrdersPage(driver)
        main_page = MainPage(driver)
        
        with allure.step("Открыть ленту заказов и записать начальный счётчик"):
            orders_page.open_feed()
            initial_count = orders_page.get_completed_all_time_count()
            allure.attach(
                f"Начальный счётчик: {initial_count}",
                name="initial_counter",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("Перейти на конструктор"):
            main_page.click_constructor_tab()
        
        with allure.step("Добавить булку в корзину"):
            main_page.drag_ingredient_to_basket('Флюоресцентная булка R2-D3')
        
        with allure.step("Добавить соус в корзину"):
            main_page.drag_ingredient_to_basket('Соус Spicy-X')
        
        with allure.step("Оформить заказ"):
            main_page.submit_order()
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.close_order_modal()
        
        with allure.step("Перейти в ленту заказов и проверить новый счётчик"):
            main_page.click_orders_feed_tab()
            updated_count = orders_page.get_completed_all_time_count()
            allure.attach(
                f"Обновленный счётчик: {updated_count}",
                name="updated_counter",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("Проверить что счётчик увеличился"):
           
            assert updated_count > initial_count, \
                f"Счётчик не увеличился. Было: {initial_count}, Стало: {updated_count}"
            allure.attach(
                f"Счётчик увеличился на {updated_count - initial_count}",
                name="assertion_result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.title('Счётчик "Выполнено за сегодня" увеличивается при создании заказа')
    @allure.story('Счётчики')
    def test_completed_today_counter_increases(self, authenticated_driver):
        """Проверить что счётчик 'за сегодня' растёт после создания заказа"""
        driver = authenticated_driver
        orders_page = OrdersPage(driver)
        main_page = MainPage(driver)
        
        with allure.step("Открыть ленту заказов и записать начальный счётчик"):
            orders_page.open_feed()
            initial_count = orders_page.get_completed_today_count()
            allure.attach(
                f"Начальный счётчик: {initial_count}",
                name="initial_counter",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("Перейти на конструктор"):
            main_page.click_constructor_tab()
        
        with allure.step("Добавить булку в корзину"):
            main_page.drag_ingredient_to_basket('Флюоресцентная булка R2-D3')
        
        with allure.step("Добавить соус в корзину"):
            main_page.drag_ingredient_to_basket('Соус Spicy-X')
        
        with allure.step("Оформить заказ"):
            main_page.submit_order()
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.close_order_modal()
        
        with allure.step("Перейти в ленту заказов и проверить новый счётчик"):
            main_page.click_orders_feed_tab()
            updated_count = orders_page.get_completed_today_count()
            allure.attach(
                f"Обновленный счётчик: {updated_count}",
                name="updated_counter",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("Проверить что счётчик увеличился"):
            
            assert updated_count > initial_count, \
                f"Счётчик не увеличился. Было: {initial_count}, Стало: {updated_count}"
            allure.attach(
                f"Счётчик увеличился на {updated_count - initial_count}",
                name="assertion_result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.title('Номер заказа появляется в разделе "В работе"')
    @allure.story('Заказы')
    def test_order_number_appears_in_work_section(self, authenticated_driver):
        """Проверить что номер заказа появляется в разделе 'В работе'"""
        driver = authenticated_driver
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Добавить булку в корзину"):
            main_page.drag_ingredient_to_basket('Флюоресцентная булка R2-D3')
        
        with allure.step("Добавить соус в корзину"):
            main_page.drag_ingredient_to_basket('Соус Spicy-X')
        
        with allure.step("Оформить заказ и получить номер"):
            order_number = main_page.submit_order_and_get_number()
            allure.attach(
                f"Номер заказа: {order_number}",
                name="order_number",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.close_order_modal()
        
        with allure.step("Перейти на ленту заказов"):
            main_page.click_orders_feed_tab()
        
        with allure.step(f"Найти заказ {order_number} в разделе 'В работе'"):
            found = orders_page.find_order_in_work_section(order_number)
        
        with allure.step("Проверить что заказ найден"):
            
            assert found, \
                f"Заказ '{order_number}' не найден в разделе 'В работе'"
            allure.attach(
                f"Заказ {order_number} найден в разделе 'В работе'",
                name="order_found",
                attachment_type=allure.attachment_type.TEXT
            )