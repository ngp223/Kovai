from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

class MenusPage:

    MENU_SECTION = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=", Menús"]/android.widget.TextView[@text="Menús"]')
    NUEVO_MENU = (AppiumBy.XPATH, '//android.widget.TextView[@text="Nuevo Menú"]')
    NOMBRE_MENU = (AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="text-input-outlined"])[1]')
    LISTA_INPUTS = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="text-input-outlined"]')
    PRIMER_ANADIR_PRODUCTO = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Añadir Producto"])[1]')
    SEGUNDO_ANADIR_PRODUCTO = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Añadir Producto"])[2]')
    TERCER_ANADIR_PRODUCTO = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Añadir Producto"])[3]')
    ARROZ = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Arroz con Bogavante, Arroces de Autor, "]/android.widget.TextView[@text=""]')
    JAMON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Jamón 5 Jotas (Ración), Entrantes Ibéricos, "]/android.widget.TextView[@text=""]')
    GIN_TONIC = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Gin Tonic Seagrams, Coctelería Premium, "]/android.widget.TextView[@text=""]')
    LISTO = (AppiumBy.XPATH, '//android.widget.TextView[@text="Listo"]')
    CREAR_MENU = (AppiumBy.XPATH, '//android.widget.TextView[@text="Crear Menú"]')
    CONFIRMAR_BORRADO = (AppiumBy.ID, 'android:id/button1')

    def __init__(self, driver):
        self.driver = driver
        self.nombre_menu_creado = None

    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(by, locator))
        element.click()

    def fill(self, by, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(by, locator))
        element.click()
        element.send_keys(str(value))

    def get_inputs(self):
        return self.driver.find_elements(*self.LISTA_INPUTS)

    def fill_iva_y_precio(self):
        inputs = self.get_inputs()
        iva = inputs[2]
        precio = inputs[3]
        iva.click()
        iva.send_keys("12")
        precio.click()
        precio.send_keys("15")
        self.driver.press_keycode(4)

    def scroll_down(self):
        size = self.driver.get_window_size()
        self.driver.swipe(int(size["width"] * 0.5), int(size["height"] * 0.7), int(size["width"] * 0.5), int(size["height"] * 0.3), 800)

    def scroll_until_visible(self, locator, max_swipes=8):
        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return element
            except:
                pass
            self.scroll_down()
        raise Exception(f"No encontrado {locator}")

    def open_menus(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Menús"))')
        self.click(*self.MENU_SECTION)

    def create_menu(self):
        self.click(*self.NUEVO_MENU)
        self.nombre_menu_creado = f"menu prueba QA {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.fill(*self.NOMBRE_MENU, self.nombre_menu_creado)
        self.fill_iva_y_precio()
        self.click(*self.PRIMER_ANADIR_PRODUCTO)
        self.click(*self.ARROZ)
        self.click(*self.LISTO)
        self.scroll_until_visible(self.SEGUNDO_ANADIR_PRODUCTO)
        self.click(*self.SEGUNDO_ANADIR_PRODUCTO)
        self.click(*self.JAMON)
        self.click(*self.LISTO)
        self.scroll_until_visible(self.TERCER_ANADIR_PRODUCTO)
        self.click(*self.TERCER_ANADIR_PRODUCTO)
        self.click(*self.GIN_TONIC)
        self.click(*self.LISTO)
        self.click(*self.CREAR_MENU)

    def get_menu_locator(self):
        return (AppiumBy.XPATH, f'//android.widget.TextView[@text="{self.nombre_menu_creado}"]')

    def menu_exists(self):
        try:
            element = self.driver.find_element(*self.get_menu_locator())
            return element.is_displayed()
        except:
            return False

    def delete_menu(self):
        self.scroll_until_visible(self.get_menu_locator())
        papelera = self.driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{self.nombre_menu_creado}"]/ancestor::android.view.ViewGroup[1]//*[@content-desc=""]')
        papelera.click()
        self.click(*self.CONFIRMAR_BORRADO)
