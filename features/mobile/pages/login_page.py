from appium.webdriver.common.appiumby import AppiumBy
from mobile.pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = '(//android.widget.EditText)[1]'
    PASSWORD = '(//android.widget.EditText)[2]'

    ACTIVATE_BUTTON = 'Activar Terminal'

    def enter_email(self, email):
        self.write(AppiumBy.XPATH, self.EMAIL, email)

    def enter_password(self, password):
        self.write(AppiumBy.XPATH, self.PASSWORD, password)

    def click_activate_terminal(self):
        self.click(
            AppiumBy.ACCESSIBILITY_ID,
            self.ACTIVATE_BUTTON
        )