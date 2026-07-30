from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.backoffice.pages.base_page import BasePage
from features.backoffice.pages.base_list_mixin import BaseListMixin
from features.backoffice.pages.base_crud_mixin import BaseCRUDMixin
import time

class MenusPage_bo(BasePage, BaseListMixin, BaseCRUDMixin):
    MENU = (By.XPATH, "//a[@href='/menus']")
    CREATE_FIRST_MENU = (By.XPATH, "//button[contains(.,'Crear Primer Menú')]")
    NEW_MENU = (By.XPATH, "//button[contains(.,'Nuevo Menú')]")
    NAME = (By.XPATH, "//input[@placeholder='Menú del día']")
    CREATE = (By.XPATH, "//button[contains(.,'Crear Menú')]")
    EDIT = (By.XPATH, ".//button[@title='Editar']")
    ADD_FIRST = (By.XPATH, "//input[@value='Primero']/ancestor::div[contains(@style,'border: 1px solid')]//button[contains(text(),'+ Añadir Producto')]")
    ADD_SECOND = (By.XPATH, "//input[@value='Segundo']/ancestor::div[contains(@style,'border: 1px solid')]//button[contains(text(),'+ Añadir Producto')]")
    ADD_DESSERT = (By.XPATH, "//input[@value='Postre']/ancestor::div[contains(@style,'border: 1px solid')]//button[contains(text(),'+ Añadir Producto')]")
    READY = (By.XPATH, "//button[contains(text(),'Listo')]")
    SAVE_CHANGES = (By.XPATH, "//button[contains(text(),'Guardar Cambios')]")
    ARROZ = (By.XPATH, "//div[contains(@style,'font-weight: 600') and contains(text(),'Arroz con Bogavante')]")
    PAELLA = (By.XPATH, "//div[contains(@style,'font-weight: 600') and contains(text(),'Paella de Marisco')]")
    NATILLAS = (By.XPATH, "//div[contains(@style,'font-weight: 600') and contains(text(),'Natillas')]")

    def open(self):
        self.click(self.MENU)

    def open_menus(self):
        self.open()

    def create(self, name):
        if self.driver.find_elements(*self.CREATE_FIRST_MENU):
            self.click(self.CREATE_FIRST_MENU)
        else:
            self.click(self.NEW_MENU)
        self.fill(self.NAME, name)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.CREATE))
        wait.until(lambda d: d.find_element(*self.CREATE).is_enabled())
        self.click(self.CREATE)
        time.sleep(3)

    def modify_menu(self, name):
        row = (By.XPATH, f"//tbody//tr[.//strong[contains(text(),'{name}')]]")
        menu_row = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(row))
        edit_button = menu_row.find_element(*self.EDIT)
        self.driver.execute_script("arguments[0].click();", edit_button)
        time.sleep(3)
        self.add_product(self.ADD_FIRST, self.ARROZ)
        self.add_product(self.ADD_SECOND, self.PAELLA)
        self.add_product(self.ADD_DESSERT, self.NATILLAS)
        self.click(self.SAVE_CHANGES)
        time.sleep(4)

    def add_product(self, add_button, product):
        self.click(add_button)
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(product))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(1)
        self.click(self.READY)
        time.sleep(3)

    def check_products(self, name, expected):
        row = (By.XPATH, f"//tbody//tr[.//strong[contains(text(),'{name}')]]")
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(row))
        return f"{expected} productos" in element.text

    def delete_menu(self, name):
        self.delete_by_name(name)
