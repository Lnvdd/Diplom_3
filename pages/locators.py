from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.education-services.ru"

class Urls:
    MAIN = BASE_URL + "/"
    FEED = BASE_URL + "/feed"
    INGREDIENT_F_BULKA = BASE_URL + "/ingredient/61c0c5a71d1f82001bdaaa6d"

class AuthLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_FORM_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    RECOVERY_FORM_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    PASSWORD_ERROR_MSG = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

class HeaderLocators:
    MAIN_LOGIN_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_LINK = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_TAB = (By.LINK_TEXT, "Конструктор")
    ORDERS_FEED_TAB = (By.LINK_TEXT, "Лента Заказов")
    LOGO_LINK = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a[@href='/']")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Выход']")

class IngredientLocators:
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

class BasketLocators:
    BURGER_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_SUBMIT_BTN = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]")

class ModalLocators:
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    ORDER_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")

class OrdersFeedLocators:
    COMPLETED_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    IN_WORK_ORDERS = (By.CLASS_NAME, "text_type_digits-default")