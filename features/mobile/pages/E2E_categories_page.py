from datetime import datetime
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException
)


class CategoriesPage:

    CATEGORIAS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description(", Categorías")'
    )

    ANADIR_CATEGORIA = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Añadir Categoría")'
    )

    NOMBRE_CATEGORIA = (
        AppiumBy.XPATH,
        '(//android.view.ViewGroup[@resource-id="modal-surface"]'
        '/android.view.ViewGroup[2]'
        '/android.widget.EditText[@resource-id="text-input-outlined"])[1]'
    )

    CREAR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description(", Crear")'
    )

    PAPELERA = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("")'
    )

    ELIMINAR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description(", Eliminar")'
    )

    def __init__(self, driver):
        self.driver = driver
        self.categoria_creada = None

    def click(self, by, locator, timeout=15):
        element = WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.element_to_be_clickable((by, locator))
        )

        element.click()
        return element

    def acceder_categorias(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().description(", Categorías"))'
        )

        self.click(*self.CATEGORIAS)

        time.sleep(3)

        self.refrescar_categorias()

    def refrescar_categorias(self):
        size = self.driver.get_window_size()

        x = size["width"] // 2

        self.driver.swipe(
            x,
            int(size["height"] * 0.25),
            x,
            int(size["height"] * 0.75),
            800
        )

        time.sleep(5)

    def crear_categoria(self):
        self.categoria_creada = (
            f"categoriaqa"
            f"{datetime.now().strftime('%d%m%Y%H%M%S')}"
        )

        self.click(*self.ANADIR_CATEGORIA)

        nombre = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.visibility_of_element_located(self.NOMBRE_CATEGORIA)
        )

        nombre.click()
        nombre.send_keys(self.categoria_creada)

        self.driver.hide_keyboard()

        self.click(*self.CREAR)

        WebDriverWait(
            self.driver,
            15
        ).until(
            EC.invisibility_of_element_located(self.NOMBRE_CATEGORIA)
        )

        time.sleep(5)

        self.refrescar_categorias()

    def buscar_categoria(self):
        categoria_locator = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@text="{self.categoria_creada}"]'
        )

        size = self.driver.get_window_size()

        x = size["width"] // 2

        for _ in range(15):
            try:
                categoria = self.driver.find_element(
                    *categoria_locator
                )

                if categoria.is_displayed():
                    return categoria

            except (
                NoSuchElementException,
                StaleElementReferenceException
            ):
                pass

            self.driver.swipe(
                x,
                int(size["height"] * 0.75),
                x,
                int(size["height"] * 0.30),
                500
            )

            time.sleep(1)

        return None

    def esperar_categoria_creada(self):
        categoria = self.buscar_categoria()

        if categoria is None:
            raise Exception(
                f"No se encontró la categoría "
                f"{self.categoria_creada}"
            )

    def eliminar_categoria(self):
        categoria = self.buscar_categoria()

        if categoria is None:
            raise Exception(
                f"No se encontró la categoría "
                f"{self.categoria_creada} para eliminar"
            )

        categoria_pos = categoria.location

        papeleras = self.driver.find_elements(
            *self.PAPELERA
        )

        if not papeleras:
            raise Exception(
                f"No se encontraron papeleras para eliminar "
                f"{self.categoria_creada}"
            )

        papelera_correcta = None
        distancia_minima = float("inf")

        for papelera in papeleras:
            try:
                papelera_pos = papelera.location

                distancia = abs(
                    papelera_pos["y"] - categoria_pos["y"]
                )

                if distancia < distancia_minima:
                    distancia_minima = distancia
                    papelera_correcta = papelera

            except StaleElementReferenceException:
                continue

        if papelera_correcta is None:
            raise Exception(
                f"No se encontró la papelera de "
                f"{self.categoria_creada}"
            )

        # Pulsamos la papelera de la categoría
        papelera_correcta.click()

        # Esperamos a que aparezca el botón de confirmación
        eliminar = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(self.ELIMINAR)
        )

        # Confirmamos la eliminación
        eliminar.click()

    def comprobar_categoria_no_aparece(self):
        categoria_locator = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@text="{self.categoria_creada}"]'
        )

        try:
            WebDriverWait(
                self.driver,
                10
            ).until(
                lambda driver:
                len(
                    driver.find_elements(
                        *categoria_locator
                    )
                ) == 0
            )

        except Exception:
            raise AssertionError(
                f"La categoría "
                f"{self.categoria_creada} "
                f"sigue existiendo"
            )