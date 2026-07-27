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
    CONFIRM_DELETE_BTN=(By.XPATH,"//button[contains(@class,'_confirmButton_') and contains(normalize-space(),'Eliminar')]")
    CONTINUE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Continuar')]")
    ROLE_NAME_INPUT=(By.XPATH,"//input[@placeholder='Ej: COCINA_CALIENTE']")
    CREATE_ROLE_BTN=(By.XPATH,"//button[@type='button' and contains(normalize-space(),'Crear rol')]")
    DELETE_ROLE_BTN=(By.XPATH,".//button[@title='Eliminar rol']")
    CONFIRM_ROLE_DELETE_BTN = (By.XPATH, "//button[contains(@class,'_confirmButton_') and contains(normalize-space(),'Eliminar')]")

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

    def create_role(self,role_name):
        self.fill(self.ROLE_NAME_INPUT,role_name)
        self.click(self.CREATE_ROLE_BTN)
        self.close_continue_popup()
        self.wait_role_in_list(role_name)

    def wait_category_in_list(self,name,timeout=10):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def wait_category_gone(self,name,timeout=10):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))

    def wait_role_in_list(self,name,timeout=20):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def wait_role_gone(self,name,timeout=20):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))

    def modify_category(self,name,new_name):
        self.wait_category_in_list(name)
        row_locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")
        row=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(row_locator))
        edit_btn=row.find_element(*self.EDIT_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",edit_btn)
        self.driver.execute_script("arguments[0].click();",edit_btn)
        input_element=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.CATEGORY_NAME_INPUT))
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

    def delete_role(self, name):
        print("Intentando borrar rol:", name)
        role_badge = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, f"//span[contains(normalize-space(),'{name}') and .//button[@title='Eliminar rol']]")))
        delete_btn = role_badge.find_element(By.XPATH, ".//button[@title='Eliminar rol']")
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", delete_btn)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(delete_btn))
        self.driver.execute_script("arguments[0].click();", delete_btn)
        confirm_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class,'_confirmButton_') and normalize-space()='Eliminar']")))
        self.driver.execute_script("arguments[0].click();", confirm_btn)
        self.wait_role_gone(name)
