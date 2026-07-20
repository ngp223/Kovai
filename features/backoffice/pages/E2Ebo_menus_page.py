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

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(3)

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.visibility_of_element_located(self.CREATE)
        )

        wait.until(
            lambda d: d.find_element(*self.CREATE).is_enabled()
        )

        self.click(self.CREATE)

        time.sleep(3)

    def delete_menu(self, name):
        self.delete_by_name(name)