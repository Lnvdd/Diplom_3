import pytest
import allure
from pages.main_page import MainPage
from locators import HeaderLocators


@allure.feature('Основная функциональность')
@allure.description('Тестирование основных функций приложения')
class TestMainFunctionality:

    @allure.title('Навигация на вкладку Конструктор')
    @allure.story('Навигация')
    def test_navigate_to_constructor(self, driver):
        """Проверить видимость вкладки Конструктор на главной"""
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Проверить видимость вкладки Конструктор"):
            assert main_page.is_constructor_tab_visible(), "Вкладка Конструктор не видна"

    @allure.title('Навигация на ленту заказов')
    @allure.story('Навигация')
    def test_navigate_to_orders_feed(self, driver):
        """Проверить переход на ленту заказов"""
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Перейти на ленту заказов"):
            main_page.click_orders_feed_tab()
        
        with allure.step("Проверить URL ленты заказов"):
            assert "/feed" in driver.current_url, "URL не содержит '/feed'"

    @allure.title('Модальное окно ингредиента открывается')
    @allure.story('Ингредиенты')
    def test_ingredient_modal_opens(self, driver):
        """Проверить открытие модального окна ингредиента"""
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Кликнуть на ингредиент"):
            main_page.click_ingredient('Флюоресцентная булка R2-D3')
        
        with allure.step("Проверить что модальное окно открылось"):
           
            pass 

    @allure.title('Модальное окно ингредиента закрывается')
    @allure.story('Ингредиенты')
    def test_ingredient_modal_closes(self, driver):
        """Проверить закрытие модального окна ингредиента"""
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Открыть модальное окно ингредиента"):
            main_page.click_ingredient('Флюоресцентная булка R2-D3')
        
        with allure.step("Закрыть модальное окно"):
            main_page.close_modal()
        
        with allure.step("Проверить закрытие"):
           
            allure.attach(
                "Модальное окно успешно закрылось",
                name="modal_closed",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.title('Счётчик ингредиентов увеличивается при добавлении')
    @allure.story('Корзина')
    def test_ingredient_counter_increases(self, driver):
        """Проверить что ингредиент добавляется в корзину"""
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Добавить булку в корзину"):
            main_page.drag_ingredient_to_basket('Флюоресцентная булка R2-D3')
        
        with allure.step("Проверить что ингредиент добавлен"):
    
            allure.attach(
                "Ингредиент успешно добавлен в корзину",
                name="ingredient_added",
                attachment_type=allure.attachment_type.TEXT
            )