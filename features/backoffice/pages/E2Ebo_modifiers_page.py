from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from random import choice

from features.backoffice.pages.base_page import BasePage


class ModifiersPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

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

    def open_modifiers(self):

        self.wait_visible(self.MODIFIERS_MENU)

        self.click(self.MODIFIERS_MENU)

    def open_create_group_form(self):

        try:

            self.click(
                self.CREATE_FIRST_GROUP_BTN,
                timeout=5
            )

        except TimeoutException:

            self.click(
                self.NEW_GROUP_BTN,
                timeout=10
            )

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

        self.click(self.CREATE_BTN)