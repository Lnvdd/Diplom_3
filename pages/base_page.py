import re
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
    
    def go_to_url(self, path):
        """Открыть страницу (альтернативный метод)"""
        self.open(path)
    
    def find_element(self, locator):
        """Найти элемент"""
        return self.driver.find_element(*locator)
    
    def find_visible_element(self, locator):
        """Найти видимый элемент"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_clickable_element(self, locator):
        """Найти кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def find_all_elements(self, locator):
        """Найти все элементы"""
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator):
        """Кликнуть на элемент"""
        element = self.find_clickable_element(locator)
        element.click()
    
    def is_element_visible(self, locator) -> bool:
        """Проверить видимость элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False
    
    def is_element_invisible(self, locator) -> bool:
        """Проверить что элемент невидим или отсутствует"""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False
    
    def wait_for_element_visible(self, locator) -> bool:
        """Ждать видимости элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_url(self, url_part):
        """Ждать пока URL содержит часть"""
        self.wait.until(EC.url_contains(url_part))
    
    def drag_and_drop(self, source_locator, target_locator):
        """Drag and drop элемента"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()
    
    def get_element_text(self, locator) -> str:
        """Получить текст элемента"""
        element = self.find_visible_element(locator)
        return element.text.strip()
    
    def get_current_url(self) -> str:
        """Получить текущий URL"""
        return self.driver.current_url
    
    def get_locator_with_text(self, xpath_template: str, text: str):
        """Получить локатор с отформатированным текстом"""
        xpath = xpath_template.format(text)
        return (By.XPATH, xpath)
    
    def wait_for_order_number(self, locator) -> str:
        """Ждать загрузки номера заказа (не 9999)"""
        class OrderNumberLoaded:
            def __init__(self, loc):
                self.locator = loc
            
            def __call__(self, driver):
                element = driver.find_element(*self.locator)
                text = element.text.strip()
                order_number = re.sub(r'[^\d]', '', text)
                if order_number and order_number != "9999":
                    return element
                return False
        
        element = self.wait.until(OrderNumberLoaded(locator))
        text = element.text.strip()
        return re.sub(r'[^\d]', '', text)