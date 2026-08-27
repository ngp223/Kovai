from datetime import datetime
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class ModifiersPage:
    MODIFICADORES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Modificadores")')
    NUEVO_GRUPO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nuevo Grupo")')
    NOMBRE_MODIFICADOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-outlined").instance(1)')
    CREAR_GRUPO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Crear Grupo")')
    LAPIZ = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("")')
    PAPELERA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
    ELIMINAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Eliminar")')
    ANADIR_MODIFICADOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Añadir Modificador")')
    GUARDAR_CAMBIOS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Guardar Cambios")')

    def __init__(self, driver):
        self.driver = driver
        self.modificador_creado = None
        self.modificador_modificado = None
        self.modificador_anadido = None

    def click(self, by, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def acceder_modificadores(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Modificadores"))')
        self.click(*self.MODIFICADORES)
        time.sleep(3)

    def crear_modificador(self):
        self.modificador_creado = f"ModificadorQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(*self.NUEVO_GRUPO)
        nombre = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.NOMBRE_MODIFICADOR))
        nombre.click()
        nombre.send_keys(self.modificador_creado)
        self.driver.hide_keyboard()
        self.click(*self.CREAR_GRUPO)
        time.sleep(5)

    def buscar_modificador(self):
        modificador_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.modificador_creado}")')
        try:
            modificador = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(modificador_locator))
            if modificador.is_displayed():
                return modificador
        except (NoSuchElementException, StaleElementReferenceException):
            return None
        return None

    def esperar_modificador_creado(self):
        modificador = self.buscar_modificador()
        if modificador is None:
            raise AssertionError(f"No se encontró el modificador {self.modificador_creado}")

    def buscar_fila_modificador(self, nombre_modificador):
        fila_locator = (AppiumBy.XPATH, f'//android.widget.TextView[@text="{nombre_modificador}"]/parent::*')
        try:
            return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(fila_locator))
        except (NoSuchElementException, StaleElementReferenceException):
            raise AssertionError(f"No se encontró la fila del modificador {nombre_modificador}")

    def modificar_modificador(self):
        modificador_original = self.modificador_creado
        fila = self.buscar_fila_modificador(modificador_original)
        lapiz = fila.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("")')
        lapiz.click()
        time.sleep(2)
        campo_nombre = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.NOMBRE_MODIFICADOR))
        valor_actual = campo_nombre.get_attribute("text")
        if not valor_actual:
            valor_actual = campo_nombre.get_attribute("value")
        if not valor_actual:
            raise AssertionError(f"No se pudo recuperar el nombre actual del modificador {modificador_original}")
        if valor_actual != modificador_original:
            raise AssertionError(
                f"Se abrió un modificador incorrecto. Esperado '{modificador_original}', encontrado '{valor_actual}'")
        self.modificador_modificado = f"{valor_actual}_modificado"
        campo_nombre.click()
        campo_nombre.clear()
        time.sleep(1)
        campo_nombre.send_keys(self.modificador_modificado)
        self.driver.hide_keyboard()
        time.sleep(1)
        self.click(*self.ANADIR_MODIFICADOR)
        time.sleep(2)
        size = self.driver.get_window_size()
        x = size["width"] // 2
        self.driver.swipe(x, int(size["height"] * 0.70), x, int(size["height"] * 0.30), 500)
        time.sleep(2)
        edittexts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
        if len(edittexts) < 2:
            raise AssertionError("No se encontró el campo para añadir el modificador")
        campo_nuevo = edittexts[-1]
        self.modificador_anadido = f"ModificadorQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        campo_nuevo.click()
        campo_nuevo.clear()
        campo_nuevo.send_keys(self.modificador_anadido)
        self.driver.hide_keyboard()
        self.click(*self.GUARDAR_CAMBIOS)
        time.sleep(5)
        self.modificador_creado = self.modificador_modificado

    def comprobar_modificador_modificado(self):
        modificador_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.modificador_modificado}")')
        try:
            modificador = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(modificador_locator))
        except Exception:
            raise AssertionError(f"El grupo modificado {self.modificador_modificado} no aparece en el listado")
        if modificador.text != self.modificador_modificado:
            raise AssertionError(f"El grupo modificado no coincide: esperado '{self.modificador_modificado}', encontrado '{modificador.text}'")

    def eliminar_modificador(self):
        modificador_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.modificador_creado}")')
        modificador = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(modificador_locator))
        modificador_y = modificador.location["y"]
        papeleras = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*self.PAPELERA))
        if not papeleras:
            raise AssertionError(f"No se encontraron papeleras para el modificador {self.modificador_creado}")
        papelera_correcta = min(papeleras, key=lambda papelera: abs(papelera.location["y"] - modificador_y))
        diferencia_y = abs(papelera_correcta.location["y"] - modificador_y)
        if diferencia_y > 50:
            raise AssertionError(f"La papelera seleccionada no corresponde al modificador {self.modificador_creado}")
        papelera_correcta.click()
        time.sleep(2)
        eliminar = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.ELIMINAR))
        eliminar.click()
        time.sleep(5)
