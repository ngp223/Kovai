from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SettingsPage:
    AJUSTES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ajustes").instance(0)')
    GENERAL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("General")')
    ASPECTO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aspecto")')
    CLARO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Claro")')
    OSCURO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Oscuro")')
    ACCESIBILIDAD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accesibilidad")')
    MEDIANA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mediana")')
    GRANDE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Grande")')
    TEXTO_EJEMPLO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Texto normal: Este es un ejemplo de cómo se verá el texto en la aplicación.")')
    NOTIFICACIONES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Notificaciones")')
    COLA_PEDIDOS_QR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Switch").instance(0)')
    ENGLISH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')
    SPANISH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Español")')
    CERRAR_SESION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cerrar sesión de usuario")')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def existe(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def acceder_ajustes(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Ajustes").instance(0))')
        self.click(self.AJUSTES)

    def cambiar_aspecto(self):
        self.click(self.ASPECTO)
        if self.existe(self.CLARO):
            self.click(self.CLARO)
            self.click(self.OSCURO)
        else:
            self.click(self.OSCURO)
            self.click(self.CLARO)

    def cambiar_accesibilidad(self):
        self.click(self.ACCESIBILIDAD)
        if self.existe(self.MEDIANA):
            self.click(self.MEDIANA)
            self.click(self.GRANDE)
        else:
            self.click(self.GRANDE)
            self.click(self.MEDIANA)

    def comprobar_tamano_texto(self):
        texto = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.TEXTO_EJEMPLO))
        tamano_actual = texto.get_attribute("bounds")
        assert tamano_actual is not None

    def desactivar_cola_pedidos_qr(self):
        self.click(self.NOTIFICACIONES)
        switch = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.COLA_PEDIDOS_QR))
        switch.click()
        time.sleep(2)

    def activar_cola_pedidos_qr(self):
        switch = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.COLA_PEDIDOS_QR))
        switch.click()
        time.sleep(2)

    def cambiar_idioma(self):
        self.click(self.GENERAL)
        if self.existe(self.SPANISH):
            self.click(self.SPANISH)
            self.click(self.ENGLISH)
        else:
            self.click(self.ENGLISH)
            self.click(self.SPANISH)

    def deshacer_cambiar_accesibilidad(self):
        self.click(self.ACCESIBILIDAD)
        if self.existe(self.GRANDE):
            self.click(self.GRANDE)
            self.click(self.MEDIANA)
        else:
            self.click(self.MEDIANA)
            self.click(self.GRANDE)

    def deshacer_cambiar_idioma(self):
        self.click(self.GENERAL)
        if self.existe(self.ENGLISH):
            self.click(self.ENGLISH)
            self.click(self.SPANISH)
        else:
            self.click(self.SPANISH)
            self.click(self.ENGLISH)

    def deshacer_cambiar_aspecto(self):
        self.click(self.ASPECTO)
        if self.existe(self.OSCURO):
            self.click(self.OSCURO)
            self.click(self.CLARO)
        else:
            self.click(self.CLARO)
            self.click(self.OSCURO)

    def cerrar_sesion(self):
        self.click(self.CERRAR_SESION)
