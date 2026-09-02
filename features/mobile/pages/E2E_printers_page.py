from datetime import datetime
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PrintersPage:
    IMPRESORAS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Impresoras").instance(0)')
    PROMOCIONES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Promociones")')
    TAMUS_HOSTELERIA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-outlined").instance(0)')
    GRACIAS_VISITA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-outlined").instance(1)')
    FOOTER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Footer")')
    APLICAR_CAMBIOS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aplicar cambios")')

    def __init__(self, driver):
        self.driver = driver
        self.tamus_original = "Tamus Hostelería"
        self.gracias_original = "Gracias por su visita"
        self.tamus_modificado = None
        self.gracias_modificado = "Muchas gracias"

    def click(self, by, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def cerrar_teclado(self):
        try:
            self.driver.hide_keyboard()
            time.sleep(1)
        except Exception:
            pass

    def acceder_impresoras(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Impresoras").instance(0))')
        self.click(*self.IMPRESORAS)
        time.sleep(3)
        self.scroll_pantalla_impresoras()

    def scroll_pantalla_impresoras(self):
        while not self.driver.find_elements(*self.APLICAR_CAMBIOS):
            self.driver.swipe(800, 1200, 800, 500, 500)
    def modificar_campo(self, locator, valor):
        self.cerrar_teclado()
        campo = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        campo.click()
        time.sleep(1)
        campo.clear()
        time.sleep(1)
        campo.send_keys(valor)
        time.sleep(1)
        self.cerrar_teclado()

    def modificar_campos(self):
        self.tamus_modificado = f"Tamus Hosteleria {datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.modificar_campo(self.TAMUS_HOSTELERIA, self.tamus_modificado)
        self.modificar_campo(self.GRACIAS_VISITA, self.gracias_modificado)
        print(f"CAMPO TAMUS MODIFICADO: {self.tamus_modificado}")
        print(f"CAMPO GRACIAS MODIFICADO: {self.gracias_modificado}")

    def aplicar_cambios(self):
        boton = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.APLICAR_CAMBIOS))
        rect = boton.rect
        x = rect["x"] + rect["width"] // 2
        y = rect["y"] + rect["height"] // 2
        print(f"BOTON APLICAR: x={x}, y={y}, width={rect['width']}, height={rect['height']}")
        self.driver.tap([(x, y)])
        time.sleep(5)

    def salir_y_volver_impresoras(self):
        self.click(*self.PROMOCIONES)
        time.sleep(3)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Impresoras").instance(0))')
        self.click(*self.IMPRESORAS)
        time.sleep(3)
        self.scroll_pantalla_impresoras()

    def comprobar_campos_modificados(self):
        locator_tamus = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.tamus_modificado}")')
        locator_gracias = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.gracias_modificado}")')

        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator_tamus))
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator_gracias))
        except Exception:
            raise AssertionError(f"Los campos no han quedado modificados correctamente: esperado '{self.tamus_modificado}' y '{self.gracias_modificado}'")

        print(f"CAMPO TAMUS CONFIRMADO: {self.tamus_modificado}")
        print(f"CAMPO GRACIAS CONFIRMADO: {self.gracias_modificado}")

    def restablecer_campos(self):
        self.modificar_campo(self.TAMUS_HOSTELERIA, self.tamus_original)
        self.modificar_campo(self.GRACIAS_VISITA, self.gracias_original)
        self.aplicar_cambios()
        print(f"CAMPO TAMUS RESTABLECIDO: {self.tamus_original}")
        print(f"CAMPO GRACIAS RESTABLECIDO: {self.gracias_original}")

    def comprobar_campos_restablecidos(self):
        locator_tamus = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.tamus_original}")')
        locator_gracias = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.gracias_original}")')

        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator_tamus))
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator_gracias))
        except Exception:
            raise AssertionError(f"Los campos no han sido restablecidos correctamente: esperado '{self.tamus_original}' y '{self.gracias_original}'")

        print(f"CAMPO TAMUS RESTABLECIDO CONFIRMADO: {self.tamus_original}")
        print(f"CAMPO GRACIAS RESTABLECIDO CONFIRMADO: {self.gracias_original}")
