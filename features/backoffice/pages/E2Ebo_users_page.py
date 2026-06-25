from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import choice
from features.backoffice.pages.base_page import BasePage
import time

class UsersPage_bo(BasePage):

    USERS_MENU=(By.XPATH,"//a[@href='/users']")
    ROLE_BTN=(By.XPATH,"//button[contains(@class,'_secondaryBtn_1qr2a_240')]")
    CREATE_FIRST_USER_BTN=(By.XPATH,"//button[contains(normalize-space(),'Crear primer usuario')]")
    NEW_USER_BTN=(By.XPATH,"//button[contains(normalize-space(),'+ Nuevo Usuario')]")
    FULLNAME_INPUT=(By.XPATH,"//input[@placeholder='Nombre completo']")
    PASSWORD_INPUT=(By.XPATH,"//input[@placeholder='1234' and @pattern='\\d{4,6}']")
    CREATE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")
    DELETE_BTN=(By.XPATH,".//button[@title='Eliminar']")
    CONFIRM_DELETE_BTN=(By.XPATH,"//button[contains(@class,'_danger')]")

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

    def wait_user_in_list(self,name,timeout=10):
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(normalize-space(),'{name}')]")))

    def wait_user_gone(self,name,timeout=10):
        WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.XPATH,f"//*[contains(normalize-space(),'{name}')]")))
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located((By.XPATH,f"//*[contains(normalize-space(),'{name}')]")))

    def delete_user(self,name):
        self.wait_user_in_list(name)
        row=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]")))
        delete_btn=row.find_element(*self.DELETE_BTN)
        time.sleep(5) # para ver q pasa por el borrado
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_btn=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm_btn)
