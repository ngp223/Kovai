from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CardsPage:

    CARTAS=(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc=", Cartas"]')
    ANADIR_CARTA=(AppiumBy.XPATH,'//android.widget.TextView[@text="Añadir Carta"]')
    NOMBRE_CARTA=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[2]')
    REFERENCIA=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[3]')
    DESCRIPCION=(AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="text-input-outlined"])[4]')
    SIGUIENTE=(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Siguiente"]/android.view.ViewGroup')
    FINALIZAR_Y_GUARDAR=(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Finalizar y Guardar"]/android.view.ViewGroup')
    PAPELERA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(0)')

    def __init__(self,driver):
        self.driver=driver
        self.carta_creada=None

    def click(self,by,locator,timeout=15):
        element=WebDriverWait(self.driver,timeout).until(lambda d:d.find_element(by,locator))
        element.click()

    def fill(self,by,locator,value,timeout=15):
        element=WebDriverWait(self.driver,timeout).until(lambda d:d.find_element(by,locator))
        element.clear()
        element.send_keys(value)

    def open_cards(self):
        self.click(*self.CARTAS)

    def create_new_card(self):
        self.carta_creada=f"Carta QA {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.click(*self.ANADIR_CARTA)
        self.fill(*self.NOMBRE_CARTA,self.carta_creada)
        self.fill(*self.REFERENCIA,"ReferenciaQA")
        self.fill(*self.DESCRIPCION,"Carta del equipo de QA")
        self.click(*self.SIGUIENTE)
        self.click(*self.SIGUIENTE)
        self.click(*self.SIGUIENTE)
        self.click(*self.FINALIZAR_Y_GUARDAR)

    def delete_created_card(self):
        carta=WebDriverWait(self.driver,30).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.carta_creada}")')))
        carta_pos=carta.location
        papeleras=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
        if not papeleras:
            raise Exception("No se encontraron papeleras")
        papelera_correcta=None
        distancia_minima=999999
        for papelera in papeleras:
            try:
                papelera_pos=papelera.location
                distancia=abs(papelera_pos["y"]-carta_pos["y"])
                if distancia<distancia_minima:
                    distancia_minima=distancia
                    papelera_correcta=papelera
            except:
                continue
        if papelera_correcta is None:
            raise Exception(f"No encontrada papelera para {self.carta_creada}")
        papelera_correcta.click()
        eliminar=WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description(", Eliminar")')))
        eliminar.click()
