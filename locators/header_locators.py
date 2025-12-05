from selenium.webdriver.common.by import By


class HeaderLocators:
    """Локаторы для навигации и элементов в header"""

    MAIN_LOGIN_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка входа в аккаунт в header (для неавторизованных пользователей)
    
    PROFILE_LINK = (By.XPATH, "//a[@href='/account']")
    # Ссылка на профиль пользователя (для авторизованных)
    
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Выход']")
    # Кнопка выхода из аккаунта

    CONSTRUCTOR_TAB = (By.LINK_TEXT, "Конструктор")
    # Вкладка для перехода на страницу конструктора бургеров
    
    ORDERS_FEED_TAB = (By.LINK_TEXT, "Лента Заказов")
    # Вкладка для перехода на ленту всех заказов

    LOGO_LINK = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a[@href='/']")
    # Логотип приложения (ссылка на главную страницу)