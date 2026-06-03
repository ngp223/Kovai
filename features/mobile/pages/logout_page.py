from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LogoutPage:

    EXIT_POS_MODE = ('xpath', '//android.widget.TextView[@text="Salir modo TPV"]')

    CHANGE_USER_BUTTON = ('xpath', '//android.view.ViewGroup[@content-desc="Cambiar Usuario"]/android.view.ViewGroup')

    BACK_BUTTON = ('xpath', '//android.view.ViewGroup[@content-desc=""]')

    CLOSE_COMPANY_SESSION = ('xpath', '//android.widget.TextView[@text="Cerrar sesión de la empresa"]')

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def exit_pos_mode(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.EXIT_POS_MODE)
        )
        element.click()
        time.sleep(2)

    def open_change_user(self):
        self.click(self.CHANGE_USER_BUTTON)

    def go_back(self):
        self.click(self.BACK_BUTTON)

    def close_company_session(self):
        self.click(self.CLOSE_COMPANY_SESSION)