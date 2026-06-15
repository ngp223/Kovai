from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductsPage_bo:

    def __init__(self, driver):
        self.driver = driver

    PRODUCTS_MENU = (
        By.XPATH,
        "//*[@id='root']/div/div/aside/nav/a[4]"
    )

    NUEVO_PRODUCT_BTN = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/header/div[2]/button"
    )

    NOMBRE_INPUT = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/form/div[1]/div[2]/input"
    )

    CREAR_BTN = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/form/div[2]/button[2]"
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

    def scroll_down(self):

        self.driver.execute_script(
            "window.scrollBy(0,800);"
        )

        time.sleep(1)

    def open_products(self):

        self.click(self.PRODUCTS_MENU)

    def create_product(self, nombre):

        self.click(self.NUEVO_PRODUCT_BTN)

        time.sleep(1)

        self.fill(self.NOMBRE_INPUT, nombre)

        self.scroll_down()

        time.sleep(1)

        self.click(self.CREAR_BTN)

        time.sleep(3)
