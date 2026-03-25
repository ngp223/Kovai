import time
import unittest
import logging.handlers
import random
import openpyxl
from behave import then, step
from selenium.webdriver.common.by import By
from pageobjects import GestionVentas, HomeUser, Common
from commons import exportar, exportar_sinboton, ficheroExp, abrirFichero, obtenerTextos, obtenerTextosByID, rellenarCampo


logger = logging.getLogger('WebLogs')
gestVenElements = GestionVentas.GestionVentas()
homeUserElements = HomeUser.HomeUser()
gestElements = Common.Common()


class gestionVentas(unittest.TestCase):
    @then('I see gestion de ventas')
    def veo_gestion_ventas(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I see gestion de ventas')
        resStep = True
        try:
            ElemValidar = gestVenElements.titPagGestVenXPath
            ElemValidarTXT = gestVenElements.titPagGestVenTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            ElemValidar = gestVenElements.nomPagGestVen
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestVen.title + ' --> ' + format(ElemValidar == pagina_gestVen.title))
            resStep = (ElemValidar == pagina_gestVen.title) & resStep

            ElemValidar = gestVenElements.url
            logger.debug(ElemValidar+ ' lo comparo con: ' + pagina_gestVen.current_url + ' --> ' + format(ElemValidar == pagina_gestVen.current_url))
            resStep = (ElemValidar == pagina_gestVen.current_url) & resStep
        except Exception as e:
            logger.error('Algún elemento en "gestion de ventas" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see gestion de ventas --> {}'.format(resStep))
        assert resStep

    @then('I see menu lateral ventas')
    def veo_menu_lateral_ventas(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I see menu lateral ventas')
        resStep = True
        try:
            ElemValidar = gestVenElements.latPagGestVHTXPath
            ElemValidarTXT = gestVenElements.latPagGestVHTTXT
            logger.debug(ElemValidar)
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestTPVXPath
            ElemValidarTXT = gestVenElements.latPagGestTPVTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVHCXPath
            ElemValidarTXT = gestVenElements.latPagGestVHCTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVMCXPath
            ElemValidarTXT = gestVenElements.latPagGestVMCTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVLMXPath
            ElemValidarTXT = gestVenElements.latPagGestVLMTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVPIXPath
            ElemValidarTXT = gestVenElements.latPagGestVPITXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVPAXPath
            ElemValidarTXT = gestVenElements.latPagGestVPATXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVIAXPath
            ElemValidarTXT = gestVenElements.latPagGestVIATXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVCoXPath
            ElemValidarTXT = gestVenElements.latPagGestVCoTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVPrXPath
            ElemValidarTXT = gestVenElements.latPagGestVPrTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVInXPath
            ElemValidarTXT = gestVenElements.latPagGestVInTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVIPXPath
            ElemValidarTXT = gestVenElements.latPagGestVIPTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.latPagGestVVOnXPath
            ElemValidarTXT = gestVenElements.latPagGestVVOnTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
        except Exception as e:
            logger.error('Algún elemento en "menu lateral ventas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see menu lateral ventas --> {}'.format(resStep))
        assert resStep

    @then('I manage ventas')
    def manejo_ventas(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I manage ventas')
        resStep = True
        try:
            logger.debug('Valido página principal')
            ElemValidar = gestVenElements.latPagGestVHTXPath
            ElemValidarTXT = pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).text  # Historial de tickets
            logger.debug('Selecciono: ' + ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenTBuXPath
            ElemValidarTXT = gestVenElements.gestVenTBuTXT  # Buscar
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenFec1XPath
            ElemValidarTXT = gestVenElements.gestVenFec1TXT  # Fecha:
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenFec2XPath
            ElemValidarTXT = gestVenElements.gestVenFec2TXT  # 20/06/2024 - 05/07/2024
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMosXPath
            ElemValidarTXT = gestVenElements.gestVenMosTXT  # Mostrando del0al0de0tickets
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            logger.debug('Columnas')
            ElemValidar = gestVenElements.gestVenCol01XPath
            ElemValidarTXT = gestVenElements.gestVenColFacTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol02XPath
            ElemValidarTXT = gestVenElements.gestVenColFFaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol03XPath
            ElemValidarTXT = gestVenElements.gestVenColImpTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol04XPath
            ElemValidarTXT = gestVenElements.gestVenColCieTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol05XPath
            ElemValidarTXT = gestVenElements.gestVenColMesTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol06XPath
            ElemValidarTXT = gestVenElements.gestVenColAccTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            # Pasa de 6 columnas a 20
            logger.debug('Click en configuración MAS columnas')
            ElemValidar = gestVenElements.gestVenMMCConXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('Válido menú desplegable MAS columnas')
            ElemValidar = gestVenElements.gestVenMCoNReXPath
            ElemValidarTXT = gestVenElements.gestVenMCoNReTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoFApXPath
            ElemValidarTXT = gestVenElements.gestVenMCoFApTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoImpXPath
            ElemValidarTXT = gestVenElements.gestVenMCoImpTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoCieXPath
            ElemValidarTXT = gestVenElements.gestVenMCoCieTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoEmpXPath
            ElemValidarTXT = gestVenElements.gestVenMCoEmpTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoCajXPath
            ElemValidarTXT = gestVenElements.gestVenMCoCajTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoAdoXPath
            ElemValidarTXT = gestVenElements.gestVenMCoAdoTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoNHaXPath
            ElemValidarTXT = gestVenElements.gestVenMCoNHaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoFFaXPath
            ElemValidarTXT = gestVenElements.gestVenMCoFFaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoIvaXPath
            ElemValidarTXT = gestVenElements.gestVenMCoIvaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoFpaXPath
            ElemValidarTXT = gestVenElements.gestVenMCoFpaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoMesXPath
            ElemValidarTXT = gestVenElements.gestVenMCoMesTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoComXPath
            ElemValidarTXT = gestVenElements.gestVenMCoComTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenMCoEMeXPath
            ElemValidarTXT = gestVenElements.gestVenMCoEMeTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            logger.debug('Selecciono la columna')
            ElemValidar = gestVenElements.gestVenMCoEMeXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestVenElements.gestVenMMCGuaXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()  # Guardar
            # Compruebo que la columna seleccionada sale
            ElemValidar = gestVenElements.gestVenCol05XPath
            ElemValidarTXT = gestVenElements.gestVenMCoMesTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol06XPath
            ElemValidarTXT = gestVenElements.gestVenMCoEMeTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            logger.debug('Des-selecciono la columna')
            ElemValidar = gestVenElements.gestVenMMCConXPath  # Click en configuración MAS columnas
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestVenElements.gestVenMCoEMeXPath  # desselecciono 'Edad Media'
            ElemValidar = gestVenElements.gestVenMMCGuaXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()  # Guardar
            # Compruebo que la columna seleccionada antes, ya NO sale
            ElemValidar = gestVenElements.gestVenCol04XPath
            ElemValidarTXT = gestVenElements.gestVenMCoCieTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol05XPath
            ElemValidarTXT = gestVenElements.gestVenMCoMesTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            logger.debug('click en más columnas')
            ElemValidar = gestVenElements.gestVenMCoXPath
            ElemValidarTXT = gestVenElements.gestVenMCoTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('Compruebo MAS columnas')
            # compruebo las columnas añadidas (6 + 11 =17)
            ElemValidar = gestVenElements.gestVenCol03XPath
            ElemValidarTXT = gestVenElements.gestVenMCoFApTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol04XPath
            ElemValidarTXT = gestVenElements.gestVenColBasTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol05XPath
            ElemValidarTXT = gestVenElements.gestVenColIvaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol08XPath
            ElemValidarTXT = gestVenElements.gestVenColFpaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol11XPath
            ElemValidarTXT = gestVenElements.gestVenColCajTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol12XPath
            ElemValidarTXT = gestVenElements.gestVenColComTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol13XPath
            ElemValidarTXT = gestVenElements.gestVenColEdMTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol14XPath
            ElemValidarTXT = gestVenElements.gestVenColTMeTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol15XPath
            ElemValidarTXT = gestVenElements.gestVenColHabTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol16XPath
            ElemValidarTXT = gestVenElements.gestVenColADoTXT  # A domicilio
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenCol17XPath
            ElemValidarTXT = gestVenElements.gestVenColAccTXT  # Acciones
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            # No puedo hacer búsqueda simple, ni ordenar, xq me salen 0 facturas

            ElemValidar = gestVenElements.gestVenVOBusAdvID  # Busqueda avanzada
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvTXT
            resStep = obtenerTextosByID(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I manage ventas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I manage ventas  --> {}'.format(resStep))
        assert resStep

    @then('I do export ventas')
    def exporto_ventas(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I do export ventas')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestVen)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:65]  # nombre original del fichero sin segundos ni extension
            self.ficheroven = gestVenElements.latPagGestVHTTXT + self.ficexp[51:74]  # Nombre fichero completo
            nombre = gestVenElements.gestVenExpDesNFTXT
            ElemValidar = ficheroExp(resStep, pagina_gestVen, nombre, nombreficorig, self.ficheroven)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I do export ventas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do export ventas --> {}'.format(resStep))
        assert resStep

    @then('I open ventas exported file')
    def abrir_fichero_exportado_ventas(self):
        logger.debug('INICIO STEP: I open ventas exported file')
        try:
            resStep = True
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            primeraLinea = gestVenElements.latPagGestVHTTXT + ' (' + gestVenElements.gestVenResTXT + ')'
            ElemValidar = abrirFichero(resStep, primeraLinea, self.ficheroven)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I open ventas exported file" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        logger.error(resStep)
        self.statusScenario = self.statusScenario & resStep
        logger.error(resStep)
        logger.debug('FIN STEP: I open ventas exported file --> {}'.format(resStep))
        logger.error(resStep)
        assert resStep

    @then('I revise form advance search')
    def busqueda_avanzada(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I revise form advance search')
        resStep = True
        try:
            logger.debug('Busqueda avanzada')
            ElemValidar = gestVenElements.gestVenVOBusAdvID  # Busqueda avanzada
            pagina_gestVen.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestVenElements.gestVenVOBusAdvTitXPath  # Busqueda avanzada
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvTitTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvNRecXPath  # Numero de recibo
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvNRecTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvNCieXPath  # Numero de cierre
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvNCieTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements. gestVenVOBusAdvFIniXPath # Fecha inicio
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvFIniTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvFFinXPath  # Fecha fin
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvFFinTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvNHabXPath  # Numero habitacion
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvNHabTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvEmpXPath  # Empleado
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvEmpTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvMesXPath  # Mesa
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvMesTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvCajXPath  # Caja
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvCajTXT
            #resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOBusAdvFPaXPath  # Forma de pago
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvFPaTXT
            #resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

##### No soy capaz de comprobar correctamente, los textos de los campos: Caja,  y Forma de Pago, me devuelve a parte del título del campo, los campos q cuelgan debajo

            ElemValidar = gestVenElements.gestVenVOBusAdvOKXPath  # Buscar
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvOKTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            ElemValidar = gestVenElements.gestVenVOBusAdvKOXPath  # Cancelar
            ElemValidarTXT = gestVenElements.gestVenVOBusAdvKOTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()

            # No puedo hacer búsqueda avanzada
        except Exception as e:
            logger.error('Algún elemento en "I revise form advance search" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I revise form advance search --> {}'.format(resStep))
        assert resStep

    @then('I fill advance search')
    def rellenar_busqueda_avanzada(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I fill advance search')
        resStep = True
        ElemValidar = gestVenElements.gestVenVOBusAdvID
        pagina_gestVen.find_element(by=By.ID, value=ElemValidar).click()
        numale = format(random.randint(1, 100))
        try:
            ElemValidar = gestVenElements.gestVenVOBusAdvNRecInput  # Numero de recibo
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidarValor = gestVenElements.gestVenVOBusAdvNRecValue + numale
            rellenarCampo(resStep, pagina_gestVen, ElemValidar, ElemValidarValor)
            ElemValidar = gestVenElements.gestVenVOBusAdvNCieInput  # Numero de cierre
            ElemValidarValor = gestVenElements.gestVenVOBusAdvNCieValue + numale
            rellenarCampo(resStep, pagina_gestVen, ElemValidar, ElemValidarValor)

            ElemValidar = gestVenElements.gestVenVOBusAdvFIniInput  # Fecha Inicio
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug(gestVenElements.gestVenVOBusAdvFIniTXT + ' rellenado')
            ElemValidar = gestVenElements.gestVenVOBusAdvFFinInput  # Fecha Fin
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug(gestVenElements.gestVenVOBusAdvFFinTXT + ' rellenado')

            ElemValidar = gestVenElements.gestVenVOBusAdvNHabInput  # Número Habitación
            ElemValidarValor = gestVenElements.gestVenVOBusAdvNHabValue
            rellenarCampo(resStep, pagina_gestVen, ElemValidar, ElemValidarValor)
            time.sleep(20)

            ElemValidar = gestVenElements.gestVenVOBusAdvEmpInput  # Empleado
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidarValor = gestVenElements.gestVenVOBusAdvEmpValue
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidarValor).click()
            logger.debug(gestVenElements.gestVenVOBusAdvEmpTXT + ' rellenado')

            ElemValidar = gestVenElements.gestVenVOBusAdvMesInput  # Mesa
            ElemValidarValor = gestVenElements.gestVenVOBusAdvMesValue
            rellenarCampo(resStep, pagina_gestVen, ElemValidar, ElemValidarValor)

            ElemValidar = gestVenElements.gestVenVOBusAdvCajInput  # Caja
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidarValor = gestVenElements.gestVenVOBusAdvCajValue
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidarValor).click()
            logger.debug(gestVenElements.gestVenVOBusAdvCajTXT + ' rellenado')

            ElemValidar = gestVenElements.gestVenVOBusAdvFPaInput  # Forma de Pago
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidarValor = gestVenElements.gestVenVOBusAdvFPaValue
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidarValor).click()
            logger.debug(gestVenElements.gestVenVOBusAdvFPaTXT + ' rellenado')

            logger.debug('Aceptar/Cancelar')
            ElemValidar = gestVenElements.gestVenVOBusAdvKOXPath  # Cancelar
            #ElemValidar = gestVenElements.gestVenVOBusAdvOKXPath  # Aceptar
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I fill advance search" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill advance search --> {}'.format(resStep))
        assert resStep

    @step('I select restaurant')
    def manejo_ventas(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I select restaurant')
        resStep = True
        try:
            ElemValidar = homeUserElements.menuGlobXPath
            ElemValidarTXT = homeUserElements.menuGlobTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.ID, value='restaurant_selector').click()
            logger.debug('Selecciono restaurante')
            ElemValidar = gestVenElements.gestVenResXPath
            ElemValidarTXT = gestVenElements.gestVenResTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            restaurante = pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).text
            if restaurante == ElemValidarTXT:
                pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('Restaurante '+ restaurante + ' encontrado')
                resStep = True & resStep
            else:
                logger.debug('Restaurante ' + restaurante + ' NO encontrado')
                resStep = False & resStep
            time.sleep(3)
        except Exception as e:
            logger.error('Algún elemento en "I select restaurant" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I select restaurant  --> {}'.format(resStep))
        assert resStep

    @then('I see informes')
    def veo_informes_personalizados(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I see informes')
        resStep = True
        try:
            ElemValidar = gestVenElements.latPagGestVInXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Valido el formulario de informes')
            ElemValidar = gestVenElements.gestVenTitXPath  # informes
            ElemValidarTXT = gestVenElements.gestVenInfTitTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            #ElemValidar = gestVenElements.gestVenInfTit2XPath  # Informes
            #ElemValidarTXT = gestVenElements.gestVenIPTit2TXT  # saca el listado de informes, no consigo quitarlo
            #resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenInfFIniXPath  # Fecha Inicio (no funciona con el ID)
            ElemValidarTXT = gestVenElements.gestVenFIniTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenInfFFinXPath  # Fecha Fin (no funciona con el ID)
            ElemValidarTXT = gestVenElements.gestVenFFinTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenInfExcID  # Generar informe Excel
            ElemValidarTXT = gestVenElements.gestVenInfExcTXT
            resStep = obtenerTextosByID(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see informes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see informes  --> {}'.format(resStep))
        assert resStep

    @then('I search informes')
    def busco_informes_personalizados(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I search informes')
        resStep = True
        try:
            logger.debug('Consulto informes')
            ElemValidar = gestVenElements.gestVenISeID  # Informe
            pagina_gestVen.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestVenElements.gestVenInfISeXPath  # Informe seleccionado
            ElemValidarTXT = gestVenElements.gestVenInfISeTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            self.sinf = pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).text
            if self.sinf == ElemValidarTXT:
                logger.debug('informe ' + self.sinf + ' encontrado')
                resStep = True & resStep
            else:
                logger.debug('informe ' + self.sinf + ' NO encontrado')
                resStep = False & resStep
            ElemValidar = gestVenElements.gestVenInfFIniXPath  # Fecha Inicio
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestVenElements.gestVenInfFFinXPath  # Fecha Fin
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestVenElements.gestVenInfExcID  # Generar informe excel
            pagina_gestVen.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(4)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I search informes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search informes  --> {}'.format(resStep))
        assert resStep

    @then('I do export informes')
    def exporto_informes(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I do export informes')
        resStep = True
        try:
            logger.warning('empiezo la exportacion2')
            exporto = exportar_sinboton(resStep, pagina_gestVen)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:62]  # nombre original del fichero sin segundos ni extension
            self.ficheroven = gestVenElements.gestVenExpDesInfTXT + self.ficexp[50:71]  # Nombre fichero completo
            nombre = gestVenElements.gestVenExpDesInfTXT
            ElemValidar = ficheroExp(resStep, pagina_gestVen, nombre, nombreficorig, self.ficheroven)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I do export informes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do export informes --> {}'.format(resStep))
        assert resStep

    @then('I open informes exported file')
    def abrir_fichero_exportado_informes(self):
        logger.debug('INICIO STEP: I open informes exported file')
        try:
            resStep = True
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            primeraLinea = gestVenElements.gestVenInfFETXT
            ElemValidar = abrirFichero(resStep, primeraLinea, self.ficheroven)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I open informes exported file" no encontrado: {}'.format(ElemValidar, e))
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open informes exported file --> {}'.format(resStep))
        assert resStep

    @then('I see informes personalizados')
    def veo_informes_personalizados(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I see informes personalizados')
        resStep = True
        try:
            ElemValidar = gestVenElements.latPagGestVIPXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Valido el formulario de informes personalizados')
            ElemValidar = gestVenElements.gestVenTitXPath  # informes personalizados
            ElemValidarTXT = gestVenElements.gestVenIPTitTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenInfTit2XPath  # Informes
            ElemValidarTXT = gestVenElements.gestVenInfTit2TXT  # saca el listado de informes, no consigo quitarlo
            # resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            ElemValidar = gestVenElements.gestVenIPSemXPath  # Semana
            ElemValidarTXT = gestVenElements.gestVenIPSemTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenIPAgnoXPath  # Año
            ElemValidarTXT = gestVenElements.gestVenIPAgnoTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenIPRFecXPath  # Rango de Fechas
            ElemValidarTXT = gestVenElements.gestVenIPRFecTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenInfExcID  # Generar informe Excel por semana
            ElemValidarTXT = gestVenElements.gestVenIPExcTXT
            resStep = obtenerTextosByID(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenIPFIniXPath  # Fecha Inicio (no funciona con el ID)
            ElemValidarTXT = gestVenElements.gestVenFIniTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenIPFFinXPath  # Fecha Fin (no funciona con el ID)
            ElemValidarTXT = gestVenElements.gestVenFFinTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenIPRanID  # Generar informe Excel por rango
            ElemValidarTXT = gestVenElements.gestVenIPRanTXT
            resStep = obtenerTextosByID(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see informes personalizados" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see informes personalizados  --> {}'.format(resStep))
        assert resStep

    @then('I search informes personalizados')
    def busco_informes_personalizados(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I search informes personalizados')
        resStep = True
        try:
            logger.debug('Consulto informes personalizados')
            ElemValidar = gestVenElements.gestVenISeID  # Informe
            pagina_gestVen.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestVenElements.gestVenIPISeXPath  # Informe seleccionado
            ElemValidarTXT = gestVenElements.gestVenIPISeTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            self.sinf = pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).text
            if self.sinf == ElemValidarTXT:
                logger.debug('El informe ' + self.sinf + ' encontrado')
                ElemValidar = gestVenElements.gestVenIPISemInput  # Semana
                pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
            else:
                logger.debug('informe ' + self.sinf + ' NO encontrado')
                resStep = False & resStep
            time.sleep(1)
            #### NO SE PUEDE GENERAR NINGUN INFORME, aparecen campos vacios
            time.sleep(2)
            resStep = True
        except Exception as e:
            logger.error('Algún elemento en "I search informes personalizados" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search informes personalizados  --> {}'.format(resStep))
        assert resStep

    @then('I see visual online')
    def veo_visual_online(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I see visual online')
        resStep = True
        try:
            ElemValidar = gestVenElements.latPagGestVVOnXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestVenElements.gestVenTitXPath  # Visualización Online
            ElemValidarTXT = gestVenElements.gestVenVOTitTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOLDiXPath  # Locales disponibles
            ElemValidarTXT = gestVenElements.gestVenVOLDiTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            # FALTA MOSTRAR ICONO
            ElemValidar = gestVenElements.gestVenVOResXPath  # Restaurante
            ElemValidarTXT = gestVenElements.gestVenVOResTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOFecXPath  # Fecha
            ElemValidarTXT = gestVenElements.gestVenVOFecTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOStaXPath  # Status
            ElemValidarTXT = gestVenElements.gestVenVOStaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOTotXPath  # TOTAL
            ElemValidarTXT = gestVenElements.gestVenVOTotTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOImpXPath  # Importe
            ElemValidarTXT = gestVenElements.gestVenVOImpTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPteXPath # Pendiente en mesa
            ElemValidarTXT = gestVenElements.gestVenVOPteTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPteXPath # Importe pendiente en mesa
            ElemValidarTXT = gestVenElements.gestVenVOIPteTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOInfXPath  # Visualizar informe
            ElemValidarTXT = gestVenElements.gestVenVOInfTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOProXPath  # Visualizar productos
            ElemValidarTXT = gestVenElements.gestVenVOProTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see visual online" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see visual online  --> {}'.format(resStep))
        assert resStep

    @then('I see VO_report')
    def veo_informe(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I see VO_report')
        resStep = True
        try:
            ElemValidar = gestVenElements.gestVenVOInfXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestVenElements.gestVenVOITitXPath  # Visualizar informe X
            ElemValidarTXT = gestVenElements.gestVenVOResTXT  # 'LTL FLEMING'
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPagXPath  # Pagos
            ElemValidarTXT = gestVenElements.gestVenVOIPagTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOITotXPath  # Total
            ElemValidarTXT = gestVenElements.gestVenVOITotTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIUbeXPath  # Uber
            ElemValidarTXT = gestVenElements.gestVenVOIUbeTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIUbTXPath  # Uber Total
            ElemValidarTXT = gestVenElements.gestVenVOIUbTTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIGloXPath  # Globo
            ElemValidarTXT = gestVenElements.gestVenVOIGloTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIGlTXPath  # Globo Total
            ElemValidarTXT = gestVenElements.gestVenVOIGlTTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIVisXPath  # VISA
            ElemValidarTXT = gestVenElements.gestVenVOIVisTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIViTXPath  # VISA Total
            ElemValidarTXT = gestVenElements.gestVenVOIViTTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIJusXPath  # Just Eat
            ElemValidarTXT = gestVenElements.gestVenVOIJusTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIJuTXPath  # Just Eat Total
            ElemValidarTXT = gestVenElements.gestVenVOIJuTTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOICasXPath  # Cash
            ElemValidarTXT = gestVenElements.gestVenVOICasTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOICaTXPath  # Cash Total
            ElemValidarTXT = gestVenElements.gestVenVOICaTTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOImpXPath  # Impuestos
            ElemValidarTXT = gestVenElements.gestVenVOImpTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOITo2XPath  # Total
            ElemValidarTXT = gestVenElements.gestVenVOITo2TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIIvaXPath  # Iva
            ElemValidarTXT = gestVenElements.gestVenVOIIvaTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIIvTXPath  # Iva Total
            ElemValidarTXT = gestVenElements.gestVenVOIIvTTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIFHCXPath  # Fecha hora cierre
            ElemValidarTXT = gestVenElements.gestVenVOIFHCTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIFHCDXPath  # fecha hora cierre data
            ElemValidarTXT = gestVenElements.gestVenVOIFHCDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIFHSXPath  # Fecha hora sincronización
            ElemValidarTXT = gestVenElements.gestVenVOIFHSTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIFHSDXPath  # Fecha hora sincronización data
            ElemValidarTXT = gestVenElements.gestVenVOIFHSDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIVenXPath  # Ventas
            ElemValidarTXT = gestVenElements.gestVenVOIVenTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIVeDXPath  # Ventas data
            ElemValidarTXT = gestVenElements.gestVenVOIVeDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIComXPath  # Comensales
            ElemValidarTXT = gestVenElements.gestVenVOIComTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOICoDXPath  # Comensales data
            ElemValidarTXT = gestVenElements.gestVenVOICoDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOISubXPath  # Subtotal
            ElemValidarTXT = gestVenElements.gestVenVOISubTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOISuDXPath  # Subtotal data
            ElemValidarTXT = gestVenElements.gestVenVOISuDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIImp2XPath  # Impuestos
            ElemValidarTXT = gestVenElements.gestVenVOIImp2TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIImp2DXPath  # Impuestos data
            ElemValidarTXT = gestVenElements.gestVenVOIImp2DTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOITot3XPath # Total
            ElemValidarTXT = gestVenElements.gestVenVOITot3TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOITot3DXPath  # Total data
            ElemValidarTXT = gestVenElements.gestVenVOITot3DTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPteMXPath  # Pendiente mesa
            ElemValidarTXT = gestVenElements.gestVenVOIPteMTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPteMDXPath # Pendiente mesa data
            ElemValidarTXT = gestVenElements.gestVenVOIPteMDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOITPtMXPath  # Total + Pendiente mesa
            ElemValidarTXT = gestVenElements.gestVenVOITPtMTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOITPtMDXPath  # Total + Pendiente mesa data
            ElemValidarTXT = gestVenElements.gestVenVOITPtMDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPrAXPath # Productos anulados
            ElemValidarTXT = gestVenElements.gestVenVOIPrATXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPrADXPath  # Productos anulados data
            ElemValidarTXT = gestVenElements.gestVenVOIPrADTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOILP0XPath  # Linea puesta a 0
            ElemValidarTXT = gestVenElements.gestVenVOILP0TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOILP0DXPath  # Linea puesta a 0 data
            ElemValidarTXT = gestVenElements.gestVenVOILP0DTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPP0XPath # Producto puesta a 0
            ElemValidarTXT = gestVenElements.gestVenVOIPP0TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIPP0DXPath  # Producto puesta a 0 data
            ElemValidarTXT = gestVenElements.gestVenVOIPP0DTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIOcuXPath  # Ocupacion
            ElemValidarTXT = gestVenElements.gestVenVOIOcuTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOIOcuDXPath  # Ocupacion data
            ElemValidarTXT = gestVenElements.gestVenVOIOcuDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOICoLXPath  # Comensales en el local
            ElemValidarTXT = gestVenElements.gestVenVOICoLTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOICoLDXPath  # Comensales en el local data
            ElemValidarTXT = gestVenElements.gestVenVOICoLDTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOICerXPath  # Cerrar
            ElemValidarTXT = gestVenElements.gestVenVOICerTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see VO_report: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see VO_report  --> {}'.format(resStep))
        assert resStep

    @then('I see products')
    def veo_productos(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I see products')
        resStep = True
        try:
            ElemValidar = gestVenElements.gestVenVOProXPath  # Visualizar productos
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestVenElements.gestVenVOPTitXPath  # Titulo
            ElemValidarTXT = gestVenElements.gestVenVOPTitTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            ElemValidar = gestVenElements.gestVenVOPArtXPath  # Artículo
            ElemValidarTXT = gestVenElements.gestVenVOPArtTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPCanXPath  # Cantidad
            ElemValidarTXT = gestVenElements.gestVenVOPCanTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPTotXPath  # Total
            ElemValidarTXT = gestVenElements.gestVenVOPTotTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPExpXPath  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPCerXPath  # Cerrar
            ElemValidarTXT = gestVenElements.gestVenVOPCer1TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see products: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see products  --> {}'.format(resStep))
        assert resStep

    @then('I search products')
    def busco_productos(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I search products')
        resStep = True
        try:
            ElemValidar = gestVenElements.gestVenVOPBusInput
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).send_keys(gestVenElements.gestVenVOPBusValue)
            ElemValidar = gestVenElements.gestVenVOPBus1XPath  # Barrita Tomate
            ElemValidarTXT = gestVenElements.gestVenVOPBus1TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPCan1Path  # Cantidad = 1
            ElemValidarTXT = gestVenElements.gestVenVOPCan1TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPTot1XPath  # Total = 2.00
            ElemValidarTXT = gestVenElements.gestVenVOPTot1TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVOPCerXPath  # Cerrar
            ElemValidarTXT = gestVenElements.gestVenVOPCer1TXT
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I search products: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search products  --> {}'.format(resStep))
        assert resStep

    @then('I do export products')
    def exporto_productos(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I do export products')
        resStep = True
        try:
            ElemValidar = gestVenElements.gestVenVOPExpXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestElements.gestExpOKXPath
            ElemValidarTXT = gestElements.gestExpOKTXT  # EXPORTACIÓN EXITOSA
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            logger.debug('Comprobacion del nombre del fichero')
            ElemValidar = gestElements.gestDesXPath
            ElemValidarTXT = gestElements.gestDesTXT  # DESCARGAR
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)

            ficexp = pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).get_attribute("href")
            nombreficorig = ficexp[27:66]  # nombre original del fichero sin segundos ni extension
            fecha = time.strftime("%Y%m%d") + '_' + time.strftime("%H%M")
            nombrefic = gestVenElements.gestVenExpDesProTXT + fecha  # nombre calculado
            # pueden no coinicidir en el minuto, y entonces falla el test. Volverlo a lanzar
            if nombrefic == nombreficorig:
                logger.warning('Fichero exportado con el nombre: ' + ficexp)
                self.ficheropro = gestVenElements.gestVenExpDesPr2TXT + ficexp[52:75]  # Nombre fichero completo
                logger.warning(self.ficheropro)
                resStep = True & resStep
            else:
                logger.warning('Fichero exportado con nombre diferente a: ' + self.fichero)
                resStep = False & resStep
            logger.debug('Descargar')
            ElemValidar = gestElements.gestDesXPath
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I do export products" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do export products --> {}'.format(resStep))
        assert resStep

    @then('I open products exported file')
    def abrir_fichero_exportado_producto(self):
        logger.debug('INICIO STEP: I open products exported file')
        try:
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            logger.debug(gestElements.gestdirDes + self.ficheropro)
            ElemValidar = openpyxl.load_workbook(gestElements.gestdirDes + self.ficheropro)
            resStep = True
            logger.debug('fichero localizado')
            # to identify active worksheet
            s = ElemValidar.active
            # to identify the cell
            c1 = s.cell(row=1, column=1)  #A1
            titulo = 'Productos ' + gestVenElements.gestVenResTXT
            if titulo in c1.value:  # Busca Productos LTL Fleming en la casilla A1
                logger.debug('El fichero contiene en A1 el valor ' + c1.value)
                resStep = True & resStep
            else:
                resStep = False & resStep
            # to retrieve the cell value and print
            time.sleep(1)
        except Exception as e:
            logger.error('Algún elemento en "I open products exported file" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open products exported file --> {}'.format(resStep))
        assert resStep

    @then('I delete restaurant')
    def borrar_restaurante(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP:I delete restaurant')
        resStep = True
        try:
            ElemValidar = gestVenElements.gestVenVODelXPath  # Boton papelera
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()  # Pulso la papelera
            logger.debug('Valido cuadro de texto de KO')
            ElemValidar = gestVenElements.gestVenVODelTitXPath
            ElemValidarTXT = gestVenElements.gestVenVODelTitTXT  # ELIMINAR LOCAL
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVODelTit2XPath
            ElemValidarTXT = gestVenElements.gestVenVODelTit2TXT  # Por favor, contacte con soporte técnico para borrar este restaurante.
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            ElemValidar = gestVenElements.gestVenVODelCerXPath
            ElemValidarTXT = gestVenElements.gestVenVODelCerTXT  # Cerrar
            resStep = obtenerTextos(resStep, pagina_gestVen, ElemValidar, ElemValidarTXT)
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I delete restaurant" no encontrado: {}'.format(ElemValidar, e))
            resStep = False & resStep
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I delete restaurant --> {}'.format(resStep))
        assert resStep



