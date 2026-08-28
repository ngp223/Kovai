from datetime import datetime
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

class PromotionsPage:
    PROMOCIONES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Promociones")')
    NUEVA_PROMOCION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nueva Promoción")')
    NOMBRE_PROMOCION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-outlined").instance(1)')
    BUSCADOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-outlined").instance(0)')
    CREAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Crear")')
    LAPIZ = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
    PAPELERA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
    ACTUALIZAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Actualizar")')
    ELIMINAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Eliminar")')

    def __init__(self, driver):
        self.driver = driver
        self.promocion_creada = None
        self.promocion_modificada = None

    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def acceder_promociones(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Promociones"))')
        self.click(*self.PROMOCIONES)
        time.sleep(2)

    def crear_promocion(self):
        self.promocion_creada = f"PromocionQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(*self.NUEVA_PROMOCION)
        campo_nombre = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NOMBRE_PROMOCION))
        campo_nombre.click()
        campo_nombre.clear()
        campo_nombre.send_keys(self.promocion_creada)
        self.driver.hide_keyboard()
        self.click(*self.CREAR)
        time.sleep(3)

    def buscar_promocion(self, nombre_promocion):
        buscador = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.BUSCADOR))
        buscador.click()
        buscador.clear()
        buscador.send_keys(nombre_promocion)
        self.driver.hide_keyboard()
        promocion_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{nombre_promocion}")')
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(promocion_locator))

    def esperar_promocion_creada(self):
        self.buscar_promocion(self.promocion_creada)

    def buscar_fila_promocion(self, nombre_promocion):
        fila_locator = (AppiumBy.XPATH, f'//android.widget.TextView[@text="{nombre_promocion}"]/parent::*')
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(fila_locator))
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            raise AssertionError(f"No se encontró la fila de la promoción {nombre_promocion}")

    def modificar_promocion(self):
        fila = self.buscar_fila_promocion(self.promocion_creada)
        try:
            lapiz = fila.find_element(*self.LAPIZ)
        except NoSuchElementException:
            raise AssertionError(f"No se encontró el lápiz de la promoción {self.promocion_creada}")
        lapiz.click()
        time.sleep(2)
        campo_nombre = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NOMBRE_PROMOCION))
        valor_actual = campo_nombre.get_attribute("text") or campo_nombre.get_attribute("value")
        if valor_actual != self.promocion_creada:
            raise AssertionError(f"Se abrió una promoción incorrecta. Esperado '{self.promocion_creada}', encontrado '{valor_actual}'")
        self.promocion_modificada = f"{valor_actual}_modificado"
        campo_nombre.click()
        campo_nombre.clear()
        campo_nombre.send_keys(self.promocion_modificada)
        self.driver.hide_keyboard()
        self.click(*self.ACTUALIZAR, timeout=5)
        time.sleep(3)

    def comprobar_promocion_modificada(self):
        promocion_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.promocion_modificada}")')
        try:
            promocion = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(promocion_locator))
        except TimeoutException:
            raise AssertionError(f"La promoción modificada {self.promocion_modificada} no aparece en el listado")
        if promocion.text != self.promocion_modificada:
            raise AssertionError(f"La promoción modificada no coincide: esperado '{self.promocion_modificada}', encontrado '{promocion.text}'")

    def eliminar_promocion(self):
        fila = self.buscar_fila_promocion(self.promocion_modificada)
        try:
            papelera = fila.find_element(*self.PAPELERA)
        except NoSuchElementException:
            raise AssertionError(f"No se encontró la papelera de la promoción {self.promocion_modificada}")
        papelera.click()
        time.sleep(2)
        self.click(*self.ELIMINAR, timeout=5)
        time.sleep(3)
        promocion_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.promocion_modificada}")')
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(promocion_locator))
        except TimeoutException:
            raise AssertionError(f"La promoción {self.promocion_modificada} continúa apareciendo después de eliminarla")
