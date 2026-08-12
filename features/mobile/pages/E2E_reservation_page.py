import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReservationPage:
    VENTAS_VIEW = (AppiumBy.XPATH, "//*[contains(@text,'VENTAS')]")
    TABLE_B1 = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="B1"]')
    GUEST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("3").instance(1)')
    ACCEPT_GUESTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aceptar")')
    ARROCES_DE_AUTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Arroces de Autor")')
    PRODUCT_ARROZ_BOGAVANTE = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc,"Arroz con Bogavante")]')
    ADD_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Añadir al pedido"]/android.view.ViewGroup')
    CART_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text=""]/ancestor::android.view.ViewGroup[1]')
    REALIZAR_PAGO_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Realizar Pago"]')
    CONFIRMAR_PAGO_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Confirmar Pago"]')
    FINALIZAR_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Finalizar"]')

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, by, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))

    def click(self, by, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator))).click()

    def wait_quantity(self, qty, timeout=15):
        xpath = f'//android.widget.TextView[@text="{qty}"]'
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.find_elements(AppiumBy.XPATH, xpath)) > 0)
        time.sleep(0.5)

    def wait_product_loaded(self, timeout=40):
        end = time.time() + timeout
        while time.time() < end:
            try:
                products = self.driver.find_elements(self.PRODUCT_ARROZ_BOGAVANTE[0], self.PRODUCT_ARROZ_BOGAVANTE[1])
                if products and products[0].is_displayed():
                    return True
            except Exception:
                pass
            time.sleep(1)
        raise Exception("❌ Arroz con Bogavante no cargó")

    def select_table_b1(self):
        self.click(self.TABLE_B1[0], self.TABLE_B1[1])

    def select_guests(self):
        self.click(self.GUEST[0], self.GUEST[1])

    def click_accept_guests(self):
        self.click(self.ACCEPT_GUESTS[0], self.ACCEPT_GUESTS[1])

    def select_product_arroz_bogavante(self):
        self.click(self.ARROCES_DE_AUTOR[0], self.ARROCES_DE_AUTOR[1])
        self.wait_product_loaded()
        self.click(self.PRODUCT_ARROZ_BOGAVANTE[0], self.PRODUCT_ARROZ_BOGAVANTE[1])
        print("✅ Arroz con Bogavante seleccionado")

    def click_add_product(self):
        self.click(self.ADD_BUTTON[0], self.ADD_BUTTON[1])
        self.wait_quantity("1")

    def increase_product(self):
        self.click(self.CART_BUTTON[0], self.CART_BUTTON[1])
        self.wait_quantity("2")
        self.click(self.CART_BUTTON[0], self.CART_BUTTON[1])
        self.wait_quantity("3")
        print("✅ Cantidad confirmada en 3")

    def click_realizar_pago(self):
        self.click(self.REALIZAR_PAGO_BUTTON[0], self.REALIZAR_PAGO_BUTTON[1])

    def click_confirmar_pago(self):
        self.click(self.CONFIRMAR_PAGO_BUTTON[0], self.CONFIRMAR_PAGO_BUTTON[1])

    def click_finalizar(self):
        self.click(self.FINALIZAR_BUTTON[0], self.FINALIZAR_BUTTON[1])
