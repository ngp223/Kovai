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
    SEND_BTN=(By.XPATH,"//button[.//*[name()='polyline']]")
    STATUS_PROGRESS=(By.XPATH,"//*[normalize-space()='En progreso']")
    CLOSE_BTN=(By.XPATH,"//button[normalize-space()='×']")

    def __init__(self,driver):
        super().__init__(driver)

    def open_support(self):
        self.wait_visible(self.SUPPORT_MENU)
        self.click(self.SUPPORT_MENU)

    def create_support_ticket(self,title,description):
        btn=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.NEW_TICKET_BTN))
        self.driver.execute_script("arguments[0].click();",btn)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.TITLE_INPUT))
        self.fill(self.TITLE_INPUT,title)
        self.fill(self.DESCRIPTION_INPUT,description)
        create=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CREATE_BTN))
        self.driver.execute_script("arguments[0].click();",create)

    def wait_ticket_in_list(self,title):
        locator=(By.XPATH,f"//span[contains(normalize-space(),\"{title}\")]")
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator))

    def modify_support_ticket(self,title,comment):
        ticket=(By.XPATH,f"//span[contains(normalize-space(),\"{title}\")]")
        ticket_element=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(ticket))
        self.driver.execute_script("arguments[0].click();",ticket_element)

        textarea=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.COMMENT_TEXTAREA))
        textarea.clear()
        textarea.send_keys(comment)

        send=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.SEND_BTN))
        self.driver.execute_script("arguments[0].click();",send)

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.STATUS_PROGRESS))

        close=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CLOSE_BTN))
        self.driver.execute_script("arguments[0].click();",close)

        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(self.COMMENT_TEXTAREA))

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[normalize-space()='En progreso']")))