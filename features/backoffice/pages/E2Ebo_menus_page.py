from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MenusPage_bo:

    def __init__(self, driver):
        self.driver = driver

    # =========================
    # MENÚS
    # =========================

    MENUS_MENU = (
        By.XPATH,
        "//a[@href='/menus']"
    )

    NUEVO_MENU_BTN = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[1]/button"
    )

    NOMBRE_MENU_INPUT = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[1]/input"
    )

    IVA_INPUT = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[3]/input"
    )

    PRECIO_INPUT = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[4]/input"
    )

    # =========================
    # PRODUCTO 1
    # =========================

    ADD_PRODUCTO_1 = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[6]/button"
    )

    PRODUCTO_1 = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[1]/div[1]/div/div[1]"
    )

    LISTO_BTN = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[2]/button"
    )

    # =========================
    # PRODUCTO 2
    # =========================

    ADD_PRODUCTO_2 = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[7]/button"
    )

    PRODUCTO_2 = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[1]/div[3]/div/div[1]"
    )

    # =========================
    # PRODUCTO 3
    # =========================

    ADD_PRODUCTO_3 = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[8]/button"
    )

    PRODUCTO_3 = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[1]/div[4]/div/div[1]"
    )

    # =========================
    # CREAR
    # =========================

    CREAR_MENU_BTN = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/div[3]/button[2]"
    )

    # =========================
    # HELPERS
    # =========================

    def click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def fill(self, locator, value, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(str(value))

    def scroll_down(self):

        self.driver.execute_script(
            "window.scrollBy(0,600);"
        )

        time.sleep(1)

    # =========================
    # OPEN
    # =========================

    def open_menus(self):
        self.click(self.MENUS_MENU)

    # =========================
    # CREATE MENU
    # =========================

    def create_menu(self, menu_name):

        self.click(self.NUEVO_MENU_BTN)

        time.sleep(1)

        self.fill(self.NOMBRE_MENU_INPUT, menu_name)
        self.fill(self.IVA_INPUT, "12")
        self.fill(self.PRECIO_INPUT, "15")

        # =====================
        # PRODUCTO 1
        # =====================

        self.click(self.ADD_PRODUCTO_1)
        self.click(self.PRODUCTO_1)
        self.click(self.LISTO_BTN)

        # =====================
        # PRODUCTO 2
        # =====================

        self.click(self.ADD_PRODUCTO_2)
        self.click(self.PRODUCTO_2)
        self.click(self.LISTO_BTN)

        # =====================
        # PRODUCTO 3
        # =====================

        self.scroll_down()

        self.click(self.ADD_PRODUCTO_3)
        self.click(self.PRODUCTO_3)
        self.click(self.LISTO_BTN)

        time.sleep(2)

        self.click(self.CREAR_MENU_BTN)

        # para ver el resultado
        time.sleep(3)