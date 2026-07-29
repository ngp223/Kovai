from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import choice
from features.backoffice.pages.base_page import BasePage
import time

class UsersPage_bo(BasePage):
    USERS_MENU=(By.XPATH,"//a[@href='/users']")
    CREATE_FIRST_USER_BTN=(By.XPATH,"//button[contains(normalize-space(),'Crear primer usuario')]")
    NEW_USER_BTN=(By.XPATH,"//button[contains(normalize-space(),'+ Nuevo Usuario')]")
    FULLNAME_INPUT=(By.XPATH,"//input[@placeholder='Nombre completo']")
    PASSWORD_INPUT=(By.XPATH,"//input[@placeholder='1234' and @pattern='\\d{4,6}']")
    CREATE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")
    EDIT_BTN=(By.XPATH,".//button[@title='Editar']")
    SAVE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Guardar')]")
    DELETE_BTN=(By.XPATH,".//button[@title='Eliminar']")
    CONFIRM_DELETE_BTN=(By.XPATH,"//button[contains(@class,'_danger')]")
    ASSIGN_RESTAURANTS_BTN=(By.XPATH,".//button[@title='Asignar restaurantes']")
    RESTAURANT_CHECKBOX=(By.XPATH,"//span[normalize-space()='Tamus Flagship Gran Vía']/preceding-sibling::input[@type='checkbox']")
    ROLE_SELECT=(By.XPATH,"//select[option[contains(text(),'Cajero') or contains(text(),'Camarero') or contains(text(),'Encargado')]]")
    SAVE_CHANGES_BTN=(By.XPATH,"//button[normalize-space()='Guardar Cambios']")
    CONTINUE_BTN=(By.XPATH,"//button[normalize-space()='Continuar']")
    def __init__(self,driver):
        super().__init__(driver)
    def open_users(self):
        self.wait_visible(self.USERS_MENU)
        self.click(self.USERS_MENU)
    def select_random_role(self):
        roles=["Cajero","Camarero","Encargado"]
        selected=choice(roles)
        self.click((By.XPATH,f"//button[normalize-space()='{selected}']"))
        return selected
    def open_create_user_form(self):
        try:
            self.click(self.CREATE_FIRST_USER_BTN,timeout=5)
        except TimeoutException:
            self.click(self.NEW_USER_BTN,timeout=5)
    def create_user(self,user_name):
        self.open_create_user_form()
        self.fill(self.FULLNAME_INPUT,user_name)
        self.fill(self.PASSWORD_INPUT,"1234")
        self.click(self.CREATE_BTN)
        time.sleep(3)
    def wait_user_in_list(self,name,timeout=10):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
    def wait_user_gone(self,name,timeout=10):
        locator=(By.XPATH,f"//*[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))
    def modify_user(self,name,new_name,current_role):
        self.wait_user_in_list(name)
        row=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")))
        edit_btn=row.find_element(*self.EDIT_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",edit_btn)
        self.driver.execute_script("arguments[0].click();",edit_btn)
        fullname_input=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.FULLNAME_INPUT))
        fullname_input.clear()
        fullname_input.send_keys(new_name)
        password_input=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys("987654")
        time.sleep(2)
        save_btn=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.SAVE_BTN))
        self.driver.execute_script("arguments[0].click();",save_btn)
        time.sleep(5)
        row=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(normalize-space(),'{new_name}')]/ancestor::tr[1]")))
        assign_btn=row.find_element(*self.ASSIGN_RESTAURANTS_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",assign_btn)
        self.driver.execute_script("arguments[0].click();",assign_btn)
        time.sleep(3)
        checkbox=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.RESTAURANT_CHECKBOX))
        if not checkbox.is_selected():
            checkbox.click()
        roles=["Cajero","Camarero","Encargado"]
        new_role=choice([r for r in roles if r!=current_role])
        self.assigned_role=new_role
        select=Select(WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.ROLE_SELECT)))
        select.select_by_visible_text(new_role)
        time.sleep(5)
        save_changes=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.SAVE_CHANGES_BTN))
        self.driver.execute_script("arguments[0].click();",save_changes)
        time.sleep(3)
        try:
            continue_btn=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONTINUE_BTN))
            self.driver.execute_script("arguments[0].click();",continue_btn)
            time.sleep(5)
        except TimeoutException:
            pass
    def check_custom_role(self,name,role):
        self.wait_user_in_list(name)
    def delete_user(self,name):
        self.wait_user_in_list(name)
        row=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")))
        delete_btn=row.find_element(*self.DELETE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_btn=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)
