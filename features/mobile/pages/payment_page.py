from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class PaymentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    CASH_OPTION = ("xpath", "//*[@text='Efectivo']")
    CONFIRM_PAYMENT = ("id", "btn_confirm_payment")
    TICKET = ("id", "ticket_view")

    # -----------------------------
    def select_payment_method(self, method):
        if method.lower() == "efectivo":
            self.click(AppiumBy.XPATH, self.CASH_OPTION[1])

    # -----------------------------
    def confirm_payment(self):
        self.click(AppiumBy.ID, self.CONFIRM_PAYMENT)

    # -----------------------------
    def is_ticket_generated(self):
        try:
            self.get_element(AppiumBy.ID, self.TICKET[1])
            return True
        except:
            return False