from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


class BillingPage:

    FACTURACION = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Facturación"]'
    )

    NUEVA_FACTURA = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc=", Nueva Factura"]/android.view.ViewGroup/android.widget.TextView[@text="Nueva Factura"]'
    )

    GENERAR_FACTURA = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Generar Factura"])[3]'
    )

    EMPRESA = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[1]'
    )

    CIF = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[2]'
    )

    DIRECCION = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[3]'
    )

    CIUDAD = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[4]'
    )

    CODIGO_POSTAL = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[5]'
    )

    CONFIRMAR_FACTURA = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Confirmar y Emitir Factura"]'
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

    def open_billing(self):
        self.click(*self.FACTURACION)

    def create_new_invoice(self):

        self.click(*self.NUEVA_FACTURA)

        self.click(*self.GENERAR_FACTURA)

        self.fill(*self.EMPRESA, "Empresa QANER")
        self.fill(*self.CIF, "E46116687")
        self.fill(*self.DIRECCION, "Calle de ejemplo, 1")
        self.fill(*self.CIUDAD, "Madrid")
        self.fill(*self.CODIGO_POSTAL, "28001")

        self.click(*self.CONFIRMAR_FACTURA)