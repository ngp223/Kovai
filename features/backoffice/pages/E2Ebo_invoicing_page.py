from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from features.backoffice.pages.base_page import BasePage
import time


class InvoicingSeriesPage(BasePage):

    INVOICING_MENU = (By.XPATH,"//a[@href='/invoicing']")
    SERIES_TAB = (By.XPATH,"//button[contains(normalize-space(),'Series')]")
    NEW_SERIES_BTN = (By.XPATH,"//button[contains(normalize-space(),'+ Nueva Serie')]")
    SERIE_NAME_INPUT = (By.XPATH,"//input[@placeholder='Ej: FS']")
    SERIE_PREFIX_INPUT = (By.XPATH,"//input[@placeholder='Ej: FS-2026-']")
    CREATE_BTN = (By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")
    DELETE_BTN = (By.XPATH,".//button[@title='Eliminar']")
    CONFIRM_DELETE_BTN = (By.XPATH,"//button[contains(@class,'_confirmButton') and contains(normalize-space(),'Eliminar')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open_invoicing(self):
        self.click(self.INVOICING_MENU)

    def open_series(self):
        self.click(self.SERIES_TAB)

    def create_series(self):
        now = datetime.now()
        name = f"QA{now.strftime('%H%M%S')}"
        prefix = f"QA{now.strftime('%d%m%y%H%M%S')}"
        self.click(self.NEW_SERIES_BTN)
        self.fill(self.SERIE_NAME_INPUT,name)
        self.fill(self.SERIE_PREFIX_INPUT,prefix)
        self.click(self.CREATE_BTN)
        return name

    def wait_series_in_list(self,name,timeout=10):
        locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def wait_series_gone(self,name,timeout=10):
        locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))

    def delete_series(self,name):
        self.wait_series_in_list(name)
        row_locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")
        row = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(row_locator))
        delete_btn = row.find_element(*self.DELETE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_btn = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)