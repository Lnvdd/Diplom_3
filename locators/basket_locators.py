from selenium.webdriver.common.by import By


class BasketLocators:
    """Локаторы для работы с корзиной и оформлением заказа"""

    BURGER_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    # Контейнер корзины (область для drag-and-drop ингредиентов)

    ORDER_SUBMIT_BTN = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]")
    # Кнопка "Оформить заказ" (основная кнопка оформления)