from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.backoffice.pages.base_page import BasePage
class SupportPage_bo(BasePage):
    SUPPORT_MENU=(By.XPATH,"//a[@href='/support']")
    NEW_TICKET_BTN=(By.XPATH,"//button[.//*[name()='svg' and .//*[name()='line']]]")
    TITLE_INPUT=(By.XPATH,"//input")
    DESCRIPTION_INPUT=(By.XPATH,"//textarea[@placeholder='Explica qué sucede...']")
    COMMENT_TEXTAREA=(By.XPATH,"//textarea[@placeholder='Escribe tu mensaje...']")
    CREATE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Crear Petición')]")
    SAVE_BTN=(By.XPATH,"//button[contains(@class,'_primaryBtn') or contains(.,'Guardar')]")
    STATUS_OPEN=(By.XPATH,"//div[contains(normalize-space(),'Abierto')]")
    STATUS_PROGRESS=(By.XPATH,"//div[contains(normalize-space(),'En progreso')]")
    CLOSE_BTN=(By.XPATH,"//button[normalize-space()='×']")
    def __init__(self,driver):
        super().__init__(driver)
        self.ticket_locator=None
    def open_support(self):
        self.wait_visible(self.SUPPORT_MENU)
        self.click(self.SUPPORT_MENU)
    def create_support_ticket(self,title,description):
        btn=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.NEW_TICKET_BTN))
        self.driver.execute_script("arguments[0].click();",btn)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.TITLE_INPUT))
        self.fill(self.TITLE_INPUT,title)
        self.fill(self.DESCRIPTION_INPUT,description)
        save=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CREATE_BTN))
        self.driver.execute_script("arguments[0].click();",save)
    def wait_ticket_in_list(self,title):
        locator=(By.XPATH,f"//span[contains(normalize-space(),'{title}')]/ancestor::*[self::div or self::tr or self::article][1]")
        WebDriverWait(self.driver,25,poll_frequency=0.5).until(EC.presence_of_element_located(locator))
        self.ticket_locator=locator
    def modify_support_ticket(self,new_title,new_description):
        ticket=WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.ticket_locator))
        self.driver.execute_script("arguments[0].click();",ticket)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.COMMENT_TEXTAREA))
        self.fill(self.COMMENT_TEXTAREA,new_description)
        save=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.SAVE_BTN))
        self.driver.execute_script("arguments[0].click();",save)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.STATUS_PROGRESS))
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(self.CLOSE_BTN))