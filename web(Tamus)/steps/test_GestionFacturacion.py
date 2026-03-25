import time
import unittest
import logging.handlers
import openpyxl
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import GestionFacturacion, Common
from commons import obtenerTextos, obtenerTextosByID, rellenarCampo, obtenerParteCampo, columnas_GF
from commons import abrirFichero,exportar, ficheroExp, avanzar_pagina, retroceder_pagina

logger = logging.getLogger('WebLogs')
gestFacElements = GestionFacturacion.GestionFacturacion()
gestElements = Common.Common()


class gestionFacturacion(unittest.TestCase):

    @then('I see gestion de facturacion')
    def see_gestion_facturacion(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I see gestion de facturacion')
        resStep = True
        try:
            ElemValidar = gestFacElements.titPagGestFacXPath
            ElemValidarTXT = gestFacElements.titPagGestFacTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)

            ElemValidar = gestFacElements.nomPagGestFac
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestFac.title + ' --> ' + format(ElemValidar == pagina_gestFac.title))
            resStep = (ElemValidar == pagina_gestFac.title) & resStep

            ElemValidar = gestFacElements.url
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestFac.current_url + ' --> ' + format(ElemValidar == pagina_gestFac.current_url))
            resStep = (ElemValidar == pagina_gestFac.current_url) & resStep
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "ggestFacElements.urlestion de facturacion" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see gestion de facturacion --> {}'.format(resStep))
        assert resStep

    @then('I see menu lateral facturacion')
    def see_menu_lateral_facturacion(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I see menu lateral facturacion')
        resStep = True
        try:
            ElemValidar = gestFacElements.latPagGestFClXPath
            ElemValidarTXT = gestFacElements.latPagGestFClTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.latPagGestFFaXPath
            ElemValidarTXT = gestFacElements.latPagGestFFaTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.latPagGestFFSXPath
            ElemValidarTXT = gestFacElements.latPagGestFFSTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.latPagGestFFCXPath
            ElemValidarTXT = gestFacElements.latPagGestFFCTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.latPagGestFFJXPath
            ElemValidarTXT = gestFacElements.latPagGestFFJTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.latPagGestFFRXPath
            ElemValidarTXT = gestFacElements.latPagGestFFRTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.latPagGestFFPXPath
            ElemValidarTXT = gestFacElements.latPagGestFFPTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.latPagGestFFEXPath
            ElemValidarTXT = gestFacElements.latPagGestFFETXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "menu lateral facturacion" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see menu lateral facturacion --> {}'.format(resStep))
        assert resStep

    @then('I manage facturacion')
    def manejo_facturacion(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I manage facturacion')
        resStep = True
        try:
            # Comprobación cabecera
            logger.debug('LISTADO DE CLIENTES')
            ElemValidar = gestFacElements.titPagGestFacXPath
            ElemValidarTXT = gestFacElements.titPagGestFacTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)

            logger.debug('Botón Exportar')
            ElemValidar = gestElements.gestExpID
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)

            logger.debug('Botón nuevo cliente')
            ElemValidar = gestFacElements.gestFacNclID
            ElemValidarTXT = gestFacElements.gestFacNclTXT
            resStep = obtenerTextosByID(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            logger.debug(resStep)
            # Comprobación buscar y resultados
            logger.debug('Ordenar columnas, primero filtro en Facturación')
            buscar = pagina_gestFac.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/input')
            buscar.send_keys(gestFacElements.gestFacPalTXT)  # palabra a buscar 'bloom'
            buscar.click()
            ElemValidar = gestFacElements.gestFacResXPath  # Mostrando..
            ElemValidarTXT = gestFacElements.gestFacResTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacCol1elXPath  # Primer valor
            ElemValidarTXT = gestFacElements.gestFacCol1elTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacColUelXPath  # Ultimo valor
            ElemValidarTXT = gestFacElements.gestFacColUelTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            logger.debug(resStep)
            logger.debug('ordenar por la segunda columna')
            pagina_gestFac.find_element(by=By.XPATH, value=gestFacElements.gestFacMCo2XPath).click()
            ElemValidar = gestFacElements.gestFacColUelXPath # el último valor es el primero
            ElemValidarTXT = gestFacElements.gestFacCol1elTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacCol1elXPath  # el primer valor es el último
            ElemValidarTXT = gestFacElements.gestFacColUelTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            columnas_GF(resStep, pagina_gestFac)  # Comprobar 6 columnas
            logger.debug(resStep)

            logger.debug('desactivar columnas y guardar')
            ElemValidar = gestFacElements.gestFacMMCConXPath
            time.sleep(2)
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()  # Mostrar más columnas
            time.sleep(2)
            ElemValidar = gestFacElements.gestFacMMCNomXPath
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()  # Desactivar nombre
            time.sleep(2)
            ElemValidar = gestFacElements.gestFacMMCGuaXPath
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()  # Guardar
            time.sleep(2)
            logger.debug('comprobamos que no se muestra la columna deshabilitada "nombre')
            logger.debug('5 columnas')
            ElemValidar = gestFacElements.gestFacMCo1XPath
            ElemValidarTXT = gestFacElements.gestFacMCoNIFTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo2XPath
            ElemValidarTXT = gestFacElements.gestFacMCoEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo3XPath
            ElemValidarTXT = gestFacElements.gestFacMCoTelTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo4XPath
            ElemValidarTXT = gestFacElements.gestFacMCoCiuTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo5XPath
            ElemValidarTXT = gestFacElements.gestFacMCoAccTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            logger.debug(resStep)

            logger.debug('Activar columnas y cancelar')
            ElemValidar = gestFacElements.gestFacMMCConXPath
            time.sleep(2)
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()  # Mostrar más columnas
            time.sleep(2)
            ElemValidar = gestFacElements.gestFacMMCNomXPath
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()  # Activar columna nombre
            time.sleep(2)
            ElemValidar = gestFacElements.gestFacMMCCanXPath
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()  # Cancelar
            time.sleep(2)
            logger.debug('comprobamos que no se muestra la columna habilitada y cancelada la operación')
            logger.debug('5 columnas')
            ElemValidar = gestFacElements.gestFacMCo1XPath
            ElemValidarTXT = gestFacElements.gestFacMCoNIFTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo2XPath
            ElemValidarTXT = gestFacElements.gestFacMCoEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo3XPath
            ElemValidarTXT = gestFacElements.gestFacMCoTelTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo4XPath
            ElemValidarTXT = gestFacElements.gestFacMCoCiuTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo5XPath
            ElemValidarTXT = gestFacElements.gestFacMCoAccTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            logger.debug('Mostrar más columnas')
            ElemValidar = gestFacElements.gestFacMCoXPath
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()
            # Pasa de 5 columnas a 9
            logger.debug('Compruebo MAS columnas')
            ElemValidar = gestFacElements.gestFacMCo1XPath
            ElemValidarTXT = gestFacElements.gestFacMCoNIFTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo2XPath
            ElemValidarTXT = gestFacElements.gestFacMCoNomTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo3XPath
            ElemValidarTXT = gestFacElements.gestFacMCoEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo4XPath
            ElemValidarTXT = gestFacElements.gestFacMCoTelTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo5XPath
            ElemValidarTXT = gestFacElements.gestFacMCoDirTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo6XPath
            ElemValidarTXT = gestFacElements.gestFacMCoCiuTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo7XPath
            ElemValidarTXT = gestFacElements.gestFacMCoProTXT  # Provincia
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo8XPath
            ElemValidarTXT = gestFacElements.gestFacMCoCPTXT # Código postal
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo9XPath
            ElemValidarTXT = gestFacElements.gestFacMCoPaiTXT # País
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacMCo10XPath
            ElemValidarTXT = gestFacElements.gestFacMCoAccTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I manage facturacion" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I manage facturacion --> {}'.format(resStep))
        assert resStep

    @then('I validate the form new client')
    def validar_formulario_nuevo_cliente(self):
        pagina_gestFac = self.driver
        ElemValidar = gestFacElements.gestFacNclID
        pagina_gestFac.find_element(by=By.ID, value=ElemValidar).click()
        time.sleep(2)
        logger.debug('INICIO STEP:I validate the form new client')
        resStep = True
        try:
            logger.debug('Valido el formulario de nuevo cliente')
            ElemValidar = gestFacElements.gestFacNCFTitXPath
            ElemValidarTXT = gestFacElements.gestFacNCFTitTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFNomXPath
            ElemValidarTXT = gestFacElements.gestFacNCFNomTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFNIFXPath
            ElemValidarTXT = gestFacElements.gestFacNCFNIFTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFTelXPath
            ElemValidarTXT = gestFacElements.gestFacNCFTelTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFEmaXPath
            ElemValidarTXT = gestFacElements.gestFacNCFEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFDirXPath
            ElemValidarTXT = gestFacElements.gestFacNCFDirTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFCiuXPath
            ElemValidarTXT = gestFacElements.gestFacNCFCiuTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFProXPath  # Provincia
            ElemValidarTXT = gestFacElements.gestFacNCFProTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFCPXPath
            ElemValidarTXT = gestFacElements.gestFacNCFCPTXT  # Código postal
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFPaiXPath
            ElemValidarTXT = gestFacElements.gestFacNCFPaiTXT  # País
            ini= 0
            fin= 6
            resStep = obtenerParteCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestFacElements.gestFacNCFConXPath
            ElemValidarTXT = gestFacElements.gestFacNCFConTXT  # Contabilidad
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFOKXPath
            ElemValidarTXT = gestFacElements.gestFacNCFOKTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacNCFKOXPath
            ElemValidarTXT = gestFacElements.gestFacNCFKOTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            resStep = True & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I validate the form new client" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I validate the form new client --> {}'.format(resStep))
        assert resStep

    @then('I fill in the mandatory fields in the form new client')
    def rellenar_cliente_nuevo(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I fill in the mandatory fields in the form new client')
        resStep = True
        try:
            logger.debug('Relleno formulario nuevo cliente')
            ElemValidar = gestFacElements.gestFacNclID
            pagina_gestFac.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestFacElements.gestFacNCFNomInput  # nombre
            ElemValidarValor = gestFacElements.gestFacNCFNomValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFNIFInput  # cif/nif
            ElemValidarValor = gestFacElements.gestFacNCFNIFValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFDirInput  # direccion
            ElemValidarValor = gestFacElements.gestFacNCFDirValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFCiuInput  # ciudad
            ElemValidarValor = gestFacElements.gestFacNCFCiuValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFProInput  # provincia
            ElemValidarValor = gestFacElements.gestFacNCFProValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFCPInput  # codigo postal
            ElemValidarValor = gestFacElements.gestFacNCFCPValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFSePXPath  # seleccionar país
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestFacElements.gestFacNCFPaiInput   # pais Alemania
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I fill in the mandatory fields in the form new client" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill in the mandatory fields in the form new client --> {}'.format(resStep))
        assert resStep

    @then('I fill in rest of fields in the form new client')
    def rellenar_resto_campos_cliente_nuevo(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I fill in rest of fields in the form new client')
        resStep = True
        try:
            logger.debug('Relleno el resto de campos no obligatorios')
            ElemValidar = gestFacElements.gestFacNCFEmaInput  # email
            ElemValidarValor = gestFacElements.gestFacNCFEmaValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFTelInput  # teléfono
            ElemValidarValor = gestFacElements.gestFacNCFTelValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            ElemValidar = gestFacElements.gestFacNCFConInput  # contabilidad
            ElemValidarValor = gestFacElements.gestFacNCFConValor
            rellenarCampo(resStep, pagina_gestFac, ElemValidar, ElemValidarValor)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I fill in rest of fields in the form new client" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill in rest of fields in the form new client --> {}'.format(resStep))
        assert resStep

    @then('I save the new client')
    def guardar_nuevo_cliente(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP:WIP')
        resStep = True
        try:
            logger.debug('Guardar cliente')
            ElemValidar = gestFacElements.gestFacNCFOKXPath # Aceptar
            # ElemValidar = gestFacElements.gestFacNCFKOXPath  # Cancelar
            Aceptar = pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).text
            logger.debug(Aceptar)
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I save the new client" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I save the new client --> {}'.format(resStep))
        assert resStep

    @then('I search and delete the new client')
    def buscaryborrar_nuevo_cliente(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP:I search and delete the new client')
        resStep = True
        try:
            logger.debug('Busco y borro el nuevo cliente')
            buscar = pagina_gestFac.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/input')
            buscar.send_keys(gestFacElements.gestFacNCFNIFValor)  # busco por cif
            buscar.click()
            ElemValidar = '//*[@id="clients-table"]/table/tbody/tr[1]/td[6]/i[2]'   # pulso borrar
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = '//*[@id="deleteClientModal"]/div/form/div[3]/button[2]'  # aceptar
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I search and delete the new client" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete the new client --> {}'.format(resStep))
        assert resStep

    @then('I search a client')
    def buscar_client(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I search a client')
        resStep = True
        try:
            logger.debug('Realizo una búsqueda')
            ElemValidar = gestFacElements.gestFacBusXPath
            ElemValidarTXT = gestFacElements.gestFacBusTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            buscar = pagina_gestFac.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/input')
            buscar.send_keys(gestFacElements.gestFacPalTXT)  # palabra a buscar 'bloom'
            buscar.click()
            logger.debug('Compruebo q todas las líneas tienen la palabra buscada ' + gestFacElements.gestFacPalTXT)
            ElemValidar = gestFacElements.gestFacRes1XPath
            textobuscado1 = pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).text.lower()
            ElemValidar = gestFacElements.gestFacRes2XPath
            textobuscado2 = pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).text.lower()
            if gestFacElements.gestFacPalTXT in textobuscado1:
                logger.debug('resultado 1 --> OK')
                if gestFacElements.gestFacPalTXT in textobuscado2:
                    logger.debug('resultado 2 --> OK')
                    resStep = True & resStep
            else:
                resStep = False & resStep
            columnas_GF(resStep, pagina_gestFac)  # Comprobar 6 columnas
            logger.debug('compruebo número de items')
            ElemValidar = gestFacElements.gestFacIt1XPAth
            ElemValidarTXT = gestFacElements.gestFacIt1TXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            ElemValidar = gestFacElements.gestFacItnXPAth
            ElemValidarTXT = gestFacElements.gestFacItnTXT
            resStep = obtenerTextos(resStep, pagina_gestFac, ElemValidar, ElemValidarTXT)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I search a client" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        logger.debug(resStep)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search a client --> {}'.format(resStep))
        assert resStep

    @then('I advance page facturacion')
    def avanzar_pagina(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I advance page')
        resStep = True
        try:
            logger.debug('Pulso avanzar')
            Pg1 = gestFacElements.gestFacPg1XPath
            Pg1TXT = gestFacElements.gestFacPg1TXT
            Mos = gestFacElements.gestFacMosXPath
            AvP = gestFacElements.gestFacAvPXPath
            MP1 = gestFacElements.gestFacMP1TXT
            MP2 = gestFacElements.gestFacMP2TXT
            MP3 = gestFacElements.gestFacMP3TXT
            MP4 = gestFacElements.gestFacMP4TXT
            MP5 = gestFacElements.gestFacMP5TXT
            ElemValidar = avanzar_pagina(resStep, pagina_gestFac, Pg1, Pg1TXT, Mos, AvP, MP1, MP2, MP3, MP4, MP5)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I advance page" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I advance page --> {}'.format(resStep))
        assert resStep

    @then('I turn back page facturacion')
    def retroceder_pagina(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I turn back page')
        resStep = True
        try:
            logger.debug('Pulso retroceder')
            Pg5 = gestFacElements.gestFacPg5XPath
            Pg5TXT = gestFacElements.gestFacPg5TXT
            Mos = gestFacElements.gestFacMosXPath
            ReP = gestFacElements.gestFacRePXPath
            MP1 = gestFacElements.gestFacMP1TXT
            MP2 = gestFacElements.gestFacMP2TXT
            MP3 = gestFacElements.gestFacMP3TXT
            MP4 = gestFacElements.gestFacMP4TXT
            MP5 = gestFacElements.gestFacMP5TXT
            ElemValidar = retroceder_pagina(resStep, pagina_gestFac, Pg5, Pg5TXT, Mos, ReP, MP1, MP2, MP3, MP4,MP5)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I turn back page" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I turn back page --> {}'.format(resStep))
        assert resStep

    @then('I export clients')
    def exporto_clientes(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I do export clients')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestFac)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:64]  # nombre original del fichero sin segundos ni extension
            self.ficherocli = gestFacElements.gestFacExpDesLisTXT + self.ficexp[50:73]  # Nombre fichero completo
            nombre = gestFacElements.gestFacExpDesNFTXT
            ElemValidar = ficheroExp(resStep, pagina_gestFac, nombre, nombreficorig, self.ficherocli)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export clients" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export clients --> {}'.format(resStep))
        assert resStep

    @then('I open clients file')
    def abrir_fichero_exportado_clientes(self):
        logger.debug('INICIO STEP: I open clients file ')
        try:
            resStep = True
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            primeraLinea = gestFacElements.gestFacExpDesLisTXT + ' (GRUPO DE RESTAURACIÓN LATERAL, S.L.)'
            ElemValidar = abrirFichero(resStep, primeraLinea, self.ficherocli)
            resStep = ElemValidar & resStep
        except Exception as e:
            logger.error('Algún elemento en "I open clients file" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open clients file --> {}'.format(resStep))
        assert resStep
