import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mobile.pages.base_page import BasePage


class LoginPage(BasePage):

    # -----------------------------
    # LOGIN
    EMAIL = '(//android.widget.EditText)[1]'
    PASSWORD = '(//android.widget.EditText)[2]'
    ACTIVATE_BUTTON = 'Activar Terminal'

    # -----------------------------
    # USUARIO ADMIN
    ADMIN_USER = ('xpath', '//android.view.ViewGroup[@content-desc=", Admin Restaurante Demo, Camarero"]')

    # -----------------------------
    # VENTAS / HOME
    VENTAS_VIEW = ('xpath', "//*[contains(@text,'VENTAS')]")

    # -----------------------------
    # MESA
    TABLE_B1 = ('xpath', '//android.view.ViewGroup[@content-desc="B1"]')

    # -----------------------------
    # COMENSALES
    GUEST_3 = ('xpath', '//android.widget.TextView[@text="3"]')
    ACCEPT_GUESTS = ('xpath', '//android.view.ViewGroup[@content-desc="Aceptar"]/android.view.ViewGroup')

    # -----------------------------
    # PRODUCTOS SCREEN
    PRODUCTS_TITLE = ('xpath', "//*[contains(@text,'Productos')]")

    # -----------------------------
    # PRODUCTO
    PRODUCT_PAELLA = (
        'xpath',
        '//android.widget.TextView[@text="Paella de Marisco"]'
    )

    # -----------------------------
    # LOGIN ACTIONS
    def enter_email(self, email):
        self.write(AppiumBy.XPATH, self.EMAIL, email)

    def enter_password(self, password):
        self.write(AppiumBy.XPATH, self.PASSWORD, password)

    def click_activate_terminal(self):
        self.click(AppiumBy.ACCESSIBILITY_ID, self.ACTIVATE_BUTTON)

    # -----------------------------
    # RESTAURANTE
    def select_restaurant(self, restaurant_name):
        self.click_text(restaurant_name)

    # -----------------------------
    # USUARIO ADMIN
    def select_user_admin(self):
        self.click(AppiumBy.XPATH, self.ADMIN_USER[1])
        time.sleep(3)  # transición a PIN

    # -----------------------------
    # PIN FLOW
    def enter_pin(self, pin="1234"):
        mapping = {
            "1": ('xpath', '//android.view.ViewGroup[@content-desc="1"]'),
            "2": ('xpath', '//android.view.ViewGroup[@content-desc="2"]'),
            "3": ('xpath', '//android.view.ViewGroup[@content-desc="3"]'),
            "4": ('xpath', '//android.view.ViewGroup[@content-desc="4"]'),
        }

        for digit in pin:
            self.click(AppiumBy.XPATH, mapping[digit][1])

    def click_access(self):
        self.click(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Acceder"]/android.view.ViewGroup')

    # -----------------------------
    # VENTAS
    def see_ventas(self):
        self.get_element(AppiumBy.XPATH, self.VENTAS_VIEW[1])

    # -----------------------------
    # MESA
    def select_table_b1(self):
        self.click(AppiumBy.XPATH, self.TABLE_B1[1])

    # -----------------------------
    # COMENSALES
    def select_guests_3(self):
        self.click(AppiumBy.XPATH, self.GUEST_3[1])
        time.sleep(1)
        self.click(AppiumBy.XPATH, self.ACCEPT_GUESTS[1])
        time.sleep(1)

    # -----------------------------
    # PRODUCTO
    def select_product_paella(self):
        self.click(AppiumBy.XPATH, self.PRODUCT_PAELLA[1])
        time.sleep(2)

    # -----------------------------
    # NUEVO: ESPERAR MESAS
    def wait_tables_loaded(self):
        # Espera hasta que al menos una mesa aparezca en pantalla
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc,"B")]')
            )
        )
        time.sleep(2)  # opcional: pequeña espera visual