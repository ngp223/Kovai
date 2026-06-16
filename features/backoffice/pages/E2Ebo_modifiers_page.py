from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import choice
import time


class ModifiersPage_bo:

    def __init__(self, driver):
        self.driver = driver

    MODIFIERS_MENU = (
        By.XPATH,
        "//a[@href='/modifiers']"
    )

    CREATE_FIRST_GROUP_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Crear primer grupo')]"
    )

    NEW_GROUP_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Nuevo Grupo')]"
    )

    GROUP_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: Punto de la carne, Extras, etc.']"
    )

    OPTION_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Nombre de la opción (Ej: Muy hecho)']"
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

    def open_modifiers(self):

        self.click(self.MODIFIERS_MENU)

        time.sleep(2)

    def open_create_group_form(self):

        try:

            print("Intentando botón: Crear primer grupo")

            self.click(
                self.CREATE_FIRST_GROUP_BTN,
                timeout=5
            )

            print("Encontrado: Crear primer grupo")

        except TimeoutException:

            print(
                "No existe 'Crear primer grupo'. "
                "Probando '+ Nuevo Grupo'"
            )

            self.click(
                self.NEW_GROUP_BTN,
                timeout=10
            )

            print("Encontrado: + Nuevo Grupo")

        time.sleep(2)

    def create_modifier_group(self, group_name):

        self.open_create_group_form()

        self.fill(
            self.GROUP_NAME_INPUT,
            group_name
        )

        option_name = choice([
            "Muy hecho",
            "Poco hecho",
            "Al punto"
        ])

        self.fill(
            self.OPTION_NAME_INPUT,
            option_name
        )

        time.sleep(1)

        self.click(self.CREATE_BTN)

        time.sleep(4)