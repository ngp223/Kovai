from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from random import choice

from features.backoffice.pages.base_page import BasePage


class UsersPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USERS_MENU = (By.XPATH,"//a[@href='/users']")
    ROLE_BTN = (By.XPATH,"//button[contains(@class,'_secondaryBtn_1qr2a_240')]")
    CREATE_FIRST_USER_BTN = (By.XPATH,"//button[contains(normalize-space(),'Crear primer usuario')]")
    NEW_USER_BTN = (By.XPATH,"//button[contains(normalize-space(),'+ Nuevo Usuario')]")
    FULLNAME_INPUT = (By.XPATH,"//input[@placeholder='Nombre completo']")
    PASSWORD_INPUT = (By.XPATH,"//input[@placeholder='1234' and @pattern='\\d{4,6}']")
    CREATE_BTN = (By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")

    def open_users(self):
        self.wait_visible(self.USERS_MENU)
        self.click(self.USERS_MENU)

    def select_random_role(self):
        roles = ["Cajero","Camarero","Encargado"]
        selected_role = choice(roles)
        role_locator = (By.XPATH,f"//button[normalize-space()='{selected_role}']")
        self.click(role_locator)
        return selected_role

    def open_create_user_form(self):
        try:
            self.click(self.CREATE_FIRST_USER_BTN,timeout=5)
        except TimeoutException:
            self.click(self.NEW_USER_BTN,timeout=10)

    def create_user(self, user_name):
        self.open_create_user_form()
        self.fill(self.FULLNAME_INPUT,user_name)
        self.fill(self.PASSWORD_INPUT,"1234")
        self.click(self.CREATE_BTN)