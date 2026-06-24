from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import choice
from features.backoffice.pages.base_page import BasePage


class ModifiersPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    MODIFIERS_MENU = (By.XPATH,"//a[@href='/modifiers']")
    CREATE_FIRST_GROUP_BTN = (By.XPATH,"//button[contains(normalize-space(),'Crear primer grupo')]")
    NEW_GROUP_BTN = (By.XPATH,"//button[contains(normalize-space(),'Nuevo Grupo')]")
    GROUP_NAME_INPUT = (By.XPATH,"//input[@placeholder='Ej: Punto de la carne, Extras, etc.']")
    OPTION_NAME_INPUT = (By.XPATH,"//input[@placeholder='Nombre de la opción (Ej: Muy hecho)']")
    CREATE_BTN = (By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")

    def open_modifiers(self):
        self.click(self.MODIFIERS_MENU)

    def open_create_group_form(self):
        try:
            self.click(self.CREATE_FIRST_GROUP_BTN,timeout=3)
        except TimeoutException:
            self.click(self.NEW_GROUP_BTN,timeout=3)

    def create_modifier_group(self, group_name):
        self.open_create_group_form()
        self.fill(self.GROUP_NAME_INPUT,group_name)
        option_name = choice(["Muy hecho","Poco hecho","Al punto"])
        self.fill(self.OPTION_NAME_INPUT,option_name)
        self.click(self.CREATE_BTN)

    def wait_group_in_list(self, name, timeout=5):
        locator = (By.XPATH,f"//div[contains(@class,'_itemName') and contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def exists_item(self, name, timeout=5):
        try:
            self.wait_group_in_list(name, timeout)
            return True
        except TimeoutException:
            return False

    def delete_modifier_group(self, name):
        self.wait_group_in_list(name)

        row = WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located((By.XPATH,
                f"//div[contains(@class,'_itemName') and contains(normalize-space(),'{name}')]/ancestor::tr[1]"
            ))
        )

        delete_btn = row.find_element(By.XPATH, ".//button[@title='Eliminar']")

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", delete_btn)
        self.driver.execute_script("arguments[0].click();", delete_btn)

        confirm = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Eliminar')]"))
        )
        self.driver.execute_script("arguments[0].click();", confirm)

    def wait_item_gone(self, name, timeout=5):
        locator = (By.XPATH,f"//div[contains(@class,'_itemName') and contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))