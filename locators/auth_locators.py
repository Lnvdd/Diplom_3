from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы для форм авторизации, регистрации и восстановления пароля"""

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле ввода имени при регистрации
    
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле ввода email при регистрации
    
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Поле ввода пароля при регистрации
    
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Кнопка для отправки формы регистрации
    
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    # Поле ввода email на странице входа
    
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Поле ввода пароля на странице входа
    
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Кнопка входа в аккаунт

    REGISTER_FORM_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    # Ссылка на форму входа со страницы регистрации
    
    RECOVERY_FORM_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    # Ссылка на форму входа со страницы восстановления пароля

    PASSWORD_ERROR_MSG = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    # Сообщение об ошибке неправильного пароля