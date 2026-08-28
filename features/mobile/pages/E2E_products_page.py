from datetime import datetime
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductsPage:
    PRODUCTOS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Productos")')
    NUEVO_PRODUCTO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nuevo Producto")')
    NOMBRE_PRODUCTO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-outlined").instance(1)')
    BUSCADOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Buscar por nombre...")')
    CREAR_PRODUCTO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Crear Producto")')
    LAPIZ = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("")')
    PAPELERA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("")')
    ELIMINAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Eliminar")')
    GUARDAR_CAMBIOS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Guardar Cambios")')

    def __init__(self, driver):
        self.driver = driver
        self.producto_creado = None
        self.producto_modificado = None

    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def acceder_productos(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Productos"))')
        self.click(*self.PRODUCTOS)
        time.sleep(2)

    def crear_producto(self):
        self.producto_creado = f"ProductoQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(*self.NUEVO_PRODUCTO)
        nombre = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NOMBRE_PRODUCTO))
        nombre.click()
        nombre.send_keys(self.producto_creado)
        self.driver.hide_keyboard()
        self.click(*self.CREAR_PRODUCTO)
        time.sleep(3)

    def buscar_producto(self, nombre_producto):
        buscador = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.BUSCADOR))
        buscador.click()
        buscador.clear()
        buscador.send_keys(nombre_producto)
        self.driver.hide_keyboard()
        producto_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{nombre_producto}")')
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(producto_locator))

    def esperar_producto_creado(self):
        self.buscar_producto(self.producto_creado)

    def modificar_producto(self):
        self.click(*self.LAPIZ, timeout=5)
        campo_nombre = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NOMBRE_PRODUCTO))
        valor_actual = campo_nombre.get_attribute("text") or campo_nombre.get_attribute("value")
        if valor_actual != self.producto_creado:
            raise AssertionError(f"Se abrió un producto incorrecto. Esperado '{self.producto_creado}', encontrado '{valor_actual}'")
        self.producto_modificado = f"{valor_actual}_modificado"
        campo_nombre.click()
        campo_nombre.clear()
        campo_nombre.send_keys(self.producto_modificado)
        self.driver.hide_keyboard()
        self.click(*self.GUARDAR_CAMBIOS, timeout=5)
        time.sleep(3)

    def comprobar_producto_modificado(self):
        producto_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.producto_modificado}")')
        try:
            producto = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(producto_locator))
        except TimeoutException:
            raise AssertionError(f"El producto modificado {self.producto_modificado} no aparece en el listado")
        if producto.text != self.producto_modificado:
            raise AssertionError(f"El producto modificado no coincide: esperado '{self.producto_modificado}', encontrado '{producto.text}'")

    def eliminar_producto(self):
        producto_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.producto_modificado}")')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(producto_locator))
        self.click(*self.PAPELERA, timeout=5)
        self.click(*self.ELIMINAR, timeout=5)
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(producto_locator))
        except TimeoutException:
            raise AssertionError(f"El producto {self.producto_modificado} continúa apareciendo después de eliminarlo")