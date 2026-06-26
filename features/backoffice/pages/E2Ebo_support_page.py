from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.backoffice.pages.base_page import BasePage


class SupportPage_bo(BasePage):

    SUPPORT_MENU=(By.XPATH,"//a[@href='/support']")
    NEW_TICKET_BTN=(By.XPATH,"//button[.//*[name()='svg' and .//*[name()='line' and @x1='12']]]")
    TITLE_INPUT=(By.XPATH,"//input[@placeholder='Ej: Problema con la impresora, error en precios...']")
    DESCRIPTION_INPUT=(By.XPATH,"//textarea[@placeholder='Explica qué sucede...']")
    CREATE_BTN=(By.XPATH,"//button[contains(normalize-space(),'Crear Petición')]")

    def __init__(self,driver):
        super().__init__(driver)

    def open_support(self):
        self.wait_visible(self.SUPPORT_MENU)
        self.click(self.SUPPORT_MENU)

    def create_support_ticket(self,title,description):
        new_btn=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.NEW_TICKET_BTN)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            new_btn
        )
        self.driver.execute_script("arguments[0].click();",new_btn)

        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.TITLE_INPUT)
        )

        self.fill(self.TITLE_INPUT,title)
        self.fill(self.DESCRIPTION_INPUT,description)

        create_btn=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.CREATE_BTN)
        )
        self.driver.execute_script("arguments[0].click();",create_btn)

    def wait_ticket_in_list(self,title,timeout=10):
        locator=(By.XPATH,f"//*[contains(normalize-space(),\"{title}\")]")
        WebDriverWait(self.driver,timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # Pendiente de implementación en la aplicación.
    # Actualmente no existe opción para eliminar una petición de soporte.
    #
    # def delete_ticket(self,title):
    #     pass
    #
    # def wait_ticket_gone(self,title,timeout=10):
    #     pass