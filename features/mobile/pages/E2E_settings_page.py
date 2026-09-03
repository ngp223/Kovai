from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage:
    AJUSTES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ajustes").instance(0)')
    ASPECTO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aspecto")')
    CLARO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Claro")')
    OSCURO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Oscuro")')
    ACCESIBILIDAD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accesibilidad")')
    MEDIANA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mediana")')
    GRANDE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Grande")')
    TEXTO_EJEMPLO = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Texto normal: Este es un ejemplo de cómo se verá el texto en la aplicación.")'
    )
    IDIOMA = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Idioma, Español, ")'
    )
    ENGLISH = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("English")'
    )
    CERRAR_SESION = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Cerrar sesión de usuario, ")'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.tamano_texto_anterior = None

    def click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def acceder_ajustes(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Ajustes").instance(0))'
        )
        self.click(self.AJUSTES)

    def cambiar_aspecto(self):
        self.click(self.ASPECTO)
        self.click(self.CLARO)
        self.click(self.OSCURO)

    def cambiar_accesibilidad(self):
        self.click(self.ACCESIBILIDAD)

        texto = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.TEXTO_EJEMPLO)
        )

        self.tamano_texto_anterior = texto.get_attribute("bounds")

        self.click(self.MEDIANA)
        self.click(self.GRANDE)

    def comprobar_tamano_texto(self):
        texto = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.TEXTO_EJEMPLO)
        )

        tamano_actual = texto.get_attribute("bounds")

        assert tamano_actual is not None
        assert self.tamano_texto_anterior is not None
        assert tamano_actual != self.tamano_texto_anterior

    def cambiar_idioma(self):
        self.click(self.IDIOMA)
        self.click(self.ENGLISH)

    def cerrar_sesion(self):
        self.click(self.CERRAR_SESION)
