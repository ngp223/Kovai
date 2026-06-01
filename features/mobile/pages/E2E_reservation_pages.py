import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mobile.pages.base_page import BasePage


class ReservationPage(BasePage):

    EMAIL = '(//android.widget.EditText)[1]'
    PASSWORD = '(//android.widget.EditText)[2]'
    ACTIVATE_BUTTON = 'Activar Terminal'

    ADMIN_USER = (
        'xpath',
        '//android.view.ViewGroup[contains(@content-desc,"Admin Restaurante Demo")]'
    )

    VENTAS_VIEW = ('xpath', "//*[contains(@text,'VENTAS')]")
    TABLE_B1 = ('xpath', '//android.view.ViewGroup[@content-desc="B1"]')

    GUEST = ('xpath', '//android.widget.TextView[@text="3"]')
    ACCEPT_GUESTS = (
        'xpath',
        '//android.view.ViewGroup[@content-desc="Aceptar"]/android.view.ViewGroup'
    )

    PRODUCT_PAELLA = ('xpath', '//android.widget.TextView[@text="Paella de Marisco"]')

    ADD_BUTTON = (
        'xpath',
        '//android.view.ViewGroup[@content-desc="Añadir al pedido"]/android.view.ViewGroup'
    )

    CART_BUTTON = (
        'xpath',
        '//android.widget.TextView[@text=""]/ancestor::android.view.ViewGroup[1]'
    )

    PLUS_BUTTON = (
        'xpath',
        '//android.view.ViewGroup[.//android.widget.TextView[@text="+"]]'
    )

    REALIZAR_PAGO_BUTTON = ('xpath', '//android.widget.TextView[@text="Realizar Pago"]')
    CONFIRMAR_PAGO_BUTTON = ('xpath', '//android.widget.TextView[@text="Confirmar Pago"]')
    FINALIZAR_BUTTON = ('xpath', '//android.widget.TextView[@text="Finalizar"]')


    def enter_email(self, email):
        self.write(AppiumBy.XPATH, self.EMAIL, email)

    def enter_password(self, password):
        self.write(AppiumBy.XPATH, self.PASSWORD, password)

    def click_activate_terminal(self):
        self.click(AppiumBy.ACCESSIBILITY_ID, self.ACTIVATE_BUTTON)

    def select_restaurant(self, restaurant_name):
        self.click_text(restaurant_name)

    def select_user_admin(self):
        self.click(AppiumBy.XPATH, self.ADMIN_USER[1])
        time.sleep(2)

    def enter_pin(self, pin="1234"):
        mapping = {
            "1": '//android.view.ViewGroup[@content-desc="1"]',
            "2": '//android.view.ViewGroup[@content-desc="2"]',
            "3": '//android.view.ViewGroup[@content-desc="3"]',
            "4": '//android.view.ViewGroup[@content-desc="4"]',
        }

        for digit in pin:
            self.click(AppiumBy.XPATH, mapping[digit])

    def click_access(self):
        self.click(
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="Acceder"]/android.view.ViewGroup'
        )

    def wait_tables_loaded(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc,"B")]')
            )
        )

    def see_ventas(self):
        self.get_element(AppiumBy.XPATH, self.VENTAS_VIEW[1])

    def select_table_b1(self):
        self.click(AppiumBy.XPATH, self.TABLE_B1[1])

    def select_guests(self):
        self.click(AppiumBy.XPATH, self.GUEST[1])
        time.sleep(1)

    def click_accept_guests(self):
        self.click(AppiumBy.XPATH, self.ACCEPT_GUESTS[1])
        time.sleep(1)

    def select_product_paella(self):
        self.click(AppiumBy.XPATH, self.PRODUCT_PAELLA[1])
        time.sleep(1)

    def click_add_product(self):
        self.click(AppiumBy.XPATH, self.ADD_BUTTON[1])
        time.sleep(1)

    def increase_product(self):

        # abrir carrito una sola vez
        self.click(AppiumBy.XPATH, self.CART_BUTTON[1])
        time.sleep(1)
        self.click(AppiumBy.XPATH, self.CART_BUTTON[1])
        time.sleep(1)


    def click_realizar_pago(self):
        self.click(AppiumBy.XPATH, self.REALIZAR_PAGO_BUTTON[1])

    def click_confirmar_pago(self):
        self.click(AppiumBy.XPATH, self.CONFIRMAR_PAGO_BUTTON[1])
        time.sleep(1)

    def click_finalizar(self):
        self.click(AppiumBy.XPATH, self.FINALIZAR_BUTTON[1])
        time.sleep(2)