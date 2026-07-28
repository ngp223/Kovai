from datetime import datetime
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.backoffice.pages.base_page import BasePage

class TablesPage_bo(BasePage):

    TABLES_MENU=(By.XPATH,"//a[@href='/tables']")
    RESTAURANT_SELECT=(By.TAG_NAME,"select")
    NEW_RATE_BTN=(By.XPATH,"//button[contains(., '+ Nueva Tarifa')]")
    RATE_NAME_INPUT=(By.XPATH,"//input[@placeholder='Ej: Tarifa Terraza 10%']")
    CREATE_RATE_BTN=(By.XPATH,"//button[@type='submit' and contains(.,'Crear')]")
    NEW_ZONE_BTN=(By.XPATH,"//button[contains(.,'+ Nueva Zona')]")
    ZONE_NAME_INPUT=(By.XPATH,"//input[@type='text']")
    CREATE_ZONE_BTN=(By.XPATH,"//button[@type='submit' and contains(.,'Crear')]")
    ZONE_SELECT=(By.XPATH,"//select[contains(@class,'_filterSelect_')]")
    FIRST_TABLE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Añadir primera mesa') or contains(normalize-space(),'Anadir primera mesa')]")
    RECTANGULAR_BTN=(By.XPATH,"//button[contains(@title,'rectangular') or contains(.,'Rectangular')]")
    TABLE=(By.XPATH,"//div[contains(@class,'_table_')][.//button[@title='Eliminar mesa']]")
    DELETE_BTN=(By.XPATH,".//button[@title='Eliminar mesa']")
    CONTINUE_BTN=(By.XPATH,"//button[contains(.,'Continuar')]")
    LIST_VIEW_BTN=(By.XPATH,"//button[contains(.,'Lista')]")
    ASSIGN_MENU_BTN=(By.XPATH,"//button[contains(.,'Asignar Cartas')]")
    MENU_SELECT=(By.XPATH,"//select[option[contains(.,'QA(NOBORRAR)')]]")
    SELECT_ALL_BTN=(By.XPATH,"//button[contains(.,'Seleccionar Todas')]")
    ASSIGN_TO_TABLE_BTN=(By.XPATH,"//button[@type='submit' and contains(.,'Asignar a')]")
    MAP_VIEW_BTN=(By.XPATH,"//button[contains(.,'Mapa')]")
    QR_BTN=(By.XPATH,".//button[@title='Ver QR']")
    CLOSE_QR_BTN=(By.XPATH,"//button[@class='close-btn']")
    DOWNLOAD_PNG_BTN = (By.XPATH, "//button[contains(normalize-space(),'Descargar PNG')]")
    PRINT_BTN = (By.XPATH, "//button[contains(normalize-space(),'Imprimir')]")
    CANCEL_PRINT_BTN = (By.CSS_SELECTOR, "cr-button.cancel-button")

    def __init__(self, driver, download_dir=None):
        super().__init__(driver)
        self.current_table = None
        self.zone_name = None
        self.rate_name = None
        self.table_zone = None
        self.download_dir = download_dir
        self.table_zone = None
        self.qr_file = None

    def open_tables(self):
        self.click(self.TABLES_MENU)
        time.sleep(2)

    def select_restaurant(self):
        Select(WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.RESTAURANT_SELECT))).select_by_visible_text("Tamus Rooftop Sevilla")
        time.sleep(3)

    def create_rate(self):
        self.rate_name=f"TarifaQA_{datetime.now():%Y%m%d_%H%M%S}"
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.NEW_RATE_BTN)).click()
        inp=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.RATE_NAME_INPUT))
        inp.send_keys(self.rate_name)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CREATE_RATE_BTN)).click()
        time.sleep(3)
        try:
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()
        except TimeoutException:
            pass
        time.sleep(3)

    def create_zone(self):
        self.zone_name=f"ZonaQA_{datetime.now():%Y%m%d_%H%M%S}"
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.NEW_ZONE_BTN)).click()
        inp=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.ZONE_NAME_INPUT))
        inp.send_keys(self.zone_name)
        for element in self.driver.find_elements(By.TAG_NAME,"select"):
            try:
                select=Select(element)
                for option in select.options:
                    if self.rate_name in option.text:
                        select.select_by_visible_text(option.text)
                        break
            except:
                pass
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CREATE_ZONE_BTN)).click()
        time.sleep(4)

    def select_created_zone(self):
        Select(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.ZONE_SELECT))).select_by_visible_text(self.zone_name)
        time.sleep(3)

    def create_table(self):
        before = len(self.driver.find_elements(*self.TABLE))
        try:
            btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.FIRST_TABLE_BTN))
        except TimeoutException:
            btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.RECTANGULAR_BTN))
        self.driver.execute_script("arguments[0].click();", btn)
        WebDriverWait(self.driver, 10).until(lambda d: len(d.find_elements(*self.TABLE)) == before + 1)
        tables = self.driver.find_elements(*self.TABLE)
        self.current_table = tables[-1]
        self.table_zone = self.zone_name
        time.sleep(2)

    def wait_table_created(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.TABLE))

    def assign_menu(self):
        lista=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.LIST_VIEW_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",lista)
        self.driver.execute_script("arguments[0].click();",lista)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.ASSIGN_MENU_BTN)).click()
        Select(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.MENU_SELECT))).select_by_visible_text("📋 QA(NOBORRAR)")
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.SELECT_ALL_BTN)).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.ASSIGN_TO_TABLE_BTN)).click()
        time.sleep(3)

    def move_table(self):
        table=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.TABLE))
        ActionChains(self.driver).move_to_element(table).click_and_hold().move_by_offset(-100,-80).release().perform()
        time.sleep(3)

    def open_qr(self):
        lista = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LIST_VIEW_BTN))
        self.driver.execute_script("arguments[0].click();", lista)
        row = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//tr[.//span[normalize-space()='{self.table_zone}']]")))
        qr = row.find_element(*self.QR_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", qr)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", qr)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CLOSE_QR_BTN))

    def download_qr(self):
        download = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DOWNLOAD_PNG_BTN))
        self.driver.execute_script("arguments[0].click();", download)
        self.validate_qr_download()

    def print_qr(self):
        old_windows = self.driver.window_handles
        print_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRINT_BTN))
        self.driver.execute_script("arguments[0].click();", print_btn)
        WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) > len(old_windows))
        new_window = [w for w in self.driver.window_handles if w not in old_windows][0]
        self.driver.switch_to.window(new_window)
        time.sleep(5)
        print("✅ Ventana impresión abierta")
        self.driver.close()
        self.driver.switch_to.window(old_windows[0])
        time.sleep(3)
        close = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLOSE_QR_BTN))
        self.driver.execute_script("arguments[0].click();", close)
        time.sleep(3)

    def validate_qr_download(self):
        timeout = 30
        start = time.time()
        qr_file = None
        while time.time() - start < timeout:
            files = os.listdir(self.download_dir)
            qr_files = [f for f in files if f.startswith("qr-") and f.endswith(".png")]
            crdownload = [f for f in files if f.endswith(".crdownload")]
            if qr_files and not crdownload:
                qr_file = max(qr_files, key=lambda f: os.path.getctime(os.path.join(self.download_dir, f)))
                break
            time.sleep(1)
        assert qr_file is not None, "❌ No se ha descargado el QR"
        self.qr_file = os.path.join(self.download_dir, qr_file)
        print(f"✅ QR descargado: {self.qr_file}")

    def return_from_print(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

    def close_qr(self):
        close = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLOSE_QR_BTN))
        self.driver.execute_script("arguments[0].click();", close)
        time.sleep(2)

    def delete_table(self):
        lista = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LIST_VIEW_BTN))
        self.driver.execute_script("arguments[0].click();", lista)
        time.sleep(2)

        mapa = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MAP_VIEW_BTN))
        self.driver.execute_script("arguments[0].click();", mapa)
        time.sleep(2)

        table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TABLE))
        delete_btn = table.find_element(*self.DELETE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", delete_btn)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", delete_btn)

        try:
            confirm = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(),'Eliminar')]")))
            self.driver.execute_script("arguments[0].click();", confirm)
        except TimeoutException:
            pass

        time.sleep(3)

    def wait_table_deleted(self):
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(self.TABLE))

    def delete_rate(self):
        rate=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//span[normalize-space()='{self.rate_name}']")))
        container=rate.find_element(By.XPATH,"./ancestor::div[.//button[@title='Eliminar']][1]")
        delete_button=container.find_element(By.XPATH,".//button[@title='Eliminar']")
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_button)
        self.driver.execute_script("arguments[0].click();",delete_button)
        confirm=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class,'_confirmButton_') and normalize-space()='Eliminar']")))
        self.driver.execute_script("arguments[0].click();",confirm)
        WebDriverWait(self.driver,10).until(EC.staleness_of(rate))

    def delete_zone(self):
        zone=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//span[normalize-space()='{self.zone_name}']")))
        container=zone.find_element(By.XPATH,"./ancestor::div[.//button[@title='Eliminar']][1]")
        delete_button=container.find_element(By.XPATH,".//button[@title='Eliminar']")
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_button)
        self.driver.execute_script("arguments[0].click();",delete_button)
        confirm=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class,'_confirmButton_') and normalize-space()='Eliminar']")))
        self.driver.execute_script("arguments[0].click();",confirm)
        time.sleep(3)
