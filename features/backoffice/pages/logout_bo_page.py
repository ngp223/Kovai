from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage_bo:

    USER_MENU = (By.XPATH,"//*[@id='root']/div/div/div/header/div[2]/div[2]/button/div[1]/div[1]")
    LOGOUT_BTN = (By.XPATH,"//*[@id='root']/div/div/div/header/div[2]/div[2]/div[2]/button[2]/span")

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_BTN)