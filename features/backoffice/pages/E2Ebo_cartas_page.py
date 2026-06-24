from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.backoffice.pages.base_page import BasePage


class CartasPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    CARTAS_MENU = (By.XPATH, "//a[contains(.,'Cartas')]")
    ADD_CARTA_BTN = (By.XPATH, "//button[contains(.,'Añadir carta')]")
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Carta')]")
    RADIO_OPTION = (By.XPATH, "//input[@type='radio']")
    CREATE_BTN = (By.XPATH, "//button[@type='submit' and contains(.,'Crear')]")
    CONTINUE_MODAL_BTN = (By.XPATH, "//button[normalize-space()='Continuar']")
    DELETE_BTN = (By.XPATH,".//button[contains(@title,'Eliminar carta')]")
    CONFIRM_DELETE_BTN = (By.XPATH,"//button[contains(@class,'_confirmButton') and normalize-space()='Eliminar']")

    def open_cartas(self):
        self.click(self.CARTAS_MENU)
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/cartas")
        )

    def create_carta(self, name):
        self.click(self.ADD_CARTA_BTN)
        self.fill(self.NAME_INPUT, name)
        self.click(self.RADIO_OPTION)
        self.click(self.CREATE_BTN)


    def close_continue_modal_if_present(self, timeout=2):
        try:
            btn = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.CONTINUE_MODAL_BTN))
            btn.click()
        except TimeoutException:
            pass

    def wait_carta_in_list(self, name, timeout=15):
        locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def delete_carta(self, name):
        self.wait_carta_in_list(name)
        row_locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")
        row = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(row_locator))
        delete_btn = WebDriverWait(row, 5).until(lambda r: r.find_element(*self.DELETE_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)