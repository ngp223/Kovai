from selenium.webdriver.common.by import By
from features.backoffice.pages.base_page import BasePage
from features.backoffice.pages.base_list_mixin import BaseListMixin
from features.backoffice.pages.base_crud_mixin import BaseCRUDMixin

class MenusPage_bo(BasePage, BaseListMixin, BaseCRUDMixin):

    MENU = (By.XPATH, "//a[@href='/menus']")
    NEW = (By.XPATH, "//button[contains(.,'Nuevo')]")
    NAME = (By.XPATH, "//input")
    CREATE = (By.XPATH, "//button[contains(.,'Crear')]")
    CONTINUE = (By.XPATH, "//button[normalize-space()='Continuar']")

    def open(self):
        self.click(self.MENU)

    def open_menus(self):
        self.open()

    def create(self, name):
        self.click(self.NEW)
        self.fill(self.NAME, name)
        self.click(self.CREATE)

    def delete_menu(self, name):
        self.delete_by_name(name)