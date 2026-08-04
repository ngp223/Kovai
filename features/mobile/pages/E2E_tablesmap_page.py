from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


class TablesMapPage:

    TABLESMAP = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Mapa de mesas"]'
    )

    GESTIONAR_TARIFAS = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Gestionar Tarifas"]'
    )

    CREAR_NUEVA_TARIFA = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc=", Crear Nueva Tarifa"]'
    )

    NOMBRE_TARIFA = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("text-input-outlined").instance(0)'
    )

    GUARDAR = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Guardar"]'
    )

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(by, locator)
        )
        element.click()

    def open_tablemap(self):
        self.click(*self.TABLESMAP)

    def crear_tarifa(self):
        nombre_tarifa = f"TarifaQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.driver.find_element(*self.GESTIONAR_TARIFAS).click()
        self.driver.find_element(*self.CREAR_NUEVA_TARIFA).click()
        self.driver.find_element(*self.NOMBRE_TARIFA).send_keys(nombre_tarifa)
        self.driver.find_element(*self.GUARDAR).click()

