from datetime import datetime
import time
from random import choice
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class UsersPage:
    USUARIOS=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description(", Usuarios")')
    NUEVO_USUARIO=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Nuevo Usuario")')
    NOMBRE_USUARIO=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("text-input-outlined").instance(1)')
    ROL_CAJERO=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Cajero")')
    ROL_CAMARERO=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Camarero")')
    ROL_ENCARGADO=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Encargado")')
    PIN_USUARIO=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("text-input-outlined").instance(3)')
    GUARDAR=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Guardar")')
    PAPELERA=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')

    def __init__(self,driver):
        self.driver=driver
        self.usuario_creado=None
        self.rol_creado=None

    def click(self,by,locator,timeout=15):
        element=WebDriverWait(self.driver,timeout).until(lambda d:d.find_element(by,locator))
        element.click()
        return element

    def acceder_usuarios(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description(", Usuarios"))')
        self.click(*self.USUARIOS)
        time.sleep(1)

    def crear_usuario(self):
        self.usuario_creado = f"UsuarioQA{datetime.now().strftime('%d%m%Y%H%M%S')}"
        self.click(*self.NUEVO_USUARIO)
        nombre = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.NOMBRE_USUARIO))
        nombre.click()
        nombre.send_keys(self.usuario_creado)
        self.driver.hide_keyboard()
        roles = [("Cajero", self.ROL_CAJERO), ("Camarero", self.ROL_CAMARERO), ("Encargado", self.ROL_ENCARGADO)]
        self.rol_creado, rol_locator = choice(roles)
        self.click(*rol_locator)
        pin = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.PIN_USUARIO))
        pin.click()
        self.driver.hide_keyboard()
        pin.send_keys("1234")
        #self.click(*self.GUARDAR) como no lo encuentra uso..
        self.driver.press_keycode(61)
        self.driver.press_keycode(61)
        self.driver.press_keycode(66)
        time.sleep(2)

    def esperar_usuario_creado(self):
        usuario_locator=(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.usuario_creado}")')
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(usuario_locator))

    def eliminar_usuario(self):
        usuario_locator=(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.usuario_creado}")')
        def buscar_y_eliminar(driver):
            try:
                usuario=driver.find_element(*usuario_locator)
                usuario_pos=usuario.location
                papeleras=driver.find_elements(*self.PAPELERA)
                if not papeleras:
                    return False
                papelera_correcta=None
                distancia_minima=999999
                for papelera in papeleras:
                    try:
                        papelera_pos=papelera.location
                        distancia=abs(papelera_pos["y"]-usuario_pos["y"])
                        if distancia<distancia_minima:
                            distancia_minima=distancia
                            papelera_correcta=papelera
                    except StaleElementReferenceException:
                        continue
                if papelera_correcta is None:
                    return False
                papelera_correcta.click()
                return True
            except StaleElementReferenceException:
                return False
        WebDriverWait(self.driver,15,poll_frequency=0.3).until(buscar_y_eliminar)
        time.sleep(1)

    def comprobar_usuario_no_aparece(self):
        usuario_locator=(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("{self.usuario_creado}")')
        WebDriverWait(self.driver,15).until(EC.invisibility_of_element_located(usuario_locator))