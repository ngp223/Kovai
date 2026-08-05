from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class BillingPage:

    FACTURACION=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Facturación")')
    NUEVA_FACTURA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Nueva Factura")')
    GENERAR_FACTURA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Generar Factura")')
    EMPRESA=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[1]')
    CIF=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[2]')
    DIRECCION=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[3]')
    CIUDAD=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[4]')
    CODIGO_POSTAL=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[5]')
    CONFIRMAR_FACTURA=(AppiumBy.XPATH,'//android.widget.TextView[@text="Confirmar y Emitir Factura"]')

    def __init__(self,driver):
        self.driver=driver

    def click(self,by,locator,timeout=20):
        element=WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable((by,locator)))
        element.click()

    def fill(self,by,locator,value,timeout=20):
        element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((by,locator)))
        element.clear()
        element.send_keys(value)

    def esperar_popup_fuera(self):
        try:
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("Reintentar")')))
        except:
            pass

    def open_billing(self):
        self.esperar_popup_fuera()
        self.click(*self.FACTURACION)
        self.esperar_popup_fuera()

    def abrir_nueva_factura(self):
        self.esperar_popup_fuera()
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(self.NUEVA_FACTURA))
        self.click(*self.NUEVA_FACTURA)
        WebDriverWait(self.driver,20).until(EC.invisibility_of_element_located(self.NUEVA_FACTURA))

    def seleccionar_ticket_mayor_y_generar(self):
        tickets=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textMatches("T-[0-9]+")')
        if not tickets:
            raise Exception("No se encontraron tickets T-XXXX")
        ticket_mayor=max(tickets,key=lambda x:int(re.search(r'\d+',x.text).group()))
        ticket_y=ticket_mayor.location["y"]
        botones=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Generar Factura")')
        if not botones:
            raise Exception("No se encontraron botones Generar Factura")
        boton_correcto=None
        distancia_minima=999999
        for boton in botones:
            try:
                boton_y=boton.location["y"]
                distancia=abs(boton_y-ticket_y)
                if distancia<distancia_minima:
                    distancia_minima=distancia
                    boton_correcto=boton
            except:
                continue
        if boton_correcto is None:
            raise Exception(f"No encontrado Generar Factura para {ticket_mayor.text}")
        boton_correcto.click()

    def create_new_invoice(self):
        self.abrir_nueva_factura()
        self.seleccionar_ticket_mayor_y_generar()
        self.fill(*self.EMPRESA,"Empresa QANER")
        self.fill(*self.CIF,"E46116687")
        self.fill(*self.DIRECCION,"Calle de ejemplo, 1")
        self.fill(*self.CIUDAD,"Madrid")
        self.fill(*self.CODIGO_POSTAL,"28001")
        self.click(*self.CONFIRMAR_FACTURA)
