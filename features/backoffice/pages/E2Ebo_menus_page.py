from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.backoffice.pages.base_page import BasePage


class MenusPage_bo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
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
    CONTINUE_MODAL_BTN = (By.XPATH, "//button[normalize-space()='Continuar']")
    DELETE_BTN = (By.XPATH,".//button[contains(@title,'Eliminar')]")
    CONFIRM_DELETE_BTN = (By.XPATH,"//button[contains(@class,'_confirmButton') and normalize-space()='Confirmar']")

    def open_menus(self):
        self.click(self.MENUS_MENU)

    def create_menu(self, menu_name):
        self.click(self.NUEVO_MENU_BTN)
        self.fill(self.NOMBRE_MENU_INPUT, menu_name)
        self.fill(self.IVA_INPUT, "12")
        self.fill(self.PRECIO_INPUT, "15")
        self.click(self.ADD_PRODUCTO_1)
        self.click(self.PRODUCTO_1)
        self.click(self.LISTO_BTN)
        self.driver.execute_script("window.scrollBy(0, 300);")
        self.click(self.ADD_PRODUCTO_2)
        self.click(self.PRODUCTO_2)
        self.click(self.LISTO_BTN)
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.click(self.ADD_PRODUCTO_3)
        self.click(self.PRODUCTO_3)
        self.click(self.LISTO_BTN)
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.click(self.CREAR_MENU_BTN)
    
    def close_continue_modal_if_present(self, timeout=2):
        try:
            btn = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.CONTINUE_MODAL_BTN))
            btn.click()
        except TimeoutException:
            pass

    def wait_menu_in_list(self, name, timeout=15):
        locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def delete_menu(self, name):
        self.wait_menu_in_list(name)
        delete_btn_locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]//button[contains(@title,'Eliminar')]")
        delete_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(delete_btn_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)