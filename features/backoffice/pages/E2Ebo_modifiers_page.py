from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import choice
from features.backoffice.pages.base_page import BasePage

class ModifiersPage_bo(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    MODIFIERS_MENU=(By.XPATH,"//a[@href='/modifiers']")
    CREATE_FIRST_GROUP_BTN=(By.XPATH,"//button[contains(normalize-space(),'Crear primer grupo')]")
    NEW_GROUP_BTN=(By.XPATH,"//button[contains(normalize-space(),'Nuevo Grupo')]")
    GROUP_NAME_INPUT=(By.XPATH,"//input[@placeholder='Ej: Punto de la carne, Extras, etc.']")
    OPTION_NAME_INPUT=(By.XPATH,"//input[@placeholder='Nombre de la opción (Ej: Muy hecho)']")
    CREATE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")
    ADD_OPTION_BTN=(By.XPATH,"//button[contains(normalize-space(),'Añadir opción')]")
    SAVE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Guardar')]")
    CONTINUE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Continuar')]")

    def open_modifiers(self):
        self.click(self.MODIFIERS_MENU)

    def close_continue_popup(self):
        try:
            btn=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONTINUE_BTN))
            self.driver.execute_script("arguments[0].click();",btn)
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(self.CONTINUE_BTN))
        except:
            pass

    def open_create_group_form(self):
        try:
            self.click(self.CREATE_FIRST_GROUP_BTN,timeout=3)
        except TimeoutException:
            self.click(self.NEW_GROUP_BTN,timeout=3)

    def create_modifier_group(self,group_name):
        self.open_create_group_form()
        self.fill(self.GROUP_NAME_INPUT,group_name)
        self.fill(self.OPTION_NAME_INPUT,choice(["Muy hecho","Poco hecho","Al punto"]))
        self.click(self.CREATE_BTN)
        self.close_continue_popup()
        self.wait_group_in_list(group_name)

    def wait_group_in_list(self,name,timeout=10):
        locator=(By.XPATH,f"//div[contains(@class,'_itemName') and normalize-space()='{name}']")
        WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def exists_item(self,name,timeout=10):
        try:
            self.wait_group_in_list(name,timeout)
            return True
        except TimeoutException:
            return False

    def edit_modifier_group(self,name):
        self.wait_group_in_list(name)
        edit_locator=(By.XPATH,f"//div[contains(@class,'_itemName') and normalize-space()='{name}']/ancestor::tr[1]//button[@title='Editar']")
        edit_btn=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(edit_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",edit_btn)
        self.driver.execute_script("arguments[0].click();",edit_btn)
        add_btn=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.ADD_OPTION_BTN))
        self.driver.execute_script("arguments[0].click();",add_btn)
        option_locator=(By.XPATH,"//input[@placeholder='Nombre de la opción (Ej: Muy hecho)']")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(option_locator))
        inputs=[i for i in self.driver.find_elements(*option_locator) if i.is_displayed()]
        inputs[-1].send_keys("aditivoQA")
        self.click(self.SAVE_BTN)
        self.close_continue_popup()
        self.wait_group_in_list(name)

    def delete_modifier_group(self,name):
        self.wait_group_in_list(name)
        delete_locator=(By.XPATH,f"//div[contains(@class,'_itemName') and normalize-space()='{name}']/ancestor::tr[1]//button[@title='Eliminar']")
        delete_btn=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(delete_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm_locator=(By.XPATH,"//button[contains(.,'Eliminar')]")
        confirm=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(confirm_locator))
        self.driver.execute_script("arguments[0].click();",confirm)
        self.close_continue_popup()

    def wait_item_gone(self,name,timeout=10):
        locator=(By.XPATH,f"//div[contains(@class,'_itemName') and normalize-space()='{name}']")
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))