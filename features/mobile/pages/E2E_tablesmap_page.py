from datetime import datetime
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

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
    RECTANGULAR=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Rectangular")')
    ELIMINAR=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Eliminar")')
    ELIMINAR_MESA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("✕")')

    def __init__(self,driver):
        self.driver=driver
        self.tarifa_creada=None
        self.zona_creada=None
        self.mesa_creada=None
        self.mesa_creada_numero=None
        self.mesa_creada_elemento=None
        self.mesa_location=None
        self.mesa_size=None

    def click(self,by,locator,timeout=15):
        element=WebDriverWait(self.driver,timeout).until(lambda d:d.find_element(by,locator))
        element.click()
        return element

    def open_tablesmap(self):
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

    def seleccionar_zona_creada(self):
        zona_locator=(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.zona_creada}")')
        def buscar_y_clickar(driver):
            try:
                zona=driver.find_element(*zona_locator)
                zona.click()
                return True
            except StaleElementReferenceException:
                return False
        WebDriverWait(self.driver,30,poll_frequency=0.3).until(buscar_y_clickar)
        time.sleep(1)

    def crear_mesa(self):
        self.driver.orientation="LANDSCAPE"
        self.click(*self.RECTANGULAR)
        self.mesa_creada_numero=1
        self.mesa_creada=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("1")')
        mesa=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.mesa_creada))
        self.mesa_creada_elemento=mesa
        self.mesa_location=mesa.location
        self.mesa_size=mesa.size
        print(f"✅ Mesa {self.mesa_creada_numero} creada y localizada")

    def esperar_mesa_creada(self):
        mesa=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.mesa_creada))
        self.mesa_creada_elemento=mesa
        self.mesa_location=mesa.location
        self.mesa_size=mesa.size
        print(f"✅ Mesa {self.mesa_creada_numero} visible en el mapa")

    def mover_mesa_creada(self):
        mesa=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.mesa_creada))
        location=mesa.location
        size=mesa.size
        start_x=int(location["x"]+size["width"]/2)
        start_y=int(location["y"]+size["height"]/2)
        end_x=start_x+150
        end_y=start_y+100
        self.driver.execute_script("mobile: dragGesture",{"startX":start_x,"startY":start_y,"endX":end_x,"endY":end_y,"duration":1000})
        time.sleep(2)
        mesa_nueva=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.mesa_creada))
        nueva_location=mesa_nueva.location
        if nueva_location["x"]==location["x"] and nueva_location["y"]==location["y"]:
            raise Exception(f"❌ La mesa {self.mesa_creada_numero} no se ha movido")
        self.mesa_creada_elemento=mesa_nueva
        self.mesa_location=nueva_location
        self.mesa_size=mesa_nueva.size
        print(f"✅ Mesa {self.mesa_creada_numero} movida de {location} a {nueva_location}")

    def borrar_mesa(self):
        mesa=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(self.mesa_creada))
        mesa.click()
        time.sleep(1)
        self.click(*self.ELIMINAR_MESA)
        time.sleep(1)

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
            except Exception:
                continue
        if boton_correcto is None:
            raise Exception(f"No encontrado boton borrar zona {self.zona_creada}")
        boton_correcto.click()
        self.click(*self.ELIMINAR_ZONA)
        WebDriverWait(self.driver,30).until(EC.invisibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.zona_creada}")')))

    def borrar_tarifa(self):
        self.driver.orientation="LANDSCAPE"
        self.click(*self.GESTIONAR_TARIFAS)
        tarifa=WebDriverWait(self.driver,30).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.tarifa_creada}")')))
        tarifa_pos=tarifa.location
        botones=self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')
        if not botones:
            raise Exception("No se encontraron lápices")
        boton_correcto=None
        distancia_minima=999999
        for boton in botones:
            try:
                boton_pos=boton.location
                distancia=abs(boton_pos["y"]-tarifa_pos["y"])
                if distancia<distancia_minima:
                    distancia_minima=distancia
                    boton_correcto=boton
            except Exception:
                continue
        if boton_correcto is None:
            raise Exception(f"No encontrado lapiz tarifa {self.tarifa_creada}")
        boton_correcto.click()
        self.click(*self.ELIMINAR_TARIFA)
        self.click(*self.CERRAR_TARIFA)
        WebDriverWait(self.driver,30).until(EC.invisibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.tarifa_creada}")')))