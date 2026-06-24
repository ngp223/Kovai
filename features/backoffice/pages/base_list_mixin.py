from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseListMixin:

    ROW_XPATH = "//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]"

    def wait_item(self, name, row_xpath=None, timeout=15):
        row_xpath = row_xpath or self.ROW_XPATH
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, row_xpath.format(name=name)))
        )

    def wait_item_gone(self, name, row_xpath=None, timeout=15):
        row_xpath = row_xpath or self.ROW_XPATH
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.XPATH, row_xpath.format(name=name)))
        )

    def exists_item(self, name, row_xpath=None, timeout=5):
        row_xpath = row_xpath or self.ROW_XPATH
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, row_xpath.format(name=name)))
            )
            return True
        except:
            return False