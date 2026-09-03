from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RequestsPage:
    PETICIONES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Peticiones")')
    NUEVA_PETICION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nueva Petición")')
    NOMBRE_PETICION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").text("¿Qué sucede?")')
    DESCRIPCION_PETICION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").text("Explica detalladamente tu petición...")')
    ENVIAR_PETICION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar Petición")')
    RESPUESTA_PETICION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").text("Escribe tu respuesta...")')
    ENVIAR_RESPUESTA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("")')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.peticion_creada = None
        self.respuesta_peticion = "no tiene solucion"

    def click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def acceder_peticiones(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Peticiones"))')
        self.click(self.PETICIONES)

    def crear_peticion(self):
        self.peticion_creada = f"PeticionQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(self.NUEVA_PETICION)
        nombre = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.NOMBRE_PETICION))
        nombre.send_keys(self.peticion_creada)
        self.driver.hide_keyboard()
        descripcion = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.DESCRIPCION_PETICION))
        descripcion.send_keys("Un problema en qa")
        self.driver.hide_keyboard()
        self.click(self.ENVIAR_PETICION)

    def buscar_peticion(self):
        peticion_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.peticion_creada}")')
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(peticion_locator))

    def comprobar_peticion_creada(self):
        self.acceder_peticiones()
        peticion = self.buscar_peticion()
        assert peticion.is_displayed()

    def modificar_peticion(self):
        peticion = self.buscar_peticion()
        peticion.click()
        respuesta = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.RESPUESTA_PETICION))
        respuesta.send_keys(self.respuesta_peticion)
        self.driver.hide_keyboard()
        self.click(self.ENVIAR_RESPUESTA)

    def comprobar_peticion_modificada(self):
        respuesta_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{self.respuesta_peticion}")')
        respuesta = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(respuesta_locator))
        assert respuesta.is_displayed()
