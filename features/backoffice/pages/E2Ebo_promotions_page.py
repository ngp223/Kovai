from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.backoffice.pages.base_page import BasePage
from features.backoffice.pages.base_list_mixin import BaseListMixin
from features.backoffice.pages.base_crud_mixin import BaseCRUDMixin


class PromotionsPage_bo(BasePage, BaseListMixin, BaseCRUDMixin):
    def __init__(self, driver):
        super().__init__(driver)
    PROMOTIONS_MENU = (By.XPATH, "//a[@href='/promotions']")
    CREATE_FIRST_PROMOTION_BTN = (By.XPATH, "//button[contains(.,'Crear primera')]")
    NEW_PROMOTION_BTN = (By.XPATH, "//button[contains(.,'Nueva Promoción')]")
    PROMOTION_NAME_INPUT = (By.XPATH, "//input[@placeholder='Ej: 2x1 en Cervezas']")
    CREATE_PROMOTION_BTN = (By.XPATH, "//button[@type='submit' and contains(.,'Crear')]")
    CONTINUE_MODAL_BTN = (By.XPATH, "//button[normalize-space()='Continuar']")
    DELETE_BTN = (By.XPATH, ".//button[@title='Eliminar']")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(@class,'_confirmButton') and normalize-space()='Eliminar']")

    def open_promotions(self):
        self.go_to_promotions()

    def go_to_promotions(self):
        self.click(self.PROMOTIONS_MENU)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/promotions"))

    def create(self, name):
        self.create_promotion(name)

    def create_promotion(self, name):
        self.open_create_form()
        self.wait_form_ready()
        input_el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.PROMOTION_NAME_INPUT))
        input_el.clear()
        input_el.send_keys(name)
        self.click(self.CREATE_PROMOTION_BTN)
        self.close_continue_modal_if_present()

    def open_create_form(self):
        try:
            self.click(self.CREATE_FIRST_PROMOTION_BTN, timeout=3)
        except TimeoutException:
            self.click(self.NEW_PROMOTION_BTN, timeout=3)

    def wait_form_ready(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.PROMOTION_NAME_INPUT))

    def wait_promotion_in_list(self, name, timeout=5):
        locator = (By.XPATH, f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def exists_item(self, name, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(normalize-space(),'{name}')]")))
            return True
        except TimeoutException:
            return False

    def wait_item_gone(self, name, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, f"//*[contains(normalize-space(),'{name}')]")))

    def close_continue_modal_if_present(self, timeout=2):
        try:
            btn = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.CONTINUE_MODAL_BTN))
            btn.click()
        except TimeoutException:
            pass

    def delete_promotion(self, name):
        self.wait_promotion_in_list(name)
        row_locator = (By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")
        row = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(row_locator))
        delete_btn = row.find_element(*self.DELETE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();", delete_btn)
        confirm_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();", confirm_btn)