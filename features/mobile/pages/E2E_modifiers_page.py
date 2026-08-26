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
    PAPELERA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
    ELIMINAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Eliminar")')

    def __init__(self, driver):
        self.driver = driver
        self.modificador_creado = None

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
