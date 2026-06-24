from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseCRUDMixin:

    ROW_XPATH = "//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]"
    DELETE_XPATH = ".//button[contains(@title,'Eliminar')]"
    CONFIRM_XPATH = "//button[contains(@class,'_confirmButton')]"

    def delete_by_name(self, name, row_xpath=None, delete_xpath=None, confirm_xpath=None, timeout=15):

        row_xpath = row_xpath or self.ROW_XPATH
        delete_xpath = delete_xpath or self.DELETE_XPATH
        confirm_xpath = confirm_xpath or self.CONFIRM_XPATH

        row = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, row_xpath.format(name=name)))
        )

        row.find_element(By.XPATH, delete_xpath).click()

        confirm = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, confirm_xpath))
        )

        confirm.click()