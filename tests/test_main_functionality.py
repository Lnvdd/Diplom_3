import pytest
import allure
from pages.main_page import MainPage
from pages.locators import HeaderLocators, Urls
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import IngredientLocators



@allure.feature('Основная функциональность')
@allure.description('Тестирование основных функций приложения')
class TestMainFunctionality:

    @allure.title('Навигация на вкладку Конструктор')
    @allure.story('Навигация')
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Проверить наличие вкладки Конструктор"):
            constructor_tab = driver.find_element(*HeaderLocators.CONSTRUCTOR_TAB)
            assert constructor_tab.is_displayed(), "Вкладка Конструктор не видна"

    @allure.title('Навигация на ленту заказов')
    @allure.story('Навигация')
    def test_navigate_to_orders_feed(self, driver):
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
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Кликнуть на ингредиент"):
            main_page.click_ingredient('Флюоресцентная булка R2-D3')
        
        with allure.step("Проверить видимость модального окна"): 
            wait = WebDriverWait(driver, 10)
            modal = wait.until(EC.visibility_of_element_located(IngredientLocators.MODAL_WINDOW))
            assert modal.is_displayed(), "Модальное окно не открылось"

    @allure.title('Модальное окно ингредиента закрывается')
    @allure.story('Ингредиенты')
    def test_ingredient_modal_closes(self, driver):
       
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Открыть модальное окно ингредиента"):
            main_page.click_ingredient('Флюоресцентная булка R2-D3')
        
        with allure.step("Закрыть модальное окно"):
            main_page.close_modal()
        
        with allure.step("Проверить закрытие модального окна"):
            wait = WebDriverWait(driver, 10)
            wait.until(EC.invisibility_of_element_located(IngredientLocators.MODAL_WINDOW))
            allure.attach(
                "Модальное окно успешно закрылось",
                name="modal_closed",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.title('Счётчик ингредиентов увеличивается при добавлении')
    @allure.story('Корзина')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        
        with allure.step("Добавить булку в корзину"):
            main_page.drag_ingredient_to_basket('Флюоресцентная булка R2-D3')
        
        with allure.step("Проверить что булка добавлена"):
            from pages.locators import BasketLocators
            
            order_btn = driver.find_element(*BasketLocators.ORDER_SUBMIT_BTN)
            assert order_btn.is_enabled(), "Кнопка заказа не активна"
            
            allure.attach(
                "Ингредиент успешно добавлен в корзину",
                name="ingredient_added",
                attachment_type=allure.attachment_type.TEXT
            )