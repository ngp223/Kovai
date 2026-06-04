from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CashClosurePage:

    CASH_CLOSURE_BUTTON = ('xpath', '//android.view.ViewGroup[@content-desc=", Cierre de Caja"]')
    DECLARED_SECTION = ('xpath', '//android.widget.TextView[@text="Normal Declarado"]')
    COPY_EXPECTED_1 = ('xpath', '(//android.widget.TextView[@text="COPIAR ESPERADO"])[1]')
    COPY_EXPECTED_2 = ('xpath', '(//android.widget.TextView[@text="COPIAR ESPERADO"])[2]')
    FINALIZE_CLOSURE = ('xpath', '//android.widget.TextView[@text="Realizar Cierre"]')

    LAST_CLOSURE_DATE = ('xpath', '(//android.widget.TextView[contains(@text,"/")])[last()]')

    LAST_CLOSURE_AMOUNT = (
        'xpath',
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div[4]/div/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[2]/div/span/span'
    )

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def open_cash_closure(self):
        self.click(self.CASH_CLOSURE_BUTTON)

    def open_declared_section(self):
        self.click(self.DECLARED_SECTION)

    def copy_expected_first(self):
        self.click(self.COPY_EXPECTED_1)

    def copy_expected_second(self):
        self.click(self.COPY_EXPECTED_2)

    def scroll_to_finalize(self):
        self.swipe_up()

    def swipe_up(self):
        size = self.driver.get_window_size()

        start_x = size["width"] / 2
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.3

        self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def finalize_closure(self):
        self.click(self.FINALIZE_CLOSURE)

    def get_last_closure_date(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LAST_CLOSURE_DATE)
        )
        return element.text

    def get_last_closure_amount(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LAST_CLOSURE_AMOUNT)
        )
        return element.text