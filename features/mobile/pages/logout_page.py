from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    EXIT_POS_MODE = '//android.widget.TextView[@text="Salir modo TPV"]'
    CHANGE_USER_BUTTON = '//android.view.ViewGroup[@content-desc="Cambiar Usuario"]/android.view.ViewGroup'
    BACK_BUTTON = '//android.view.ViewGroup[@content-desc=""]'
    CLOSE_COMPANY_SESSION = '//android.widget.TextView[@text="Cerrar sesión de la empresa"]'
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def exists(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))
            return True
        except:
            return False
    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator))).click()
    def exit_pos_mode(self):
        if self.exists(self.EXIT_POS_MODE):
            self.click(self.EXIT_POS_MODE)
            return True
        return False
    def open_change_user(self):
        if self.exists(self.CHANGE_USER_BUTTON):
            self.click(self.CHANGE_USER_BUTTON)
            return True
        return False
    def go_back(self):
        if self.exists(self.BACK_BUTTON):
            self.click(self.BACK_BUTTON)
            return True
        return False
    def close_company_session(self):
        if self.exists(self.CLOSE_COMPANY_SESSION):
            self.click(self.CLOSE_COMPANY_SESSION)
            return True
        return False
