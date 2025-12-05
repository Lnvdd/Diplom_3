from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    """Локаторы для страницы ленты заказов"""

    COMPLETED_ALL_TIME = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    # Счётчик всех выполненных заказов за всё время
    
    COMPLETED_TODAY = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    # Счётчик выполненных заказов за сегодня

    IN_WORK_ORDERS = (By.CLASS_NAME, "text_type_digits-default")
    # Список номеров заказов, находящихся в работе (в статусе "в процессе")