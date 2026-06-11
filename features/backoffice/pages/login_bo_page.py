from selenium.webdriver.common.by import By


class LoginPage_bo:

    def __init__(self, driver):
        self.driver = driver

        self.user = (By.ID, "email")
        self.password = (By.ID, "password")
        self.button = (By.XPATH, "//button[@type='submit']")

    def login_bo(self, user, password):

        self.driver.find_element(*self.user).clear()
        self.driver.find_element(*self.user).send_keys(user)

        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)

        self.driver.find_element(*self.button).click()