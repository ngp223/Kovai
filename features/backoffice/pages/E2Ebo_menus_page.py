from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from features.backoffice.pages.base_page import BasePage


class MenusPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # =========================
    # LOCATORS
    # =========================
    MENUS_MENU = (By.XPATH, "//a[@href='/menus']")
    NUEVO_MENU_BTN = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[1]/button")

    NOMBRE_MENU_INPUT = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[1]/input")
    IVA_INPUT = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[3]/input")
    PRECIO_INPUT = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[4]/input")

    ADD_PRODUCTO_1 = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[6]/button")
    PRODUCTO_1 = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[1]/div[1]/div/div[1]")

    ADD_PRODUCTO_2 = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[7]/button")
    PRODUCTO_2 = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[1]/div[3]/div/div[1]")

    ADD_PRODUCTO_3 = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[3]/div/div[2]/div[8]/button")
    PRODUCTO_3 = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[1]/div[4]/div/div[1]")

    LISTO_BTN = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[4]/div/div[2]/div[2]/button")
    CREAR_MENU_BTN = (By.XPATH, "//*[@id='root']/div/div/div/main/div/div[3]/div/div[3]/button[2]")

    CONFIRM_DELETE_BTN = (
        By.XPATH,
        "//button[contains(@class,'_confirmButton') and contains(.,'Confirmar')]"
    )

    # =========================
    # NAV
    # =========================
    def open_menus(self):
        self.click(self.MENUS_MENU)

    # =========================
    # CREATE MENU
    # =========================
    def create_menu(self, menu_name):

        self.click(self.NUEVO_MENU_BTN)

        self.fill(self.NOMBRE_MENU_INPUT, menu_name)
        self.fill(self.IVA_INPUT, "12")
        self.fill(self.PRECIO_INPUT, "15")

        self.click(self.ADD_PRODUCTO_1)
        self.click(self.PRODUCTO_1)
        self.click(self.LISTO_BTN)

        self.scroll_down(300)

        self.click(self.ADD_PRODUCTO_2)
        self.click(self.PRODUCTO_2)
        self.click(self.LISTO_BTN)

        self.scroll_down(500)

        self.click(self.ADD_PRODUCTO_3)
        self.click(self.PRODUCTO_3)
        self.click(self.LISTO_BTN)

        self.scroll_down(600)

        self.click(self.CREAR_MENU_BTN)

    # =========================
    # DELETE MENU (STABLE SUITE VERSION)
    # =========================
    def delete_menu(self, menu_name):

        # fila REAL del menú (scoped por botón delete)
        menu_row_locator = (
            By.XPATH,
            f"//*[contains(.,'{menu_name}')]/ancestor::div[.//button[@title='Eliminar']][1]"
        )

        row = self.wait_visible(menu_row_locator)

        # botón delete dentro de la fila correcta
        delete_btn = row.find_element(By.XPATH, ".//button[@title='Eliminar']")

        self._safe_scroll_into_view(delete_btn)
        delete_btn.click()

        # confirmar borrado
        self.click(self.CONFIRM_DELETE_BTN)

        # esperar desaparición REAL del DOM
        WebDriverWait(self.driver, 10).until(
            lambda d: len(
                d.find_elements(By.XPATH, f"//*[contains(.,'{menu_name}')]")
            ) == 0
        )