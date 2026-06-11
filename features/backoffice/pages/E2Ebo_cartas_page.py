from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartasPage_bo:

    def __init__(self, driver):
        self.driver = driver

    CARTAS_MENU = (By.XPATH, "//a[contains(.,'Cartas')]")
    ADD_CARTA_BTN = (By.XPATH, "//button[contains(.,'Añadir carta')]")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Ej: Carta Estándar, Carta Premium...']")
    RADIO_OPTION = (By.XPATH, "//input[@type='radio']")
    CREATE_BTN = (By.XPATH, "//button[@type='submit' and contains(.,'Crear')]")

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def fill(self, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)

    def open_cartas(self):
        self.click(self.CARTAS_MENU)

    def create_carta(self, name):

        self.click(self.ADD_CARTA_BTN)
        self.fill(self.NAME_INPUT, name)
        self.click(self.RADIO_OPTION)
        self.click(self.CREATE_BTN)