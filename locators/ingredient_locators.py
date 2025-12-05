from selenium.webdriver.common.by import By


class IngredientLocators:
    """Локаторы для модального окна ингредиента"""

    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    # Модальное окно с информацией об ингредиенте
    
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    # Кнопка закрытия модального окна ингредиента