from selenium.webdriver.common.by import By

class Ingredients:
    """Константы названий ингредиентов"""
    BULLA = "Флюоресцентная булка R2-D3"
    SAUCE_SPICY = "Соус Spicy-X"
 

class IngredientLocators:
    """Локаторы для ингредиентов"""
    
    MODAL_WINDOW = (By.CSS_SELECTOR, "[class*='Modal_modal']")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    
    INGREDIENT_BULLA = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]")
    INGREDIENT_BULLA_COUNTER = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]/ancestor::*//p[contains(@class, 'counter')]")
    
   
    INGREDIENT_BY_NAME_XPATH = "//p[contains(text(), '{}')]"
    INGREDIENT_COUNTER_BY_NAME_XPATH = "//p[contains(text(), '{}')]/ancestor::*//p[contains(@class, 'counter')]"