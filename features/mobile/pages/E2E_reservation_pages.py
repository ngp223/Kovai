import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReservationPage:

    VENTAS_VIEW = ('xpath', "//*[contains(@text,'VENTAS')]")
    TABLE_B1 = ('xpath', '//android.view.ViewGroup[@content-desc="B1"]')

    GUEST = ('xpath', '//android.widget.TextView[@text="3"]')
    ACCEPT_GUESTS = ('xpath', '//android.view.ViewGroup[@content-desc="Aceptar"]/android.view.ViewGroup')

    PRODUCT_PAELLA = ('xpath', '//android.widget.TextView[@text="Paella de Marisco"]')
    ADD_BUTTON = ('xpath', '//android.view.ViewGroup[@content-desc="Añadir al pedido"]/android.view.ViewGroup')

    CART_BUTTON = ('xpath', '//android.widget.TextView[@text=""]/ancestor::android.view.ViewGroup[1]')

    REALIZAR_PAGO_BUTTON = ('xpath', '//android.widget.TextView[@text="Realizar Pago"]')
    CONFIRMAR_PAGO_BUTTON = ('xpath', '//android.widget.TextView[@text="Confirmar Pago"]')
    FINALIZAR_BUTTON = ('xpath', '//android.widget.TextView[@text="Finalizar"]')

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def wait_quantity(self, qty, timeout=15):
        """
        Espera hasta que aparezca en pantalla el contador con el valor esperado.
        """
        xpath = f'//android.widget.TextView[@text="{qty}"]'

        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(AppiumBy.XPATH, xpath)) > 0
        )

        # pequeña estabilización por si la app refresca
        time.sleep(0.5)

    def select_table_b1(self):
        self.click(AppiumBy.XPATH, self.TABLE_B1[1])

    def select_guests(self):
        self.click(AppiumBy.XPATH, self.GUEST[1])
        time.sleep(2)

    def click_accept_guests(self):
        self.click(AppiumBy.XPATH, self.ACCEPT_GUESTS[1])

    def select_product_paella(self):
        self.click(AppiumBy.XPATH, self.PRODUCT_PAELLA[1])

    def click_add_product(self):
        self.click(AppiumBy.XPATH, self.ADD_BUTTON[1])

        # Esperar a que el contador muestre 1
        self.wait_quantity("1")

    def increase_product(self):
        # 1 -> 2
        self.click(AppiumBy.XPATH, self.CART_BUTTON[1])
        self.wait_quantity("2")

        # 2 -> 3
        self.click(AppiumBy.XPATH, self.CART_BUTTON[1])
        self.wait_quantity("3")

        print("✅ Cantidad confirmada en 3")

    def click_realizar_pago(self):
        self.click(AppiumBy.XPATH, self.REALIZAR_PAGO_BUTTON[1])

    def click_confirmar_pago(self):
        self.click(AppiumBy.XPATH, self.CONFIRMAR_PAGO_BUTTON[1])

    def click_finalizar(self):
        self.click(AppiumBy.XPATH, self.FINALIZAR_BUTTON[1])