from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
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
    DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Descripción opcional de la carta...']")
    SAVE = (By.XPATH, "//button[contains(.,'Guardar')]")
    RESTAURANT = (By.TAG_NAME, "select")
    ASSIGN_MASTER = (By.XPATH, "//button[contains(.,'Asignar una carta maestra')]")
    CLOSE = (By.XPATH, "//button[normalize-space()='Cerrar']")

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
            self.click(self.CONTINUE, timeout=2)
        except Exception:
            pass

    def edit_carta(self, name):
        edit_btn = (By.XPATH, f"//tr[contains(.,'{name}')]//button[@title='Editar carta maestra']")
        self.click(edit_btn)

    def modify_description(self, text):
        self.fill(self.DESCRIPTION, text)

    def save_changes(self):
        self.click(self.SAVE)

    def confirm_changes(self):
        try:
            self.click(self.CONTINUE, timeout=2)
        except Exception:
            pass

    def change_restaurant(self, restaurant):
        select = Select(self.driver.find_element(*self.RESTAURANT))
        select.select_by_visible_text(restaurant)
        time.sleep(2)

    def assign_master_card(self, name):
        self.click(self.ASSIGN_MASTER)
        assign_btn = (By.XPATH, f"//div[contains(.,'{name}')]/following-sibling::button[contains(.,'Asignar')]")
        self.click(assign_btn)
        time.sleep(1)

    def verify_assigned(self, name):
        button = (By.XPATH, f"//div[contains(.,'{name}')]/following-sibling::button[contains(.,'Quitar')]")
        self.wait_visible(button)

    def close_assign_modal(self):
        self.click(self.CLOSE)

    def verify_default_card(self, name):
        default_btn = (By.XPATH, f"//tr[contains(.,'{name}')]//button[contains(.,'Marcar por defecto')]")
        self.wait_visible(default_btn)
        time.sleep(2)

    def delete_carta(self, name):
        self.delete_by_name(name)