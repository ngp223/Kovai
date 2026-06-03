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

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, locator))
        ).click()

    def exit_pos_mode(self):
        try:
            self.click(self.EXIT_POS_MODE)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CHANGE_USER_BUTTON)
                )
            )

        except:
            pass

    def open_change_user(self):
        self.click(self.CHANGE_USER_BUTTON)

    def go_back(self):
        self.click(self.BACK_BUTTON)

    def close_company_session(self):
        self.click(self.CLOSE_COMPANY_SESSION)