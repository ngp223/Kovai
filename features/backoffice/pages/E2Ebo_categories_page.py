from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.backoffice.pages.base_page import BasePage
import time

class CategoriesPage_bo(BasePage):
    CATEGORIES_MENU=(By.XPATH,"//a[@href='/categories']")
    NEW_CATEGORY_BTN=(By.XPATH,"//button[contains(normalize-space(),'Nueva Categoría')]")
    CATEGORY_NAME_INPUT=(By.XPATH,"//input[@placeholder='Ej: Bebidas']")
    CREATE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")
    EDIT_BTN=(By.XPATH,".//button[@title='Editar']")
    SAVE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Guardar')]")
    DELETE_BTN=(By.XPATH,".//button[@title='Eliminar']")
    CONFIRM_DELETE_BTN=(By.XPATH,"//button[contains(@class,'_confirmButton') and contains(normalize-space(),'Eliminar')]")
    CONTINUE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Continuar')]")

    def __init__(self,driver):
        super().__init__(driver)

    def close_continue_popup(self):
        try:
            btn=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONTINUE_BTN))
            self.driver.execute_script("arguments[0].click();",btn)
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(self.CONTINUE_BTN))
        except:
            pass

    def open_categories(self):
        self.wait_visible(self.CATEGORIES_MENU)
        self.click(self.CATEGORIES_MENU)

    def create_category(self,category_name):
        self.click(self.NEW_CATEGORY_BTN)
        self.fill(self.CATEGORY_NAME_INPUT,category_name)
        self.click(self.CREATE_BTN)
        self.close_continue_popup()

    def wait_category_in_list(self,name,timeout=10):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def wait_category_gone(self,name,timeout=10):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))

    def modify_category(self,name,new_name):
        self.wait_category_in_list(name)
        row_locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")
        row=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(row_locator))
        edit_btn=row.find_element(*self.EDIT_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",edit_btn)
        self.driver.execute_script("arguments[0].click();",edit_btn)
        input_locator=(By.XPATH,"//input[@placeholder='Ej: Bebidas']")
        input_element=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(input_locator))
        input_element.clear()
        input_element.send_keys(new_name)
        save_btn=WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.SAVE_BTN))
        self.driver.execute_script("arguments[0].click();",save_btn)
        self.close_continue_popup()
        time.sleep(2)

    def delete_category(self,name):
        self.wait_category_in_list(name)
        row_locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")
        row=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(row_locator))
        delete_btn=row.find_element(*self.DELETE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_btn=WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)
        self.close_continue_popup()