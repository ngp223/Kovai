from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.backoffice.pages.base_page import BasePage
import time


class BackupsPage_bo(BasePage):

    BACKUPS_MENU=(By.XPATH,"//a[@href='/backups']")
    CREATE_BACKUP_BTN=(By.XPATH,"//button[contains(normalize-space(),'Crear respaldo completo')]")
    CONTINUE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Continuar')]")
    ROWS=(By.XPATH,"//tbody/tr")
    DOWNLOAD_BTN=(By.XPATH,".//button[@title='Descargar']")
    DELETE_BTN=(By.XPATH,".//button")
    CONFIRM_DELETE_TITLE=(By.XPATH,"//h2[contains(normalize-space(),'Eliminar Copia de Seguridad')]")
    CONFIRM_DELETE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Confirmar Eliminación')]")

    def __init__(self,driver):
        super().__init__(driver)

    def open_backups(self):
        self.wait_visible(self.BACKUPS_MENU)
        self.click(self.BACKUPS_MENU)

    def create_backup(self):
        before=len(self.driver.find_elements(*self.ROWS))
        self.click(self.CREATE_BACKUP_BTN)
        try:
            btn=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONTINUE_BTN))
            self.driver.execute_script("arguments[0].click();",btn)
        except:
            pass
        WebDriverWait(self.driver,120).until(EC.invisibility_of_element_located(self.CONTINUE_BTN))
        WebDriverWait(self.driver,120).until(lambda d: len(d.find_elements(*self.ROWS))>before)

    def get_last_backup_text(self):
        rows=self.driver.find_elements(*self.ROWS)
        return rows[-1].text.split("\n")[0]

    def wait_backup_in_list(self,backup_text,timeout=20):
        locator=(By.XPATH,f"//tr[contains(.,\"{backup_text}\")]")
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def wait_backup_gone(self,backup_text,timeout=20):
        locator=(By.XPATH,f"//tr[contains(.,\"{backup_text}\")]")
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))

    def get_backup_row(self,backup_text):
        row_locator=(By.XPATH,f"//tr[contains(.,\"{backup_text}\")]")
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(row_locator))

    def download_backup(self,backup_text):
        row=self.get_backup_row(backup_text)
        download_btn=WebDriverWait(row,10).until(EC.element_to_be_clickable(self.DOWNLOAD_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",download_btn)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();",download_btn)

    def delete_backup(self,backup_text):
        row=self.get_backup_row(backup_text)
        delete_btn=row.find_elements(*self.DELETE_BTN)[-1]
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_TITLE))
        confirm_btn=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)