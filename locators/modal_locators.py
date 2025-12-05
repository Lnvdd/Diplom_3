from selenium.webdriver.common.by import By


class ModalLocators:
    """Локаторы для модальных окон (ингредиентов, заказов и т.д.)"""

    MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    # Основное контейнер модального окна (любого типа)
    
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    # Модальное окно с деталями заказа
    
    ORDER_DETAILS_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    # Модальное окно с полными деталями заказа

    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    # Элемент с номером заказа (h2 с классом Modal_modal__title)
    
    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    # Номер заказа внутри модального окна (используется для проверки загрузки)

    ORDER_CLOSE_BTN = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]//button[contains(@class, 'Modal_modal__close')] | "
        "//section[contains(@class, 'Modal_modal')]//div[contains(@class, 'Modal_modal__close')]"
    )
    # Кнопка закрытия модального окна 