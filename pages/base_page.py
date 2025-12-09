import allure
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from locators.urls import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def go_to_url(self, url: str):
        with allure.step(f"Перейти на URL: {url}"):
            self.driver.get(url)

    def open(self, path=""):
        with allure.step(f"Открыть страницу {path}"):
            url = f"{Urls.BASE_URL}{path}"
            self.driver.get(url)


    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)


    def click_element(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()


    def is_element_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_invisible(self, locator) -> bool:
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_condition(self, condition_func, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition_func)

    def wait_for_order_number_loaded(self, locator, timeout=10):
        return self.wait_for_condition(order_number_loaded(locator), timeout)


    def get_current_url(self) -> str:
        return self.driver.current_url

    def wait_for_url_change(self, old_url: str):
        self.wait.until(EC.url_changes(old_url))

    def wait_for_url_contains(self, url_part: str):
        self.wait.until(EC.url_contains(url_part))


    def get_element_text(self, locator) -> str:
        element = self.find_visible_element(locator)
        return element.text.strip()

    def clear_and_send_keys(self, locator, text: str):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)


    def verify_element_visible(self, locator, message: str = "Элемент должен быть видимым"):
        assert self.is_element_visible(locator), message

    def verify_element_invisible(self, locator, message: str = "Элемент должен быть невидимым"):
        assert self.is_element_invisible(locator), message

    def verify_url_contains(self, url_part: str, message: str = None):
        if message is None:
            message = f"URL должен содержать '{url_part}'"
        assert url_part in self.get_current_url(), message

    def verify_element_text(self, locator, expected_text: str, message: str = None):
        if message is None:
            message = f"Текст должен быть '{expected_text}'"
        actual_text = self.get_element_text(locator)
        assert actual_text == expected_text, f"{message} (получил: '{actual_text}')"


class order_number_loaded:

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)
            text = element.text.strip()
            order_number = re.sub(r'[^\d]', '', text)
            if order_number and order_number != "9999":
                return element
            return False
        except StaleElementReferenceException:
            return False