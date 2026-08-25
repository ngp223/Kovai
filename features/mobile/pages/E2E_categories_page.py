from datetime import datetime
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class CategoriesPage:
    CATEGORIAS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Categorías")')
    ANADIR_CATEGORIA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Añadir Categoría")')
    NOMBRE_CATEGORIA = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="modal-surface"]/android.view.ViewGroup[2]/android.widget.EditText[@resource-id="text-input-outlined"])[1]')
    ORDEN_CATEGORIA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-outlined").instance(4)')
    CREAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Crear")')
    GUARDAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Guardar")')
    EDITAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("")')
    PAPELERA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
    ELIMINAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(", Eliminar")')
    BUSCAR_CATEGORIAS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Buscar categorías...")')
    NOMBRE_ROL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ej: COCINA_CALIENTE")')
    CREAR_ROL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Crear rol")')

    def __init__(self, driver):
        self.driver = driver
        self.categoria_creada = None
        self.rol_creado = None
        self.buscador_categorias = None

    def click(self, by, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def acceder_categorias(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description(", Categorías"))')
        self.click(*self.CATEGORIAS)
        time.sleep(3)

    def crear_rol(self):
        self.rol_creado = f"ROLQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        nombre = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.NOMBRE_ROL))
        nombre.click()
        nombre.send_keys(self.rol_creado)
        self.driver.hide_keyboard()
        self.click(*self.CREAR_ROL)
        time.sleep(5)

    def buscar_rol(self):
        rol_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.rol_creado}")')
        size = self.driver.get_window_size()
        x = size["width"] // 2
        for _ in range(15):
            try:
                rol = self.driver.find_element(*rol_locator)
                if rol.is_displayed():
                    print(f"ROL ENCONTRADO: {rol.text}")
                    rol_y = rol.location["y"]
                    papeleras = self.driver.find_elements(*self.PAPELERA)
                    if papeleras:
                        papelera = min(papeleras, key=lambda p: abs(p.location["y"] - rol_y))
                        print("PAPELERA ENCONTRADA")
                        papelera.click()
                        time.sleep(5)
                        return rol
            except (NoSuchElementException, StaleElementReferenceException):
                pass
            self.driver.swipe(x, int(size["height"] * 0.75), x, int(size["height"] * 0.30), 500)
            time.sleep(1)
        print(f"ROL NO ENCONTRADO: {self.rol_creado}")
        return None

    def eliminar_rol(self):
        rol = self.buscar_rol()
        if rol is None:
            raise Exception(f"No se encontró el rol {self.rol_creado} para eliminar")

    def crear_categoria(self):
        self.categoria_creada = f"categoriaqa{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(*self.ANADIR_CATEGORIA)
        nombre = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.NOMBRE_CATEGORIA))
        nombre.send_keys(self.categoria_creada)
        orden = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.ORDEN_CATEGORIA))
        orden.click()
        self.driver.hide_keyboard()
        orden.send_keys("0")
        time.sleep(1)
        self.click(*self.CREAR)
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(self.NOMBRE_CATEGORIA))
        time.sleep(5)

    def buscar_categoria(self):
        self.buscador_categorias = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.BUSCAR_CATEGORIAS))
        self.buscador_categorias.click()
        self.buscador_categorias.clear()
        self.buscador_categorias.send_keys(self.categoria_creada)
        self.driver.hide_keyboard()
        time.sleep(1)
        categoria_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.categoria_creada}")')
        try:
            categoria = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(categoria_locator))
            if categoria.is_displayed():
                return categoria
        except (NoSuchElementException, StaleElementReferenceException):
            return None
        return None

    def esperar_categoria_creada(self):
        try:
            categoria = self.buscar_categoria()
            if categoria is None:
                raise Exception(f"No se encontró la categoría {self.categoria_creada}")
        except Exception:
            raise AssertionError(f"No se encontró la categoría {self.categoria_creada}")

    def modificar_categoria(self):
        categoria_original = self.categoria_creada
        categoria_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{categoria_original}")')
        categoria = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(categoria_locator))
        papeleras = self.driver.find_elements(*self.PAPELERA)
        papelera_correcta = papeleras[-1]
        papelera_y = papelera_correcta.location["y"]
        editar_buttons = self.driver.find_elements(*self.EDITAR)
        editar_correcto = min(editar_buttons, key=lambda e: abs(e.location["y"] - papelera_y))
        editar_correcto.click()
        time.sleep(2)
        campo_nombre_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("android.widget.EditText").resourceId("text-input-outlined").text("{categoria_original}")')
        campo_nombre = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(campo_nombre_locator))
        texto_nuevo = f"_modificado_{datetime.now().strftime('%d%m%Y%H%M%S')}"
        nuevo_nombre = categoria_original + texto_nuevo
        self.categoria_creada = nuevo_nombre
        campo_nombre.click()
        time.sleep(1)
        campo_nombre.send_keys(self.categoria_creada)
        time.sleep(1)
        guardar = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.GUARDAR))
        guardar.click()
        time.sleep(3)
        buscador = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.BUSCAR_CATEGORIAS))
        buscador.click()
        time.sleep(1)
        buscador.clear()
        time.sleep(1)
        buscador.send_keys(self.categoria_creada)
        time.sleep(2)
        self.driver.hide_keyboard()
        time.sleep(2)

    def comprobar_categoria_modificada(self):
        categoria_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.categoria_creada}")')
        try:
            categoria = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(categoria_locator))
        except Exception:
            raise AssertionError(f"La categoría modificada {self.categoria_creada} no aparece en el listado")
        if categoria.text != self.categoria_creada:
            raise AssertionError(f"La categoría modificada no coincide: esperada '{self.categoria_creada}', encontrada '{categoria.text}'")

    def eliminar_categoria(self):
        categoria_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.categoria_creada}")')
        try:
            categoria = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(categoria_locator))
        except Exception:
            raise Exception(f"No se encontró la categoría {self.categoria_creada} en el listado antes de eliminarla")
        papeleras = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*self.PAPELERA))
        papelera_correcta = papeleras[-1]
        papelera_correcta.click()
        time.sleep(2)
        eliminar = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.ELIMINAR))
        eliminar.click()
        time.sleep(5)

