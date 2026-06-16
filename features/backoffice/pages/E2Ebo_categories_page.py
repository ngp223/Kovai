from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CategoriesPage_bo:

    def __init__(self, driver):
        self.driver = driver

    CATEGORIES_MENU = (
        By.XPATH,
        "//a[@href='/categories']"
    )

    NEW_CATEGORY_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Nueva Categoría')]"
    )

    CATEGORY_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: Bebidas']"
    )

    CREATE_BTN = (
        By.XPATH,
        "//button[@type='submit' and contains(normalize-space(),'Crear')]"
    )

    def click(self, locator, timeout=15):

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def fill(self, locator, value, timeout=15):

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(value)

    def open_categories(self):

        self.click(self.CATEGORIES_MENU)

        time.sleep(2)

    def create_category(self, category_name):

        self.click(
            self.NEW_CATEGORY_BTN,
            timeout=10
        )

        time.sleep(2)

        self.fill(
            self.CATEGORY_NAME_INPUT,
            category_name
        )

        time.sleep(1)

        self.click(self.CREATE_BTN)

        time.sleep(4)