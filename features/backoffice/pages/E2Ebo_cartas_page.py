from selenium.webdriver.common.by import By

from features.backoffice.pages.base_page import BasePage


class CartasPage_bo(BasePage):

    CARTAS_MENU = (
        By.XPATH,
        "//a[contains(.,'Cartas')]"
    )

    ADD_CARTA_BTN = (
        By.XPATH,
        "//button[contains(.,'Añadir carta')]"
    )

    NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: Carta Estándar, Carta Premium...']"
    )

    RADIO_OPTION = (
        By.XPATH,
        "//input[@type='radio']"
    )

    CREATE_BTN = (
        By.XPATH,
        "//button[@type='submit' and contains(.,'Crear')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open_cartas(self):
        self.click(self.CARTAS_MENU)

    def create_carta(self, name):
        self.click(self.ADD_CARTA_BTN)
        self.fill(self.NAME_INPUT, name)
        self.click(self.RADIO_OPTION)
        self.click(self.CREATE_BTN)