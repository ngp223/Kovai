from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class PromotionsPage_bo:

    def __init__(self, driver):
        self.driver = driver

    PROMOTIONS_MENU = (
        By.XPATH,
        "//a[@href='/promotions']"
    )

    CREATE_FIRST_PROMOTION_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Crear primera promoción')]"
    )

    NEW_PROMOTION_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Nueva Promoción')]"
    )

    PROMOTION_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: 2x1 en Cervezas']"
    )

    CREATE_PROMOTION_BTN = (
        By.XPATH,
        "//button[@type='submit' and contains(.,'Crear Promoción')]"
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

    def open_promotions(self):

        self.click(self.PROMOTIONS_MENU)

        time.sleep(2)

    def open_create_promotion_form(self):

        try:
            print("Intentando botón: Crear primera promoción")

            self.click(
                self.CREATE_FIRST_PROMOTION_BTN,
                timeout=5
            )

            print("Encontrado: Crear primera promoción")

        except TimeoutException:

            print(
                "No existe 'Crear primera promoción'. "
                "Probando '+ Nueva Promoción'"
            )

            self.click(
                self.NEW_PROMOTION_BTN,
                timeout=10
            )

            print("Encontrado: + Nueva Promoción")

        time.sleep(2)

    def create_promotion(self, promotion_name):

        self.open_create_promotion_form()

        self.fill(
            self.PROMOTION_NAME_INPUT,
            promotion_name
        )

        time.sleep(2)

        self.click(self.CREATE_PROMOTION_BTN)

        time.sleep(4)