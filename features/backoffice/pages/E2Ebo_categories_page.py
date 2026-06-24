from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.backoffice.pages.base_page import BasePage


class CategoriesPage_bo(BasePage):

    CATEGORIES_MENU=(By.XPATH,"//a[@href='/categories']")
    NEW_CATEGORY_BTN=(By.XPATH,"//button[contains(normalize-space(),'Nueva Categoría')]")
    CATEGORY_NAME_INPUT=(By.XPATH,"//input[@placeholder='Ej: Bebidas']")
    CREATE_BTN=(By.XPATH,"//button[@type='submit' and contains(normalize-space(),'Crear')]")
    CONFIRM_DELETE_BTN=(By.XPATH,"//button[contains(@class,'_confirmButton') and normalize-space()='Eliminar']")

    def __init__(self,driver):
        super().__init__(driver)

    def open_categories(self):
        self.click(self.CATEGORIES_MENU)

    def create_category(self,category_name):
        self.click(self.NEW_CATEGORY_BTN)
        self.fill(self.CATEGORY_NAME_INPUT,category_name)
        self.click(self.CREATE_BTN)

    def wait_category(self,name,timeout=5):
        locator=(By.XPATH,f"//div[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def exists_item(self,name,timeout=5):
        try:
            self.wait_category(name,timeout)
            return True
        except TimeoutException:
            return False

    def wait_item_gone(self,name,timeout=5):
        locator=(By.XPATH,f"//div[contains(normalize-space(),'{name}')]")
        WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))

    def delete_category(self,name):
        self.wait_category(name)
        row=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,f"//div[contains(normalize-space(),'{name}')]/ancestor::tr[1]")))
        delete_btn=row.find_element(By.XPATH,".//button[@title='Eliminar']")
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",delete_btn)
        self.driver.execute_script("arguments[0].click();",delete_btn)
        confirm=WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.driver.execute_script("arguments[0].click();",confirm)