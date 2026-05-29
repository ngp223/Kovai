from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # -----------------------------
    # CLICK
    # -----------------------------
    def click(self, by, locator):

        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )

        element.click()

    # -----------------------------
    # WRITE
    # -----------------------------
    def write(self, by, locator, text):

        element = self.wait.until(
            EC.presence_of_element_located((by, locator))
        )

        element.clear()
        element.send_keys(text)

    # -----------------------------
    # GET ELEMENT
    # -----------------------------
    def get_element(self, by, locator):

        return self.wait.until(
            EC.presence_of_element_located((by, locator))
        )

    # -----------------------------
    # CLICK TEXT
    # -----------------------------
    def click_text(self, text):

        xpath = f'//*[@text="{text}"]'

        self.click(AppiumBy.XPATH, xpath)