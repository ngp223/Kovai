from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


class MenusPage:

    MENU_SECTION = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc=", Menús"]/android.widget.TextView[@text="Menús"]'
    )

    NUEVO_MENU = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Nuevo Menú"]'
    )

    NOMBRE_MENU = (
        AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="text-input-outlined"])[1]'
    )

    LISTA_INPUTS = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="text-input-outlined"]'
    )

    PRIMER_ANADIR_PRODUCTO = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Añadir Producto"])[1]'
    )

    SEGUNDO_ANADIR_PRODUCTO = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Añadir Producto"])[2]'
    )

    TERCER_ANADIR_PRODUCTO = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Añadir Producto"])[3]'
    )

    ARROZ = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="Arroz con Bogavante, Arroces de Autor, "]/android.widget.TextView[@text=""]'
    )

    JAMON = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="Jamón 5 Jotas (Ración), Entrantes Ibéricos, "]/android.widget.TextView[@text=""]'
    )

    GIN_TONIC = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="Gin Tonic Seagrams, Coctelería Premium, "]/android.widget.TextView[@text=""]'
    )

    LISTO = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Listo"]'
    )

    CREAR_MENU = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Crear Menú"]'
    )

    def __init__(self, driver):
        self.driver = driver

    # =========================
    # CLICK
    # =========================
    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(by, locator)
        )
        element.click()

    # =========================
    # FILL
    # =========================
    def fill(self, by, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(by, locator)
        )
        element.click()
        element.send_keys(str(value))

    # =========================
    # INPUTS LISTA
    # =========================
    def get_inputs(self):
        return self.driver.find_elements(*self.LISTA_INPUTS)

    def fill_iva_y_precio(self):

        inputs = self.get_inputs()

        iva = inputs[2]
        precio = inputs[3]

        iva.click()
        precio.clear()
        iva.send_keys("12")

        precio.click()
        precio.send_keys("15")

        self.driver.press_keycode(4)  # BACK

    # =========================
    # SCROLL BASE
    # =========================
    def scroll_down(self):

        size = self.driver.get_window_size()

        self.driver.swipe(
            int(size["width"] * 0.5),
            int(size["height"] * 0.70),
            int(size["width"] * 0.5),
            int(size["height"] * 0.30),
            800
        )

    # =========================
    # SCROLL INTELIGENTE (NUEVO)
    # =========================
    def scroll_until_visible(self, locator, max_swipes=6):

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return element
            except:
                pass

            self.scroll_down()

        raise Exception(f"No se encontró el elemento: {locator}")

    # =========================
    # OPEN MENUS
    # =========================
    def open_menus(self):

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().text("Menús"))'
        )

        self.click(*self.MENU_SECTION)

    # =========================
    # CREATE MENU
    # =========================
    def create_menu(self):

        self.driver.implicitly_wait(1)

        self.click(*self.NUEVO_MENU)

        self.fill(*self.NOMBRE_MENU, "menu prueba QA")

        self.fill_iva_y_precio()

        # =====================
        # PRIMER PRODUCTO
        # =====================
        self.click(*self.PRIMER_ANADIR_PRODUCTO)
        self.click(*self.ARROZ)
        self.click(*self.LISTO)

        # =====================
        # SEGUNDO PRODUCTO (SCROLL INTELIGENTE)
        # =====================
        self.scroll_until_visible(self.SEGUNDO_ANADIR_PRODUCTO)
        self.click(*self.SEGUNDO_ANADIR_PRODUCTO)
        self.click(*self.JAMON)
        self.click(*self.LISTO)

        # =====================
        # TERCER PRODUCTO (SCROLL INTELIGENTE)
        # =====================
        self.scroll_until_visible(self.TERCER_ANADIR_PRODUCTO)
        self.click(*self.TERCER_ANADIR_PRODUCTO)
        self.click(*self.GIN_TONIC)
        self.click(*self.LISTO)

        # =====================
        # FINAL
        # =====================
        self.click(*self.CREAR_MENU)