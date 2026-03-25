import time
import openpyxl
import unittest
import random
import logging.handlers
from behave import then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobjects import GestionUsuarios, HomeUser, Common
from commons import obtenerTextos, obtenerTextosByID, rellenarCampo, crear_rol, exportar, ficheroExp,abrirFichero


logger = logging.getLogger('WebLogs')
gestUsuElements = GestionUsuarios.GestionUsuarios()
gestElements = Common.Common()


class gestionUsuarios(unittest.TestCase):

    @then('I see gestion de usuarios')
    def see_gestion_usuarios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I see gestion de usuarios')
        resStep = True
        try:
            ElemValidar = gestUsuElements.titPagGestUsuXPath
            ElemValidarTXT = gestUsuElements.titPagGestUsuTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)

            ElemValidar = gestUsuElements.nomPagGestUsu
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestUsu.title + ' --> ' + format(ElemValidar == pagina_gestUsu.title))
            resStep = (ElemValidar == pagina_gestUsu.title) & resStep

            ElemValidar = gestUsuElements.url
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestUsu.current_url + ' --> ' + format(ElemValidar == pagina_gestUsu.current_url))
            resStep = (ElemValidar == pagina_gestUsu.current_url) & resStep

            ElemValidar = gestUsuElements.gestUsuBusXPath
            ElemValidarTXT = gestUsuElements.gestUsuBusTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuMosXPath
            ElemValidarTXT = gestUsuElements.gestUsuMosTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            logger.debug('Mostrando')
            ElemValidar = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).text
            resStep = (ElemValidar == gestUsuElements.gestUsuMosTXT) & resStep

            ElemValidar = gestElements.gestExpID  ## Botón Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)

            ElemValidar = gestUsuElements.gestUsuNUsID  ## Botón dar de Alta
            ElemValidarTXT = gestUsuElements.gestUsuNUsTXT
            resStep = obtenerTextosByID(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)

            logger.debug('Compruebo las columnas de Gestion de Usuarios')
            ElemValidar = gestUsuElements.gestUsuColNyAXPath
            ElemValidarTXT = gestUsuElements.gestUsuColNyATXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColUsuXPath
            ElemValidarTXT = gestUsuElements.gestUsuColUsuTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColRolXPath
            ElemValidarTXT = gestUsuElements.gestUsuColRolTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColResXPath
            ElemValidarTXT = gestUsuElements.gestUsuColResTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColEstXPath
            ElemValidarTXT = gestUsuElements.gestUsuColEstTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColAccXPath
            ElemValidarTXT = gestUsuElements.gestUsuColAccTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuEliXPath
            ElemValidarTXT = gestUsuElements.gestUsuEliTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            resStep = True & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "gestion de usuarios" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see gestion de usuarios --> {}'.format(resStep))
        assert resStep

    @then('I see menu lateral usuarios')
    def see_menu_lateral_usuarios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I see menu lateral usuarios')
        resStep = True
        try:
            ElemValidar = gestUsuElements.latPagGestUUsXPath
            ElemValidarTXT = gestUsuElements.latPagGestUUsTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "menu lateral usuarios" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see menu lateral usuarios --> {}'.format(resStep))
        assert resStep

    @then('I see menu lateral roles')
    def see_menu_lateral_usuarios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I see menu lateral roles')
        resStep = True
        try:
            ElemValidar = gestUsuElements.latPagGestURoXPath
            ElemValidarTXT = gestUsuElements.latPagGestURoTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "menu lateral roles" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see menu lateral roles --> {}'.format(resStep))
        assert resStep

    @then('I validate the form new user')
    def dar_de_alta_usuarios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I validate the form new user')
        resStep = True
        try:
            logger.debug('Pulsar Dar de alta')
            ElemValidar = gestUsuElements.gestUsuNUsID
            pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestUsuElements.gestUsuNUTitXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUTitTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNUNyAXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUNyATXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNUNusXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUNusTXT  # Nombre de usuario
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNUResXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUResTXT  # Restaurante
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURolXPath
            ElemValidarTXT = gestUsuElements.gestUsuNURolTXT  # Rol
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)

            # Desplegable de rol
            ElemValidar = gestUsuElements.gestUsuNURoXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestUsuElements.gestUsuNURo1XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo1TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo2XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo2TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo3XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo3TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo4XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo4TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo5XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo5TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo6XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo6TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo7XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo7TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo8XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo8TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo9XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo9TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo10XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo10TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo11XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo11TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo12XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo12TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo13XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo13TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo14XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo14TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo15XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo15TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo16XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo16TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo17XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo17TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo18XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo18TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            # Avanzo el desplegable
            ElemValidar = gestUsuElements.gestUsuNURoXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).send_keys(Keys.PAGE_DOWN)
            ElemValidar = gestUsuElements.gestUsuNURo19XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo19TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURo20XPath
            ElemValidarTXT = gestUsuElements.gestUsuNURo20TXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNUTESXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUTESTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNUConXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUConTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNURCoXPath
            ElemValidarTXT = gestUsuElements.gestUsuNURCoTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuNUSCoXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUSCoTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I validate the form new user" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I validate the form new user --> {}'.format(resStep))
        assert resStep

    @then('I fill in the mandatory fields in the form new user')
    def dar_de_alta_usuarios_campos_obligatorios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I fill in the mandatory fields in the form new user')
        resStep = True
        ElemValidar = gestUsuElements.gestUsuNUsID
        pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
        time.sleep(2)
        numale = format(random.randint(1, 100))
        time.sleep(2)
        try:
            logger.debug('Rellenar usuario')
            ElemValidar = gestUsuElements.gestUsuNUsNyAInput  # Nombre y Apellido
            ElemValidarValor = gestUsuElements.gestUsuNUsNyAValor + numale
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
            self.newuser = ElemValidarValor
            logger.debug(self.newuser)
            ElemValidar = gestUsuElements.gestUsuNUsUsuInput  # Usuario
            ElemValidarValor = gestUsuElements.gestUsuNUsNyAValor + numale + '@es.es'
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
            logger.debug('Restaurante')
            ElemValidar = gestUsuElements.gestUsuNUsResMen  # Menú Restaurante
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuNUsResSel  # Restaurante seleccionado
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuNUsRolInput # retorno a cuestionario
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)

            logger.debug('Rol')
            ElemValidar = gestUsuElements.gestUsuNUsRolInput  # Menu Rol
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar= gestUsuElements.gestUsuNUsRolValor # Rol seleccionado
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)

            logger.debug('Contraseña')
            ElemValidar = gestUsuElements.gestUsuNUsPWDInput  # Contraseña
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidarValor = gestUsuElements.gestUsuNUsPWDValor
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
            ElemValidar = gestUsuElements.gestUsuNUsPWD2Input # Repetir contraseña
            ElemValidarValor = gestUsuElements.gestUsuNUsPWD2Valor
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)

            logger.debug('Botón dar de Alta - Aceptar')
            ElemValidar = gestUsuElements.gestUsuNUsOKXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUsOKTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            Aceptar = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar)
            logger.debug('Botón dar de Alta - Cancelar')
            ElemValidar = gestUsuElements.gestUsuNUsKOXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUsKOTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            Cancelar = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar)
            logger.debug('Aceptar/Cancelar')
            Aceptar.click()
            time.sleep(1)
            resStep = True & resStep
            #Cancelar.click()
        except Exception as e:
            logger.error('Algún elemento en "I fill in the mandatory fields in the form new user" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill in the mandatory fields in the form new user --> {}'.format(resStep))
        assert resStep

    @then('I fill in the form new user')
    def dar_de_alta_usuarios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I fill in the form new user')
        resStep = True
        ElemValidar = gestUsuElements.gestUsuNUsID
        pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
        time.sleep(1)
        numale = format(random.randint(1, 100))
        try:
            logger.debug('Rellenar usuario')
            ElemValidar = gestUsuElements.gestUsuNUsNyAInput  # Nombre y Apellido
            ElemValidarValor = gestUsuElements.gestUsuNUsNyAValor + numale
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
            self.newuser = ElemValidarValor
            logger.debug(self.newuser)
            ElemValidar = gestUsuElements.gestUsuNUsUsuInput  # Usuario
            ElemValidarValor = gestUsuElements.gestUsuNUsNyAValor + numale + '@es.es'
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
            logger.debug('Restaurante')
            ElemValidar = gestUsuElements.gestUsuNUsResMen  # Menú Restaurante
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            logger.debug('Restaurante - Expandir todo')
            ElemValidar = gestUsuElements.gestUsuNUsExp
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuNUsResSel  # Restaurante seleccionado
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            logger.debug('Restaurante - Contraer todo')
            ElemValidar = gestUsuElements.gestUsuNUsCon
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuNUsRolInput  # retorno a cuestionario
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)

            logger.debug('Rol')
            ElemValidar = gestUsuElements.gestUsuNUsRolInput  # Menu Rol
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuNUsRolValor  # Rol seleccionado
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)

            logger.debug('SIN_Contraseña')
            ElemValidar = gestUsuElements.gestUsuNUSCCoXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            logger.debug('CON_Contraseña')
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)

            logger.debug('Contraseña')
            ElemValidar = gestUsuElements.gestUsuNUsPWDInput  # Contraseña
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidarValor = gestUsuElements.gestUsuNUsPWDValor
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
            ElemValidar = gestUsuElements.gestUsuNUsPWD2Input # Repetir contraseña
            ElemValidarValor = gestUsuElements.gestUsuNUsPWD2Valor
            rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)

            logger.debug('Envío correo recordar contraseña')
            ElemValidar = gestUsuElements.gestUsuNUECoXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)

            logger.debug('Botón dar de Alta - Aceptar')
            ElemValidar = gestUsuElements.gestUsuNUsOKXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUsOKTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            Aceptar = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar)
            logger.debug('Botón dar de Alta - Cancelar')
            ElemValidar = gestUsuElements.gestUsuNUsKOXPath
            ElemValidarTXT = gestUsuElements.gestUsuNUsKOTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            Cancelar = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar)
            logger.debug('Aceptar/Cancelar')
            Aceptar.click()
            time.sleep(1)
            #Cancelar.click()
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I fill in the form new user" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill in the form new user --> {}'.format(resStep))
        assert resStep

    @then('I manage usuarios')
    def manejo_usuarios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I manage usuarios')
        resStep = True
        try:
            logger.debug('Ordenar columnas')
            ElemValidar = gestUsuElements.gestUsuCol1elXPath
            ElemValidarTXT = gestUsuElements.gestUsuCol1elTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColUelXPath
            ElemValidarTXT = gestUsuElements.gestUsuColUelTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.XPATH, value='//*[@id="userlist-table"]/table/thead/tr[1]/th[1]/div/span').click()
            time.sleep(1)
            logger.debug('cambio de orden')
            ElemValidar = gestUsuElements.gestUsuColUelXPath
            ElemValidarTXT = gestUsuElements.gestUsuCol1elTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuCol1elXPath
            ElemValidarTXT = gestUsuElements.gestUsuColUelTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)

            logger.debug('Mostrar usuarios eliminados')
            ElemValidar = gestUsuElements.gestUsuEliXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            # no sale ningún usuario eliminado
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I manage usuarios" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I manage usuarios --> {}'.format(resStep))
        assert resStep


    @then('I search a user')
    def buscar_usuario(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I search a user')
        resStep = True
        try:
            logger.debug('Realizo la búsqueda del usuario')
            ElemValidar = gestUsuElements.gestUsuBusXPath
            ElemValidarTXT = gestUsuElements.gestUsuBusTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            buscar = pagina_gestUsu.find_element(by=By.XPATH, value='//*[@id="userlist-action"]/div[1]/div/input')
            buscar.send_keys(gestUsuElements.gestUsuPalTXT)
            buscar.click()
            time.sleep(1)
            logger.debug('Compruebo q todas las líneas tienen la palabra buscada')
            ElemValidar = gestUsuElements.gestUsuRes1XPath
            textobuscado1 = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).text
            logger.debug(textobuscado1)
            if gestUsuElements.gestUsuPalTXT in textobuscado1:
                logger.debug('resultado 1 --> OK')
                resStep = True & resStep
            else:
                resStep = False & resStep
            time.sleep(1)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I search a user" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search a user --> {}'.format(resStep))
        assert resStep

    @then('I export user')
    def exporto_usuario(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I do export user')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestUsu)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:69]  # nombre original del fichero sin segundos ni extension
            self.ficherousu = gestUsuElements.nomPagGestUsu + self.ficexp[55:78]  # Nombre fichero completo
            nombre = gestUsuElements.gestUsuExpDesNFTXT
            ElemValidar = ficheroExp(resStep, pagina_gestUsu, nombre, nombreficorig, self.ficherousu)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export user" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export user --> {}'.format(resStep))
        assert resStep

    @then('I open user exported file')
    def abrir_fichero_exportado_usuarios(self):
        logger.debug('INICIO STEP: I open user exported file')
        resStep = True
        try:
            resStep = True
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            primeraLinea = gestUsuElements.nomPagGestUsu + ' (Global)'
            ElemValidar = abrirFichero(resStep, primeraLinea, self.ficherousu)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I open user exported file" no encontrado: {}'.format(ElemValidar, e))
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open user exported file --> {}'.format(resStep))
        assert resStep

    @then('I edit a user')
    def editar_usuario(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I edit a user')
        resStep = True
        try:
            logger.debug('ACCIONES - EDITAR')
            # ElemValidarTXT = gestUsuElements.gestUsuOpEdiTXT
            # FALTA VALIDAR EL ALERT 'EDIT' QUE SALE AL PASAR POR ENCIMA EL RATÓN

            ElemValidar = gestUsuElements.gestUsuOpEdiXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuNUsXPath
            self.user = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).text
            if self.user == self.newuser:
                logger.debug('ACCIONES - EDITAR -- Cancelar Edición')
                ElemValidar = gestUsuElements.gestUsuEdiTitXPath
                ElemValidarTXT = gestUsuElements.gestUsuEdiTitTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuEdiKOXPath
                ElemValidarTXT = gestUsuElements.gestUsuEdiKOTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Cancelar
                time.sleep(2)

                logger.debug('ACCIONES - EDITAR -- Deshabilitar usuario')
                ElemValidar = gestUsuElements.gestUsuOpEdiXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestUsuElements.gestUsuEdiUsDXPath  # Deshabilitar usuario
                ElemValidarTXT = gestUsuElements.gestUsuEdiUsDTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuEdiOKXPath  # Aceptar
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(4)


                logger.error('ACCIONES - COMPROBAR usuario deshabilitado --> no se puede')
                # Los botones de ESTADO o ACCIONES con .text no devuelven ningún valor

                logger.debug('ACCIONES - EDITAR -- Habilitar usuario')
                ElemValidar = gestUsuElements.gestUsuOpEdiXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
                ElemValidar = gestUsuElements.gestUsuEdiUsDXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # usuario Habilitado
                ElemValidar = gestUsuElements.gestUsuEdiOKXPath
                time.sleep(1)
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Aceptar
                time.sleep(3)

                logger.error('ACCIONES - COMPROBAR usuario habilitado --> no se puede')
                # Los botones de ESTADO o ACCIONES con .text no devuelven ningún valor

                logger.debug('ACCIONES - EDITAR -- Modificar campo: Nombre y Apellidos')
                ElemValidar = gestUsuElements.gestUsuOpEdiXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuEdiNyAXPath
                ElemValidarTXT = gestUsuElements.gestUsuEdiNyATXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)  # Nombre y Apellidos
                ElemValidar = gestUsuElements.gestUsuEdiNyAInput  # Nombre y Apellido
                ElemValidarValor = gestUsuElements.gestUsuEdiNyAValor
                rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
                self.newuser = ElemValidarValor
                logger.debug('Comprobar campo: Nombre de usuario')
                ElemValidar = gestUsuElements.gestUsuEdiNUsXPath
                ElemValidarTXT = gestUsuElements.gestUsuEdiNUsTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar,
                                        ElemValidarTXT)  # Nombre de usuario (email)
                ElemValidar = gestUsuElements.gestUsuEdiOKXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Aceptar
                time.sleep(3)

                logger.debug(' ACCIONES - EDITAR -- Añadir Restaurante y expandir')
                ElemValidar = gestUsuElements.gestUsuOpEdiXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuEdiResInput
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
                ElemValidar = gestUsuElements.gestUsuEdiExpXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Expandir
                ElemValidar = gestUsuElements.gestUsuEdiResSel  # Restaurante seleccionado
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(5)
                ElemValidar = gestUsuElements.gestUsuEdiConXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Contraer
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuEdiOKXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Aceptar
                time.sleep(3)

                logger.debug(' ACCIONES - EDITAR -- Quitar Restaurante')
                ElemValidar = gestUsuElements.gestUsuOpEdiXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuEdiResInput
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuEdiExpXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Expandir
                ElemValidar = gestUsuElements.gestUsuEdiResSel  # Restaurante seleccionado
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuEdiOKXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Aceptar
                time.sleep(3)

                logger.debug('ACCIONES - EDITAR -- Modificar campo: Rol')
                ElemValidar = gestUsuElements.gestUsuOpEdiXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
                ElemValidar = gestUsuElements.gestUsuEdiRolInput  # Menu Rol
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
                ElemValidar = gestUsuElements.gestUsuEdiRolSel  # Rol seleccionado
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
                ElemValidar = gestUsuElements.gestUsuEdiOKXPath
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Aceptar
                time.sleep(3)
                resStep = True & resStep
            else:
                logger.debug('Usuario ' + self.newuser + ' no encontrado')
                resStep = False & resStep
        except Exception as e:
            logger.error('Algún elemento en "I edit a user" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I edit a user --> {}'.format(resStep))
        assert resStep


    @then('I delete user')
    def eliminar_usuario(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I delete user')
        resStep = True
        try:
            ElemValidar = gestUsuElements.gestUsuOpDelXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            self.user = pagina_gestUsu.find_element(by=By.XPATH, value=gestUsuElements.gestUsuNUsXPath).text
            if self.user == self.newuser:
                ElemValidar = gestUsuElements.gestUsuOpDelTitXPath  # BAJA DE USUARIO
                ElemValidarTXT = gestUsuElements.gestUsuOpDelTitTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuOpDelTi2XPath  # ¿Está seguro que desea dar de baja al usuario?
                ElemValidarTXT = gestUsuElements.gestUsuOpDelTi2TXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuOpDelKOXPath  # Cancelar borrado de usuario mandatory
                ElemValidarTXT = gestUsuElements.gestUsuOpDelKOTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuOpDelOKXPath  # Aceptar borrado de usuario mandatory
                ElemValidarTXT = gestUsuElements.gestUsuOpDelOKTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.debug('Usuario ' + self.newuser + ' no encontrado')
                resStep = False & resStep
            time.sleep(1)
        except Exception as e:
            logger.error('Algún elemento en "I delete user" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I delete user --> {}'.format(resStep))
        assert resStep

    @step('I click roles')
    def see_menu_lateral_roles(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I click roles')
        resStep = True
        try:
            ElemValidar = gestUsuElements.latPagGestURoXPath
            ElemValidarTXT = gestUsuElements.latPagGestURoTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
        except Exception as e:
            logger.error('Algún elemento en "I click roles" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click roles --> {}'.format(resStep))
        assert resStep

    @step('I see roles')
    def see_roles(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP:I see roles')
        resStep = True
        try:
            logger.debug('Valido página roles')
            ElemValidar = gestUsuElements.gestUsuRoltitXPath
            ElemValidarTXT = gestUsuElements.gestUsuRoltitTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuRolCreID
            ElemValidarTXT = gestUsuElements.gestUsuRolCreTXT
            resStep = obtenerTextosByID(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColSRolXPath
            ElemValidarTXT = gestUsuElements.gestUsuColSRolTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColPerXPath
            ElemValidarTXT = gestUsuElements.gestUsuColPerTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColAcnXPath
            ElemValidarTXT = gestUsuElements.gestUsuColAcnTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuColAcsXPath
            ElemValidarTXT = gestUsuElements.gestUsuColAcsTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see roles" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see roles --> {}'.format(resStep))
        assert resStep

    @then('I create a rol')
    def create_rol(self):
        pagina_gestUsu = self.driver
        resStep = True
        try:
            logger.debug('INICIO STEP:I create a rol')
            crearrol = crear_rol(resStep, pagina_gestUsu)
            self.rol = crearrol[0]
            time.sleep(2)
            logger.debug('I see new role')
            ElemValidar = gestUsuElements.gestUsuNewRolXPath
            self.rolcre = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).text
            if self.rol == self.rolcre:
                logger.debug('El rol creado es ' + self.rol)
            else:
                logger.debug('El rol NO se ha creado')
            ElemValidarTXT = self.rol
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I create a rol" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create a rol --> {}'.format(resStep))
        assert resStep

    @then('I rename a rol')
    def rename_rol(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP:I renombro un rol')
        resStep = True
        try:
            logger.debug('Selecciono rol')
            ElemValidar = gestUsuElements.gestUsuNewRolXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuRolRenID   # opción RENOMBRAR
            ElemValidarTXT = gestUsuElements.gestUsuRolRenTXT
            resStep = obtenerTextosByID(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestUsuElements.gestUsuRolRenTitleXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolRenTitleTXT   #'RENOMBRAR'
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuRolRenNomXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolRenNomTXT  # 'Nombre*'
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            self.rolren = gestUsuElements.gestUsuCreRolNomValor + '_renombrado'
            ElemValidar = gestUsuElements.gestUsuRolRenInput
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).send_keys(self.rolren)
            ElemValidar = gestUsuElements.gestUsuRolRenNomKOXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolRenNomKOTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            #pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click() # Cancelar renombrar
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuRolRenNomOKXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolRenNomOKTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Aceptar renombrar
            time.sleep(5)
            # pagina_gestUsu.refresh()  # refresco la pagina
            ElemValidar = gestUsuElements.gestUsuNewRolrenXPath
            ElemValidarTXT = self.rolren
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I rename a rol" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I rename a rol --> {}'.format(resStep))
        assert resStep

    @then('I delete a rol')
    def delete_rol(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP:I delete a rol')
        pagina_gestUsu.refresh()  # refresco la pagina
        time.sleep(5)
        resStep = True
        try:
            logger.debug('Selecciono rol')
            ElemValidar = gestUsuElements.gestUsuNewRolrenXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuRolDelID
            ElemValidarTXT = gestUsuElements.gestUsuRolDelTXT
            resStep = obtenerTextosByID(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)  # opción ELIMINAR
            pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuRolDelTitleXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolDelTitleTXT  # 'ELIMINAR rol'
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuRolDelTextXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolDelTextTXT  # 'Texto'
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuRolDelNomKOXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolDelNomKOTXT  # Cancelar
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            #pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Cancelar eliminar rol
            ElemValidar = gestUsuElements.gestUsuRolDelNomOKXPath
            ElemValidarTXT = gestUsuElements.gestUsuRolDelNomOKTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()  # Aceptar eliminar rol
            time.sleep(2)
            logger.debug('Valido que el nuevo rol ha sido eliminado y consulto el último')
            ElemValidar = gestUsuElements.gestUsuRolSelXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestUsuElements.gestUsuNewRolXPath
            rolant = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidarTXT = rolant  # rol anterior
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I delete a rol" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I delete a rol --> {}'.format(resStep))
        assert resStep

    @then('I add permission to a rol')
    def add_per(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP:I add permission to a rol')
        resStep = True
        try:
            logger.debug('Selecciono rol')
            ElemValidar = gestUsuElements.gestUsuNewRolXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            srol = pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).text
            if srol == self.rol:
                logger.debug(srol)
                logger.debug(self.rol)
                time.sleep(2)
                logger.debug('Validar página principal Roles, con Rol seleccionado')
                ElemValidar = gestUsuElements.gestUsuMLRSFPXPath  # Filtrar permisos
                ElemValidarTXT = gestUsuElements.gestUsuMLRSFPTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuMLRSFPInput
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).send_keys(
                    gestUsuElements.gestUsuMLRSFPValor)  # filtro por S
                ElemValidar = gestUsuElements.gestUsuMLRSPerID  # Permiso
                pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
                ElemValidar = gestUsuElements.gestUsuMLRSPerValor  # Permiso seleccionado
                ElemValidarTXT = gestUsuElements.gestUsuMLRSPerTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestUsuElements.gestUsuMLRSAccID  # Acción
                pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
                ElemValidar = gestUsuElements.gestUsuMLRSAccValor  # acción: Lectura
                ElemValidarTXT = gestUsuElements.gestUsuMLRSAccTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()

                ElemValidar = gestUsuElements.gestUsuMLRSAPInput  # Añadir permiso
                ElemValidarTXT = gestUsuElements.gestUsuMLRSAPTXT
                #resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                logger.error('no consigo validar el texto de "Añadir permiso')
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestUsuElements.gestUsuMLRSGuaXPath  # Guardar cambios
                ElemValidarTXT = gestUsuElements.gestUsuMLRSGuaTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuMLRSGuaID
                pagina_gestUsu.find_element(by=By.ID, value=ElemValidar).click()
                ElemValidar = gestUsuElements.gestUsuMLRSMRoTitXPath  # validar ventaja emergente
                ElemValidarTXT = gestUsuElements.gestUsuMLRSMRoTitTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuMLRSMRoTexXPath
                ElemValidarTXT = gestUsuElements.gestUsuMLRSMRoTexTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuMLRSMRoCanXPath  # cancelar ventana emergente
                ElemValidarTXT = gestUsuElements.gestUsuMLRSMRoCanTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuMLRSMRoModXPath  # aceptar ventana emergente
                ElemValidarTXT = gestUsuElements.gestUsuMLRSMRoModTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                # cancelar ventana emergente
                # pagina_gestUsu.find_element(by=By.XPATH, value=gestUsuElements.gestUsuMLRSMRoCanXPath).click()
                # aceptar ventana emergente
                pagina_gestUsu.find_element(by=By.XPATH, value=gestUsuElements.gestUsuMLRSMRoModXPath).click()
                time.sleep(1)
                resStep = True & resStep
            else:
                logger.debug('Rol ' + self.rol + ' no encontrado')
                resStep = False & resStep
            time.sleep(1)
        except Exception as e:
            logger.error('Algún elemento en "I add permission to a rol" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I add permission to a rol --> {}'.format(resStep))
        assert resStep

    @then('I valid permission added')
    def see_roles(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP:I valid permission added')
        resStep = True
        pagina_gestUsu.refresh()  # refresco la pagina
        time.sleep(5)
        try:
            logger.debug('Selecciono rol')
            ElemValidar = gestUsuElements.gestUsuNewRolrenXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            ElemValidar = gestUsuElements.gestUsuMLRSPAXPath  # Rol seleccionado, permiso añadido
            ElemValidarTXT = gestUsuElements.gestUsuMLRSPerTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)

            ElemValidar = gestUsuElements.gestUsuMLRSPAAXPath    # Rol seleccionado, acción del permiso añadido
            ElemValidarTXT = gestUsuElements.gestUsuMLRSAccTXT
            resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
            ElemValidar = gestUsuElements.gestUsuMLRSPAEXPath  # Eliminar Permiso añadido al rol
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I valid permission added')
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid permission added --> {}'.format(resStep))
        assert resStep

    @then('I change password')
    def cambiar_contraseña_usuario(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I change password')
        resStep = True
        try:
            ElemValidar = gestUsuElements.gestUsuOpCPWDXPath
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            self.user = pagina_gestUsu.find_element(by=By.XPATH, value=gestUsuElements.gestUsuNUsXPath).text
            if self.user == self.newuser:
                ElemValidar = gestUsuElements.gestUsuCPWDTitXPath
                ElemValidarTXT = gestUsuElements.gestUsuCPWDTitTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuOpCPWDConXPath
                ElemValidarTXT = gestUsuElements.gestUsuOpCPWDConTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuOpCPWDRCoXPath
                ElemValidarTXT = gestUsuElements.gestUsuOpCPWDRCoTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuCPWDOKXPath
                ElemValidarTXT = gestUsuElements.gestUsuCPWDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuCPWDKOXPath
                ElemValidarTXT = gestUsuElements.gestUsuCPWDKOTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                ElemValidar = gestUsuElements.gestUsuOpCPWDConInput  # Contraseña
                ElemValidarValor = gestUsuElements.gestUsuOpCPWDConValor
                rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarValor)
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuOpCPWDRCoInput  # Repetir contraseña
                ElemValidarTXT = gestUsuElements.gestUsuOpCPWDRCoValor
                rellenarCampo(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                time.sleep(2)
                ElemValidar = gestUsuElements.gestUsuCPWDOKXPath
                ElemValidarTXT = gestUsuElements.gestUsuCPWDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestUsu, ElemValidar, ElemValidarTXT)
                pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
                resStep = True & resStep
            else:
                logger.debug('Usuario ' + self.newuser + ' no encontrado')
                resStep = False & resStep
        except Exception as e:
            logger.error('Algún elemento en "I change password" no encontrado: {}'.format(ElemValidar, e))
            resStep = False

        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I change password --> {}'.format(resStep))
        assert resStep

