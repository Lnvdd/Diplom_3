from selenium.webdriver.common.by import By


class IngredientLocators:
    MODAL_WINDOW = (By.CSS_SELECTOR, "[class*='ingredient']")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'close')]")
    INGREDIENT_ITEM = (By.XPATH, "//p[contains(text(), '{}')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(text(), '{}')]/following-sibling::span")


class Ingredients:
    BULLA = "Флюоресцентная булка R2-D3"