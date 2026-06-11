from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:

    URL = "https://kovai.hi-iberia.es/dashboard"

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):

        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(email)

        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT)
        ).click()

    def is_logged_in(self):

        self.wait.until(
            lambda d: "/login" not in d.current_url
        )
        time.sleep(5)

        return True