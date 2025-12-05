from selenium.webdriver.common.by import By


class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru" # Базовый URL приложения
    MAIN = f"{BASE_URL}/" # Главная страница (конструктор бургеров)
    FEED = f"{BASE_URL}/feed"   # Страница ленты заказов
    INGREDIENT_F_BULKA = f"{BASE_URL}/ingredient/61c0c5a71d1f82001bdaaa6d" # Страница ингредиента