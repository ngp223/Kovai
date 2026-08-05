from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TablesMapPage:

    TABLESMAP=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Mapa de mesas")')
    GESTIONAR_TARIFAS=(AppiumBy.XPATH,'//android.widget.TextView[@text="Gestionar Tarifas"]')
    CREAR_NUEVA_TARIFA=(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc=", Crear Nueva Tarifa"]')
    NOMBRE_TARIFA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("text-input-outlined").instance(0)')
    PRECIO_TARIFA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("text-input-outlined").instance(1)')
    GUARDAR=(AppiumBy.XPATH,'//android.widget.TextView[@text="Guardar"]')
    CERRAR_TARIFA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
    NUEVA_ZONA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("+ Nueva")')
    NOMBRE_ZONA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("text-input-outlined")')
    CREAR_ZONA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description(", Crear Zona")')
    ELIMINAR_ZONA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Eliminar")')
    EDITAR_TARIFA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
    ELIMINAR_TARIFA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Eliminar Tarifa")')

    def __init__(self,driver):
        self.driver=driver
        self.tarifa_creada=None
        self.zona_creada=None

    def click(self,by,locator,timeout=15):
        element=WebDriverWait(self.driver,timeout).until(lambda d:d.find_element(by,locator))
        element.click()

    def fill(self,by,locator,value,timeout=15):
        element=WebDriverWait(self.driver,timeout).until(lambda d:d.find_element(by,locator))
        element.click()
        element.send_keys(value)

    def open_tablemap(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Mapa de mesas"))')
        self.click(*self.TABLESMAP)

    def crear_tarifa(self):
        self.tarifa_creada=f"TarifaQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(*self.GESTIONAR_TARIFAS)
        self.click(*self.CREAR_NUEVA_TARIFA)
        self.driver.find_element(*self.NOMBRE_TARIFA).send_keys(self.tarifa_creada)
        self.driver.find_element(*self.PRECIO_TARIFA).send_keys("3.33")
        self.click(*self.GUARDAR)
        self.click(*self.CERRAR_TARIFA)

    def crear_zona(self):
        self.zona_creada=f"ZonaQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(*self.NUEVA_ZONA)
        self.driver.find_element(*self.NOMBRE_ZONA).send_keys(self.zona_creada)
        self.click(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.tarifa_creada}")')
        self.driver.orientation="PORTRAIT"
        self.click(*self.CREAR_ZONA)
        
    def borrar_zona(self):
        self.driver.orientation="LANDSCAPE"
        zona=WebDriverWait(self.driver,30).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.zona_creada}")')))
        zona_pos=zona.location
        botones=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
        if not botones:
            raise Exception("No se encontraron botones de tres puntos")
        boton_correcto=None
        distancia_minima=999999
        for boton in botones:
            try:
                boton_pos=boton.location
                distancia=abs(boton_pos["y"]-zona_pos["y"])
                if distancia<distancia_minima:
                    distancia_minima=distancia
                    boton_correcto=boton
            except:
                continue
        if boton_correcto is None:
            raise Exception(f"No encontrado boton borrar zona {self.zona_creada}")
        boton_correcto.click()
        self.click(*self.ELIMINAR_ZONA)
        WebDriverWait(self.driver,30).until(EC.invisibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.zona_creada}")')))

    def borrar_tarifa(self):
        self.driver.orientation = "LANDSCAPE"
        self.click(*self.GESTIONAR_TARIFAS)
        tarifa = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.tarifa_creada}")')))
        tarifa_pos = tarifa.location
        botones = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
        if not botones:
            raise Exception("No se encontraron lápices")
        boton_correcto = None
        distancia_minima = 999999
        for boton in botones:
            try:
                boton_pos = boton.location
                distancia = abs(boton_pos["y"] - tarifa_pos["y"])
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    boton_correcto = boton
            except:
                continue
        if boton_correcto is None:
            raise Exception(f"No encontrado lapiz tarifa {self.tarifa_creada}")
        boton_correcto.click()
        self.click(*self.ELIMINAR_TARIFA)
        self.click(*self.CERRAR_TARIFA)
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.tarifa_creada}")')))
