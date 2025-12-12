import pytest
import allure
from pages.main_page import MainPage
from locators import HeaderLocators, IngredientLocators
from locators.ingredient_locators import Ingredients

@allure.feature("Основная функциональность")
@allure.description("Тестирование основных функций приложения")
class TestMainFunctionality:
    
    @allure.title("Навигация на вкладку Конструктор")
    @allure.story("Навигация")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        with allure.step("Проверить видимость вкладки Конструктор"):
            assert main_page.is_constructor_tab_visible(), "Вкладка Конструктор не видна"
    
    @allure.title("Навигация на ленту заказов")
    @allure.story("Навигация")
    def test_navigate_to_orders_feed(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        with allure.step("Перейти на ленту заказов"):
            main_page.click_orders_feed_tab()
        with allure.step("Проверить URL ленты заказов"):
            current_url = main_page.get_current_url()
            assert "/feed" in current_url, "URL не содержит '/feed'"
    
    @allure.title("Модальное окно ингредиента открывается")
    @allure.story("Ингредиенты")
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        with allure.step(f"Кликнуть на ингредиент '{Ingredients.BULLA}'"):
            main_page.click_ingredient(Ingredients.BULLA)
        with allure.step("Проверить что модальное окно открылось"):
            assert main_page.is_element_visible(
                IngredientLocators.MODAL_WINDOW
            ), "Модальное окно не открылось"
    
    @allure.title("Модальное окно ингредиента закрывается кликом на крестик")
    @allure.story("Ингредиенты")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        with allure.step(f"Открыть модальное окно ингредиента '{Ingredients.BULLA}'"):
            main_page.click_ingredient(Ingredients.BULLA)
        with allure.step("Закрыть модальное окно кликом на крестик"):
            main_page.close_modal()
        with allure.step("Проверить что модальное окно закрылось"):
            assert main_page.is_element_invisible(
                IngredientLocators.MODAL_WINDOW
            ), "Модальное окно должно закрыться"
    
    @allure.title("Счётчик ингредиентов увеличивается при добавлении")
    @allure.story("Корзина")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        with allure.step("Добавить булку в корзину"):
            main_page.drag_ingredient_to_basket(Ingredients.BULLA)
        with allure.step("Получить значение счётчика булки"):
            counter_value = main_page.get_ingredient_counter(Ingredients.BULLA)
        with allure.step("Проверить что счётчик равен 2"):
            assert counter_value == 2, \
                f"Счётчик булки должен быть 2, но стал {counter_value}"
