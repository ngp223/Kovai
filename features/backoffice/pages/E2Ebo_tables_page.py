from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from features.backoffice.pages.base_page import BasePage
import time


class TablesPage_bo(BasePage):

    TABLES_MENU=(By.XPATH,"//a[@href='/tables']")
    RESTAURANT_SELECT=(By.TAG_NAME,"select")
    ADD_FIRST_TABLE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Añadir primera mesa') or contains(normalize-space(),'Anadir primera mesa')]")
    DELETE_TABLE_BTN=(By.XPATH,"//button[@title='Eliminar mesa']")

    def __init__(self,driver):
        super().__init__(driver)

    def open_tables(self):
        self.wait_visible(self.TABLES_MENU)
        self.click(self.TABLES_MENU)

    def select_restaurant(self):
        select=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.RESTAURANT_SELECT)
        )
        Select(select).select_by_visible_text("Tamus Rooftop Sevilla")

    def create_table(self):
        btn=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.ADD_FIRST_TABLE_BTN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            btn
        )

        time.sleep(5)

    def wait_table_created(self,timeout=10):
        WebDriverWait(self.driver,timeout).until(
            EC.visibility_of_element_located(self.DELETE_TABLE_BTN)
        )

    def delete_table(self):
        btn=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.DELETE_TABLE_BTN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            btn
        )

        time.sleep(2)

    def wait_table_deleted(self,timeout=10):
        WebDriverWait(self.driver,timeout).until(
            EC.invisibility_of_element_located(self.DELETE_TABLE_BTN)
        )