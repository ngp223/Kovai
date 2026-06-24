from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from features.backoffice.pages.base_page import BasePage


class PromotionsPage_bo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    PROMOTIONS_MENU = (By.XPATH, "//a[@href='/promotions']")
    CREATE_FIRST_PROMOTION_BTN = (By.XPATH, "//button[contains(.,'Crear primera')]")
    NEW_PROMOTION_BTN = (By.XPATH, "//button[contains(.,'Nueva Promoción')]")
    PROMOTION_NAME_INPUT = (By.XPATH, "//input[@placeholder='Ej: 2x1 en Cervezas']")
    CREATE_PROMOTION_BTN = (By.XPATH, "//button[@type='submit' and contains(.,'Crear')]")
    CONTINUE_MODAL_BTN = (By.XPATH, "//button[normalize-space()='Continuar']")
    DELETE_BTN = (By.XPATH, ".//button[@title='Eliminar']")
    CONFIRM_DELETE_BTN = (By.XPATH,"//button[contains(@class,'_confirmButton') and normalize-space()='Eliminar']")

    def go_to_promotions(self):
        self.click(self.PROMOTIONS_MENU)
        WebDriverWait(self.driver, 2).until(EC.url_contains("/promotions"))

    def open_create_form(self):
        try:
            self.click(self.CREATE_FIRST_PROMOTION_BTN, timeout=2)
        except TimeoutException:
            self.click(self.NEW_PROMOTION_BTN, timeout=2)

    def create_promotion(self, name):
        self.open_create_form()
        self.fill(self.PROMOTION_NAME_INPUT, name)
        self.click(self.CREATE_PROMOTION_BTN)

    def close_continue_modal_if_present(self, timeout=2):
        try:
            btn = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.CONTINUE_MODAL_BTN))
            btn.click()
        except TimeoutException:
            pass

    def wait_promotion_in_list(self, name, timeout=2):
        locator = (By.XPATH, f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def delete_promotion(self, name):
        self.wait_promotion_in_list(name)
        row_locator = ( By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")
        row = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(row_locator))
        delete_btn = row.find_element(*self.DELETE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)