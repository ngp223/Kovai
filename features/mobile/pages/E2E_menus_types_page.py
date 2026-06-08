from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


class CardsPage:

    CARTAS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc=", Cartas"]'
    )

    ANADIR_CARTA = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Añadir Carta"]'
    )

    NOMBRE_CARTA = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[2]'
    )

    REFERENCIA = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[3]'
    )

    DESCRIPCION = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[4]'
    )

    SIGUIENTE = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="Siguiente"]/android.view.ViewGroup'
    )

    FINALIZAR_Y_GUARDAR = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="Finalizar y Guardar"]/android.view.ViewGroup'
    )

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(by, locator)
        )
        element.click()

    def fill(self, by, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(by, locator)
        )
        element.clear()
        element.send_keys(value)

    def open_cards(self):
        self.click(*self.CARTAS)

    def create_new_card(self):

        self.click(*self.ANADIR_CARTA)

        self.fill(*self.NOMBRE_CARTA, "Carta QA")
        self.fill(*self.REFERENCIA, "ReferenciaQA")
        self.fill(*self.DESCRIPCION, "Carta del equipo de QA")

        self.click(*self.SIGUIENTE)
        self.click(*self.SIGUIENTE)
        self.click(*self.SIGUIENTE)

        self.click(*self.FINALIZAR_Y_GUARDAR)