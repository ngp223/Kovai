from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL = '(//android.widget.EditText)[1]'
    PASSWORD = '(//android.widget.EditText)[2]'
    ACTIVATE_BUTTON = 'Activar Terminal'
    ADMIN_USER = '//android.view.ViewGroup[contains(@content-desc,"Admin Restaurante Demo")]'
    ACCESS_BUTTON = '//android.view.ViewGroup[@content-desc="Acceder"]/android.view.ViewGroup'
    RETRY_NOW = '//android.widget.TextView[@text="Reintentar ahora"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, by, locator):
        self.wait.until(
            EC.element_to_be_clickable((by, locator))
        ).click()

    def write(self, by, locator, text):
        el = self.wait.until(
            EC.presence_of_element_located((by, locator))
        )
        el.clear()
        el.send_keys(text)

    def enter_email(self, email):
        self.write(AppiumBy.XPATH, self.EMAIL, email)

    def enter_password(self, password):
        self.write(AppiumBy.XPATH, self.PASSWORD, password)

    def click_activate_terminal(self):
        self.click(AppiumBy.ACCESSIBILITY_ID, self.ACTIVATE_BUTTON)

    def select_restaurant(self, restaurant_name):

        xpath = f'//android.widget.TextView[@text="{restaurant_name}"]'

        self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
        ).click()

        self._handle_retry_now()

    # POPUP
    def _handle_retry_now(self):

        try:
            retry = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.RETRY_NOW)
                )
            )

            if retry.is_displayed():
                retry.click()
                print("⚠ Popup 'Reintentar ahora' cerrado")

        except:
            pass

    def select_user_admin(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.ADMIN_USER)
            )
        ).click()

    def enter_pin(self, pin="1234"):

        mapping = {
            "1": '//android.view.ViewGroup[@content-desc="1"]',
            "2": '//android.view.ViewGroup[@content-desc="2"]',
            "3": '//android.view.ViewGroup[@content-desc="3"]',
            "4": '//android.view.ViewGroup[@content-desc="4"]',
        }

        for digit in pin:
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, mapping[digit])
                )
            ).click()

    def click_access(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.ACCESS_BUTTON)
            )
        ).click()

    def wait_tables_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc,"B")]')
            )
        )
