import time
import openpyxl
import unittest
import logging.handlers
from behave import then,step,when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects import GestionAlmacen, Common
from commons import obtenerTextos, obtenerTextosByID, rellenarCampo, columnas_GA, obtenerParteCampo
from commons import abrirFichero,exportar, ficheroExp, avanzar_pagina, retroceder_pagina,deshabilitar_nueva_ventana_edge

logger = logging.getLogger('WebLogs')
gestAlmElements = GestionAlmacen.GestionAlmacen()
gestElements = Common.Common()


class gestionAlmacen(unittest.TestCase):
    @then('I see gestion de almacen')
    def see_gestion_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see gestion de almacen')
        resStep = True
        try:
            ElemValidar = gestAlmElements.titPagGestAlmXPath
            ElemValidarTXT = gestAlmElements.titPagGestAlmTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.nomPagGestAlm
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestAlm.title + ' --> ' + format(ElemValidar == pagina_gestAlm.title))
            resStep = (ElemValidar == pagina_gestAlm.title) & resStep
            ElemValidar = gestAlmElements.url
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestAlm.current_url + ' --> ' + format(ElemValidar== pagina_gestAlm.current_url))
            resStep = (ElemValidar == pagina_gestAlm.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
            ElemValidar = gestAlmElements.gestAlmMosProvXPath
            ElemValidar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.debug(ElemValidar + ' lo comparo con: ' + gestAlmElements.gestAlmMos1TXT + ' --> ' + format(ElemValidar == gestAlmElements.gestAlmMos1TXT))
            resStep = (ElemValidar == gestAlmElements.gestAlmMos1TXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see gestion de almacen" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see gestion de almacen --> {}'.format(resStep))
        assert resStep

    @then('I see menu lateral de almacen')
    def veo_menu_lateral_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see menu lateral de almacen')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestProvXPath # Proveedores
            ElemValidarTXT = gestElements.gestProv3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestLPrXPath  # Listado de proveedores
            ElemValidarTXT = gestAlmElements.gestAlmExpFMPProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestFPrXPath  # Facturas de proveedor
            ElemValidarTXT = gestAlmElements.latPagGestFPrTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMPrXPath  # Productos de proveedor
            ElemValidarTXT = gestAlmElements.latPagGestMPrTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMCaXPath  # Catálogos
            ElemValidarTXT = gestAlmElements.gestAlmCatTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMInXPath  # Ingredientes
            ElemValidarTXT = gestAlmElements.gestAlmIng2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMCateXPath  # Categorías
            ElemValidarTXT = gestAlmElements.latPagGestMCateTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMUnXPath # Unidades
            ElemValidarTXT = gestElements.gestUni2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMerXPath # latPagGestMerTXT
            ElemValidarTXT = gestAlmElements.latPagGestMerTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMeAXPath # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMeIXPath # Inventario
            ElemValidarTXT = gestAlmElements.latPagGestMeITXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMeTXPath # Traspasos y Salidas
            ElemValidarTXT = gestAlmElements.latPagGestMeTTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestMeDXPath # Descuadres
            ElemValidarTXT = gestAlmElements.latPagGestMeDTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestPedXPath # Pedidos
            ElemValidarTXT = gestAlmElements.latPagGestPedTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestPePXPath # Pedidos a proveedor
            ElemValidarTXT = gestAlmElements.latPagGestPePTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestPAEXPath # Albarán de entrada
            ElemValidarTXT = gestAlmElements.latPagGestPAETXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestPeCXPath # Pedidos de cliente
            ElemValidarTXT = gestAlmElements.latPagGestPeCTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestPASXPath # Albarán de salida
            ElemValidarTXT = gestAlmElements.latPagGestPASTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestCEXPath # Compras externas
            ElemValidarTXT = gestAlmElements.latPagGestCETXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestRecXPath # Receta
            ElemValidarTXT = gestAlmElements.latPagGestRecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestReCXPath # Recetas de carta
            ElemValidarTXT = gestAlmElements.latPagGestReCTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestReEXPath # Escandallos
            ElemValidarTXT = gestAlmElements.latPagGestReETXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestReSXPath # Subrecetas
            ElemValidarTXT = gestAlmElements.gestAlmSRec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestRCoXPath # Combos
            ElemValidarTXT = gestAlmElements.latPagGestRCoTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestReMXPath # Modificadores
            ElemValidarTXT = gestAlmElements.latPagGestReMTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestInCXPath # Informes de compra
            ElemValidarTXT = gestAlmElements.latPagGestInCTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.latPagGestInSXPath # Informes de stock
            ElemValidarTXT = gestAlmElements.latPagGestInSTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see menu lateral de almacen" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see menu lateral de almacen --> {}'.format(resStep))
        assert resStep

    @then('I manage almacen')
    def manejo_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I manage almacen')
        resStep = True
        try:
            logger.debug('Botón nuevo proveedor')
            ElemValidar = gestAlmElements.gestAlmNProvID
            ElemValidarTXT = gestAlmElements.gestAlmNProvTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT)  & resStep

            logger.debug('Botón Exportar')
            ElemValidar = gestElements.gestExpID
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT)  & resStep

            logger.debug('Columnas y cambiar orden en la primera columna')
            ElemValidar = gestAlmElements.gestAlmBusProInput
            buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscar.send_keys(gestAlmElements.gestAlmBusPalTXT) # Busco: HIGIENE
            buscar.click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmCol1elXPath
            ElemValidarTXT = gestAlmElements.gestAlmCol1elTXT # ADIS HIGIENE S.L.
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmRes3XPath
            ElemValidarTXT = gestAlmElements.gestAlmColUelTXT # ZAMBU-HIGIENE SL
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Cambio orden')
            ElemValidar = gestAlmElements.gestAlmMCo2XPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmRes3XPath  #último elemento, el primero
            ElemValidarTXT = gestAlmElements.gestAlmCol1elTXT # ADIS HIGIENE S.L.
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmCol1elXPath  #primer elemento, el último
            ElemValidarTXT = gestAlmElements.gestAlmColUelTXT # ZAMBU-HIGIENE SL
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Marcar más columnas')
            ElemValidar = gestAlmElements.gestAlmMCoXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Compruebo MAS columnas, q son 16')
            ElemValidar = gestAlmElements.gestAlmMCo1XPath # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo2XPath # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo3XPath # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo4XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoCIFTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo5XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoTelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo6XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoTe2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo7XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoTe3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo8XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo9XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoEm2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo10XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoEmCTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo11XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoEmPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo12XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoPeMTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo13XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoDTOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo14XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoRapTXT # Rappel
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo15XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoIntTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo16XPath # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Desactivo mostrar más columnas vuelvo a 8')
            ElemValidar = gestAlmElements.gestAlmMCoXPath
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            columnas_GA(resStep, pagina_gestAlm)

            logger.debug('Activar columnas "telefono" y guardar')
            ElemValidar = gestAlmElements.gestAlmMCoConXPath
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMCoSelXPath  # Teléfono 2
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarTXT = gestAlmElements.gestAlmMCoSelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMCoOKXPath  # Guardo cambio
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('Compruebo las 8 columnas más la activada "Teléfono2"')
            ElemValidar = gestAlmElements.gestAlmMCo1XPath # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo2XPath
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo3XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoCIFTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo4XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoTelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo5XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoTe2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo6XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo7XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoDTOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo8XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoRapTXT # Rappel
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo9XPath
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Desactivar columnas "Teléfono 2" y guardar')
            ElemValidar= gestAlmElements.gestAlmMCoConXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoSelXPath # Teléfono 2
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMCoOKXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Compruebo las 8 columnas')
            columnas_GA(resStep, pagina_gestAlm)

            logger.debug('Desactivar columna Rappel y guardar')
            ElemValidar = gestAlmElements.gestAlmMCoConXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoDesXPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoDesTXT # Rappel
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoOKXPath
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Compruebo las 7 columnas, sin Rappel')
            ElemValidar = gestAlmElements.gestAlmMCo1XPath # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo2XPath
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo3XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoCIFTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo4XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoTelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo5XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo6XPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoDTOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCo7XPath
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Activo Rappel y guardo')
            ElemValidar = gestAlmElements.gestAlmMCoConXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoDesXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMCoOKXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Compruebo las 8 columnas')
            columnas_GA(resStep, pagina_gestAlm)

            logger.debug('Activar columnas y cancelar')
            ElemValidar = gestAlmElements.gestAlmMCoConXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoSelXPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoSelTXT # Teléfono 2'
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoKOXPath
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Compruebo las 8 columnas sin cambios')
            columnas_GA(resStep, pagina_gestAlm)

            logger.debug('Desactivar columnas y cancelar')
            ElemValidar = gestAlmElements.gestAlmMCoConXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoDesXPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoDesTXT # Rappel
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoKOXPath
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Comrpuebo las 8 columnas sin cambios')
            columnas_GA(resStep, pagina_gestAlm)

            logger.debug('Activar columnas y cancelar')
            ElemValidar = gestAlmElements.gestAlmMCoConXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoSelXPath
            ElemValidarTXT = gestAlmElements.gestAlmMCoSelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMCoKOXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Compruebo las 8 columnas sin cambios')
            columnas_GA(resStep, pagina_gestAlm)
        except Exception as e:
            logger.error('Algún elemento en "I manage almacen" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I manage almacen --> {}'.format(resStep))
        assert resStep

    @then('I validate the form new provider')
    def valido_formulario_nuevo_proveedor(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I validate the form new provider')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmNProvID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.titPagGestAlmXPath  # cabecera, LISTADO DE PROVEEDORES
            ElemValidarTXT = gestAlmElements.titPagGestAlmTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestVolverListID  # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPGuaID  # Guardar
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPRefXPath  # Referencia*
            ElemValidarTXT = gestElements.gestReferencia1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPCifXPath # CIF
            ElemValidarTXT = gestAlmElements.gestAlmNPCifTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTelXPath # Teléfono
            ElemValidarTXT = gestAlmElements.gestAlmNPTelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTel2XPath # Teléfono 2
            ElemValidarTXT = gestAlmElements.gestAlmNPTel2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPNomXPath # Nombre*
            ElemValidarTXT = gestElements.gestNom2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPEmaXPath  # email
            ElemValidarTXT = gestAlmElements.gestAlmNPEmaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPEma2XPath  # email2
            ElemValidarTXT = gestAlmElements.gestAlmNPEma2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPRSoXPath  # razón social
            ElemValidarTXT = gestAlmElements.gestAlmNPRSoTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPEmaCXPath  # email comercial
            ElemValidarTXT = gestAlmElements.gestAlmNPEmaCTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPFaxXPath  # fax
            ElemValidarTXT = gestAlmElements.gestAlmNPFaxTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPDirXPath  # dirección
            ElemValidarTXT = gestAlmElements.gestAlmNPDirTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPPIntXPath  # proveedor interno
            ElemValidarTXT = gestAlmElements.gestAlmNPPIntTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPConXPath  # contabilidad
            ElemValidarTXT = gestAlmElements.gestAlmConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPDAlXPath  # descuento albarán
            ElemValidarTXT = gestAlmElements.gestAlmNPDAlTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPRapXPath  # rappel
            ElemValidarTXT = gestAlmElements.gestAlmNPRapTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPPedXPath  # Pedidos
            ElemValidarTXT = gestElements.gestAlPed1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPEmPXPath  # email pedidos
            ElemValidarTXT = gestAlmElements.gestAlmNPEmPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPPeMXPath  # pedido mínimo
            ElemValidarTXT = gestAlmElements.gestAlmNPPeMTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPDEPXPath  # días de emisión de pedido
            ElemValidarTXT = gestAlmElements.gestAlmNPDEPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPLunXPath  # lunes
            ElemValidarTXT = gestAlmElements.gestAlmNPLunTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTELXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPTEnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPMarXPath  # martes
            ElemValidarTXT = gestAlmElements.gestAlmNPMarTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTEMXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPTEnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPMieXPath  # miércoles
            ElemValidarTXT = gestAlmElements.gestAlmNPMieTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTEXXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPTEnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPJueXPath  # jueves
            ElemValidarTXT = gestAlmElements.gestAlmNPJueTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTEJXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPTEnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPVieXPath  # viernes
            ElemValidarTXT = gestAlmElements.gestAlmNPVieTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTEVXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPTEnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPSabXPath  # sábado
            ElemValidarTXT = gestAlmElements.gestAlmNPSabTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTESXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPTEnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPDomXPath  # domingo
            ElemValidarTXT = gestAlmElements.gestAlmNPDomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNPTEDXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPTEnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('acciones en el formulario nuevo proveedor --> interrogación pedidos')
            interrogPed = gestAlmElements.gestAlmNPInPXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=interrogPed).click()
            cancelarInterrogPed = gestAlmElements.gestAlmNPCIPXPath
            time.sleep(1)
            pagina_gestAlm.find_element(by=By.XPATH, value=cancelarInterrogPed).click()
        except Exception as e:
            logger.error("Algún elemento en 'I validate the form new provider' no encontrado: {}".format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: "I validate the form new provider" --> {}'.format(resStep))
        assert resStep

    @then('I fill in the mandatory fields in the form new provider')
    def rellenar_formulario_obligatorio_nuevo_proveedor(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I fill in the mandatory fields in the form new provider')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmNProvID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmNPRefInput  # referencia
            ElemValidarValor = gestAlmElements.gestAlmNPRefValor
            self.newpro = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPNomInput  # nombre
            ElemValidarValor = gestAlmElements.gestAlmNPNomValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPRSoInput  # razón social
            ElemValidarValor = gestAlmElements.gestAlmNPRSoValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPDAlInput  # dto albarán
            ElemValidarValor = gestAlmElements.gestAlmNPDAlValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPRapInput  # rappel
            ElemValidarValor = gestAlmElements.gestAlmNPRapValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPEmPInput  # email pedido
            ElemValidarValor = gestAlmElements.gestAlmNPEmPValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPPeMInput  # pedido mínimo
            ElemValidarValor = gestAlmElements.gestAlmNPPeMValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPLuCInput  # cantidad lunes
            ElemValidarValor = gestAlmElements.gestAlmNPLuCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmNPMarXPath  # desactivar martes
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmNPMieXPath  # desactivar miércoles
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmNPJueXPath  # desactivar jueves
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmNPVieXPath  # desactivar viernes
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmNPSabXPath  # desactivar sábado
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmNPDomXPath  # desactivar domingo
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I fill in the mandatory fields in the form new provider" no encontrado: {}'.format(
                    ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill in the mandatory fields in the form new provider --> {}'.format(resStep))
        assert resStep

    @then('I fill in the form new provider')
    def rellenar_formulario_nuevo_proveedor(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I fill in the form new provider')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmNProvID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmNPRefInput  # referencia
            ElemValidarValor = gestAlmElements.gestAlmNPRefValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            self.newpro = ElemValidarValor
            # el cif se rellena automaticamente al escoger almacen
            ElemValidar = gestAlmElements.gestAlmNPNomInput  # nombre
            ElemValidarValor = gestAlmElements.gestAlmNPNomValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPRSoInput  # razón social
            ElemValidarValor = gestAlmElements.gestAlmNPRSoValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPDirInput  # dirección
            ElemValidarValor = gestAlmElements.gestAlmNPDirValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPConInput  # contabilidad
            ElemValidarValor = gestAlmElements.gestAlmNPConValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPDAlInput  # dto albarán
            ElemValidarValor = gestAlmElements.gestAlmNPDAlValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPRapInput  # rappel
            ElemValidarValor = gestAlmElements.gestAlmNPRapValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPEmPInput  # email pedido
            ElemValidarValor = gestAlmElements.gestAlmNPEmPValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPPeMInput  # pedido mínimo
            ElemValidarValor = gestAlmElements.gestAlmNPPeMValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPLuCInput  # cantidad lunes
            ElemValidarValor = gestAlmElements.gestAlmNPLuCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPMaCInput  # cantidad martes
            ElemValidarValor = gestAlmElements.gestAlmNPMaCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPMiCInput  # cantidad miércoles
            ElemValidarValor = gestAlmElements.gestAlmNPMiCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPJuCInput  # cantidad jueves
            ElemValidarValor = gestAlmElements.gestAlmNPJuCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPViCInput  # cantidad viernss
            ElemValidarValor = gestAlmElements.gestAlmNPViCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPSaCInput  # cantidad sábado
            ElemValidarValor = gestAlmElements.gestAlmNPSaCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPDoCInput  # cantidad domingo
            ElemValidarValor = gestAlmElements.gestAlmNPDoCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).send_keys(Keys.PAGE_UP)
            ElemValidar = gestAlmElements.gestAlmNPTelInput  # teléfono
            ElemValidarValor = gestAlmElements.gestAlmNPTelValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPEmaInput  # email
            ElemValidarValor = gestAlmElements.gestAlmNPEmaValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPEmCInput  # email comercial
            ElemValidarValor = gestAlmElements.gestAlmNPEmCValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPTe2Input  # teléfono 2
            ElemValidarValor = gestAlmElements.gestAlmNPTe2Valor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPEm2Input  # email 2
            ElemValidarValor = gestAlmElements.gestAlmNPEm2Valor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmNPFaxInput  # fax
            ElemValidarValor = gestAlmElements.gestAlmNPFaxValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('acciones en el formulario nuevo proveedor --> proveedor interno')
            pagina_gestAlm.find_element(by=By.XPATH, value=gestAlmElements.gestAlmNPPIntXPath).click()
            pagina_gestAlm.find_element(by=By.ID, value=gestAlmElements.gestAlmNPPISocSelID).click()
            ElemValidar = gestAlmElements.gestAlmNPPISocSelXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPPISocOKTXT # proveedor interno, LATERAL FLEMING, S.L.
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            pagina_gestAlm.find_element(by=By.ID, value=gestAlmElements.gestAlmNPPIAlmSelID).click()
            ElemValidar = gestAlmElements.gestAlmNPPIAlmOKXPath
            ElemValidarTXT = gestAlmElements.gestAlmNPPIAlmOKTXT # proveedor interno, almacén seleccionado
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I fill in the form new provider" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill in the form new provider --> {}'.format(resStep))
        assert resStep

    @then('I save the new provider')
    def guardar_nuevo_proveedor(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I save the new provider')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmNPGuaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()  # Guardar proveedor
            ElemValidar = gestAlmElements.gestAlmDelProXPath  # aparecen las acciones
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        except Exception as e:
            logger.error('Algún elemento en "I save the new provider" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I save the new provider --> {}'.format(resStep))
        assert resStep

    @then('I search and delete the new provider')
    def buscaryborrar_nuevo_proveedor(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete the new provider')
        resStep = True
        try:
            logger.debug('Busco y borro el nuevo provider')
            ElemValidar = gestAlmElements.gestAlmBusProInput
            buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscar.send_keys(self.newpro)  # busco proveedor
            buscar.click()
            ElemValidar = gestAlmElements.gestAlmBusProValor
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            self.nuevopro = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(self.newpro)
            logger.info(self.nuevopro)
            if self.newpro == self.nuevopro:
                logger.debug('Borrar')
                ElemValidar = gestAlmElements.gestAlmDelProXPath
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

                ElemValidar = gestAlmElements.gestAlmDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlmDelOKXPath  # Aceptar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('El proveedor ' + self.newpro + 'ha sido borrado')
            else:
                logger.debug('El proveedor ' + self.newpro + 'NO ha sido borrado')
                time.sleep(2)
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete the new provider" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete the new provider --> {}'.format(resStep))
        assert resStep


    @then('I search a provider')
    def buscar_proveedor(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I search a provider')
        resStep = True
        try:
            logger.debug('Realizo una búsqueda')
            ElemValidar = gestAlmElements.gestAlmProvBusXPath # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmBusProInput
            buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscar.send_keys(gestAlmElements.gestAlmBusPalTXT) # HIGIENE
            buscar.click()
            logger.debug('Compruebo q todas las líneas tienen la palabra buscada')
            ElemValidar = gestAlmElements.gestAlmRes1XPath
            textobuscado1 = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = gestAlmElements.gestAlmRes2XPath
            textobuscado2 = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = gestAlmElements.gestAlmRes3XPath
            textobuscado3 = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if gestAlmElements.gestAlmBusPalTXT in textobuscado1: # HIGIENE
                logger.debug('resultado 1 --> OK')
                if gestAlmElements.gestAlmBusPalTXT in textobuscado2:
                    logger.debug('resultado 2 --> OK')
                    if gestAlmElements.gestAlmBusPalTXT in textobuscado3:
                        logger.debug('resultado 3 --> OK ')
                        resStep = True & resStep
            else:
                resStep = False & resStep

            logger.debug('Compruebo las columnas de la busqueda mostrada')
            columnas_GA(resStep, pagina_gestAlm) # 8 (Ref.,Proveedor,CIF, Tel�fono, Email, Desc. albar�n, Rappel, Acciones)

            logger.debug('compruebo número de items')
            ElemValidar = gestAlmElements.gestAlmIt1XPath
            ElemValidarTXT = gestAlmElements.gestAlmIt1TXT # 1
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmItnXPath
            ElemValidarTXT = gestAlmElements.gestAlmItnTXT # 3
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I search a provider" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search a provider --> {}'.format(resStep))
        assert resStep

    @then('I export providers')
    def exporto_proveedores(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export providers')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:62]  # nombre original del fichero sin segundos ni extension, ej: Listado%20de%20proveedores_20240927_1229
            self.ficheropro = gestAlmElements.gestAlmExpFMPProvTXT + self.ficexp[53:94]  # Nombre fichero completo, ej: Listado de proveedores_20240927_12293623.xlsx
            nombre = gestAlmElements.gestAlmExpDesLPrTXT
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheropro) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export providers" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export providers --> {}'.format(resStep))
        assert resStep

    @then('I open providers file')
    def abrir_fichero_exportado_proveedores(self):
        logger.debug('INICIO STEP: I open file providers')
        resStep = True  # necesario si no, no entra en el try si el paso anterior es True
        try:
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            primeraLinea = gestAlmElements.gestAlmExpFMPProvTXT + ' (Global)'
            resStep = abrirFichero(resStep, primeraLinea, self.ficheropro)
        except Exception as e:
            logger.error('Algún elemento en "I open file providers" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open file providers --> {}'.format(resStep))
        assert resStep

    @then('I advance page almacen')
    def avanzar_pagina_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I advance page almacen')
        resStep = True
        try:
            Pg1 = gestAlmElements.gestAlmPg1XPath
            Pg1TXT = gestAlmElements.gestAlmPg1TXT
            Mos = gestAlmElements.gestAlmMosProvXPath
            AvP = gestAlmElements.gestAlmAvPXPath
            MP1 = gestAlmElements.gestAlmMos1TXT
            MP2 = gestAlmElements.gestAlmMos2TXT
            MP3 = gestAlmElements.gestAlmMos3TXT
            MP4 = gestAlmElements.gestAlmMos4TXT
            MP5 = gestAlmElements.gestAlmMos5TXT
            ElemValidar = avanzar_pagina(resStep, pagina_gestAlm, Pg1, Pg1TXT, Mos, AvP, MP1, MP2, MP3, MP4, MP5)
        except Exception as e:
            logger.error('Algún elemento en "I advance page almacen" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
            logger.error(resStep)
        logger.error(resStep)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I advance page almacen --> {}'.format(resStep))
        assert resStep

    @then('I turn back page almacen')
    def retroceder_pagina_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I turn back page almacen')
        resStep = True
        try:
            Pg5 = gestAlmElements.gestAlmPg5XPath
            Pg5TXT = gestAlmElements.gestAlmPg5TXT
            Mos = gestAlmElements.gestAlmMosProvXPath
            ReP = gestAlmElements.gestAlmRePXPath
            MP1 = gestAlmElements.gestAlmMos1TXT
            MP2 = gestAlmElements.gestAlmMos2TXT
            MP3 = gestAlmElements.gestAlmMos3TXT
            MP4 = gestAlmElements.gestAlmMos4TXT
            MP5 = gestAlmElements.gestAlmMos5TXT
            ElemValidar = retroceder_pagina(resStep, pagina_gestAlm, Pg5, Pg5TXT, Mos, ReP, MP1, MP2, MP3, MP4,MP5)
        except Exception as e:
            logger.error('Algún elemento en "I turn back page almacen" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I turn back page almacen --> {}'.format(resStep))
        assert resStep

    @step('I click provider´s invoices')
    def click_productos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click provider´s invoices')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestFPrXPath  # Facturas de proveedor
            ElemValidarTXT = gestAlmElements.latPagGestFPrTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click provider´s invoices" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click provider´s invoices --> {}'.format(resStep))
        assert resStep


    @then('I see provider´s invoices')
    def veo_facturas_de_proveedor(self):
        logger.debug('INICIO STEP: I see invoices')
        pagina_gestAlm = self.driver
        resStep = True
        try:
            logger.debug('Valido listado facturas')
            ElemValidar = gestAlmElements.gestAlmFPTitXPath  # LISTADO DE FACTURAS DE PROVEEDOR
            ElemValidarTXT = gestAlmElements.gestAlmFProvTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPBusXPath
            ElemValidarTXT = gestElements.gestBusTXT # Buscar:
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Busqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPNueFacID  # Nueva factura
            ElemValidarTXT = gestAlmElements.gestAlmFPNueFacTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPFecXPath  # Fecha:
            ElemValidarTXT = gestElements.gestFec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPFec2XPath  # Valor de fecha
            ElemValidarTXT = gestAlmElements.gestAlmFec2Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosFacPXPath  # Mostrando..
            ElemValidarTXT = gestAlmElements.gestAlmFPMosTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPTitTotXPath  # Total:
            ElemValidarTXT = gestElements.gestTotal2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPCanTotXPath  # Cantidad, total
            ElemValidarTXT = gestAlmElements.gestAlmFPCanTotTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc2XPath  # Nº de factura de proveedor
            ElemValidarTXT = gestAlmElements.gestAlmFPNFPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc3XPath  # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc4XPath  # Sociedad
            ElemValidarTXT = gestAlmElements.gestAlmNPPISocTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc5XPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc6XPath  # Base total
            ElemValidarTXT = gestAlmElements.gestAlmFPBTTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc7XPath  # Total impuestos
            ElemValidarTXT = gestAlmElements.gestAlmFPTITXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc8XPath  # Total
            ElemValidarTXT = gestElements.gestTotal1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc9XPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFPc10XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see invoices" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see invoices --> {}'.format(resStep))
        assert resStep

    @step('I click products')
    def click_materiasprimas_productos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click products')
        resStep = True
        try:
            logger.debug('Selecciono productos')
            ElemValidar = gestAlmElements.latPagGestMPrXPath  # Productos de proveedor
            ElemValidarTXT = gestAlmElements.latPagGestMPrTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPPTABLA  # Tabla cargada
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            logger.debug('Tabla cargada')
        except Exception as e:
            logger.error('Algún elemento en "I click products" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click products --> {}'.format(resStep))
        assert resStep

    @step('I see mas columnas')
    def veo_mascolumnas_materiasprimas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see mas columnas')
        resStep = True
        try:
            logger.debug('Más columnas')
            ElemValidar = gestAlmElements.gestAlmMPPMCoXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Al marcar Mas Columnas aparece Alérgenos')
            ElemValidar = gestAlmElements.gestAlmMPMasColNewXPath  # Alérgenos
            ElemValidarTXT = gestAlmElements.gestAlmMPMasColNewTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Desactivo más columnas')
            ElemValidar = gestAlmElements.gestAlmMPPMCoXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Selecciono una columna')
            ElemValidar = gestAlmElements.gestAlmMPMasColConfXPath  # Configuración columnas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPMasColSelXPath  # Selecciono Ref.
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPMasColKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPMasColOKXPath  # Guardar
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Verifico columna añadida')
            ElemValidar = gestAlmElements.gestAlmMPPCo2XPath # columna añadida : Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see mas columnas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see mas columnas --> {}'.format(resStep))
        assert resStep

    @then('I see products of materias primas')
    def veo_productos_materiasprimas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see products of materias primas')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMPPTitXPath  # Listado de productos
            ElemValidarTXT = gestAlmElements.gestAlmFProdTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPPFilXPath  # Filtros:
            ElemValidarTXT = gestElements.gestFilTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPFURXPath  # Uso en receta
            ElemValidarTXT = gestAlmElements.gestAlmMPPFURTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPFUPXPath  # Uso de personal
            ElemValidarTXT = gestAlmElements.gestAlmMPPFUPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Búsqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT # QA
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCloID  # Clonar productos
            ElemValidarTXT = gestAlmElements.gestAlmMPPCloTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNItemID  # Nuevo producto
            ElemValidarTXT = gestAlmElements.gestAlmNProdTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosProdXPath  # Mostrando..productos
            ElemValidarTXT = gestAlmElements.gestAlmMPPMosTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo1XPath  # Cód. Externo
            ElemValidarTXT = gestAlmElements.gestAlmMPPCExtTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo2XPath  # Producto
            ElemValidarTXT = gestAlmElements.gestAlmMPPProTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo3XPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo4XPath  # Precio por unidad (€)
            ElemValidarTXT = gestAlmElements.gestAlmMPPPUnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo5XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo6XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPMCoXPath  # Mostrar más columnas
            ElemValidarTXT = gestElements.gestMMCoTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see products of materias primas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see products of materias primas --> {}'.format(resStep))
        assert resStep


    @then('I select uso en receta y/o personal')
    def selecciono_uso_receta_personal(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I select uso en receta y/o personal')
        resStep = True
        try:
            logger.debug('Selecciono uso en: receta/personal')
            ElemValidar = gestAlmElements.gestAlmMPPFURXPath  # Uso en receta
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMosProdXPath  # Mostrando .. productos/receta
            UsoReceta = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if UsoReceta == gestAlmElements.gestAlmMPPMURTXT:
                logger.debug('Uso en receta seleccionado: ' + UsoReceta)
                ElemValidar = gestAlmElements.gestAlmMPPFURXPath
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()  # deselecciono uso en receta
                time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMPPFUPXPath  # Uso en personal
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()  # selecciono uso en personal
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMosProdXPath  # Mostrando .. productos/personal
            UsoPersonal = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if UsoPersonal == gestAlmElements.gestAlmMPPMUPTXT:
                logger.debug('Uso en personal seleccionadoUso en personal seleccionado ' + UsoPersonal)
                ElemValidar = gestAlmElements.gestAlmMPPFURXPath  # Marco de nuevo Uso en receta
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestAlmElements.gestAlmMosProdXPath  # Mostrando..todos los productos
                UsoRecetaPersonal = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
                if UsoRecetaPersonal == gestAlmElements.gestAlmMPPMURPTXT:
                    logger.debug('Uso en receta y uso en personal seleccionado ' + UsoRecetaPersonal)
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I select uso en receta y/o personal" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I select uso en receta y/o personal --> {}'.format(resStep))
        assert resStep


    @then('I export products')
    def exporto_productos(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export products')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:60]  # nombre original del fichero sin segundos ni extension
            self.ficheroMPpro = gestAlmElements.gestAlmExpFMPPTXT + self.ficexp[51:92]  # Nombre fichero completo
            nombre = gestAlmElements.gestAlmExpDesFMPProdTXT
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroMPpro) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export products" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export products --> {}'.format(resStep))
        assert resStep

    @then('I open MP_products file')
    def abro_fichero_exportado_MP_productos(self):
        logger.debug('INICIO STEP: I open MP_products file')
        resStep = True  # necesario si no, no entra en el try si el paso anterior es true
        try:
            resStep = True
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFMPPTXT + ' (Global)'
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroMPpro)
        except Exception as e:
            logger.error('Algún elemento en "I open MP_products file" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open MP_products file  --> {}'.format(resStep))
        assert resStep

    @then('I valid form advance search products')
    def busqueda_avanzada(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form advance search products')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada de productos')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBARefXPath  # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBACIAXPath  # Ingrediente
            ElemValidarTXT = gestAlmElements.gestAlmIng4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmC1XPath  # Categoría
            ElemValidarTXT = gestAlmElements.gestAlmCategTXT
            ini= 0
            fin= 9
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmC2XPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            ini= 0
            fin= 9
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I valid form advance search products" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form advance search products --> {}'.format(resStep))
        assert resStep

    @then('I do advance search products')
    def hago_busqueda_avanzada_productos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search products')
        resStep = True
        try:
            logger.debug('relleno de los campos')
            ElemValidar = gestAlmElements.gestAlmMPBAIngInput  # Ingrediente
            ElemValidarValor = gestAlmElements.gestAlmMPBAIngValor # ALHAMBRA
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPBACatInput  # Categoría
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlmMPBACatValor  # Selecciono Categoría
            cat = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if cat == gestAlmElements.gestAlmMPBACatNombre: # Cervezas
                logger.debug ('La categoría ' + cat + ' ha sido encontrada')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.debug('La categoría ' + cat + 'NO  ha sido encontrada')
                resStep = False
            ElemValidar = gestAlmElements.gestAlmMPBAProInput  # Proveedor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).send_keys('M')
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath # Buscar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            logger.debug('Verifico resultado busqueda avanzada productos')
            ElemValidar = gestAlmElements.gestAlmMPBAProvResXPath # MAHOU, S.A.
            ElemValidarTXT = gestAlmElements.gestAlmMPBAProvNombre
            proveedorsel = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if ElemValidarTXT == proveedorsel: # MAHOU, S.A.
                logger.debug('La busqueda avanzada es correcta')
                resStep = True & resStep
            else:
                logger.debug('El proveedor ' + ElemValidarTXT + ' NO ha sido encontrado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I do advance search products" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search products --> {}'.format(resStep))
        assert resStep

    @then('I clone product')
    def clono_producto(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I clone product')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmMPPCloID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(3)
            logger.debug('Valido formulario clonar')
            ElemValidar = gestAlmElements.gestAlmMPCTitXPath  # Clonar productos
            ElemValidarTXT = gestAlmElements.gestAlmMPCTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCPOXPath  # Proveedor origen
            ElemValidarTXT = gestAlmElements.gestAlmMPCPOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCPDXPath  # Proveedor destino
            ElemValidarTXT = gestAlmElements.gestAlmMPCPDTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCoKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCoOKXPath  # Clonar
            ElemValidarTXT = gestAlmElements.gestAlmMPCOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Relleno formulario clonar')
            ElemValidar = gestAlmElements.gestAlmMPCPOInput  #  Proveedor origen
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMPCPOValor  # Selecciono proveedor origen
            ElemValidarTXT = gestAlmElements.gestAlmMPCPONomValor # CALIDAD PASCUAL SA
            provo = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if provo == ElemValidarTXT:
                logger.debug('El proveedor origen ' + provo + ' ha sido encontrado')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                resStep = True & resStep
            else:
                logger.debug('El proveedor origen ' + provo + ' NO ha sido encontrado')
                resStep = False
            ElemValidar = gestAlmElements.gestAlmMPCPDInput  # Proveedor destino
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMPCPDValor  # Selecciono proveedor destino
            ElemValidarTXT = gestAlmElements.proveedor # 1QANER2810241010_nombre
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.info(resStep)
            provd = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if provd == ElemValidarTXT:
                logger.debug('El proveedor destino ' + provd + ' ha sido encontrado')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                resStep = True & resStep
            else:
                logger.debug('El proveedor destino ' + provd + ' NO ha sido encontrado')
                resStep = False
            logger.debug('Seleccionar producto')
            ElemValidar = gestAlmElements.gestAlmMPCPSelPXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(10)
            ElemValidar = gestAlmElements.gestAlmMCoOKXPath  # OK
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Verificar producto clonado')
            ElemValidar = gestAlmElements.gestAlmMPCPrvClXPath # Proveedor
            provclon = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info('El proveedor destino es ' + provd)
            logger.info('El proveedor destino es ' + provclon)
            ElemValidar = gestAlmElements.gestAlmMPCPrdClXPath
            ElemValidarTXT = gestAlmElements.gestAlmMPCPrdClTXT # 'Tombu Rosado (c/ 6 botellas)'
            prodclon = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info('El producto clonado es ' + ElemValidarTXT)
            logger.info('El producto clonado es ' + prodclon)
            if (provclon == provd) & (prodclon == ElemValidarTXT):
                logger.debug('El producto  ' + provclon + ' ha sido clonado')
                resStep = True & resStep
            else:
                logger.debug('El producto  ' + provclon + ' NO ha sido clonado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I clone product" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I clone product --> {}'.format(resStep))

    @then('I delete product cloned')
    def borrar_producto_clonado(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I delete product cloned')
        resStep = True
        try:
            logger.debug('Buscar producto')
            ElemValidar = gestAlmElements.gestAlmMPCBusXPath  # Buscar
            ElemValidarValor = gestAlmElements.proveedor #
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            logger.debug('Validar opción Eliminar Producto. Borrar producto')
            ElemValidar = gestAlmElements.gestAlmMPCProvEncXPath
            proveedor = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if ElemValidarValor == proveedor:
                logger.debug('Borrar producto')
                ElemValidar = gestAlmElements.gestAlmMPCDelXPath
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlmMPCDelTitXPath  # ELIMINAR PRODUCTO
                ElemValidarTXT = gestAlmElements.gestAlmMPCDelTitTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlmMPCDelTit2XPath  #  ¿Está seguro de eliminar este producto?
                ElemValidarTXT = gestAlmElements.gestAlmMPCDelTit2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlmMPCDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlmMPCDelOKXPath  # Eliminar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
            else:
                logger.debug('Producto no encontrado para borrar')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I delete product cloned" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I delete product cloned --> {}'.format(resStep))
        assert resStep

    @step('I valid the form of a new product')
    def validar_formulario_producto_materiasprimas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid the form of a new product')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlmMPCreTitXPath  # PRODUCTO DE PROVEEDOR
            ElemValidarTXT = gestAlmElements.gestAlmMPCreTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreRefXPath  # Referencia*
            ElemValidarTXT = gestElements.gestReferencia1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreCBXPath  # Código de barras
            ElemValidarTXT = gestAlmElements.gestAlmMPCreCBTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCrePCIXPath  # Producto para consumo interno
            ElemValidarTXT = gestAlmElements.gestAlmMPCrePCITXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreNAlXPath  # Nombre comercial de albarán*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreNAlTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreNInXPath  # Nombre de ingrediente*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreNInTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreProXPath  # Proveedor*
            ElemValidarTXT = gestElements.gestProv2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreCatXPath  # Categoría
            ElemValidarTXT = gestAlmElements.gestAlmCategTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreDAlXPath  # Descuento albarán (%)
            ElemValidarTXT = gestAlmElements.gestAlmMPCreDAlTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreRapXPath  # Rappel (%)
            ElemValidarTXT = gestAlmElements.gestAlmMPCreRapTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreSob1XPath  # Sobreescribir
            ElemValidarTXT = gestAlmElements.gestAlmMPCreSobTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreSob2XPath  # Sobreescribir
            ElemValidarTXT = gestAlmElements.gestAlmMPCreSobTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreUdXPath  # Unidades
            ElemValidarTXT = gestElements.gestUni2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreUCXPath  # Unidad de Compra*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreUCTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreCon1XPath  # Conversión*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreUAXPath  # Unidad de Almacenamiento
            ElemValidarTXT = gestAlmElements.gestAlmMPCreUATXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreCon2XPath  # Conversión*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreURXPath  # Unidad de receta*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreURTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCrePrXPath  # Precio
            ElemValidarTXT = gestElements.gestPrecioTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCrePrUXPath  # Precio por unidad (€)*
            ElemValidarTXT = gestAlmElements.gestAlmMPCrePrUTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreIVAXPath  # IVA*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreIVATXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCrePrUnXPath  # Precio unitario (€)
            ElemValidarTXT = gestAlmElements.gestAlmMPCrPrUnTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCreKOXPath  # Volver
            ElemValidarTXT = gestAlmElements.gestAlmMPCreKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I valid the form of a new product" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid the form of a new product --> {}'.format(resStep))
        assert resStep

    @then('I create a product with all fields')
    def crear_producto_todosloscampos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create a product with all fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlmMPCreRefInput  # referencia
            ElemValidarValor = gestAlmElements.gestAlmMPCreRefValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreCBInput  # Código de barras
            ElemValidarValor = gestAlmElements.gestAlmMPCreCBValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreNAlInput  # N.Albarán
            ElemValidarValor = gestAlmElements.gestAlmMPCreNAlValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            self.nprod = ElemValidarValor
            ElemValidar = gestAlmElements.gestAlmMPCreProInput  # Proveedor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreProValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreNInInput  # N. Ingrediente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreNInValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreSob1XPath  # Pulso sobreescribir
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreDAlInput  # Dto. Albarán
            ElemValidarValor = gestAlmElements.gestAlmMPCreDAlValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreSob2XPath  # Pulso sobreescribir
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreRapInput  # Rappel
            ElemValidarValor = gestAlmElements.gestAlmMPCreRapValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreUCInput  # Unidad Compra
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreUCValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreCon1Input  # Conversión
            ElemValidarValor = gestAlmElements.gestAlmMPCreCon1Valor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreUAInput  # Unidad de Almacenamiento
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreUAValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreCon2Input  # Conversión
            ElemValidarValor = gestAlmElements.gestAlmMPCreCon2Valor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCrePrUInput  # Precio por unidad
            ElemValidarValor = gestAlmElements.gestAlmMPCrePrUValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreIVAInput  # IVA
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar= gestAlmElements.gestAlmMPCreIVAValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCrePCIXPath  # Producto para consumo interno
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreOKXPath  # Guardar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(5)
        except Exception as e:
            logger.error('Algún elemento en "I create a product with all fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create a product with all fields --> {}'.format(resStep))
        assert resStep


    @step('I create a product with mandatory fields')
    def crear_producto_camposobligatorios(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create a product with mandatory fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlmMPCreRefInput  # referencia
            ElemValidarValor = gestAlmElements.gestAlmMPCreRefValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreNAlInput  # N.Albarán
            ElemValidarValor = gestAlmElements.gestAlmMPCreNAlValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            self.nprod = ElemValidarValor
            ElemValidar = gestAlmElements.gestAlmMPCreProInput  # Proveedor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreProValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreNInInput  # N. Ingrediente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreNInValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreUCInput  # Unidad Compra
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreUCValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreCon1Input  # Conversión
            ElemValidarValor = gestAlmElements.gestAlmMPCreCon1Valor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreUAInput  # Unidad de Almacenamiento
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreUAValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreCon2Input  # Conversión
            ElemValidarValor = gestAlmElements.gestAlmMPCreCon2Valor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCrePrUInput  # Precio por unidad
            ElemValidarValor = gestAlmElements.gestAlmMPCrePrUValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreIVAInput  # IVA
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar= gestAlmElements.gestAlmMPCreIVAValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPCreOKXPath  # Guardar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(5)
        except Exception as e:
            logger.error('Algún elemento en "I create a product with mandatory fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create a product with mandatory fields --> {}'.format(resStep))
        assert resStep

    @then('I search and delete a product')
    def buscaryborrar_nuevo_producto(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete a product')
        resStep = True
        try:
            logger.debug('Busco y borro el producto')
            ElemValidar = gestAlmElements.gestAlmMPNProXPath # busco borrar
            nproduct = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if self.nprod == nproduct or self.prodmod == nproduct:
                logger.debug('El producto '+ self.nprod + ' ha sido encontrado')
                ElemValidar = gestAlmElements.gestAlmMPProDelXPath  # Icono borrar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(5)
                ElemValidar = gestAlmElements.gestAlmMPProDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlmMPProDelOKXPath  # Eliminar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('El producto ' + self.nprod + ' ha sido eliminado')
                time.sleep(2)
            else:
                logger.debug('El producto ' + nproduct + ' NO ha sido encontrado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete a product" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete a product --> {}'.format(resStep))
        assert resStep

    @then('I click to accion historico de precios')
    def click_historico_precios_productos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I click to accion historico de precios')
        resStep = True
        try:
            logger.debug('Histórico de precios producto')
            ElemValidar = gestAlmElements.gestAlmMPAHPXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMPAHPTitXPath  # HISTORICO DE PRECIO
            ElemValidarTXT = gestAlmElements.gestAlmMPAHPTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAHPFecXPath  # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAHPPreXPath  # Precio
            ElemValidarTXT = gestElements.gestPrecioTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAHPVar1XPath  # Variación
            ElemValidarTXT = gestAlmElements.gestAlmVarTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAHPVar2XPath  # Variación
            ElemValidarTXT = gestAlmElements.gestAlmVarTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAHPCerXPath  # Cerrar
            ElemValidarTXT = gestElements.gestCOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click to accion historico de precios" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to accion historico de precios --> {}'.format(resStep))
        assert resStep

    @then('I click to accion distribuidor')
    def click_distribuidor_productos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I click to accion Distribuidor')
        resStep = True
        try:
            logger.debug('Distribuidor producto')
            ElemValidar = gestAlmElements.gestAlmMPADXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMPADTitXPath  # Distribuidor
            ElemValidarTXT = gestAlmElements.gestAlmMPADTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPADInput
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPADValor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidarTXT = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMCoOK2XPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPADKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click to accion Distribuidor" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to accion Distribuidor --> {}'.format(resStep))
        assert resStep

    @then('I valid form to accion alergenos')
    def valido_alergenos_productos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I valid form to accion alergenos')
        resStep = True
        try:
            logger.debug('form alergenos producto')
            ElemValidar = gestAlmElements.gestAlmMPAAXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            ElemValidar = gestAlmElements.gestAlmMPAATitXPath  # ALÉRGENOS
            ElemValidarTXT = gestAlmElements.gestAlmMPAATitTXT + self.nprod.upper()
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            aler = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if ElemValidarTXT in aler:
                logger.debug('El producto ' + self.nprod + ' es localizado')
            else:
                loggerdebug('El producto NO es localizado')
            ElemValidar = gestAlmElements.gestAlmMPAATit2XPath  # Producto libre de alérgenos
            ElemValidarTXT = gestAlmElements.gestAlmMPAATit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAAAddXPath  # Añadir alérgeno
            ElemValidarTXT = gestAlmElements.gestAlmMPAAAddTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAANomXPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAAAcrXPath  # Acrónimo
            ElemValidarTXT = gestAlmElements.gestAlmMPAAAcroTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAANivXPath  # Nivel
            ElemValidarTXT = gestAlmElements.gestAlmMPAANivTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAAAccXPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAAKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAAOKXPath  # Guardar
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPAAspaXPath # aspa
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()  # cierro con el aspa
        except Exception as e:
            logger.error('Algún elemento en "I valid form to accion alergenos" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form to accion alergenos --> {}'.format(resStep))
        assert resStep

    @then('I fill form to accion alergenos')
    def relleno_alergenos_productos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I fill form to accion alergenos')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmMPAAXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            logger.debug('Rellenar formulario de alergenos producto: alérgeno 1')
            ElemValidar = gestAlmElements.gestAlmMPAAEleInput
            ElemValidarTXT = gestAlmElements.gestAlmMPAAEleTXT
            ini = 85
            fin = 91
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPAAEleValor # Gluten
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPAAEle2Input  # Trazas/Contiene
            ElemValidarTXT = gestAlmElements.gestAlmMPAAEle2TXT
            ini = 0
            fin = 6
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPAAEle2Valor  # lugar Trazas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPAAAddXPath  # Añadir alérgeno
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPAAOKXPath  # Guardar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(5)
            logger.debug('Comprobar alérgeno añadido')
            ElemValidar = gestAlmElements.gestAlmMPAAXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmMPAAEleAddXPath
            Eleadd = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text  # Elemento añadido
            if Eleadd == gestAlmElements.gestAlmMPAAEleTXT:
                logger.debug('El alérgeno ' + Eleadd + ' ha sido añadido')
                resStep = True & resStep
            else:
                logger.debug('El elérgeno ' + Eleadd + ' NO ha sido añadido')
                resStep = False
            logger.debug('Rellenar formulario de alergenos producto: alérgeno 2')

            ElemValidar = gestAlmElements.gestAlmMPAAEleInput
            ElemValidarTXT = gestAlmElements.gestAlmMPAA2EleTXT
            ini = 102
            fin = 108
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPAA2EleValor  # Huevos
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPAAEle2Input  # Trazas/Contiene
            ElemValidarTXT = gestAlmElements.gestAlmMPAA2Ele2TXT
            ini = 7
            fin = 15
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPAA2Ele2Valor  # lugar Contiene
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPAAAddXPath  # Añadir alérgeno
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Ordeno descendente por nombre')
            ElemValidar = gestAlmElements.gestAlmMPAANomXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Ordeno descendente por acrónimo')
            ElemValidar = gestAlmElements.gestAlmMPAAAcrXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Ordeno descendente por nivel')
            ElemValidar = gestAlmElements.gestAlmMPAANivXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Marcar libre de alergenos')
            ElemValidar = gestAlmElements.gestAlmMPAATit2XPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            ElemValidar = gestAlmElements.gestAlmMPAAOKXPath  # Guardar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I fill form to accion alergenos" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill form to accion alergenos --> {}'.format(resStep))
        assert resStep

    @then('I click to accion edit product')
    def edito_producto(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I click to accion editar')
        resStep = True
        try:
            logger.debug('Edito producto')
            ElemValidar = gestAlmElements.gestAlmMPAEXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmGItemID  # se muestra Guardar
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.ID, ElemValidar)))
        except Exception as e:
            logger.error('Algún elemento en "I click to accion edit product" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to accion edit product --> {}'.format(resStep))
        assert resStep

    @then('I modify the product')
    def modifico_producto(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I modify the product')
        resStep = True
        try:
            logger.debug('Modifico un campo')
            ElemValidar = gestAlmElements.gestAlmMPCreNAlInput  # modifico Nombre comercial de albarán
            ElemValidarValor = gestAlmElements.gestAlmMPCreNAlValor + 'mod'
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlmMPCreOKXPath  # Guardar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Compruebo modificación')
            ElemValidar = gestAlmElements.gestAlmMPPTABLA  # Producto
            self.prodmod = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info ('El nombre es modificado a ' + ElemValidarValor)
            logger.info ('Extraigo el producto ' +  self.prodmod)
            if self.prodmod == ElemValidarValor:
                logger.debug('El valor del campo Producto ha sido modificado a ' + self.prodmod)
                resStep = True & resStep
            else:
                logger.debug('El valor del campo Producto NO ha sido modificado a ' + self.prodmod)
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I modify the product" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I modify the product --> {}'.format(resStep))
        assert resStep

    @then('I click to accion deshabilitar')
    def deshabilito(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I click to accion deshabilitar')
        resStep = True
        try:
            logger.debug('Deshabilito producto')
            ElemValidar = gestAlmElements.gestAlmMPADEXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPADEKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPADEOKXPath  # Deshabilitar
            ElemValidarTXT = gestAlmElements.gestAlmMPADEOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar= gestAlmElements.gestAlmMPADEPXPath
            self.prodes = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.debug('El producto a deshabilitar es: ' + self.nprod )
            if self.nprod == self.prodes:
                ElemValidar = gestAlmElements.gestAlmMPADEOKXPath
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('El producto ' + self.prodes + ' es deshabilitado')
                resStep = True & resStep
            else:
                logger.debug('El producto ' + self.prodes + ' NO es deshabilitado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I click to accion deshabilitar" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to accion deshabilitar --> {}'.format(resStep))
        assert resStep

    @step('I click catalogs')
    def click_catalogo(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click catalogs')
        resStep = True
        try:
            logger.debug('Selecciono catálogos')
            ElemValidar = gestAlmElements.latPagGestMCaXPath  # Catálogos
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I click catalogs" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click catalogs --> {}'.format(resStep))
        assert resStep

    @step('I see catalog')
    def veo_catalogo_materiasprimas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see catalog')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMPCatTitXPath  # LISTADO DE CATÁLOGOS
            ElemValidarTXT = gestAlmElements.gestAlmCAtTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCatNewID  # Nuevo catálogo
            ElemValidarTXT = gestAlmElements.gestAlMPCatNewTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosCatXPath  # Mostrando..catálogos
            ElemValidarTXT = gestAlmElements.gestAlmPCaMosTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmPCaCo1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmPCaCo2XPath  # Catálogo
            ElemValidarTXT = gestAlmElements.gestAlmCat2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmPCaCo3XPath  # Descripción
            ElemValidarTXT = gestElements.gestDescripTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmPCaCo4XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see catalog" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see catalog --> {}'.format(resStep))
        assert resStep

    @when('I click to create a catalog')
    def click_crear_catalogo(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click to create a catalog')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlmMPCatNewID  # Nuevo catálogo
            time.sleep(10) # necesario para que encuentre el botón de Nuevo catálogo
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click to create a catalog" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to create a catalog --> {}'.format(resStep))
        assert resStep


    @step('I create a catalog')
    def creo_catalogo(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create a catalog')
        resStep = True
        try:
            logger.debug('Valido formulario catalogo')
            ElemValidar = gestAlmElements.gestAlmTitCreXPath  # CREACIÓN DE CATÁLOGOS
            ElemValidarTXT = gestAlmElements.gestAlMPCatCTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCPas1XPath  # Información básica
            ElemValidarTXT = gestAlmElements.gestAlMPCatCPas1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCPas2XPath  # Añadir Productos de Proveedor
            ElemValidarTXT = gestAlmElements.gestAlMPCatCPas2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCPas3XPath  # Añadir Almacenes
            ElemValidarTXT = gestAlmElements.gestAlMPCatCPas3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCAntXPath  # Anterior
            ElemValidarTXT = gestAlmElements.gestAlMPCatCAntTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCSigXPath  # Siguiente
            ElemValidarTXT = gestAlmElements.gestAlMPCatCSigTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestVolverListID  # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()

            logger.debug('Selecciono materias primas,catálogo de nuevo')
            ElemValidar = gestAlmElements.gestAlmMPCatNewID  # Nuevo Catálogo
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPCatCNomInput
            ElemValidarValor = gestAlmElements.gestAlMPCatCNomValor
            self.newcat = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCDesInput
            ElemValidarValor = gestAlmElements.gestAlMPCatCDesValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCNomXPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCDesXPath  # Descripción
            ElemValidarTXT = gestElements.gestDescripTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Paso a segunda pantalla y valido')
            ElemValidar = gestAlmElements.gestAlMPCatCSigXPath  # Siguiente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            ElemValidar = gestAlmElements.gestAlMPCatCBus1XPath  # Busco producto
            ElemValidarValor = gestAlmElements.gestAlmMPCPrdClTXT # Tombu Rosado (c/ 6 botellas)
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCAddXPath  # Añadir listado
            ElemValidarTXT = gestAlmElements.gestAlMPCatCAddTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() #  2 elementos
            ElemValidar = gestAlmElements.gestAlMPCatCTab11XPath  # Campo1 Tabla1 , Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCTab12XPath  # Campo2 Tabla1
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCTab13XPath  # Campo3 Tabla1, Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Busco ingrediente para el catálogo')
            ElemValidar = gestAlmElements.gestAlMPCatCBus1XPath  # Busco 3 BARRICAS, S.A
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).clear()
            ElemValidarValor = gestAlmElements.gestAlMPCatCAdd2OKTXT
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCAdd2XPath  # Añadir con flecha
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPCatCTab21XPath  # Campo1 Tabla2, Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCTab22XPath  # Campo2 Tabla2
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCTab23XPath  # Campo3 Tabla2, Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCQuiXPath  # Quitar todos
            ElemValidarTXT = gestAlmElements.gestAlMPCatCQuiTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Productos quitados y busco de nuevo')
            ElemValidar = gestAlmElements.gestAlMPCatCBus1XPath  # Buscar
            ElemValidarValor = gestAlmElements.gestAlmMPCPONomValor # CALIDAD PASCUAL SA
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCAddOKXPath  # Añadir el primero
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Primer producto añadido')
            ElemValidar = gestAlmElements.gestAlMPCatCBus1XPath  # Buscar x segunda vez
            ElemValidarValor = gestAlmElements.gestAlmMPCPrdClTXT # 'Baked Beans Heinz F/2.62 Kg'
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCAdd2XPath  # Añadir con flecha
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Segundo producto añadido y busco ese segundo en los añadidos')
            ElemValidar = gestAlmElements.gestAlMPCatCBus2XPath  # Buscar en los añadidos el segundo
            ElemValidarValor = gestAlmElements.gestAlmMPCPrdClTXT #'Baked Beans Heinz F/2.62 Kg'
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCAdd2KOXPath  # Quitar el segundo con flecha
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Segundo producto quitado,vuelvo atrá')
            ElemValidar = gestAlmElements.gestAlMPCatCAntXPath # Anterior
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Vuelvo adelante y valido tercera pantalla')
            ElemValidar = gestAlmElements.gestAlMPCatCSigXPath  # Siguiente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPCatCBus3XPath  # Buscar almacén
            ElemValidarValor = gestAlmElements.gestAlmNPPIAlmOKTXT  # LTL Strachan
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCatCAddAXPath  # Añadir almacén con flecha
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMPCatCAddAOKXPath  # Almacén añadido
            ElemValidarTXT = gestAlmElements.gestAlmNPPIAlmOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Almacén añadido')
            ElemValidar = gestAlmElements.gestAlMPCatCTab31XPath  # Campo1 Tabla3
            ElemValidarTXT = gestElements.gestAlmacenTXT # Almacén
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCTab41XPath  # Campo1 Tabla4
            ElemValidarTXT = gestElements.gestAlmacenTXT # Almacén (sale en las dos pantallas)
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCatCTOKXPath  # Guardar
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Nuevo catálogo guardado ' + self.newcat)
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I create a catalog" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create a catalog --> {}'.format(resStep))
        assert resStep


    @step('I search a catalog')
    def busco_catalogo(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I search a catalog')
        resStep = True
        try:
            logger.debug('Hacer busqueda')
            ElemValidar = gestAlmElements.gestAlMPCatBusInput  # Buscar
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarValor = self.newcat
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I search a catalog" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search a catalog --> {}'.format(resStep))
        assert resStep

    @step('I delete a catalog')
    def borro_catalogo(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I delete a catalog')
        resStep = True
        try:
            logger.debug('Eliminar')
            ElemValidar = gestAlmElements.gestAlMPCDelXPath  # Botón Borrar Catálogo
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPCatDelXPath
            nuevocat = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text  # Cátalogo buscado
            if nuevocat == self.newcat:
                logger.debug('El catálogo ' + self.newcat + ' ha sido encontrado')
                ElemValidar = gestAlmElements.gestAlMPCatNewDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPCatNewDelOKXPath  # Eliminar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('El catálogo ' + self.newcat + ' ha sido borrado')
            else:
                logger.debug('El catálogo '+ self.newcat + ' NO ha sido encontrado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I delete a catalog" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I delete a catalog --> {}'.format(resStep))
        assert resStep

    @then('I export catalogs')
    def exporto_catalogo(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export catalogs')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:65]  # nombre original del fichero sin segundos ni extension, ej: Listado de catálogos_20241104_0956
            self.ficheroMPcat = gestAlmElements.gestAlmExpFMPCatTXT + self.ficexp[56:79]  # Nombre fichero completo, ej: Listado de catálogos_20241104_09561572.xlsx
            nombre = gestAlmElements.gestAlmExpDesFMPCTXT
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroMPcat) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export catalogs" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export catalogs --> {}'.format(resStep))
        assert resStep

    @then('I open catalog file')
    def abro_catalogo_exportado(self):
        logger.debug('INICIO STEP: I open catalog file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            primeraLinea = gestAlmElements.gestAlmExpFMPCatTXT + ' (Global)'
            resStep= abrirFichero(resStep, primeraLinea, self.ficheroMPcat)
        except Exception as e:
            logger.error('Algún elemento en "I open catalog file" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open catalog file  --> {}'.format(resStep))
        assert resStep

    @step('I click ingredients')
    def click_ingredientes(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click ingredients')
        resStep = True
        try:
            logger.debug('Selecciono ingredients')
            ElemValidar = gestAlmElements.latPagGestMInXPath  # Ingredientes
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmPIDelXPath # espera para cargar la tabla
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        except Exception as e:
            logger.error('Algún elemento en "I click ingredients" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click ingredients --> {}'.format(resStep))
        assert resStep

    @then('I see ingredients')
    def veo_ingredientes_materiasprimas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see ingredients')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMPIngTitXPath  # LISTADO DE INGREDIENTES
            ElemValidarTXT = gestAlmElements.gestAlmIngTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Búsqueda Avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmNItemID  # Nuevo ingrediente
            ElemValidarTXT = gestAlmElements.gestAlMPIngNewTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosProdXPath  # Mostrando..productos,ingredientes
            ElemValidarTXT = gestAlmElements.gestAlmPInMosTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo1XPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo2XPath  # Categoría
            ElemValidarTXT = gestAlmElements.gestAlmCategTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo3XPath  # Unidad de receta
            ElemValidarTXT = gestAlmElements.gestAlMPIngURTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo4XPath  # Precio elegido
            ElemValidarTXT = gestAlmElements.gestAlMPIngPETXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo5XPath  # Precio máx.
            ElemValidarTXT = gestAlmElements.gestAlMPIngPMaxTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo6XPath  # Precio mín.
            ElemValidarTXT = gestAlmElements.gestAlMPIngPMinTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo7XPath  # Precio medio
            ElemValidarTXT = gestAlmElements.gestAlMPIngPMedTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo8XPath  # Precio medio ponderado
            ElemValidarTXT = gestAlmElements.gestAlMPIngPMPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo9XPath  # Controlar en inventario
            ElemValidarTXT = gestAlmElements.gestAlMPIngCITXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo10XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Mas columnas, selecciono campo')
            ElemValidar = gestAlmElements.gestAlmMPMasColConfXPath # ajustes más columnas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPIMCCIXPath # Código interno
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar =  gestAlmElements.gestAlmMCoKO1XPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar =  gestAlmElements.gestAlmMCoOK2XPath # Guardar
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('Verifico nueva columna: código interno')
            ElemValidar = gestAlmElements.gestAlmMPPCo1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Mas columnas, desselecciono campo')
            ElemValidar = gestAlmElements.gestAlmMPMasColConfXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPIMCURXPath # Unidad de receta
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar =  gestAlmElements.gestAlmMCoOK2XPath# Guardar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('Verifico nueva columna: código interno')
            ElemValidar = gestAlmElements.gestAlmMPPCo4XPath  # En la columna de unidad de receta, está Precio elegido
            ElemValidarTXT = gestAlmElements.gestAlMPIngPETXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Mas columnas, selecciono TODO')
            ElemValidar = gestAlmElements.gestAlmMPPMCoXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('Verifico nueva columna: código interno')
            ElemValidar = gestAlmElements.gestAlmMPPCo4XPath  # En la columna de unidad de receta, está unidad de receta
            ElemValidarTXT = gestAlmElements.gestAlMPIngURTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see ingredients" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see ingredients --> {}'.format(resStep))
        assert resStep

    @step('I click to create an item')
    def click_crear_ingrediente(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click to create an item')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlmNItemID  # Nuevo ingrediente
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click to create an item" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to create an item --> {}'.format(resStep))
        assert resStep

    @step('I valid ingredients')
    def click_crear_ingredientes(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid ingredients')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPINITitXPath  # Título
            ElemValidarTXT = gestAlmElements.gestAlMPINITitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPININomXPath  # Nombre*
            ElemValidarTXT = gestElements.gestNom2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINIUReXPath  # Unidad de receta*
            ElemValidarTXT = gestAlmElements.gestAlmMPCreURTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINICatXPath  # Categoría*
            ElemValidarTXT = gestAlmElements.gestAlmCateg2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINITipCatXPath  # Tipo Categoría
            ElemValidarTXT = gestAlmElements.gestAlMPINITipCatTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINIContXPath  # Contabilidad
            ElemValidarTXT = gestAlmElements.gestAlmConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINIAlertXPath # Mostrar Alerta
            ElemValidarTXT = gestAlmElements.gestAlMPINIAlertTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINIConInvXPath  # Controlar en inventario
            ElemValidarTXT = gestAlmElements.gestAlMPINIConInvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINIMarXPath # Marcas
            ElemValidarTXT = gestAlmElements.gestAlmMarTXT
            ElemValidar = gestAlmElements.gestAlMPINIOKXPath  # Crear ingrediente
            ElemValidarTXT = gestAlmElements.gestAlMPINIOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPINIKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I valid ingredients" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid ingredients --> {}'.format(resStep))
        assert resStep

    @step('I create an ingredient with all fields')
    def crear_ingrediente_todosloscampos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create an ingredient with all fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPININomInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlMPININomValor + '_allFields'
            self.ing = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPINIUReSel  #  Listado unidad de receta
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINIUReInput
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINICatSel  #  Escojo categoría
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINICatInput # Aguas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINITipCatInput  # Bebida
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidarTXT = gestAlmElements.gestAlMPINITipCatValor
            ini = 0
            fin = 6
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMPINIAlertInput
            ElemValidarValor = gestAlmElements.gestAlMPINIAlertValor # 10
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPINIConInvInput  # Check
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINIMarID  #  Escojo marca
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMPINIMarValor # Lobrador
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINIOKXPath  # Crear
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmBusInput
            WebDriverWait(pagina_gestAlm, 50).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            time.sleep(5)
        except Exception as e:
            logger.error('Algún elemento en "I create an ingredient with all fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create an ingredient with all fields --> {}'.format(resStep))
        assert resStep


    @step('I create an ingredient with mandatory fields')
    def crear_ingrediente_camposobligatorios(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create an ingredient with mandatory fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPININomInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlMPININomValor + '_mandatoryFields'
            self.ing = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPINIUReSel  #  Listado unidad de receta
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINIUReInput
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINICatSel  #  Escojo categoría
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINICatInput # Aguas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPINITipCatInput  # Bebida
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidarTXT = gestAlmElements.gestAlMPINITipCatValor
            ini = 0
            fin = 6
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMPINIAlertInput
            ElemValidarValor = gestAlmElements.gestAlMPINIAlertValor # 10
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPINIOKXPath  # Crear
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmBusInput
            WebDriverWait(pagina_gestAlm, 50).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            time.sleep(100)
        except Exception as e:
            logger.error('Algún elemento en "I create an ingredient with mandatory fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create an ingredient with mandatory fields --> {}'.format(resStep))
        assert resStep


    @step('I modify an ingredient')
    def modifico_ingrediente(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I modify an ingredient')
        resStep = True
        try:
            logger.debug('Busco el ingrediente')
            ElemValidar = gestAlmElements.gestAlmBusInput
            buscaring = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscaring.click()
            time.sleep(2)
            buscaring.send_keys(self.ing)
            time.sleep(4)
            ElemValidar = gestAlmElements.gestAlMPCategTABLA # Tabla
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ingredient = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if self.ing == ingredient :
                logger.debug('El ingrediente' + ingredient + ' ha sido encontrado')
                ElemValidar = gestAlmElements.gestAlMPIngEditXPath  # Icono Editar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPIngETitXPath  # MODIFICAR ingrediente
                ElemValidarTXT = gestAlmElements.gestAlMPIngETitTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngENomXPath  # Nombre*
                ElemValidarTXT = gestElements.gestNom2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngEURXPath  # Unidad de receta*
                ElemValidarTXT = gestAlmElements.gestAlmMPCreURTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngECatXPath  # Categoria*
                ElemValidarTXT = gestAlmElements.gestAlmCateg2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngETCaXPath  # Tipo de categoria*
                ElemValidarTXT = gestAlmElements.gestAlMPINITipCatTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngEContXPath  # Contabilidad
                ElemValidarTXT = gestAlmElements.gestAlmConTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngEAlertXPath  # Mostrar alerta de stock bajo con cantidad inferior a*
                ElemValidarTXT = gestAlmElements.gestAlMPINIAlertTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngEMarXPath  # Marcas
                ElemValidarTXT = gestAlmElements.gestAlmMarTXT
                ini = 0
                fin = 6
                obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
                ElemValidar = gestAlmElements.gestAlMPIngEConInvXPath  # Controlar en inventario
                ElemValidarTXT = gestAlmElements.gestAlMPINIConInvTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPIngENomInput  # Nombre
                ElemValidarValor = self.ing + '_modif'
                self.ing = ElemValidarValor
                rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
                ElemValidar = gestAlmElements.gestAlMPIngECatSel  # Escojo categoría
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPIngECatInput  # Categoria
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPIngEConInvXPath  # desmardo controlar en inventario
                ElemValidarTXT = gestAlmElements.gestAlMPIngCITXT
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngEKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPIngEOKXPath  # Modificar
                ElemValidarTXT = gestElements.gestMOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('El ingrediente' + self.ing + ' ha sido modificado')
                ElemValidar = gestAlmElements.gestAlmBusInput
                WebDriverWait(pagina_gestAlm, 50).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
                time.sleep(5)
                resStep = True & resStep
            else:
                logger.debug('El ingrediente' + self.inf + ' NO ha sido encontrado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I modify an unit" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I modify an unit --> {}'.format(resStep))
        assert resStep

    @then('I search and delete an ingredient')
    def buscaryborrar_nuevo_ingrediente(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete an ingredient')
        resStep = True
        try:
            logger.debug('Busco y borro el ingrediente')
            ElemValidar = gestAlmElements.gestAlmBusInput
            buscaring = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscaring.click()
            buscaring.clear()
            ElemValidar = gestAlmElements.gestAlmPIDelXPath # espera para cargar la tabla
            WebDriverWait(pagina_gestAlm, 30).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            buscaring.send_keys(self.ing)
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmBusIngValor
            ingrediente = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(ingrediente)
            if self.ing == ingrediente :
                logger.debug('El ingrediente '+ ingrediente + ' ha sido encontrado')
                ElemValidar = gestAlmElements.gestAlmPIDelXPath  # Icono borrar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

                ElemValidar = gestAlmElements.gestAlMPINIDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPINIDelOKXPath  # Eliminar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('El producto ' + ingrediente + ' ha sido eliminado')
                time.sleep(2)
                resStep = True & resStep
            else:
                logger.debug('El ingrediente ' + ingrediente + ' NO ha sido encontrado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete an ingredient" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete an ingredient --> {}'.format(resStep))
        assert resStep

    @then('I export ingredients')
    def exporto_MP_ingredientes(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export ingredients')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:63]  # nombre original del fichero sin segundos ni extension, ej: Listado%20de%20ingredientes_20240927_1229
            self.ficheroing = gestAlmElements.gestAlmExpFMPIngTXT + self.ficexp[54:77] # Nombre fichero completo, ej: Listado de ingredientes_20240927_12293623.xlsx
            logger.info(self.ficheroing)
            nombre = gestAlmElements.gestAlmExpDesFMPITXT
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroing) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export ingredients" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export ingredients --> {}'.format(resStep))
        assert resStep

    @then('I open ingredients file')
    def abro_ingredientes_exportado(self):
        logger.debug('INICIO STEP: I open ingredients file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            # to load the workbook with its path
            primeraLinea = gestAlmElements.gestAlmExpFMPIngTXT + ' (Global)'
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroing)
        except Exception as e:
            logger.error('Algún elemento en "I open ingredients file" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open ingredients file  --> {}'.format(resStep))
        assert resStep

    @then('I valid form advance search ingredient')
    def valido_formulario_busquedaavanzada_ingrediente(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form advance search ingredient')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBARefXPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBACIAXPath  # Controlar en inventario
            ElemValidarTXT = gestAlmElements.gestAlMPIngCITXT
            ini = 0
            fin = 23
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmC1XPath # Categoría*
            ElemValidarTXT = gestAlmElements.gestAlmCateg2TXT
            ini= 0
            fin= 9
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmC2XPath  # Tipo de categoría
            ElemValidarTXT = gestAlmElements.gestAlMPINITipCatTXT
            ini= 0
            fin= 17
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(5)
        except Exception as e:
            logger.error('Algún elemento en "I valid form advance search ingredient" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form advance search ingredient --> {}'.format(resStep))
        assert resStep


    @then('I do advance search ingredient')
    def hago_busqueda_avanzada_ingrediente(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search ingredient')
        resStep = True
        try:
            logger.debug('relleno de los campos')
            ElemValidar = gestAlmElements.gestAlmMPBIngRefInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlmMPBAIngValor # ALHAMBRA
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlmMPBACatInput  # Categoría
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlmMPBACatValor  # Selecciono Categoría
            cat = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if cat == gestAlmElements.gestAlmMPBACatNombre:
                logger.debug ('La categoría ' + cat + ' ha sido encontrada')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.debug('La categoría ' + cat + 'NO  ha sido encontrada')
                resStep = False
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Verifico resultado')
            ElemValidar = gestAlmElements.gestAlMPIBusXPath
            ElemValidarTXT = gestAlmElements.gestAlmMPBAIngValor # 'ALHAMBRA'
            primervalor = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if primervalor == ElemValidarTXT:
                logger.debug('La busqueda avanzada de: ' + ElemValidarTXT + ' es correcta')
                resStep = True & resStep
            else:
                logger.debug('La busqueda avanzada de: ' + ElemValidarTXT + ' NO es correcta')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I do advance search ingredient" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search ingredient --> {}'.format(resStep))
        assert resStep

    @step('I click materias primas categories')
    def click_categorias(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click materias primas categories')
        resStep = True
        try:
            logger.debug('Selecciono materias primas,categorias')
            ElemValidar = gestAlmElements.latPagGestMCateXPath  # categorias
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPCategTABLA  # Tabla cargada
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        except Exception as e:
            logger.error('Algún elemento en "I click materias primas categories" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click materias primas categories --> {}'.format(resStep))
        assert resStep

    @then('I see categories of materias primas')
    def veo_categorías_materiasprimas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see categorias of materias primas')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMPCategTitXPath  # Listado de categorías
            ElemValidarTXT = gestAlmElements.gestAlmCategTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPBusXPath  # Buscar
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Búsqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPCategNewID  # Nueva categoría
            ElemValidarTXT = gestAlmElements.gestAlMPCategNewTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo2XPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo3XPath  # Tipo de categoría
            ElemValidarTXT = gestAlmElements.gestAlMPCategTipCatTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo4XPath  # Contabilidad
            ElemValidarTXT = gestAlmElements.gestAlmConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo5XPath  # Ingredientes
            ElemValidarTXT = gestAlmElements.gestAlMPCategIngGenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPPCo6XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see categorias of materias primas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see categorias of materias primas --> {}'.format(resStep))
        assert resStep

    @then('I export categories')
    def exporto_categorías(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export categories')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[27:66]  # nombre original del fichero sin segundos ni extension, ej: Listado de categorías_20241211_1257
            self.ficherocateg = gestAlmElements.gestAlmExpFMPCategTXT + self.ficexp[57:90]  # Nombre fichero completo, ej: Listado de categorias_20240927_12293623.xlsx
            nombre = gestAlmElements.gestAlmExpDesFMPCategTXT
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficherocateg) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export categories" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export categories --> {}'.format(resStep))
        assert resStep

    @then('I open categories file')
    def abro_fichero_categorías_exportado(self):
        logger.debug('INICIO STEP: I open categories file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFMPCategTXT + ' (Global)'
            resStep = abrirFichero(resStep, primeraLinea, self.ficherocateg)
        except Exception as e:
            logger.error('Algún elemento en "I open categories file" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open categories file  --> {}'.format(resStep))
        assert resStep


    @then('I valid form advance search categories')
    def busqueda_avanzada_categorias(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form advance search categories')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada categorías')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBACategNomXPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBACategTypXPath  # Tipo de categoría
            ElemValidarTXT = gestAlmElements.gestAlMPCategTipCatTXT #
            ini = 0
            fin = 17
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMPBACategConXPath  # Contabilidad
            ElemValidarTXT = gestAlmElements.gestAlmConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I valid form advance search categories" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form advance search categories--> {}'.format(resStep))
        assert resStep

    @then('I do advance search categories')
    def hago_busqueda_avanzada_categorias(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search categories ')
        resStep = True
        try:
            logger.debug('relleno de los campos busqueda avanzada catg')
            ElemValidar = gestAlmElements.gestAlmMPBACategNomInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlmMPBACatNombre # Cervezas
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMPCategTypeInput  # Tipo de Categoría
            time.sleep(3)
            ElemValidarValor = gestAlmElements.gestAlMPINITipCatValor  # Bebida
            typcateg = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if typcateg == ElemValidarValor:
                logger.debug ('El tipo de categoría ' + typcateg + ' ha sido encontrada')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.debug('El tipo de categoría ' + typcateg + 'NO  ha sido encontrada')
                resStep = False
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)

            logger.debug('Verifico resultado')
            ElemValidar = gestAlmElements.gestAlmMPBACategResXPath
            categ = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidarTXT = gestAlmElements.gestAlmMPBACatNombre  # Cervezas
            logger.info(categ)
            if categ == ElemValidarTXT:
                logger.debug('La busqueda avanzada de: ' + categ + ' es correcta')
                resStep = True & resStep
            else:
                logger.debug('La busqueda avanzada de: ' + categ + ' NO es correcta')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I do advance search categories" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search categories categories --> {}'.format(resStep))
        assert resStep


    @when('I click to create a category')
    def click_crear_categoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click to create a category')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlmMPCategNewID  # Nueva categoría
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I click to create a category" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to create a category --> {}'.format(resStep))
        assert resStep

    @step('I valid form new category')
    def valido_form_nuevacategoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form new category')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPCategNewTitXPath  # Título
            ElemValidarTXT = gestAlmElements.gestAlMPCategNewTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategNewNomXPath  # Nombre*
            ElemValidarTXT = gestElements.gestNom2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategNewTCXPath  # Tipo de categoría*
            ElemValidarTXT = gestAlmElements.gestAlMPINITipCatTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategNewContXPath  # Contabilidad
            ElemValidarTXT = gestAlmElements.gestAlmConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategIGenXPath  # Ingredientes genericos
            ElemValidarTXT = gestAlmElements.gestAlMPCategIngGenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategNewOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategNewKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I valid form new category" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form new category --> {}'.format(resStep))
        assert resStep


    @step('I valid form edit category')
    def valido_form_edicioncategoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form edit category')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPCategAETitXPath  # Título
            ElemValidarTXT = gestAlmElements.gestAlMPCategEdiTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategAENomXPath  # Nombre*
            ElemValidarTXT = gestElements.gestNom2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategAETCXPath  # Tipo de categoría*
            ElemValidarTXT = gestAlmElements.gestAlMPINITipCatTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategAEContXPath  # Contabilidad
            ElemValidarTXT = gestAlmElements.gestAlmConTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategAEIGenXPath  # Ingredientes genericos
            ElemValidarTXT = gestAlmElements.gestAlMPCategIngGenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategAEOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategAEKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I valid form edit category" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form edit category --> {}'.format(resStep))
        assert resStep

    @step('I create a category with all fields')
    def crear_categoría_todosloscampos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create a category with all fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPCategNewInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlMPCategNewValor + '_allFfields'
            self.categoria = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCategType2Input  # Tipo de Categoría
            ElemValidarValor = gestAlmElements.gestAlMPINITipCatValor  # Bebida
            typcateg = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if typcateg == ElemValidarValor:
                logger.debug ('El tipo de categoría ' + typcateg + ' ha sido encontrada')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.debug('El tipo de categoría ' + typcateg + 'NO  ha sido encontrada')
                resStep = False
            ElemValidar = gestAlmElements.gestAlMPCategNewContInput # Contabilidad
            ElemValidarValor = gestAlmElements.gestAlMPCategNewContValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCategIGenXPath # Ingredientes genéricos
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPCategNewOKXPath  # Aceptar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I create a category with all fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create a category with all fields --> {}'.format(resStep))
        assert resStep

    @step('I create a category with mandatory fields')
    def crear_categoría_camposobligatorios(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create a category with mandatory fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPCategNewInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlMPCategNewValor + '_mandatoryfields'
            self.categoria = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCategType2Input  # Tipo de Categoría
            ElemValidarValor = gestAlmElements.gestAlMPINITipCatValor  # Bebida
            typcateg = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if typcateg == ElemValidarValor:
                logger.debug ('El tipo de categoría ' + typcateg + ' ha sido encontrada')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.debug('El tipo de categoría ' + typcateg + 'NO  ha sido encontrada')
                resStep = False
            ElemValidar = gestAlmElements.gestAlMPCategNewOKXPath  # Aceptar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I create a category with mandatory fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create a category with mandatory fields --> {}'.format(resStep))
        assert resStep

    @then('I click to action edit category')
    def edito_categoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I click to action edit category')
        resStep = True
        try:
            logger.debug('Edito categoría')
            ElemValidar = gestAlmElements.gestAlMPCategAEXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(10)
        except Exception as e:
            logger.error('Algún elemento en "I click to action edit category" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to action edit category --> {}'.format(resStep))
        assert resStep

    @when('I search a category')
    def busco_categoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search a category')
        resStep = True
        try:
            logger.debug('Busco la categoría')
            ElemValidar = gestAlmElements.gestAlMPCategBusInput
            buscarcateg = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscarcateg.click()
            time.sleep(1)
            buscarcateg.send_keys(self.categoria)
            ElemValidar = gestAlmElements.gestAlmBusCategValor
            categ = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(categ)
            if self.categoria == categ:
                logger.debug('La categoría ' + self.categoria + ' ha sido encontrada')
                resStep = True & resStep
            else:
                logger.debug('La categoría ' + self.categoria + ' NO ha sido eliminada')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search a category" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search a category --> {}'.format(resStep))
        assert resStep

    @step('I modify the category')
    def modifico_categoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I modify the category')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPCategAENomInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlMPCategNewValor + '_modif'
            self.categoria = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCategAEContInput  # Contabilidad
            ElemValidarValor = gestAlmElements.gestAlMPCategNewContValor + '_modif'
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPCategAEIGenXPath  # Ingredientes genéricos
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            ElemValidar = gestAlmElements.gestAlMPCategAETypInput  # Tipo de Categoría
            ElemValidarValor = gestAlmElements.gestAlmStOtrosTXT  # Otros
            typcateg = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if typcateg == ElemValidarValor:
                logger.debug('El tipo de categoría ' + typcateg + ' ha sido encontrada')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.debug('El tipo de categoría ' + typcateg + 'NO  ha sido encontrada')
                resStep = False
            ElemValidar = gestAlmElements.gestAlMPCategAEKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPCategAEOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I modify the category" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I modify the category --> {}'.format(resStep))
        assert resStep

    @then('I search and delete a category')
    def buscaryborrar_categoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete a category')
        resStep = True
        try:
            logger.debug('Busco la categoría')
            ElemValidar = gestAlmElements.gestAlMPCategBusInput
            buscarcateg = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscarcateg.click()
            time.sleep(1)
            buscarcateg.send_keys(self.categoria)
            ElemValidar = gestAlmElements.gestAlmMPBACategResXPath
            categ = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(categ)
            if self.categoria == categ:
                logger.debug('La categoría '+ categ + ' ha sido encontrada')
                ElemValidar = gestAlmElements.gestAlMPCategADelXPath  # Icono borrar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPCategADelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPCategADelOKXPath  # Aceptar
                ElemValidarTXT = gestElements.gestAOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('La categoría ' + categ + ' ha sido eliminada')
                time.sleep(2)
            else:
                logger.debug('La categoría '+ categ + ' NO ha sido eliminada')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete a category" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete a category --> {}'.format(resStep))
        assert resStep

    @step('I click materias primas units')
    def buscaryborrar_categoría(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I click materias primas units')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestMUnXPath  # unidades
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPUnitTABLA  # Tabla cargada
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        except Exception as e:
            logger.error('Algún elemento en "I click materias primas units" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click materias primas units --> {}'.format(resStep))
        assert resStep

    @then('I see units of materias primas')
    def veo_unidades_materiasprimas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see units of materias primas')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmLisTitXPath  # Listado de unidades
            ElemValidarTXT = gestAlmElements.gestAlmUnitTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPUBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMPUFilXPath  # Filtros:
            ElemValidarTXT = gestElements.gestFilTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitAlmXPath # Almacenamiento
            ElemValidarTXT = gestAlmElements.gestAlMPUnitAlmTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitRecXPath  # Receta
            ElemValidarTXT = gestAlmElements.gestAlMPUnitRecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see units of materias primas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see units of materias primas --> {}'.format(resStep))
        assert resStep

    @then('I advance page units')
    def avanzar_pagina_unidades(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I advance page units')
        resStep = True
        try:
            Pg1 = gestAlmElements.gestAlMPUnitPg1XPath
            Pg1TXT = gestAlmElements.gestAlMPUnitPg1TXT
            Mos = gestAlmElements.gestAlmMosUnitXPath
            AvP = gestAlmElements.gestAlMPUnitAvPXPath
            MP1 = gestAlmElements.gestAlmPUnitM1TXT
            MP2 = gestAlmElements.gestAlmPUnitM2TXT
            MP3 = gestAlmElements.gestAlmPUnitM3TXT
            MP4 = gestAlmElements.gestAlmPUnitM4TXT
            MP5 = gestAlmElements.gestAlmPUnitM5TXT
            resStep = avanzar_pagina(resStep, pagina_gestAlm, Pg1, Pg1TXT, Mos, AvP, MP1, MP2, MP3, MP4, MP5)
        except Exception as e:
            logger.error('Algún elemento en "I advance page units" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I advance page units--> {}'.format(resStep))
        assert resStep

    @then('I turn back page units')
    def retroceder_pagina_unidades(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I turn back page units')
        resStep = True
        try:
            Pg5 = gestAlmElements.gestAlMPUnitPg5XPath
            Pg5TXT = gestAlmElements.gestAlMPUnitPg5TXT
            Mos = gestAlmElements.gestAlmMosUnitXPath
            ReP = gestAlmElements.gestAlMPUnitRePXPath
            MP1 = gestAlmElements.gestAlmPUnitM1TXT
            MP2 = gestAlmElements.gestAlmPUnitM2TXT
            MP3 = gestAlmElements.gestAlmPUnitM3TXT
            MP4 = gestAlmElements.gestAlmPUnitM4TXT
            MP5 = gestAlmElements.gestAlmPUnitM5TXT
            ElemValidar = retroceder_pagina(resStep, pagina_gestAlm, Pg5, Pg5TXT, Mos, ReP, MP1, MP2, MP3, MP4,MP5)
        except Exception as e:
            logger.error('Algún elemento en "I turn back page units" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I turn back page units --> {}'.format(resStep))
        assert resStep


    @then('I export units')
    def exporto_unidades(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export units')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombre = gestAlmElements.gestAlmExpDesFMPUnitsTXT # Listado%20de%20unidades_
            nombreficorig = self.ficexp[27:59]  # nombre original del fichero sin segundos ni extension, ej: Listado de unidades_20241211_12572787
            self.ficherounits = gestAlmElements.gestAlmExpFMPUnitsTXT + self.ficexp[50:73]  # Nombre fichero completo, ej: Listado de unidades_20240927_12293623.xlsx
            logger.info('self.ficherounits es ' + self.ficherounits)
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficherounits) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export units" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export units --> {}'.format(resStep))
        assert resStep


    @then('I open units file')
    def abro_fichero_unidades_exportado(self):
        logger.debug('INICIO STEP: I open units file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFMPUnitsTXT + ' (Global)'
            resStep = abrirFichero(resStep, primeraLinea, self.ficherounits)
        except Exception as e:
            logger.error('Algún elemento en "I open units file" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open units file  --> {}'.format(resStep))
        assert resStep


    @step('I click to create an unit')
    def click_crear_unidad(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click to create an unit')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPUnitNewID  # Nueva unidad
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(4)
        except Exception as e:
            logger.error('Algún elemento en "I click to create an unit" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to create an unit --> {}'.format(resStep))
        assert resStep


    @step('I valid form new unit')
    def valido_form_nuevaunidad(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form new unit')
        resStep = True # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPUnitNewTitXPath  # Título
            ElemValidarTXT = gestAlmElements.gestAlMPUnitNewTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitNewNomXPath  # Nombre*
            ElemValidarTXT = gestElements.gestNom2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitNewAbrXPath  # Abreviatura
            ElemValidarTXT = gestAlmElements.gestAlMPUnitAbrTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitNewComXPath  # Compra
            ElemValidarTXT = gestAlmElements.gestAlMPUnitComTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitNewAlmXPath  # Almacenamiento
            ElemValidarTXT = gestAlmElements.gestAlMPUnitAlmTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitNewRecXPath  # Receta
            ElemValidarTXT = gestAlmElements.gestAlMPUnitRecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitNewOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMPUnitNewKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I valid form new unit" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form new unit --> {}'.format(resStep))
        assert resStep


    @step('I create an unit with all fields')
    def crear_unidad_todosloscampos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create an unit with all fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPUnitNewNomInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlMPUnitNewNomValor + '_ALLFIELDS'
            self.unidad = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPUnitNewAbrInput  # Abreviatura
            ElemValidarValor = gestAlmElements.gestAlMPUnitNewAbrValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlMPUnitNewComXPath # Compra
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPUnitNewAlmXPath # Almacenamiento
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPUnitNewRecXPath # Receta
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMPUnitNewOKXPath  # Aceptar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I create an unit with all fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create an unit with all fields --> {}'.format(resStep))
        assert resStep


    @step('I create an unit with mandatory fields')
    def crear_unidad_campos_obligatorios(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create an unit with mandatory fields')
        resStep = True  # necesario si no, no entra en el try
        try:
            ElemValidar = gestAlmElements.gestAlMPUnitNewNomInput  # Nombre
            ElemValidarValor = gestAlmElements.gestAlMPUnitNewNomValor + '_MANDATORYFIELDS'
            self.unidad = ElemValidarValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
        except Exception as e:
            logger.error('Algún elemento en "I create an unit with mandatory fields" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create an unit with mandatory fields --> {}'.format(resStep))
        assert resStep

    @then('I modify an unit')
    def edito_unidad(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I modify an unit')
        resStep = True
        try:
            logger.debug('Busco la unidad')
            ElemValidar = gestAlmElements.gestAlmBusUnitInput
            buscarunit = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscarunit.click()
            time.sleep(2)
            buscarunit.send_keys(self.unidad)
            ElemValidar = gestAlmElements.gestAlmBusUnitValor
            nuevaunit = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if self.unidad == nuevaunit:
                logger.debug('La unidad '+ nuevaunit + ' ha sido encontrada')
                ElemValidar = gestAlmElements.gestAlMPUnitEditXPath  # Icono Editar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPUnitModTitXPath  # MODIFICAR UNIDAD
                ElemValidarTXT = gestAlmElements.gestAlMPUnitModTitTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPUnitModNomXPath  # Nombre*
                ElemValidarTXT = gestElements.gestNom2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPUnitModAbrXPath  # Abreviatura
                ElemValidarTXT = gestAlmElements.gestAlMPUnitAbrTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPUnitModNomInput  # Nombre
                ElemValidarValor = gestAlmElements.gestAlMPUnitModNomValor
                self.unidadm = ElemValidarValor
                rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
                ElemValidar = gestAlmElements.gestAlMPUnitModAbrInput  # Abreviatura
                ElemValidarValor = gestAlmElements.gestAlMPUnitModAbrValor
                rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
                ElemValidar = gestAlmElements.gestAlMPUnitEditKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPUnitEditOKXPath  # Modificar
                ElemValidarTXT = gestElements.gestMOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('La unidad ' + nuevaunit + ' ha sido modificada')
                time.sleep(2)
            else:
                logger.debug('La unidad '+ nuevaunit + ' NO ha sido encontrada')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I modify an unit" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I modify an unit --> {}'.format(resStep))
        assert resStep


    @then('I search and delete an unit in buy')
    def buscaryborrar_nueva_unidad(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete an unit in buy')
        resStep = True
        try:
            logger.debug('Busco y borro la unidad en compra')
            ElemValidar = gestAlmElements.gestAlmBusUnitInput
            buscarunit = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscarunit.click()
            time.sleep(2)
            buscarunit.send_keys("qaner")
            ElemValidar = gestAlmElements.gestAlmBusUnitValor
            unit = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if self.unidad == unit or self.unidadm == unit:
                logger.debug('La unidad '+ unit + ' ha sido encontrada')
                ElemValidar = gestAlmElements.gestAlMPUnitDelXPath  # Icono Borrar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPUnitDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPUnitDelOKXPath  # Aceptar
                ElemValidarTXT = gestElements.gestAOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('La unidad ' + unit + ' ha sido eliminada')
                time.sleep(2)
            else:
                logger.debug('La unidad '+ unit + ' NO ha sido encontrada')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete an unit in buy" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete an unit in buy --> {}'.format(resStep))
        assert resStep


    @then('I search and delete an unit in storage')
    def buscaryborrar_nueva_unidad(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete an unit in storage')
        resStep = True
        try:
            logger.debug('Busco y borro la unidad en almacenamiento')
            ElemValidar = gestAlmElements.gestAlMPUnitAlmXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmBusUnitValor
            unit = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(self.unidad)
            logger.info(unit)
            if self.unidad == unit or self.unidadm == unit:
                logger.debug('La unidad '+ self.unidad + ' ha sido encontrada')
                ElemValidar = gestAlmElements.gestAlMPUnitDelXPath  # Icono Borrar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPUnitDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPUnitDelOKXPath  # Aceptar
                ElemValidarTXT = gestElements.gestAOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('La unidad ' + unit + ' ha sido eliminada')
                time.sleep(2)
            else:
                logger.debug('La unidad '+ self.unidad + ' NO ha sido encontrada')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete an unit in storage" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete an unit in storage --> {}'.format(resStep))
        assert resStep


    @then('I search and delete an unit in recipe')
    def buscaryborrar_nueva_unidad(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete an unit in recipe')
        resStep = True
        try:
            logger.debug('Busco y borro la unidad en receta')
            ElemValidar = gestAlmElements.gestAlMPUnitRecXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmBusUnitValor
            unit = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(self.unidad)
            logger.info(unit)
            if self.unidad == unit or self.unidadm == unit:
                logger.debug('La unidad '+ self.unidad + ' ha sido encontrada')
                ElemValidar = gestAlmElements.gestAlMPUnitDelXPath  # Icono Borrar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlMPUnitDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMPUnitDelOKXPath  # Aceptar
                ElemValidarTXT = gestElements.gestAOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('La unidad ' + unit + ' ha sido eliminada')
                time.sleep(2)
            else:
                logger.debug('La unidad '+ self.unidad + ' NO ha sido encontrada')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete an unit in recipe" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete an unit in recipe --> {}'.format(resStep))
        assert resStep


    @step('I click the store')
    def click_mercancia_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click the store')
        resStep = True
        try:
            logger.debug('Selecciono almacén de mercancía')
            ElemValidar = gestAlmElements.latPagGestMeAXPath  # Escojo almacén de mercancía
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERATABLA  # Almacenes cargados
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            logger.debug('Almacenes cargados')
        except Exception as e:
            logger.error('Algún elemento en "I click the store" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click the store --> {}'.format(resStep))
        assert resStep


    @then('I see store')
    def see_mercancia_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see store')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmLisTitXPath # LISTADO DE ALMACENES
            ElemValidarTXT = gestAlmElements.gestAlmAlmTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERATit2XPath # Almacenes intermedios
            ElemValidarTXT = gestAlmElements.gestAlMERATit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERATit3XPath # No hay almacenes intermedios
            ElemValidarTXT = gestAlmElements.gestAlMERATit3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERATit4XPath # Almacenes de restaurante
            ElemValidarTXT = gestAlmElements.gestAlMERATit4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAlmXPath # (9) LTL Fleming
            ElemValidarTXT = gestAlmElements.gestAlmSel2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAIc1XPath
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERAIc2XPath
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERAVUbXPath # Ver ubicaciones
            ElemValidarTXT = gestAlmElements.gestAlMERAVUbTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see store" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see store --> {}'.format(resStep))
        assert resStep


    @then('I see the email')
    def envio_email(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see the email')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMERAIc2XPath
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERAEEmXPath # EDITAR EMAIL
            ElemValidarTXT = gestAlmElements.gestAlMERAEEmTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAETitXPath # Email
            ElemValidarTXT = gestAlmElements.gestAlMERAETitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            modemail = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            modemail.send_keys('fleming_mod@lateral.com' )
            modemail.click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERAEOKXPath # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAEKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I see the email" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see the email --> {}'.format(resStep))
        assert resStep


    @then('I see locations')
    def veo_ubicaciones(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see locations')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMERAVUbXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERAUTitXPath # EDITAR EMAIL
            ElemValidarTXT = gestAlmElements.gestAlMERAUTitTXT # UBICACIONES EN ALMACÉN - LTL FLEMING
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUIc1XPath # icono1
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERAUDelXPath # borrar ubicacion
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERAUub1XPath # (410) Congelado
            ElemValidarTXT = gestAlmElements.gestAlMERAUub1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUub2XPath # (410) Refrigerado
            ElemValidarTXT = gestAlmElements.gestAlMERAUub2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUub3XPath # (89) Sala
            ElemValidarTXT = gestAlmElements.gestAlMERAUub3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUub4XPath # (90) Seco
            ElemValidarTXT = gestAlmElements.gestAlMERAUub4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUEdiXPath # editar ubicación1
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERAUETitXPath # Editar ubicación
            ElemValidarTXT = gestAlmElements.gestAlMERAUETitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUENomXPath # Nombre*
            ElemValidarTXT = gestElements.gestNom2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUENomInput # cambiar ubicacion: Congomelado
            modeub = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            modeub.click()
            time.sleep(2)
            ubicacion = gestAlmElements.gestAlMERAUDSelTXT + '' # congelado, NO MODIFICO NADA
            modeub.send_keys(ubicacion)
            ElemValidar = gestAlmElements.gestAlMERAUEKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUEOKXPath # Guardar
            ElemValidarTXT = gestElements.gestGOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERAUDelXPath # Borrar ubicación1
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERAUDSelXPath # Borrar ubicación
            ubdel = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(resStep)
            if ubdel == (gestAlmElements.gestAlMERAUDSelTXT + '') :
                ElemValidar = gestAlmElements.gestAlMERAUDOKXPath # Eliminar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMERAUDKOXPath # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() #### NO BORRO NADA
                logger.debug('La ubicación  ' + ubdel + ' ha sido borrada')
            else:
                logger.debug('La ubicación  ' + ubdel + ' NO ha sido borrada')
                resStep = False
            ElemValidar = gestElements.gestVolverID  # Volver
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I see locations" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see locations --> {}'.format(resStep))
        assert resStep


    @then('I see selected store')
    def veo_almacen_seleccionado(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see selected store')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMERAlmXPath # selecciono almacén
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlmTitCreXPath # STOCK EN ALMACÉN - LTL FLEMING
            ElemValidarTXT = gestAlmElements.gestAlMERASelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestVolverID # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERABusXPath # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAMarXPath # Marcas:
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosProAlmXPath # Mostrando..
            ElemValidarTXT = gestAlmElements.gestAlmMERAMosTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERABusInput # Buscar producto en almacén
            buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscar.send_keys(gestAlmElements.gestAlMERABusValor) # CERVEZA HEINEKEN
            ElemValidar = gestAlmElements.gestAlmMosProAlmXPath  # Mostrando..1 de 1
            ElemValidarTXT = gestAlmElements.gestAlmMERAMos1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERACodIXPath  # Cod Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAIngrXPath  # Ingrediente
            ElemValidarTXT = gestAlmElements.gestAlmIng4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERACanXPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUniXPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERACodSelXPath  # Cod Interno
            ElemValidarTXT = gestAlmElements.gestAlMERACodValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAIngSel2XPath  #  [LTL,PPZ,SGB]
            ElemValidarTXT = gestAlmElements.gestAlMERAIng2Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERACanSelXPath  # varia el valor a lo largo del tiempo
            #ElemValidarTXT = gestAlmElements.gestAlMERACanValor
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAUniSelXPath  # L
            ElemValidarTXT = gestAlmElements.gestAlMERAUniValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAIngSelXPath  # CERVEZA HEINEKEN (CAÑERO)
            ElemValidarTXT = gestAlmElements.gestAlMERAIngValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep # consulto ingrediente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # consulto ingrediente
            ElemValidar = gestAlmElements.gestAlMERAISTitXPath  # Visualización de stock
            ElemValidarTXT = gestAlmElements.gestAlMERAISTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAISFIXPath  # Fecha inicio*
            ElemValidarTXT = gestAlmElements.gestAlmFecIniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAISFFXPath # Fecha fin*
            ElemValidarTXT = gestAlmElements.gestAlmFecFinTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAISAspaXPath  # aspa
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERAISGrafID  # chart
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.ID, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERAISGraf2ID  # canvas
            WebDriverWait(pagina_gestAlm, 15).until(EC.invisibility_of_element_located((By.ID, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERAISOKXPath  # Cerrar
            ElemValidarTXT = gestElements.gestCOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see select store" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see select store --> {}'.format(resStep))
        assert resStep


    @then("I see location's preferences")
    def preferencias_ubicacion(self):
        pagina_gestAlm = self.driver
        logger.debug("INICIO STEP: I see location's preferences")
        resStep = True
        try:
             ElemValidar = gestAlmElements.gestAlMERAVUbXPath # Ver ubicaciones
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             time.sleep(2)
             ElemValidar = gestAlmElements.gestAlMERAUub1XPath # Congelado
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             ElemValidar = gestAlmElements.gestAlMERAPTab1XPath # Para que cargue la tabla
             WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
             ElemValidar = gestAlmElements.gestAlMERAPrefTITXPath  # PREFERENCIAS DE UBICACIÓN - CONGELADO
             ElemValidarTXT = gestAlmElements.gestAlMERAPrefTITTXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAVolID  # Volver
             ElemValidarTXT = gestElements.gestVolverTXT
             resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlmMERABusXPath  # Buscar:
             ElemValidarTXT = gestElements.gestBusTXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPrefFilXPath  # Filtros:
             ElemValidarTXT = gestElements.gestFilTXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAIng2Path  # Ingredientes
             ElemValidarTXT = gestAlmElements.gestAlmIng2TXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERASRe2XPath  # Subrecetas
             ElemValidarTXT = gestAlmElements.gestAlmSRec2TXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAProd2XPath  # Productos
             ElemValidarTXT = gestElements.gestProd2TXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPrefCPTXPath  # Cambiar para todos:
             ElemValidarTXT = gestAlmElements.gestAlMERAPrefCPTTXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlmBusAlmInput
             buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
             buscar.send_keys(gestAlmElements.gestAlmMPBAIngValor) # ALHAMBRA
             buscar.click()
             time.sleep(2)
             ElemValidar = gestAlmElements.gestAlMERAPTab1XPath  # Ingredientes, subrecetas y productos de carta
             ElemValidarTXT = gestAlmElements.gestAlMERAPTab1TXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPTab2XPath  # Mostrar
             ElemValidarTXT = gestAlmElements.gestAlMERAPTab2TXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPRes1XPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPRes1TXT # ALHAMBRA
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPResUltXPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPResUltTXT # P Alhambra Reservar
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPTab1XPath  # Cambiar orden
             logger.info('Cambio orden')
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             time.sleep(2)
             ElemValidar = gestAlmElements.gestAlMERAPRes1XPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPResUltTXT # P Alhambra Reservar
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPResUltXPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPResUlt2TXT # 1/3 Alhambra Reserva
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPTab1XPath  # Cambiar orden
             logger.info('Cambio orden otra vez')
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             ElemValidar = gestAlmElements.gestAlMERAPRes1XPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPResUlt2TXT # 1/3 Alhambra Reserva
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPResUltXPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPResUltTXT # P Alhambra Reservar
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPTab2OffTXT  # Activar/Desactivar Mostrar
             logger.info('Desactivo mostrar')
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Desctivado
             time.sleep(1)
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Activado
             logger.info('Activo mostrar')
             time.sleep(1)
             logger.info('Desactivo ingredientes')
             ElemValidar = gestAlmElements.gestAlMERAIng2Path
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Desactivo ingredientes
             time.sleep(2)
             # Desactivo ingredientes desaparecen los azules, de 9 elementos pasa a 6
             ElemValidar = gestAlmElements.gestAlMERAPrefDesIngXPath
             WebDriverWait(pagina_gestAlm, 15).until(EC.invisibility_of_element_located((By.XPATH, ElemValidar))) # compruebo el Mostrar del elemento 7
             logger.info('compruebo que el Mostrar del elemento 7 no está')
             logger.info('Activo ingredientes')
             ElemValidar = gestAlmElements.gestAlMERAIng2Path
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Activo ingredientes
             time.sleep(2)
             # Activo ingredientes de nuevo, y vuelve a haber 9
             ElemValidar = gestAlmElements.gestAlMERAPrefDesIngXPath
             WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
             logger.info('compruebo que el Mostrar del elemento 7 SI está')
             logger.info('Desactivo subrecetas')
             ElemValidar = gestAlmElements.gestAlMERAPrefSReXPath
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Desactivo subrecetas
             time.sleep(2)
             # NO CAMBIA NADA
             logger.info('Activo subrecetas')
             ElemValidar = gestAlmElements.gestAlMERAPrefSReXPath
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Activo subrecetas
             time.sleep(2)
             logger.info('Desactivo Productos')
             ElemValidar = gestAlmElements.gestAlMERAPrefProdXPath
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Desactivo productos
             time.sleep(2)
             # Desactivo products quedan tres
             ElemValidar = gestAlmElements.gestAlMERAPrefDesProXPath
             WebDriverWait(pagina_gestAlm, 15).until(EC.invisibility_of_element_located((By.XPATH, ElemValidar))) # compruebo el Mostrar del elemento 7
             logger.info('compruebo que el Mostrar del elemento 4 no está')
             logger.info('Activo productos')
             ElemValidar = gestAlmElements.gestAlMERAPrefProdXPath
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Activo productos
             time.sleep(2)
             # Activo ingredientes de nuevo, y vuelve a haber 9
             ElemValidar = gestAlmElements.gestAlMERAPrefDesProXPath
             WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
             logger.info('compruebo que el Mostrar del elemento 4 SI está')
             logger.info('Cambiar para todos')
             ElemValidar = gestAlmElements.gestAlMERAPrefCPTXPath
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             ElemValidar = gestAlmElements.gestAlMERAPrefCTTitXPath  # CAMBIAR todos
             ElemValidarTXT = gestAlmElements.gestAlMERAPrefCTTitTXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPrefCTAspaXPath # aspa
             WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
             ElemValidar = gestAlmElements.gestAlMERAPrefCTTit2XPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPrefCTTit2TXT # ¿Está seguro que quiere desactivar..
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPrefCTOKXPath
             ElemValidarTXT = gestAlmElements.gestAlMERAPrefCTOKTXT # Cambiar
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlMERAPrefCTKOXPath
             ElemValidarTXT = gestElements.gestKOTXT # Cancelar
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             logger.info('Volver')
             ElemValidar = gestAlmElements.gestAlMERAVolID
             pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
             time.sleep(2)
        except Exception as e:
            logger.error("Algún elemento en I see location's preferences no encontrado: {}".format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug("FIN STEP: I see location's preferences --> {}".format(resStep))
        assert resStep


    @step('I click the inventory')
    def click_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click the inventory')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestMeIXPath  # Inventario
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I click the inventory" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click the inventory --> {}'.format(resStep))
        assert resStep


    @then('I see the inventory')
    def ver_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see the inventory')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmLisTitXPath # LISTADO DE INVENTARIOS
            ElemValidarTXT = gestAlmElements.gestAlmInvTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep =  obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID # Búsqueda Avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT
            resStep =  obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestDesPlaID # Descargar plantilla
            ElemValidarTXT = gestElements.gestDesPlaTXT
            resStep =  obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINIID # Nuevo inventario
            ElemValidarTXT = gestAlmElements.gestAlMERINITXT
            resStep =  obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIBusXPath  # Buscar
            ElemValidarTXT = gestElements.gestBusTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIMarXPath  # Marcas
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIAllXPath  # Todas
            ElemValidarTXT = gestElements.gestAllTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIFilXPath  # Filtros
            ElemValidarTXT = gestElements.gestFilTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIBorXPath  # Borrador
            ElemValidarTXT = gestAlmElements.gestAlmStBor2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIProXPath  # Programado
            ElemValidarTXT = gestAlmElements.gestAlMERIProTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIComXPath  # Completado
            ElemValidarTXT = gestAlmElements.gestAlmStComTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIFecXPath  # Fecha:
            ElemValidarTXT = gestElements.gestFec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIFec2XPath  # Valor de fecha
            ElemValidarTXT = gestAlmElements.gestAlmFec2Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIMosXPath  # Mostrando..
            ElemValidarTXT = gestAlmElements.gestAlmMos6TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIFecInvXPath  # Fecha de inventario
            ElemValidarTXT = gestAlmElements.gestAlMERIFecInvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIFecCreXPath  # Fecha de creación
            ElemValidarTXT = gestElements.gestFecCreTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIAlmXPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIUbiXPath  # Ubicaciones
            ElemValidarTXT = gestElements.gestUbic2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIEstXPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERICreXPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIAccXPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see the inventory" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see the inventory --> {}'.format(resStep))
        assert resStep


    @then('I export inventories')
    def exporto_inventario(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export inventories')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombre = gestAlmElements.gestAlmExpDesFMerInvTXT # Listado%20de%20inventarios_
            nombreficorig = self.ficexp[27:62]  # nombre original del fichero sin segundos ni extension, ej: Listado de inventarios_20241211_12572787
            self.ficheroinv = gestAlmElements.gestAlmExpFMerInvTXT + self.ficexp[53:77]  # Nombre fichero completo, ej: Listado de inventarios_20240927_12293623.xlsx
            logger.debug('ficheroinv es ' + self.ficheroinv)
            logger.debug('nombreficorig ' + nombreficorig)
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroinv) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export inventories" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export inventories --> {}'.format(resStep))
        assert resStep


    @then('I open the inventory file')
    def abro_fichero_inventario_exportado(self):
        logger.debug('INICIO STEP: I open the inventory file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFMerInvTXT + ' (Global)'
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroinv)
        except Exception as e:
            logger.error('Algún elemento en "I open the inventory file" no encontrado: {}'.format(resStep, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open the inventory file  --> {}'.format(resStep))
        assert resStep


    @then('I valid inventory form advance search')
    def busqueda_avanzada_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid inventory form advance search')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada de inventarios')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFIXPath # Fecha inicio*
            ElemValidarTXT = gestAlmElements.gestAlmFecIniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFFXPath  # Fecha fin*
            ElemValidarTXT = gestAlmElements.gestAlmFecFinTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmC1XPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmC2XPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            ini = 0
            fin = 6
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERIATPBEXPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            ini = 0
            fin = 7
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERIUbECPCXPath  # Ubicación
            ElemValidarTXT = gestElements.gestUbic1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I valid inventory form advance search" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid inventory form advance search --> {}'.format(resStep))
        assert resStep

    @then('I do advance search inventory')
    def hago_busqueda_avanzada_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search inventory')
        resStep = True
        try:
            logger.info('Relleno la búsqueda avanzada de inventario')
            ElemValidar = gestAlmElements.gestAlMERIFIInput  # Fecha inicio
            ElemValidarValor = gestElements.gestFIInput
            #rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor) # no va
            ElemValidar = gestAlmElements.gestAlMERIFFInput  # Fecha fin
            ElemValidarValor = gestElements.gestFFInput
            #rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor) # no va
            ElemValidar = gestAlmElements.gestAlMERIBusAvdStXPath # Estado: Completado
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERIBusAvdAlXPath # Almacen: LTL Fleming
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERIUbInput  # Ubicación: Congelado
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Verifico resultado busqueda avanzada inventario')
            ElemValidar = gestAlmElements.gestAlMERIBAResAlXPath # LTL Fleming
            ElemValidarTXT = gestAlmElements.gestAlmSelTXT
            valoralm = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info(valoralm)
            logger.info(ElemValidarTXT)
            ElemValidar1 = gestAlmElements.gestAlMERIBAResUbXPath # Ubicación: Congelado
            ElemValidarTXT1 = gestAlmElements.gestAlMERAUDSelTXT
            valorub = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar1).text
            logger.info(ElemValidarTXT1)
            logger.info(valorub)
            if valoralm == ElemValidarTXT and valorub == ElemValidarTXT1:
                logger.debug('La busqueda avanzada de: ' + ElemValidarTXT + ' y su ubicación ' + valorub + 'es correcta')
                resStep = True & resStep
            else:
                logger.debug('La busqueda avanzada de: ' + ElemValidarTXT + ' NO es correcta')
                resStep = False
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I do advance search inventory" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search inventory --> {}'.format(resStep))
        assert resStep

    @then('I download the template inventory')
    def descargarplantilla_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I download the template inventory')
        resStep = True
        try:
            logger.debug('Abrir Descarga plantilla')
            ElemValidar = gestElements.gestDesPlaID # Descargar plantilla
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERIDPTitXPath  # DESCARGAR PLANTILLA
            ElemValidarTXT = gestAlmElements.gestAlMERIDPTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIDPAspaXPath  # aspa
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERIDPAlmXPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            ini = 0
            fin = 7
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERIDPAlmInput # LTL Fleming
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERIDPRITXPath  # Realizar inventario total
            ElemValidarTXT = gestAlmElements.gestAlMERIDPRITTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERIDPKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIDPOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I download the template inventory" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I download the template inventory --> {}'.format(resStep))
        assert resStep

    @when('I click a new inventory')
    def click_nuevo_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click a new inventory')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmNInvID  # Nuevo inventario
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(3)
        except Exception as e:
            logger.error('Algún elemento en "I click a new inventory" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click a new inventory --> {}'.format(resStep))
        assert resStep

    @then('I create an inventory')
    def crear_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create an inventory')
        resStep = True
        try:
            logger.debug('Valido formulario nuevo inventario')
            ElemValidar = gestAlmElements.gestAlmTitCreXPath  # Inventario
            ElemValidarTXT = gestAlmElements.gestAlMERINTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINFEIXPath  # Fecha estimada de inventario
            ElemValidarTXT = gestAlmElements.gestAlMERINFEITXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAlmXPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            ini = 0
            fin = 7
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINMUXPath  # Mostrar ubicaciones
            ElemValidarTXT = gestAlmElements.gestAlMERINMUTXT
            ini = 0
            fin = 19
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERINMUSelXPath  # Todos
            ElemValidarTXT = gestAlmElements.gestAlMERINMUSelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINInfID  # Información: Los ...
            ElemValidarTXT = gestAlmElements.gestAlMERINInfTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(5)
            logger.debug('Relleno formulario nuevo inventario')
            ElemValidar = gestAlmElements.gestAlMERINFecXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINFec7Valor # Fecha: X/X/2025
            ElemValidarTXT =  pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text # Fecha: X/X/2025
            logger.debug('La fecha seleccionada es: ' + ElemValidarTXT)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINSAXPath  # Seleccionar Almacén
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINASXPath  # LTL Fleming
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIXPath  # INGREDIENTES
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Valido campos ingredientes_inventario')
            ElemValidar = gestAlmElements.gestAlMERINAddIUbiXPath  # Ubicación
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarTXT = gestElements.gestUbic1TXT
            ini = 0
            fin = 9
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERINAddIIngXPath  # Ingrediente:
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarTXT = gestAlmElements.gestAlmIng3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINAddIUniXPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINAddICanXPath  # Cantidad:
            ElemValidarTXT = gestElements.gestCan2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
            logger.debug('Relleno campos ingredientes_inventario')
            ElemValidar = gestAlmElements.gestAlMERINAddIUbIValor  # Ubicación ingrediente: Sala
            time.sleep(5)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERINAddISelIInput  # Ingrediente
            time.sleep(5)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERINAddISelIValor  # APEROL
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIUniInput  # Unidad
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIUniValor  # BOTELLA (1000 ML)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERINAddICanIInput  # 2
            ElemValidarValor = gestElements.gestCantidad1TXT
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIOKXPath  # Añadir producto
            ElemValidarTXT = gestAlmElements.gestAlMERINAddIOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            ElemValidar = gestAlmElements.gestAlMERINAddIUbSRXPath  # Subrecetas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIUbSRValor  # Ubicación subreceta: Sala
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddISelSRInput
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddISelSRValor  # AQUARIUS LIMON BAG-IN-BOX
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddICanSRInput  # 2
            ElemValidarValor = gestElements.gestCantidad2TXT
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddISROKXPath  # Añadir subreceta
            ElemValidarTXT = gestAlmElements.gestAlMERINAddISROKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            ElemValidar = gestAlmElements.gestAlMERINAddIUbPXPath  # Productos
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIUbPValor  # Ubicación producto: Sala
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddISelPInput  #
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddISelPValor  # 1/2 Mojito
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddICanPInput  # 2
            ElemValidarValor = gestElements.gestCantidad2TXT
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIPOKXPath  # Añadir
            ElemValidarTXT = gestElements.gestAñadirTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestElements.gestVolverListID  # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestCarPlaID  # Cargar plantilla
            ElemValidarTXT = gestElements.gestCarPlaTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINRIID  # Resumen del inventario
            ElemValidarTXT = gestAlmElements.gestAlMERINRITXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINGBID  # Guardar borrador
            ElemValidarTXT = gestAlmElements.gestAlMERINGBTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Refresco inventario')
            ElemValidar = gestAlmElements.latPagGestMeIXPath  # Inventario
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I create an inventory" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create an inventory --> {}'.format(resStep))
        assert resStep

    @then('I see the inventary created')
    def see_inventary(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see the inventary created')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMecInput # espera para cargar la tabla
            WebDriverWait(pagina_gestAlm, 30).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERISeeXPath  # Ver inventario
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERISeeIXPath
            WebDriverWait(pagina_gestAlm, 30).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarTXT = gestAlmElements.gestAlMERISee1ITXT # (1 Ingredientes)
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERISeeAXPath # LTL Fleming
            ElemValidarTXT = gestAlmElements.gestAlmSelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINAddIXPath  # INGREDIENTES
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERISee1XPath # veo APEROL
            ElemValidarTXT = gestAlmElements.gestAlMERISee1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINAddIUbSRXPath # Subrecetas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERISee2XPath  # veo AQUARIUS LIMON BAG-IN-BOX
            ElemValidarTXT = gestAlmElements.gestAlMERISee2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERINAddIUbPXPath  # Productos
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERISee3XPath  # veo 1/2 Mojito
            ElemValidarTXT = gestAlmElements.gestAlMERISee3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestVolverListID  # Volver
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I see the inventary created" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see the inventary created --> {}'.format(resStep))


    @then('I edit an inventary')
    def edit_inventary(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I edit an inventary')
        resStep = True
        try:
            logger.debug('Ordeno inventario')
            ElemValidar = gestAlmElements.gestAlMERIFecCreXPath  # Fecha creación
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERISeeEditXPath  # Editar inventario
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERISeeETitXPath  # EDITAR INVENTARIO
            ElemValidarTXT = gestAlmElements.gestAlMERISeeETitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERISeeETit2XPath # Escoge la ubicación de almacén que desea modificar
            ElemValidarTXT = gestAlmElements.gestAlMERISeeETit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERISeeEUbXPath # Ubicación
            ElemValidarTXT = gestElements.gestUbic1TXT
            ini = 0
            fin = 9
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERISeeEUbValor  # Refrigerado
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERISeeEAccXPath  # Acción
            ElemValidarTXT = gestAlmElements.gestAlMERISeeEAccTXT
            ini = 0
            fin = 6
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERISeeEAccValor # Añadir
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERISeeEOKXPath # Aceptar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(5)
            logger.debug('Añado otro ingrediente_inventario')
            ElemValidar = gestAlmElements.gestAlMERINAddIXPath # pulso INGREDIENTE
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddISelInput # desplegable ingrediente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddISelI2Valor  # A MIM GAS NATURAL VR50
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIUniInput  # Unidad
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIUni2Valor  # CAJA 20 BOTELLA
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddICanIInput  # 2
            ElemValidarValor = gestElements.gestCantidad2TXT
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERINAddIOKXPath  # Añadir producto
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERINGBID  # Aceptar
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestElements.gestVolverListID  # Volver
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Comprobamos ingrediente añadido al inventario')
            ###
            ElemValidar = gestAlmElements.gestAlMERISeeXPath  # Ver inventario
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(10)
            ElemValidar = gestAlmElements.gestAlMERISeeIXPath
            ElemValidarTXT = gestAlmElements.gestAlMERISee2ITXT # (2 Ingredientes)
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestVolverListID  # Volver
            time.sleep(2)
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I edit an inventary" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I edit an inventary --> {}'.format(resStep))
        assert resStep

    @then('I search and delete an inventory')
    def buscaryborrar_nuevo_inventario(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete an inventory')
        resStep = True
        try:
            logger.debug('Busco y borro el inventario')
            ElemValidar = gestAlmElements.gestAlMERIBusInput
            buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            self.creado = gestAlmElements.gestAlMERSelIDelTXT
            buscar.send_keys(self.creado)  # busco inventario: qa@tamus.io
            buscar.click()
            time.sleep(3)
            ElemValidar = gestAlmElements.gestAlMERIFecInput
            self.fechainv = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.debug('El inventario a borrar tiene fecha ' + self.fechainv)
            ElemValidar = gestAlmElements.gestAlMERISelDelXPath
            self.creadoinv = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.debug('El inventario a borrar esta creado por ' + self.creadoinv)
            self.inv = gestAlmElements.gestAlmSelTXT + ' (' + self.fechainv + ')' # Ej:LTL Fleming (01/02/2025)

            if self.creado == self.creadoinv:
                logger.debug('Borrar')
                ElemValidar = gestAlmElements.gestAlMERIDelXPath  # icono borrar
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestAlmElements.gestAlMERIDelTitXPath  # ELIMINAR INVENTARIO
                ElemValidarTXT = gestAlmElements.gestAlMERIDelTitTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMERIDelTit2XPath # ¿Está seguro de querer eliminar este inventario?
                ElemValidarTXT = gestAlmElements.gestAlMERIDelTit2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMERIDelSelXPath  # Ej:LTL Fleming (01/02/2025)
                ElemValidarTXT = gestAlmElements.gestAlmSelTXT + ' (' + self.fechainv + ')'
                logger.debug('El inventario a borrar es ' + ElemValidarTXT)
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMERIDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestAlMERIDelOKXPath  # Eliminar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('El inventario ' + self.inv + 'ha sido borrado')
            else:
                logger.debug('El inventario ' + self.inv + 'NO ha sido borrado')
                time.sleep(2)
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete an inventory" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete an inventory --> {}'.format(resStep))
        assert resStep

    @when('I click transfers and departures')
    def click_traspasos_salidas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click transfers and departures')
        resStep = True
        try:
             ElemValidar = gestAlmElements.latPagGestMeTXPath # Traspasos y Salidas
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click transfers and departures" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click transfers and departures --> {}'.format(resStep))
        assert resStep

    @step('I see transfers and departures')
    def ver_traspasos_salidas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see transfers and departures')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmLisTitXPath # LISTADO DE TRASPASOS Y SALIDAS
            ElemValidarTXT = gestAlmElements.gestAlMERTSTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep =  obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID # Búsqueda Avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT
            resStep =  obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMID # Nuevo movimiento
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMTXT
            resStep =  obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSBusXPath # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSMarXPath # Marcas
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSAllXPath  # Todas
            ElemValidarTXT = gestElements.gestAllTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosMovXPath  # Mostrando..
            #ElemValidarTXT = gestAlmElements.gestAlmMos7TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            # no se borran los movientos, con lo que el número se incrementa, y no se puede automatizar/comprobar
            ElemValidar = gestAlmElements.gestAlMERTSCodIntXPath # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlMERTSCodIntTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSFecMovXPath  # Fecha de Movimiento
            ElemValidarTXT = gestAlmElements.gestAlMERTSFecMovTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSFecCreXPath  # Fecha de creación
            ElemValidarTXT = gestElements.gestFecCreTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNomXPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSCanXPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSUniXPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSAOriXPath  # Almacén origen
            ElemValidarTXT = gestAlmElements.gestAlmAOriTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSADesXPath  # Almacén destino
            ElemValidarTXT = gestAlmElements.gestAlmADesTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSTMXPath # Tipo de movimiento
            ElemValidarTXT = gestAlmElements.gestAlMERTSTMTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSStXPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSAccXPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see transfers and departures" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see transfers and departures --> {}'.format(resStep))
        assert resStep

    @then('I click a new movement')
    def nuevo_movimiento(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click a new movement')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMERTSNMID  # Nuevo movimiento
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click a new movement" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click a new movement --> {}'.format(resStep))
        assert resStep

    @then('I create a new movement: merma')
    def crear_movimiento_merma(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I create a new movement: merma')
        resStep = True
        try:
            logger.debug('Valido formulario adicional nuevo movimiento')
            ElemValidar = gestAlmElements.gestAlMERTSNMTitXPath  # NUEVO MOVIMIENTO
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMTit2XPath  # ¿Qué tipo de movimiento de stock desea realizar?
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMTit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMT1XPath  # Traspaso entre almacenes
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMT1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMT2XPath  # Merma
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMT2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMT3XPath  # Comida de familia
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMT3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMT4XPath  # Consumo de ingredientes genéricos
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMT4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMT5XPath  # Buffet consumo
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMT5TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMT6XPath  # Buffet merma
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMT6TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERTSNMKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMT6XPath  # Buffet merma
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERTSNMKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            WebDriverWait(pagina_gestAlm, 30).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Valido formulario nuevo movimiento_buffet')
            ElemValidar = gestAlmElements.gestAlMERTSNMBMTitXPath  # BUFFET MERMA
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMBMTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMBMTit2XPath  # Fecha de la variacion de stock
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMBMTit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMBMTit3XPath  # Almacen Origen
            ElemValidarTXT = gestAlmElements.gestAlmAOriTXT
            ini = 0
            fin = 14
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestElements.gestVolverListID  # cabecera, volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMOKID  # Generar movimiento de stock
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMOKTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAIngXPath  # INGREDIENTES
            ElemValidarTXT = gestAlmElements.gestAlmIngTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERASReXPath  # SUBRECETAS
            ElemValidarTXT = gestAlmElements.gestAlmSRecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERAProdXPath  # PRODUCTOS
            ElemValidarTXT = gestElements.gestProdTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMBMPieXPath  # Coste total: 0.00000 €
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMBMPieTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
            logger.debug('Relleno formulario nuevo movimiento_merma')
            ElemValidar = gestAlmElements.gestAlMERTSNMBMSAXPath  # Seleccionar Almacen
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMASXPath  # LTL Fleming
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERAIngXPath  # INGREDIENTES
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(5)
            logger.debug('Valido formulario nuevo movimiento_merma_ingredientes')
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol1XPath # Ingrediente:
            WebDriverWait(pagina_gestAlm,60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarTXT = gestAlmElements.gestAlmIng3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol2XPath # Unidad
            WebDriverWait(pagina_gestAlm, 50).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol3XPath # Cantidad:
            ElemValidarTXT = gestElements.gestCan2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol1Input # Escoger ingrediente
            WebDriverWait(pagina_gestAlm, 30).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol1Valor # ALBAHACA
            WebDriverWait(pagina_gestAlm, 30).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol2Input # Escoger unidad
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol2Valor # G
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMBMCol3Input # Cantidad,2
            ElemValidarValor = gestElements.gestCantidad2TXT
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar= gestAlmElements.gestAlMERTSNMBMAddXPath # Añadir
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestElements.gestVolverListID  # volver
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSMBMKO2Tit1XPath  # CAMBIOS SIN GUARDAR
            ElemValidarTXT = gestAlmElements.gestAlMERTSMBMKO2Tit1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmCSGTit2XPath  # Hay cambios sin guardar. ¿Está seguro que desea salir de la página?
            ElemValidarTXT = gestAlmElements.gestAlmCSGTit2SPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmVSGXPath # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmCSGKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSNMOKID  # Guardar movimiento y cancelar luego
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERTSNMBMTitOK1XPath # Generar movimiento de stock
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMBMTitOK1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMBMTitOK2XPath # ¿Está seguro de generar el movimiento de stock en esta fecha?
            ElemValidarTXT = gestAlmElements.gestAlMERTSNMBMTitOK2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMBMOKXPath # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSNMBMKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERTSNMOKID  # Guardar movimiento y aceptar
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERTSNMBMOKXPath  # Aceptar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Capturo campo Fecha de creación')
            ElemValidar = gestAlmElements.gestAlMERTSBusXPath # Espero a que aparezca la palabra 'Buscar' para estar en pag.principal
            WebDriverWait(pagina_gestAlm, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidar = gestAlmElements.gestAlMERTSNMFecXPath # Fecha de creación
            self.fecmerma = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.info('La fecha completa de la merma es ' + self.fecmerma)
            self.fecmerma = self.fecmerma[0:10]
            logger.info('La fecha de la merma es ' + self.fecmerma)
        except Exception as e:
            logger.error('Algún elemento en "I create a new movement: Merma" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I create a new movement: Merma --> {}'.format(resStep))
        assert resStep

    @then('I see and cancel a movement')
    def ver_desactivar_movimiento(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see and cancel a movement')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlMERTSMBMKO2XPath  # desactivar movimiento
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Desactivo movimiento')
            ElemValidar = gestAlmElements.gestAlMERTSMBMTitKOXPath  # CANCELAR MOVIMIENTO DE STOCK
            ElemValidarTXT = gestAlmElements.gestAlMERTSMBMTitKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSMBMTitKO2XPath  # ¿Estás seguro que desea cancelar este movimiento de stock?
            ElemValidarTXT = gestAlmElements.gestAlMERTSMBMTitKO2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSMBMKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERTSMBMOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            if self.fecmerma == gestAlmElements.hoy:
                logger.info('Descuadre localizado')
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.info('Descuadre desactivado')
                resStep = True & resStep
            else:
                logger.info('Descuadre NO localizado')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I see and cancel a movement" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see and cancel a movement --> {}'.format(resStep))
        assert resStep

    @then('I export transfers and departures')
    def exporto_transpasos_salidas(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export transfers and departures')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:59]  # nombre original del fichero sin segundos ni extension, ej: Traspasos y Salidas_20250228_09072711
            self.ficheroTS = gestAlmElements.gestAlmExpFTSTXT + self.ficexp[
                                                                     50:94]  # Nombre fichero completo, ej: Traspasos y Salidas_20250228_09072711.xlsx
            nombre = gestAlmElements.gestAlmExpDesLTSTXT # Traspasos%20y%20Salidas_20250228_09343728.xlsx
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroTS) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export transfers and departures" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export transfers and departures --> {}'.format(resStep))
        assert resStep

    @then('I open transfers and departures file')
    def abrir_fichero_traspasos_y_salidas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I open transfers and departures file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFTSTXT + ' (Global)'
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroTS)
        except Exception as e:
            logger.error('Algún elemento en "I open transfers and departures file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open transfers and departures file --> {}'.format(resStep))
        assert resStep

    @then('I do advance search transfers and departures')
    def busqueda_avanzada_traspasos_salidas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search transfers and departures')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada de transpasos y salidas')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFIXPath # Fecha inicio*
            ElemValidarTXT = gestAlmElements.gestAlmFecIniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFFXPath  # Fecha fin*
            ElemValidarTXT = gestAlmElements.gestAlmFecFinTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmC1XPath  # Almacén origen
            ElemValidarTXT = gestAlmElements.gestAlmAOriTXT
            ini = 0
            fin = 14
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmC2XPath  # Almacén destino
            ElemValidarTXT = gestAlmElements.gestAlmADesTXT
            ini = 0
            fin = 15
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERIATPBEXPath  # Tipo de movimiento
            ElemValidarTXT = gestAlmElements.gestAlMERTSTMTXT
            ini = 0
            fin = 18
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERIUbECPCXPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            ini = 0
            fin = 6
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)

            logger.info('Relleno la búsqueda de transpasos y salidas')
            ElemValidar = gestAlmElements.gestAlMERTSBASAXPath # Seleccionar almacen
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSBAASXPath # Seleccionar almacen: LTL Fleming
            ElemValidarTXT = gestAlmElements.gestAlmSel2TXT
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            ElemValidar = gestAlmElements.gestAlMERTSBABMXPath # Tipo movimiento
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSBATMBMXPath # Tipo movimiento: Buffet merma
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.info('Compruebo la búsqueda')
            ElemValidar = gestAlmElements.gestAlMERTSBATMFDXPath # Fecha del día
            ElemValidarTXT =  gestAlmElements.hoy
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I do advance search transfers and departures" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search transfers and departures --> {}'.format(resStep))
        assert resStep

    @step('I click imbalances')
    def click_descuadre(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click the imbalance')
        resStep = True
        try:
            logger.debug('Selecciono materias primas,descuadre')
            ElemValidar = gestAlmElements.latPagGestMeDXPath  # Descuadres
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I click imbalances" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click imbalances --> {}'.format(resStep))
        assert resStep

    @then('I see imbalances')
    def veo_descuadres(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see imbalances')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmLisTitXPath  # LISTADO DE DESCUADRES
            ElemValidarTXT = gestAlmElements.gestAlMERDesTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERDesMarXPath  # Marcas:
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERDesMarValor  # Todas
            ElemValidarTXT = gestAlmElements.gestAlmAllTXT
            ini = 0
            fin = 5
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERDesFecXPath  # Fecha:
            ElemValidarTXT = gestElements.gestFec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesFecValor  # Valor de fecha
            ElemValidarTXT = gestAlmElements.gestAlmFec1Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosDesXPath  # Mostrando..
            #ElemValidarTXT = gestAlmElements.gestAlmMos8TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            # no se borran los descuadres, con lo que el número se incrementa, y no se puede automatizar/comprobar
            logger.debug('Compruebo las columnas')
            ElemValidar = gestAlmElements.gestAlMERDesCol1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol2XPath  # Ingrediente
            ElemValidarTXT = gestAlmElements.gestAlmIng4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol3XPath # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol4XPath # Variación
            ElemValidarTXT = gestAlmElements.gestAlmVarTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol5XPath # Variación media
            ElemValidarTXT = gestAlmElements.gestAlmVarMTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol6XPath # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol7XPath # Variación (%)
            ElemValidarTXT = gestAlmElements.gestAlmVar2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol8XPath # Variación media (%)
            ElemValidarTXT = gestAlmElements.gestAlmVarM2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesCol9XPath # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see imbalances" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see imbalances --> {}'.format(resStep))
        assert resStep

    @then('I export imbalances')
    def exporto_descuadres(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export imbalances')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:61]  # nombre original del fichero sin segundos ni extension, ej: Listado de descuadres_20250319_14111122
            self.ficheroDes = gestAlmElements.gestAlmExpFDesTXT + self.ficexp[
                                                                     52:96]  # Nombre fichero completo, ej: Listado de descuadres_20250319_14111122.xlsx
            nombre = gestAlmElements.gestAlmExpDesLDesTXT # Listado de descuadres_20250228_09343728.xlsx
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroDes) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I export imbalances" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export imbalances --> {}'.format(resStep))
        assert resStep

    @then('I open imbalances file')
    def abrir_fichero_descuadres(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I open imbalances file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFDesTXT + ' (Global)'
            logger.debug(primeraLinea)
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroDes)
        except Exception as e:
            logger.error('Algún elemento en "I open imbalances file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open imbalances file --> {}'.format(resStep))
        assert resStep

    @then('I do advance search imbalances')
    def busqueda_avanzada_descuadres(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search imbalances')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada de descuadres')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFIXPath # Fecha inicio*
            ElemValidarTXT = gestAlmElements.gestAlmFecIniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmFFXPath  # Fecha fin*
            ElemValidarTXT = gestAlmElements.gestAlmFecFinTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            ElemValidar = gestAlmElements.gestAlmC1XPath  # Ingredientes
            ElemValidarTXT = gestAlmElements.gestAlmIng2TXT
            ini = 0
            fin = 12
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmC2XPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            logger.info('Relleno la búsqueda de descuadres')
            ElemValidar = gestAlmElements.gestAlMERDesBASIXPath # Seleccionar ingrediente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERDesBAISXPath # A MIM GAS CARBONATADA ALUMINIO
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERDesBASAXPath # Seleccionar almacen
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERDesBAASXPath # LTL Fleming
            ElemValidarTXT = gestAlmElements.gestAlmSel2TXT
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.info('Compruebo la búsqueda')
            ElemValidar = gestAlmElements.gestAlMERDesBAResXPath # Materias primas
            ElemValidarTXT =  gestAlmElements.gestAlmMP2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERDesBARes1XPath # A MIM GAS CARBONATADA ALUMINIO
            ElemValidarTXT =  gestAlmElements.gestAlMERDesBARes1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I do advance search imbalances" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search imbalances --> {}'.format(resStep))
        assert resStep

