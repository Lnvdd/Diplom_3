import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import Urls  


class BasePage:
    """Базовый класс для всех страниц приложения"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def open(self, path):
        """Открыть страницу по пути"""
        with allure.step(f"Открыть страницу {path}"):
            self.driver.get(f"{Urls.BASE_URL}{path}")
    
    def find_element(self, locator):
        """Найти элемент"""
        return self.driver.find_element(*locator)
    
    def find_visible_element(self, locator):
        """Найти видимый элемент"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_clickable_element(self, locator):
        """Найти кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_element(self, locator):
        """Кликнуть на элемент"""
        element = self.find_clickable_element(locator)
        element.click()
    
    def is_element_visible(self, locator) -> bool:
        """Проверить видимость элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
    
    def wait_for_url(self, url_part):
        """Ждать пока URL содержит часть"""
        self.wait.until(EC.url_contains(url_part))
    
    def drag_and_drop(self, source_locator, target_locator):
        """Drag and drop элемента"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()