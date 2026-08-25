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

    def comprobar_rol_no_aparece(self):
        rol_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.rol_creado}")')
        def rol_no_visible(driver):
            try:
                roles = driver.find_elements(*rol_locator)
                for rol in roles:
                    try:
                        if rol.is_displayed():
                            return False
                    except StaleElementReferenceException:
                        continue
                return True
            except NoSuchElementException:
                return True
        try:
            WebDriverWait(self.driver, 15).until(rol_no_visible)
        except Exception:
            raise AssertionError(f"El rol {self.rol_creado} sigue existiendo")
        
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

    def eliminar_categoria(self):
        categoria_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.categoria_creada}").instance(0)')
        try:
            categoria = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(categoria_locator))
        except Exception:
            raise Exception(f"No se encontró la categoría {self.categoria_creada} en el listado antes de eliminarla")
        if categoria.text != self.categoria_creada:
            raise Exception(f"La categoría encontrada no corresponde con la categoría recién creada: esperada '{self.categoria_creada}', encontrada '{categoria.text}'")
        papeleras = self.driver.find_elements(*self.PAPELERA)
        if not papeleras:
            raise Exception(f"No se encontraron papeleras para eliminar {self.categoria_creada}")
        papelera_correcta = papeleras[-1]
        papelera_correcta.click()
        time.sleep(1)
        eliminar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ELIMINAR))
        eliminar.click()
        time.sleep(3)

    def comprobar_categoria_no_aparece(self):
        if self.buscador_categorias is None:
            raise Exception("No se encontró el buscador de categorías utilizado durante la búsqueda")
        try:
            self.buscador_categorias.click()
            self.buscador_categorias.clear()
            self.driver.hide_keyboard()
        except StaleElementReferenceException:
            buscador = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            if buscador:
                buscador[-1].click()
                buscador[-1].clear()
                self.driver.hide_keyboard()
        time.sleep(1)
        categoria_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.categoria_creada}")')
        def categoria_no_visible(driver):
            try:
                categorias = driver.find_elements(*categoria_locator)
                for categoria in categorias:
                    try:
                        if categoria.is_displayed():
                            return False
                    except StaleElementReferenceException:
                        continue
                return True
            except NoSuchElementException:
                return True
        try:
            WebDriverWait(self.driver, 15).until(categoria_no_visible)
        except Exception:
            raise AssertionError(f"La categoría {self.categoria_creada} sigue existiendo")