from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import choice
import time


class UsersPage_bo:

    def __init__(self, driver):
        self.driver = driver

    # LOCATORS
    USERS_MENU = (By.XPATH, "//a[@href='/users']")
    ROLE_BTN = (By.XPATH, "//button[contains(@class,'_secondaryBtn_1qr2a_240')]")
    CREATE_FIRST_USER_BTN = (By.XPATH, "//button[contains(normalize-space(),'Crear primer usuario')]")
    NEW_USER_BTN = (By.XPATH, "//button[contains(normalize-space(),'+ Nuevo Usuario')]")
    FULLNAME_INPUT = (By.XPATH, "//input[@placeholder='Nombre completo']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='1234' and @pattern='\\d{4,6}']")
    CREATE_BTN = (By.XPATH, "//button[@type='submit' and contains(normalize-space(),'Crear')]")

    # GENERICS
    def click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def fill(self, locator, value, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)

    # ACTIONS
    def open_users(self):
        self.click(self.USERS_MENU)
        time.sleep(2)

    def select_random_role(self):
        roles = ["Cajero", "Camarero", "Encargado"]
        selected_role = choice(roles)

        role_locator = (
            By.XPATH,
            f"//button[normalize-space()='{selected_role}']"
        )
        self.click(role_locator)
        time.sleep(2)

        return selected_role

    def open_create_user_form(self):
        try:
            print("Intentando: Crear primer usuario")
            self.click(self.CREATE_FIRST_USER_BTN, timeout=5)
        except TimeoutException:
            print("Usando '+ Nuevo Usuario'")
            self.click(self.NEW_USER_BTN, timeout=10)

        time.sleep(2)

    def create_user(self, user_name):
        self.open_create_user_form()
        self.fill(self.FULLNAME_INPUT, user_name)
        self.fill(self.PASSWORD_INPUT, "1234")
        self.click(self.CREATE_BTN)
        time.sleep(4)