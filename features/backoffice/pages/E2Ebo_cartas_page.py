from selenium.webdriver.common.by import By
from features.backoffice.pages.base_page import BasePage
from features.backoffice.pages.base_list_mixin import BaseListMixin
from features.backoffice.pages.base_crud_mixin import BaseCRUDMixin

class CartasPage_bo(BasePage, BaseListMixin, BaseCRUDMixin):

    CARTAS_MENU = (By.XPATH, "//a[contains(.,'Cartas')]")
    ADD_BTN = (By.XPATH, "//button[contains(.,'Añadir carta')]")
    NAME = (By.XPATH, "//input[contains(@placeholder,'Carta')]")
    RADIO = (By.XPATH, "//input[@type='radio']")
    CREATE = (By.XPATH, "//button[contains(.,'Crear')]")
    CONTINUE = (By.XPATH, "//button[normalize-space()='Continuar']")

    def open(self):
        self.click(self.CARTAS_MENU)

    def open_cartas(self):
        self.open()

    def create(self, name):
        self.click(self.ADD_BTN)
        self.fill(self.NAME, name)
        self.click(self.RADIO)
        self.click(self.CREATE)
        try:
            self.click(self.CONTINUE, timeout=5)
        except:
            pass

    def delete_carta(self, name):
        self.delete_by_name(name)