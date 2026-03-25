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
from pathlib import Path
from selenium import webdriver

logger = logging.getLogger('WebLogs')
gestAlmElements = GestionAlmacen.GestionAlmacen()
gestElements = Common.Common()

class gestionAlmacen2(unittest.TestCase):

    @when('I click orders')
    def click_pedidos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click orders')
        resStep = True
        try:
             ElemValidar = gestAlmElements.latPagGestPePXPath # Pedidos a proveedor
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click orders" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click orders --> {}'.format(resStep))
        assert resStep

    @then('I see orders')
    def veo_pedidos_a_proveedor(self):
        logger.debug('INICIO STEP: I see orders')
        pagina_gestAlm = self.driver
        resStep = True
        try:
            logger.debug('Valido listado pedidos a proveedor')
            ElemValidar = gestAlmElements.gestAlmLisTitXPath  # LISTA DE PEDIDOS A PROVEEDOR
            ElemValidarTXT = gestAlmElements.gestALPEDProvTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Busqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmPEDNPedID  # Nuevo pedido
            ElemValidarTXT = gestAlmElements.gestAlmPEDNPedTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDMarXPath  # Marcas:
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDMarValor  # Todas
            ElemValidarTXT = gestAlmElements.gestAlmAllTXT
            ini = 0
            fin = 5
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDFilXPath # Filtros:
            ElemValidarTXT = gestElements.gestFilTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStCanXPath # Cancelados
            ElemValidarTXT = gestAlmElements.gestAlmStCan2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStBorXPath # Borradores
            ElemValidarTXT = gestAlmElements.gestAlmStBorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStPteXPath # Pendiente
            ElemValidarTXT = gestAlmElements.gestAlmStPteTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStEPXPath # En proceso
            ElemValidarTXT = gestAlmElements.gestAlmStEPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStComXPath # Completados
            ElemValidarTXT = gestAlmElements.gestAlmStComTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStIncXPath # Incidencias
            ElemValidarTXT = gestAlmElements.gestAlPEDStIncTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDFecXPath  # Fecha:
            ElemValidarTXT = gestElements.gestFec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDFecValor  # Valor de fecha
            ElemValidarTXT = gestAlmElements.gestAlmFec3Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosPedXPath  # Mostrando..
            #ElemValidarTXT = gestAlmElements.gestAlmMos9TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            # Los pedidos desaparecen cada X tiempo, no merece la pena automatizar este valor
            ElemValidar = gestAlmElements.gestAlPEDPie3XPath  # Subtotal:1482.91 €
            ElemValidarTXT = gestAlmElements.gestAlPEDPie3TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDPie1XPath  # Mostrar totales entregados
            ElemValidarTXT = gestAlmElements.gestAlPEDPie1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlPEDSubEntXPath  # Subtotal (Entregado)
            ElemValidarTXT = gestAlmElements.gestAlPEDSubEntTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDPie2XPath  # Ocultar franquicias
            ElemValidarTXT = gestAlmElements.gestAlPEDPie2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMosPedXPath  # Mostrando..
            # ElemValidarTXT = gestAlmElements.gestAlmMos10TXT
            # resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            # Los pedidos desaparecen cada X tiempo, no merece la pena automatizar este valor
            time.sleep(2)

            logger.debug('Valido valores de los pedidos')
            # No me devuelve los textos de los iconos: En proceso, q es un camión..etc, fallo de la comunicacón q es una señal de precaucación..
            #ElemValidar = gestAlmElements.gestAlPEDStatus1XPath  # En proceso
            #ElemValidarTXT = gestAlmElements.gestAlmStEPTXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            #ElemValidar = gestAlmElements.gestAlPEDComun1XPath  # Fallo de comunicación
            #ElemValidarTXT = gestAlmElements.gestAlPEDComun1TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Generar albarán de entrada') # icono folio
            ElemValidar = gestAlmElements.gestAlPEDOp2XPath  # Generar albarán de entrada
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click() # Nos muestra la web, ALBARÁN DE ENTRADA
            time.sleep(2)
            ElemValidar = gestElements.gestVolverListID  # Volver
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click() # NOS MUESTRA EL MENSAJE, CAMBIOS SIN GUARDAR
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERTSMBMKO2Tit1XPath  # CAMBIOS SIN GUARDAR
            ElemValidarTXT = gestAlmElements.gestAlMERTSMBMKO2Tit1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmCSGTit2XPath  # Hay cambios sin guardar. ¿Está seguro que desea volver sin guardar?
            ElemValidarTXT = gestAlmElements.gestAlmCSGTit2VSGTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmCSGKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmGVXPath  # Guardar y volver
            ElemValidarTXT = gestElements.gestGVTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmVSGXPath  # Volver sin guardar
            ElemValidarTXT = gestElements.gestVSGTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Recargar página, vuelta sin guardar,albaran')
            ElemValidar = gestAlmElements.latPagGestPePXPath  # Recargar página
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Exportar') # icono impresora
            ElemValidar = gestAlmElements.gestAlPEDExpXPath  # Exportar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlPEDTitExpXPath  # EXPORTAR
            ElemValidarTXT = gestElements.gestExp2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestMensajeID  # ¿Desea incluir los precios de cada producto en el PDF?
            ElemValidarTXT = gestAlmElements.gestAlPEDTit2ExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDOKExpXPath  # Valorado
            ElemValidarTXT = gestAlmElements.gestAlPEDOKExpTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDNVExpXPath  # No valorado
            ElemValidarTXT = gestAlmElements.gestAlPEDNVExpTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDKOExpXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I see orders" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see orders --> {}'.format(resStep))
        assert resStep

    @then('I fill fields in the form new order')
    def rellenar_formulario_nuevo_pedido(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I fill fields in the form new order')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmPEDNPedID # Nuevo pedido
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validar formulario nuevo pedido pagina 1')
            ElemValidar = gestAlmElements.gestAlmTitCreXPath  # PEDIDO
            ElemValidarTXT = gestAlmElements.gestAlmPedTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1FecXPath # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1AlmXPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1CrePorXPath # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestVolverListID  # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1MosPedXPath # Mostrar ingredientes pedidos
            ElemValidarTXT = gestAlmElements.gestAlPEDN1MosPedTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDSubtXPath # Subtotal
            ElemValidarTXT = gestElements.gestSubtotalTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1BusXPath # Buscar
            ElemValidarTXT = gestElements.gestBusTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1CatXPath  # Categoría
            ElemValidarTXT = gestAlmElements.gestAlmCategTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol1XPath  # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol2XPath  # Descripción
            ElemValidarTXT = gestElements.gestDescripTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol3XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol4XPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol5XPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol6XPath  # Precio
            ElemValidarTXT = gestElements.gestPrecioTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol7XPath  # Importe
            ElemValidarTXT = gestElements.gestImporteTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Hago busqueda producto,pagina 1')
            ElemValidar = gestAlmElements.gestAlPEDN1SAXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlPEDN1ASXPath  # LTL Fleming
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(5)
            ElemValidar = gestAlmElements.gestAlPEDN1BusInput # CERVEZA HEINEKEN
            ElemValidarValor = gestAlmElements.gestAlMERABusValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            logger.debug('Rellenar campos nuevo pedido pagina 1')
            ElemValidar = gestAlmElements.gestAlPEDN1SUXPath # Unidad
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlPEDN1USXPath  # # UD (50 L)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlPEDN1CanInput # Cantidad
            ElemValidarValor = gestElements.gestCantidad1TXT # 1
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            logger.debug('Valido campo añadido pagina 1')
            ElemValidar = gestAlmElements.gestAlPEDN1PriEleXPath # CERVEZA HEINEKEN (CAÑERO)
            ElemValidarTXT = gestAlmElements.gestAlMERAIngValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1PreTXPath  # Precio resultante
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1ImpTXPath  # Importe resultante
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1SubTXPath  # Subtotal resultante
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN1MosPedXPath # Mostrar ingredientes pedidos
            ElemValidarTXT = gestAlmElements.gestAlPEDN1MosPedTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Aparece segundo elemento y más')
            ElemValidar = gestAlmElements.gestAlPEDN1SegEleXPath  # Aparecen más elementos, compruebo uno
            ElemValidarTXT = '7UP 20cl'
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
            logger.debug('Solo aparece el elemento seleccionado')
            ElemValidar = gestAlmElements.gestAlPEDN1MosPedXPath  # Mostrar ingredientes pedidos
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlPEDN1PriEleXPath
            ElemValidarTXT = gestAlmElements.gestAlMERAIngValor # CERVEZA HEINEKEN (CAÑERO)
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
            logger.debug('Cambio de página')
            ElemValidar = gestAlmElements.gestAlmNPedOKID # Resumen del pedido
            ElemValidarTXT = gestAlmElements.gestAlPEDN1ResPedTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlPEDN2STitXPath # RESUMEN DEL PEDIDO
            ElemValidarTXT = gestAlmElements.gestAlPEDN2STitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2SAlmXPath  # Almacén: LTL Fleming
            ElemValidarTXT = gestAlmElements.gestAlPEDN2SAlmTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2ProvSelXPath  # HEINEKEN ESPAÑA, S.A.
            ElemValidarTXT = gestAlmElements.gestAlPEDN2ProvSelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2FPXPath  # Fecha de pedido: XX/XX/2025
            ElemValidarTXT = gestAlmElements.gestAlPEDN2FPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2DesXPath  # Descripción
            ElemValidarTXT = gestElements.gestDescripTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2UdXPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2ProvXPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2CanXPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2PreXPath  # Precio
            ElemValidarTXT = gestElements.gestPrecioTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2ImpXPath  # Importe
            ElemValidarTXT = gestElements.gestImporteTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2DesValor  # CERVEZA HEINEKEN(CAÑERO)
            ElemValidarTXT = gestAlmElements.gestAlMERAIngValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2UdValor  # UD (50 L)
            ElemValidarTXT = gestAlmElements.gestAlPEDN2UdSel2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2ProvValor  # HEINEKEN ESPAÑA, S.A.
            ElemValidarTXT = gestAlmElements.gestAlPEDN2ProvSelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2CanValor  # 1
            ElemValidarTXT = gestElements.gestCantidad1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2PreValor  # 70.74 €
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2ImpValor  # 70.74 €
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2Subt1XPath  # Subtotal:
            ElemValidarTXT = gestElements.gestSubtotalTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDN2Subt2XPath  # 70.74 €
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Confirmar pedido')
            ElemValidar = gestAlmElements.gestAlPEDN2ConfPedID # Confirmar pedido
            ElemValidarTXT = gestAlmElements.gestAlPEDN2ConfPedTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(3) # hay q esperar unos segundos para que se cree correctamente
        except Exception as e:
            logger.error('Algún elemento en "I fill fields in the form new order" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill fields in the form new order --> {}'.format(resStep))
        assert resStep

    @then('I search and delete the new order') # no está hecho xq los pedidos no se pueden borrar
    def buscaryborrar_nuevo_pedido(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete the new order')
        resStep = True
        try:
            logger.debug('Busco y borro el nuevo pedido')
            ElemValidar = gestAlmElements.gestAlPEDseaXPath
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
            logger.error('Algún elemento en "I search and delete the new order" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete the new order --> {}'.format(resStep))
        assert resStep

    @then('I export orders')
    def exporto_pedidos(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export orders')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:72]  # nombre original del fichero sin hora ni extension, ej:Lista de pedidos a proveedor_20250415
            logger.debug('El nombreficorig es ' + nombreficorig)
            self.ficheroPedidos = gestAlmElements.gestAlmExpFPedTXT + self.ficexp[
                                                                  63:102]  # Nombre fichero completo, ej: Lista de pedidos a proveedor_20250415_12170343.xlsx
            logger.debug('El nombre de ficheroPedidos es '+ self.ficheroPedidos)
            nombre = gestAlmElements.gestAlmExpDesLPedTXT  # Lista%20de%20pedidos%20a%20proveedor_
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroPedidos)
        except Exception as e:
            logger.error(
                'Algún elemento en "I export orders" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export orders --> {}'.format(resStep))
        assert resStep

    @then('I open orders file')
    def abrir_fichero_pedidos(self):
        logger.debug('INICIO STEP: I open orders file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFPedTXT + ' (Global)'
            logger.debug(primeraLinea)
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroPedidos)
        except Exception as e:
            logger.error('Algún elemento en "I open orders file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open orders file --> {}'.format(resStep))
        assert resStep


    @then('I valid form advance search orders')
    def valido_formulario_busquedaavanzada_pedidos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form advance search orders')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada pedidos')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBARefXPath  # Referencia
            ElemValidarTXT = gestElements.gestReferencia2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBACIAXPath # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            ini = 0
            fin = 7
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestALAlbBAFIXPath  # Fecha inicio*
            ElemValidarTXT = gestAlmElements.gestAlmFecIniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALAlbBAFFXPath # Fecha fin*
            ElemValidarTXT = gestAlmElements.gestAlmFecFinTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIATPBEXPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            ini = 0
            fin = 6
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERIUbECPCXPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDBAProvXPath # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            ini = 0
            fin = 9
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDBAPProvXPath  # Producto de proveedor
            ElemValidarTXT = gestAlmElements.gestAlPEDBAPProvTXT
            ini = 0
            fin = 21
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDBATotXPath  # Total
            ElemValidarTXT = gestElements.gestTotal1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I valid form advance search orders" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I valid form advance search orders --> {}'.format(resStep))
        assert resStep

    @then('I do advance search orders')
    def hago_busqueda_avanzada_pedidos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search orders')
        resStep = True
        try:
            logger.info('Relleno la búsqueda avanzada de pedidos')
            ElemValidar = gestAlmElements.gestAlMERDesBASAXPath # Seleccionar almacen
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestAlMERDesBAASXPath # LTL Fleming
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlMERTSBABMXPath # Tipo movimiento
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestAlMERTSBAOrdXPath  # Pedido completado
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(3)
            logger.debug('Busco pedido de LTL Fleming,completado')
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Verifico resultado busqueda avanzada pedidos')
            ElemValidar = gestAlmElements.gestAlPEDBAXPath # P2509/198577
            #ElemValidarTXT =  gestAlmElements.gestAlPED6TXT
            logger.debug(ElemValidarTXT)
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I do advance search orders" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search orders--> {}'.format(resStep))
        assert resStep

    @then('I do filters orders')
    def uso_filtros_ordenes(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do filters orders')
        resStep = True
        try:
            logger.debug('Ejecuto filtros. Desactivo En proceso e incidencias salen 3')
            ElemValidar = gestAlmElements.gestAlPEDStEPXPath  # En proceso
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlPEDStIncXPath  # Incidencias
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlPED1XPath # P2509/198577
            #ElemValidarTXT = gestAlmElements.gestAlPED6TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPED2XPath # P2524/198573
            #ElemValidarTXT = gestAlmElements.gestAlPED2TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPED3XPath # P2507/198572
            #lemValidarTXT = gestAlmElements.gestAlPED1TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Ejecuto filtros, desactivo completado')
            ElemValidar = gestAlmElements.gestAlPEDStComXPath
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Valido que salen 2')
            ElemValidar = gestAlmElements.gestAlPED1XPath # P2524/198573
            #ElemValidarTXT = gestAlmElements.gestAlPED2TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPED2XPath # P2507/198572
            #ElemValidarTXT = gestAlmElements.gestAlPED1TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

        except Exception as e:
            logger.error('Algún elemento en "I do filters orders" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do filters orders --> {}'.format(resStep))
        assert resStep


    @then('I see an order')
    def ver_pedido(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see an order')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlPEDseaXPath  # Busco por número de pedido
            #ElemValidarValor = gestAlmElements.gestAlPED3TXT
            #rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestAlPEDseeXPath  # El ojo
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug( 'Veo pedido')
            ElemValidar = gestAlmElements.gestAlmTitCreXPath  # PEDIDO
            ElemValidarTXT = gestAlmElements.gestAlmPedTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestVolverListID  # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestHacDevID  # Hacer devolución (tiene que estar en estado Completado)
            ElemValidarTXT = gestElements.gestHacDevTXT
            #resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDseeFecXPath # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDseeCPXPath # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDseeRefXPath # Referencia
            ElemValidarTXT = gestElements.gestReferencia2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDseeAlmXPath # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDseeNotXPath # Notas
            ElemValidarTXT = gestElements.gestNotasTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDseeProvXPath # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            # valores q no consigo recuperar: HEINEKEN ESPAÑA, S.A., qa@tamus.io, Completado, Notas
            ElemValidar = gestAlmElements.gestAlPEDseeASXPath # LTL Fleming
            ElemValidarTXT = gestAlmElements.gestAlmSelTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol1XPath  # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol2XPath  # Descripción
            ElemValidarTXT = gestElements.gestDescripTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol3XPath  # Cantidad pedida
            ElemValidarTXT = gestAlmElements.gestAlPEDseeCanPedTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol4XPath  # Cantidad enviada
            ElemValidarTXT = gestAlmElements.gestAlPEDseeCanEnvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol5XPath  # Cantidad recibida
            ElemValidarTXT = gestAlmElements.gestAlPEDseeCanRecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol6XPath  # Cantidad devuelta
            ElemValidarTXT = gestAlmElements.gestAlPEDseeCanDevTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol7XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol8XPath  # Precio
            ElemValidarTXT = gestElements.gestPrecioTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol9XPath  # Importe
            ElemValidarTXT = gestElements.gestImporteTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol10XPath  # Notas
            ElemValidarTXT = gestElements.gestNotasTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Valores del pedido consultado')
            ElemValidar = gestAlmElements.gestAlPEDCol1Value  # 37
            ElemValidarTXT = gestAlmElements.gestAlPEDCol1Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol2Value  # Heineken Barril 50 L.
            ElemValidarTXT = gestAlmElements.gestAlPEDCol2Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol3Value  # 1
            ElemValidarTXT = gestElements.gestCantidad1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol4Value  # 1
            ElemValidarTXT = gestElements.gestCantidad1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol5Value  # 0
            ElemValidarTXT = gestElements.gestCantidad0TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol6Value  # 0
            ElemValidarTXT = gestElements.gestCantidad0TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol7Value  # UD (50 L)
            ElemValidarTXT = gestAlmElements.gestAlPEDN2UdSel2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol8Value  # 70.74 €
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCol9Value  # 70.74 €
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDSubtXPath  # Subtotal:
            ElemValidarTXT = gestElements.gestSubtotalTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDSubtValor  # 70.74 €
            ElemValidarTXT = gestAlmElements.gestAlPEDSubTValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Añadir nota')
            logger.debug('Consultar nota y borrarla')

        except Exception as e:
            logger.error('Algún elemento en "I see an order" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see an order --> {}'.format(resStep))
        assert resStep


    @then('I see orders by brand')
    def ver_pedidos_pormarca(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see orders by brand')
        resStep = True
        try:
             ElemValidar = gestAlmElements.gestAlPEDMarValor # Marcas
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             ElemValidar = gestAlmElements.gestAlPEDMarValorSel # Volapié
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             logger.debug('Verifico resultado búsqueda por marca')
             ElemValidar = gestAlmElements.gestAlPEDMarProXPath # OMS Y VIñAS SL
             ElemValidarTXT = gestAlmElements.gestAlPEDMarProTXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
             ElemValidar = gestAlmElements.gestAlPEDMarAlmXPath # TDV Sanchinarro
             ElemValidarTXT = gestAlmElements.gestAlPEDMarAlmTXT
             resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see orders by brand" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see orders by brand --> {}'.format(resStep))
        assert resStep

    @when('I click delivery notes(in)')
    def click_albaranes(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click delivery notes(in)')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestPAEXPath  # Albaranes de entrada
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            self.tipoALB = 'IN'
        except Exception as e:
            logger.error('Algún elemento en "I click delivery notes(in)" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click delivery notes(in) --> {}'.format(resStep))
        assert resStep

    @then('I see delivery notes(in)')
    def veo_albaranes_entrada(self):
        logger.debug('INICIO STEP: I see delivery notes(in)')
        pagina_gestAlm = self.driver
        resStep = True
        try:
            logger.debug('Valido albaranes de entrada')
            ElemValidar = gestAlmElements.gestAlmLisTitXPath  # LISTADO DE ALBARANES DE ENTRADA
            ElemValidarTXT = gestAlmElements.gestALPEDAlbTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Búsqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT  # QA
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmPEDNPedID  # Nuevo Albarán
            ElemValidarTXT = gestAlmElements.gestAlmPEDNAlbTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDAlbMarXPath  # Marcas:
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDAlbMarAllXPath  # Todas
            ElemValidarTXT = gestAlmElements.gestAlmAllTXT
            ini = 0
            fin = 5
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDAlbFecXPath  # Fecha:
            ElemValidarTXT = gestElements.gestFec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbFecValor  # Valor de fecha
            ElemValidarTXT = gestAlmElements.gestAlmFec2Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosAlbXPath  # Mostrando..
            #ElemValidarTXT = gestAlmElements.gestAlmMos11TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Compruebo las columnas')
            ElemValidar = gestAlmElements.gestAlPEDAlbCol1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol2XPath  # Referencia
            ElemValidarTXT = gestElements.gestReferencia2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol3XPath  # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol4XPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol5XPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol6XPath  # Subtotal
            ElemValidarTXT = gestElements.gestSubtotal2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol7XPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol8XPath  # Pedido
            ElemValidarTXT = gestElements.gestAlPed2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol9XPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol10XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbPie1XPath  # Subtotal:
            ElemValidarTXT = gestElements.gestSubtotalTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbPie2XPath  # El valor varía
            #ElemValidarTXT = gestAlmElements.gestAlPEDAlbPie1TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see delivery notes(in)" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see delivery notes(in) --> {}'.format(resStep))
        assert resStep

    @then('I fill fields in the form new delivery notes')
    def rellenar_formulario_nuevo_albarán(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I fill fields in the form delivery notes')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestAlmPEDNPedID  # Nuevo albarán
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validar formulario nuevo albarán pagina 1')
            ElemValidar = gestElements.gestVolverListID  # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestGBID  # Guardar borrador
            ElemValidarTXT = gestElements.gestGBTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestConfirmarID # Confirmar
            ElemValidarTXT = gestElements.gestConfirmarTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbFecXPath  # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbCPXPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbRefXPath  # Referencia
            ElemValidarTXT = gestElements.gestReferencia2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbAlmXPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbProvXPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbCPXPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB1XPath  # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB2XPath  # Descripción
            ElemValidarTXT = gestElements.gestDescripTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB3XPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB4XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB5XPath  # Precio
            ElemValidarTXT = gestElements.gestPrecioTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB6XPath  # Descuento
            ElemValidarTXT = gestElements.gestDescuentoTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB7XPath  # Importe
            ElemValidarTXT = gestElements.gestImporteTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbB8XPath  # Importe desc.
            ElemValidarTXT = gestElements.gestImporteDTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            #ElemValidar = gestAlmElements.gestALPEDNAlbB9XPath  # Añadir
            #ElemValidarTXT = gestElements.gestAñadirTXT
            # resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep no devuelve el valor
            ElemValidar = gestAlmElements.gestALPEDNAlbC1XPath  # Ref.
            ElemValidarTXT = gestElements.gestReferencia3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC2XPath  # Descripción
            ElemValidarTXT = gestElements.gestDescripTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC3XPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC4XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC5XPath  # Precio
            ElemValidarTXT = gestElements.gestPrecioTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC6XPath  # Descuento
            ElemValidarTXT = gestElements.gestDescuentoTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC7XPath  # Importe
            ElemValidarTXT = gestElements.gestImporteTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC8XPath  # Importe desc.
            ElemValidarTXT = gestElements.gestImporteDTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbC9XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbPie1XPath  # Subtotal
            ElemValidarTXT = gestElements.gestSubtotalTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbPie2XPath  # €
            ElemValidarTXT = gestElements.gestSubtotal3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Error porque no tiene líneas')
            ElemValidar = gestElements.gestConfirmarID # Confirmar
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestALPEDNAlbErrorTitXPath  # FALTAN LíNEAS
            ElemValidarTXT = gestAlmElements.gestALPEDNAlbErrorTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbErrorTit2XPath  # Para guardar o enviar ..
            ElemValidarTXT = gestAlmElements.gestALPEDNAlbErrorTit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNAlbErrorOKXPath  # Cerrar
            ElemValidarTXT = gestElements.gestCOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()

            logger.debug('Rellenar albarán')
            ElemValidar = gestAlmElements.gestALPEDNAlbRefInput  # Referencia
            ElemValidarTXT = gestAlmElements.gestAlmNPRefValor
            self.albar = ElemValidarTXT
            logger.debug('El nuevo albarán es ' + self.albar)
            Referencia = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            Referencia.click()
            Referencia.send_keys(ElemValidarTXT)
            ElemValidar = gestAlmElements.gestALPEDNAlbAlmInput  # Almacén
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbAlmValor  # LTL Fleming
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbProvInput  # Proveedor
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            if self.tipoALB == 'IN':
                ElemValidar = gestAlmElements.gestAlmTitCreXPath  # ALBARÁN DE ENTRADA
                ElemValidarTXT = gestAlmElements.gestALPEDNAlbTitTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDNAlbProvValor  # MAHOU, S.A.
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
            else:
                ElemValidar = gestAlmElements.gestAlmTitCreXPath  # ALBARÁN DE SALIDA
                ElemValidarTXT = gestAlmElements.gestALPEDNAlbTit2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDNAlbProv2Valor  # MAHOU, S.A.
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
                ElemValidar = gestAlmElements.gestALPEDNAlbMotXPath  # Motivo
                ElemValidarTXT = gestAlmElements.gestALPEDNAlbMotTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDNAlbMotInput # Entrega a cliente
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbRef2Input  # Ref.
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbRefValor  # 235 BT
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestElements.gestPrecioID  # Precio
            Precio = (pagina_gestAlm.find_element(by=By.ID, value=ElemValidar))
            Precio.click()
            Precio.clear()
            Precio.send_keys(gestAlmElements.gestAlPEDCol1Valor)  # 37
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbAddInput  # Añadir
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbEditXPath  # Editar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestElements.gestAlCanID  # Cantidad
            ElemValidarTXT = gestElements.gestCantidad2TXT
            Cantidad = pagina_gestAlm.find_element(by=By.ID, value=ElemValidar)
            Cantidad.clear()
            Cantidad.send_keys(ElemValidarTXT)
            ElemValidar = gestAlmElements.gestALPEDNAlbAddInput  # Modificar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbRefValor2  # 235 CV
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbAddInput  # Añadir
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbDelXPath  # Borrar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbEditXPath  # Editar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestElements.gestAlCanID  # Cantidad
            ElemValidarTXT = gestElements.gestCantidad1TXT
            Cantidad = pagina_gestAlm.find_element(by=By.ID, value=ElemValidar)
            Cantidad.clear()
            Cantidad.send_keys(ElemValidarTXT)
            ElemValidar = gestAlmElements.gestALPEDNAlbAddInput  # Modificar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNAlbPie2XPath  # 37€
            ElemValidarTXT = gestAlmElements.gestAlPEDCol1Valor + ' ' + gestElements.gestSubtotal3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestGBID # Guardar borrador
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.ID, ElemValidar)))
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(5) # tiene q estar estos segundos, para q de tiempo a Confirmar luego y borrarlo
            logger.debug('Albarán guardado')
            ElemValidar = gestElements.gestConfirmarID # Confirmar
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.ID, ElemValidar)))
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I fill fields in the form new delivery notes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I fill fields in the form new delivery notes --> {}'.format(resStep))
        assert resStep

    @then('I search and delete the new delivery notes')
    def buscaryborrar_nuevo_albarán(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP:I search and delete the new delivery notes')
        resStep = True
        try:
            logger.debug('Busco y borro el nuevo albarán')
            ElemValidar = gestAlmElements.gestAlPEDAlbBusInput # Buscar
            WebDriverWait(pagina_gestAlm, 20).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
            buscar.send_keys(self.albar)  # busco albarán
            buscar.click()
            time.sleep(2)
            if self.tipoALB == 'IN':
                ElemValidar = gestAlmElements.gestAlPEDAlbBusValue
            else:
                ElemValidar = gestAlmElements.gestAlPEDAlbBus2Value
            self.nuevoalb = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            if self.albar == self.nuevoalb:
                logger.debug('OJO') # hay que rechazar primero
                if self.tipoALB == 'IN':
                    ElemValidar = gestAlmElements.gestAlPEDAlbOjoXPath # Ojo primer albarán
                else:
                    ElemValidar = gestAlmElements.gestAlPEDAlbOjo2XPath  # Ojo primer albarán
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestElements.gestRechazarID # Rechazar
                pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestALPEDAlbRecTit1XPath # RECHAZAR ALBARÁN
                ElemValidarTXT = gestAlmElements.gestALPEDAlbRecTit1TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDAlbRecTit2XPath  # Va a rechazar un albarán...
                ElemValidarTXT = gestAlmElements.gestALPEDAlbRecTit2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDAlbRecKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDAlbRecOKXPath  # Aceptar
                ElemValidarTXT = gestElements.gestAOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                WebDriverWait(pagina_gestAlm, 20).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                ElemValidar = gestAlmElements.gestAlPEDAlbBusInput  # Buscar
                WebDriverWait(pagina_gestAlm, 20).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
                buscar = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar)
                buscar.clear()
                buscar.send_keys(self.albar)  # busco albarán
                buscar.click()
                if self.tipoALB == 'IN':
                    ElemValidar = gestAlmElements.gestALPEDAlbDelXPath # Borrar albarán de entrada
                else:
                    ElemValidar = gestAlmElements.gestALPEDAlbDel2XPath # Borrar albarán de salida
                WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                ElemValidar = gestAlmElements.gestALPEDAlbDelTit1XPath # ELIMINAR ALBARÁN
                ElemValidarTXT = gestAlmElements.gestALPEDAlbDelTit1TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDAlbDelTit2XPath  # ¿Está seguro de eliminar este albarán?'
                ElemValidarTXT = gestAlmElements.gestALPEDAlbDelTit2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDAlbDelKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDAlbDelOKXPath  # Eliminar
                ElemValidarTXT = gestElements.gestDOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                time.sleep(2)
                logger.debug('El albarán ' + self.albar + ' ha sido borrado')
            else:
                logger.debug('El albarán ' + self.albar + ' NO ha sido borrado')
                time.sleep(2)
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete the new delivery notes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete the new delivery notes --> {}'.format(resStep))
        assert resStep

    @then('I export delivery notes(in)')
    def exporto_albarán(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export delivery notes(in)')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:75]  # nombre original del fichero sin hora ni extension, ej:Listado de albaranes de entrada_20250512
            logger.debug('El nombreficorig es ' + nombreficorig)
            self.ficheroAlbaran = gestAlmElements.gestAlmExpFAlbETXT + self.ficexp[
                                                                  66:99]  # Nombre fichero completo, ej: Listado de albaranes de entrada_20250512_08263794.xlsx
            logger.debug('El nombre de ficheroAlbaran es '+ self.ficheroAlbaran)
            nombre = gestAlmElements.gestAlmExpDesLAlbETXT  # Listado de albaranes de entrada_20250512_08263794.xlsx
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroAlbaran)
        except Exception as e:
            logger.error(
                'Algún elemento en "I export delivery notes(in)" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export delivery notes(in) --> {}'.format(resStep))
        assert resStep

    @then('I open delivery notes(in) file')
    def abrir_fichero_albarán(self):
        logger.debug('INICIO STEP: I open delivery notes(in) file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFAlbETXT + ' (Global)'
            logger.debug(primeraLinea)
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroAlbaran)
        except Exception as e:
            logger.error('Algún elemento en "I open delivery notes(in) file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open delivery notes(in) file --> {}'.format(resStep))
        assert resStep

    @then('I valid form advance search delivery notes(in)')
    def valido_formulario_busquedaavanzada_albaranes(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I valid form advance search delivery notes(in)')
        resStep = True
        try:
            ElemValidar = gestElements.gestAvSeaID
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validación formulario búsqueda avanzada albaranes')
            ElemValidar = gestAlmElements.gestAlmBATitXPath  # BÚSQUEDA AVANZADA
            ElemValidarTXT = gestElements.gestAvSea2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBARefXPath  # Referencia
            ElemValidarTXT = gestElements.gestReferencia2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBACIAXPath # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            ini = 0
            fin = 7
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestALAlbBAFIXPath  # Fecha inicio*
            ElemValidarTXT = gestAlmElements.gestAlmFecIniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALAlbBAFFXPath # Fecha fin*
            ElemValidarTXT = gestAlmElements.gestAlmFecFinTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlMERIATPBEXPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            ini = 0
            fin = 6
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlMERIUbECPCXPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDBAProvXPath # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            ini = 0
            fin = 9
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDBAPProvXPath  # Producto de proveedor
            ElemValidarTXT = gestAlmElements.gestAlPEDBAPProvTXT
            ini = 0
            fin = 21
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDBATotXPath  # Total
            ElemValidarTXT = gestElements.gestTotal1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath  # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error(
                'Algún elemento en "I do advance search delivery notes(in)" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search delivery notes(in)--> {}'.format(resStep))
        assert resStep

    @then('I do advance search delivery notes(in)')
    def hago_busqueda_avanzada_albaranes(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I do advance search delivery notes(in)')
        resStep = True
        try:
            logger.debug('Busco albarán Pendiente de Validar que no hay ninguno')
            ElemValidar = gestAlmElements.gestAlMERTSBATMBMXPath # Rechazado
            ElemValidarTXT = gestAlmElements.gestAlmStRechTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestAlmMPBAKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMPBAOKXPath # Buscar
            ElemValidarTXT = gestElements.gestBus2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Verifico resultado busqueda avanzada de albaranes=0')
            ElemValidar = gestAlmElements.gestAlmMosAlbXPath # Mostrando del0al0de0albaranes
            #ElemValidarTXT =  gestAlmElements.gestAlmMos12TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I do advance search delivery notes(in)" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do advance search delivery notes(in)--> {}'.format(resStep))
        assert resStep

    @when('I click delivery notes(out)')
    def click_albaran_entrada(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click delivery notes(out)')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestPASXPath # Albarán de salida
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            self.tipoALB = 'OUT'
        except Exception as e:
            logger.error('Algún elemento en "I click delivery notes(out)" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click delivery notes(out) --> {}'.format(resStep))
        assert resStep

    @then('I see delivery notes(out)')
    def veo_albaranes_salida(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see delivery notes(out)')
        resStep = True
        try:
            logger.debug('Valido albaranes de salida')
            ElemValidar = gestAlmElements.gestAlmLisTitXPath  # LISTADO DE ALBARANES DE SALIDA
            ElemValidarTXT = gestAlmElements.gestALPEDAlbTit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Búsqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT  # QA
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmPEDNPedID  # Nuevo Albarán
            ElemValidarTXT = gestAlmElements.gestAlmPEDNAlbTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDAlbMarXPath  # Marcas:
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDAlbMarAllXPath  # Todas
            ElemValidarTXT = gestAlmElements.gestAlmAllTXT
            ini = 0
            fin = 5
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDAlbFec2XPath # Fecha:
            ElemValidarTXT = gestElements.gestFec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbFecValor  # Valor de fecha
            ElemValidarTXT = gestAlmElements.gestAlmFec2Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbFilXPath  # Filtros
            ElemValidarTXT = gestElements.gestFilTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbSta1XPath  # Devolución
            ElemValidarTXT = gestAlmElements.gestAlmStDevTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbSta2XPath  # Entrega
            ElemValidarTXT = gestAlmElements.gestAlmStEntTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbSta3XPath  # Otros
            ElemValidarTXT = gestAlmElements.gestAlmStOtrosTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosAlbXPath  # Mostrando..
            #ElemValidarTXT = gestAlmElements.gestAlmMos12TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Compruebo las columnas')
            ElemValidar = gestAlmElements.gestAlPEDAlbCol1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol2XPath  # Referencia
            ElemValidarTXT = gestElements.gestReferencia2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol3XPath  # Fecha
            ElemValidarTXT = gestElements.gestFecTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol4XPath  # Proveedor
            ElemValidarTXT = gestElements.gestProvTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol5XPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol6XPath  # Subtotal
            ElemValidarTXT = gestElements.gestSubtotal2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol7XPath  # Estado
            ElemValidarTXT = gestElements.gestStaTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol8XPath  # Pedido
            ElemValidarTXT = gestElements.gestAlPed2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol9XPath  # Creado por
            ElemValidarTXT = gestAlmElements.gestAlmCrePorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol10XPath  # Motivo
            ElemValidarTXT = gestAlmElements.gestAlPEDAlbCol10TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbCol11XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbPie1XPath  # Subtotal:
            ElemValidarTXT = gestElements.gestSubtotalTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDAlbPie2XPath  # El valor suele cambiar
            #ElemValidarTXT = gestAlmElements.gestAlPEDAlbPie2TXT
            #resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see delivery notes(out)" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see delivery notes(out) --> {}'.format(resStep))
        assert resStep

    @when('I click client order')
    def click_pedidos(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click client order')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestPeCXPath # Pedidos de cliente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click client order" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click client order --> {}'.format(resStep))
        assert resStep


    @then('I see client order')
    def veo_pedidos_a_proveedor(self):
        logger.debug('INICIO STEP: I see client order')
        pagina_gestAlm = self.driver
        resStep = True
        try:
            logger.debug('Valido listado pedidos de cliente')
            ElemValidar = gestAlmElements.gestAlmLisTitXPath  # LISTA DE PEDIDOS DE CLIENTE
            ElemValidarTXT = gestAlmElements.gestALPEDCLITitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Busqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDMarXPath  # Marcas:
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDMarValor  # Todas
            ElemValidarTXT = gestAlmElements.gestAlmAllTXT
            ini = 0
            fin = 5
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDFilXPath # Filtros:
            ElemValidarTXT = gestElements.gestFilTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStCanXPath # Cancelados
            ElemValidarTXT = gestAlmElements.gestAlmStCan2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStBorXPath # Borradores
            ElemValidarTXT = gestAlmElements.gestAlmStBorTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStPteXPath # Pendiente
            ElemValidarTXT = gestAlmElements.gestAlmStPteTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStEPXPath # En proceso
            ElemValidarTXT = gestAlmElements.gestAlmStEPTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStComXPath # Completado
            ElemValidarTXT = gestAlmElements.gestAlmStComTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDStIncXPath # Incidencias
            ElemValidarTXT = gestAlmElements.gestAlPEDStIncTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDFecXPath  # Fecha:
            ElemValidarTXT = gestElements.gestFec2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDFecValor  # Valor de fecha
            ElemValidarTXT = gestAlmElements.gestAlmFec3Valor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlmMosPedXPath  # Mostrando..
            ElemValidarTXT = gestAlmElements.gestAlmMos13TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDPie3XPath  # gestAlPEDPie4TXT
            ElemValidarTXT = gestAlmElements.gestAlPEDPie4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDPie1XPath  # Mostrar totales entregados
            ElemValidarTXT = gestAlmElements.gestAlPEDPie1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDSubEntXPath  # Subtotal
            ElemValidarTXT = gestElements.gestSubtotal2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDPie2XPath  # Ocultar franquicias
            ElemValidarTXT = gestAlmElements.gestAlPEDPie2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see client order" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see client order --> {}'.format(resStep))
        assert resStep

    @then('I export client order')
    def exporto_pedidos(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export client order')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:68]  # nombre original del fichero sin hora ni extension ej:XXX
            logger.debug('El nombreficorig es ' + nombreficorig)
            self.ficheroPedCli = gestAlmElements.gestAlmExpFPedCliTXT + self.ficexp[
                                                                  63:102]  # Nombre fichero completo, ej: XXX
            logger.debug('El nombre de ficheroPedCli es '+ self.ficheroPedCli)
            nombre = gestAlmElements.gestAlmExpDesLPedCliTXT  # XXX
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroPedCli)
        except Exception as e:
            logger.error(
                'Algún elemento en "I export client order" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export client order --> {}'.format(resStep))
        assert resStep

    @then('I open client order file')
    def abrir_fichero_pedidos(self):
        logger.debug('INICIO STEP: I open client order file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFPedCliTXT + ' (Global)'
            logger.debug(primeraLinea)
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroPedCli)
        except Exception as e:
            logger.error('Algún elemento en "I open client order file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open client order file --> {}'.format(resStep))
        assert resStep

    @then('I export delivery notes(out)')
    def exporto_albarán_salida(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export delivery notes(out)')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:74]  # nombre original del fichero sin hora ni extension ej:Listado de albaranes de salida_20250512
            logger.debug('El nombreficorig es ' + nombreficorig)
            self.ficheroAlbaran = gestAlmElements.gestAlmExpFAlbSTXT + self.ficexp[
                                                                  65:98]  # Nombre fichero completo, ej: Listado de albaranes de salida_20250512_08263794.xlsx
            logger.debug('El nombre de ficheroAlbaran es '+ self.ficheroAlbaran)
            nombre = gestAlmElements.gestAlmExpDesLAlbSTXT  # Listado de albaranes de salida_20250512_08263794.xlsx
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroAlbaran)
        except Exception as e:
            logger.error(
                'Algún elemento en "I export delivery notes(out)" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export delivery notes(out) --> {}'.format(resStep))
        assert resStep

    @then('I open delivery notes(out) file')
    def abrir_fichero_albarán_salida(self):
        logger.debug('INICIO STEP: I open delivery notes(out) file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFAlbSTXT + ' (Global)'
            logger.debug(primeraLinea)
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroAlbaran)
        except Exception as e:
            logger.error('Algún elemento en "I open delivery notes(out) file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open delivery notes(out) file --> {}'.format(resStep))
        assert resStep

    @when('I click external purchases')
    def click_compras_externas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click external purchases')
        resStep = True
        try:
            ElemValidar = gestAlmElements.latPagGestCEXPath # Compras externas
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I click external purchases" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click external purchases --> {}'.format(resStep))
        assert resStep

    @then('I see external purchases')
    def veo_compras_externas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I see external purchases')
        resStep = True
        try:
            logger.debug('Valido external purchases')
            ElemValidar = gestAlmElements.gestALPEDTitXPath  # COMPRAS EXTERNAS
            ElemValidarTXT = gestAlmElements.gestALPEDCETitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID  # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestAvSeaID  # Búsqueda avanzada
            ElemValidarTXT = gestElements.gestAvSeaTXT  # QA
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEID  # Nueva compra
            ElemValidarTXT = gestAlmElements.gestALPEDNCETXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestAlPEDCEBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDCEMarXPath  # Marcas:
            ElemValidarTXT = gestAlmElements.gestAlmMar2TXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDCEAllXPath  # Todas
            ElemValidarTXT = gestAlmElements.gestAlmAllTXT
            ini = 0
            fin = 5
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlPEDCEMosXPath  # Mostrando..
            ElemValidarTXT = gestAlmElements.gestAlmMos14TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Compruebo las columnas')
            ElemValidar = gestAlmElements.gestALPEDCEC1XPath  # Cód. Interno
            ElemValidarTXT = gestAlmElements.gestAlmMCoCodTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC2XPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC3XPath  # Fecha de compra
            ElemValidarTXT = gestElements.gestFecComTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC4XPath  # Fecha de creación
            ElemValidarTXT = gestElements.gestFecCreTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC5XPath  # Nombre
            ElemValidarTXT = gestElements.gestNomTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC6XPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC7XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC8XPath  # Precio unitario (€)
            ElemValidarTXT = gestElements.gestPrecioUnit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC9XPath  # Total
            ElemValidarTXT = gestElements.gestTotal1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC10XPath  # Total + IVA
            ElemValidarTXT = gestElements.gestTotalI2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC11XPath  # IVA
            ElemValidarTXT = gestElements.gestAlIVATXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDCEC12XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see external purchases" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see external purchases --> {}'.format(resStep))
        assert resStep

    @then('I fill fields in the form new external purchases')
    def rellenar_formulario_compras_externas(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I fill fields in the form new external purchases')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestALPEDNCEID  # Nuevo compra
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Validar formulario nuevo compra')
            ElemValidar = gestElements.gestVolverListID  # Volver
            ElemValidarTXT = gestElements.gestVolverTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEFVSXPath  # Fecha de la variacion de stock
            ElemValidarTXT = gestAlmElements.gestALPEDNCEFVSTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEAlmXPath  # Almacén
            ElemValidarTXT = gestElements.gestAlmacenTXT
            ini = 0
            fin = 7
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestALPEDNCEIngXPath  # INGREDIENTES
            ElemValidarTXT = gestAlmElements.gestAlmIngTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEV1XPath  # Ingrediente:
            ElemValidarTXT = gestAlmElements.gestAlmIng3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEV2XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEV3XPath  # Cantidad:
            ElemValidarTXT = gestElements.gestCan2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEV4XPath  # Precio unitario (€):
            ElemValidarTXT = gestElements.gestPrecioUnitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEV5XPath  # IVA
            ElemValidarTXT = gestElements.gestAlIVATXT
            ini = 0
            fin = 3
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestALPEDNCEV6XPath  # Total:
            ElemValidarTXT = gestElements.gestTotal2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEV7XPath  # Total + IVA
            ElemValidarTXT = gestElements.gestTotalITXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEC1XPath  # Ingrediente:
            ElemValidarTXT = gestAlmElements.gestAlmIng4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEC2XPath  # Cantidad
            ElemValidarTXT = gestElements.gestCanTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEC3XPath  # Unidad
            ElemValidarTXT = gestElements.gestUniTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEC4XPath  # Precio unitario (€)
            ElemValidarTXT = gestElements.gestPrecioUnit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEC5XPath  # IVA
            ElemValidarTXT = gestElements.gestAlIVATXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            resStep = obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestALPEDNCEC6XPath  # Total
            ElemValidarTXT = gestElements.gestTotal1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEC7XPath  # Total + IVA
            ElemValidarTXT = gestElements.gestTotalI2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEC8XPath  # Eliminar
            ElemValidarTXT = gestElements.gestDOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            logger.debug('Relleno el formulario')
            ElemValidar = gestAlmElements.gestALPEDNCEAlmInput  # Almacén
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEAlmValor  # LTL Fleming
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEIngInput  # Seleccionar ingrediente
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEIngValor  # Albahaca
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEUnitInput  # selecciono unidad
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEUnitValor  # UD (100 G)
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCECanInput  # seleccionar cantidad
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidarValor = gestElements.gestCantidad1TXT  # 1
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            ElemValidar = gestAlmElements.gestALPEDNCEPreUnitInput  # Seleccionar precio unitario
            ElemValidarValor = gestElements.gestCantidad2TXT  # 2
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEPreIVAInput  # IVA 21%
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEAddXPath # Añadir
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestALPEDNCETot1XPath  # Coste total:
            ElemValidarTXT = gestAlmElements.gestALPEDNCETot1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCETot2XPath  # 2.42 €
            ElemValidarTXT = gestAlmElements.gestALPEDNCETot2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEOKID # Generar compra externa
            ElemValidarTXT = gestAlmElements.gestALPEDNCEOKTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEGCEtitXPath # GENERAR COMPRA EXTERNA
            ElemValidarTXT = gestAlmElements.gestALPEDNCEGCEtitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEGCEtit2XPath # ¿Está seguro de generar la compra externa en esta fecha?
            ElemValidarTXT = gestAlmElements.gestALPEDNCEGCEtit2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDNCEGCEKOXPath # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEOKID # Generar compra externa
            pagina_gestAlm.find_element(by=By.ID, value=ElemValidar).click()
            time.sleep(1)
            ElemValidar = gestAlmElements.gestALPEDNCEGCEOKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
        except Exception as e:
            logger.error('Algún elemento en "I fill fields in the form new external purchases" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I I fill fields in the form new external purchases --> {}'.format(resStep))
        assert resStep

    @then('I search and delete the new external purchases')
    def ver_desactivar_compra_externa(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I search and delete the new external purchases')
        resStep = True
        try:
            ElemValidar = gestAlmElements.gestALPEDCE1XPath
            compraexterna = pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).text
            logger.debug(compraexterna)
            logger.debug(gestAlmElements.hoy)
            if compraexterna == gestAlmElements.hoy:
                ElemValidar = gestAlmElements.gestALPEDNCEDELXPath  # eliminar compra externa
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                logger.debug('Cancelar commpra externa')
                ElemValidar = gestAlmElements.gestALPEDNCEDELTitXPath  # CANCELAR COMPRA EXTERNA
                ElemValidarTXT = gestAlmElements.gestALPEDNCEDELTitTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDNCEDELTit2XPath  # ¿Estás seguro que desea cancelar esta compra externa?
                ElemValidarTXT = gestAlmElements.gestALPEDNCEDELTit2TXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDNCEDELKOXPath  # Cancelar
                ElemValidarTXT = gestElements.gestKOTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                ElemValidar = gestAlmElements.gestALPEDNCEDELOKXPath  # Aceptar
                ElemValidarTXT = gestElements.gestAOKTXT
                resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
                pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
                resStep = True & resStep
            else:
                logger.info('DCompra externa NO localizada')
                resStep = False
        except Exception as e:
            logger.error('Algún elemento en "I search and delete the new external purchases" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search and delete the new external purchases --> {}'.format(resStep))
        assert resStep


    @then('I export external purchases')
    def exporto_comprasexternas(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export external purchases')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:54]  # nombre original del fichero sin hora ni extension, ej: Compras externas_20250527
            logger.debug('El nombreficorig es ' + nombreficorig)
            self.ficheroComExt = gestAlmElements.gestAlmExpFCETXT + self.ficexp[
                                                                  45:73]  # Nombre fichero completo, ej: Compras externas_20250527_12170818.xlsx
            logger.debug('El nombre de ficheroComExt es '+ self.ficheroComExt)
            nombre = gestAlmElements.gestAlmExpDesLCETXT  # Listado%20de%20compras%20externas_
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroComExt)
        except Exception as e:
            logger.error(
                'Algún elemento en "I export external purchases" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export external purchases --> {}'.format(resStep))
        assert resStep

    @then('I open external purchases file')
    def abrir_fichero_comprasexternas(self):
        logger.debug('INICIO STEP: I open external purchases file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFCETXT + ' (Global)'
            logger.debug(primeraLinea)
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroComExt)
        except Exception as e:
            logger.error('Algún elemento en "I open external purchases file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open external purchases file --> {}'.format(resStep))
        assert resStep

    @when('I click menu recipes')
    def click_recetas_carta(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click menu recipes')
        resStep = True
        try:
             ElemValidar = gestAlmElements.latPagGestReCXPath # Recetas de carta
             pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
             ElemValidar = gestAlmElements.gestAlmRC1erElXPath  # tabla cargada
             WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        except Exception as e:
            logger.error('Algún elemento en "I click menu recipes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click menu recipes --> {}'.format(resStep))
        assert resStep

    @then('I see menu recipes')
    def veo_recetas_carta(self):
        logger.debug('INICIO STEP: I see menu recipes')
        pagina_gestAlm = self.driver
        resStep = True
        try:
            logger.debug('Valido listado recetas de carta')
            ElemValidar = gestAlmElements.gestAlmLisTitXPath  # RELACIÓN DE PRODUCTOS DE CARTA Y ESCANDALLOS
            ElemValidarTXT = gestAlmElements.gestALPEDRCTitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestElements.gestExpID # Exportar
            ElemValidarTXT = gestElements.gestExpTXT
            resStep = obtenerTextosByID(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCBusXPath  # Buscar:
            ElemValidarTXT = gestElements.gestBusTXT
            ini = 0
            fin = 7
            obtenerParteCampo(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT, ini, fin)
            ElemValidar = gestAlmElements.gestAlmMosRCXPath  # Mostrando..
            ElemValidarTXT = gestAlmElements.gestAlmMos15TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol1XPath  # Producto de carta
            ElemValidarTXT = gestAlmElements.gestALPEDRCPCarTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol2XPath  # Escandallo
            ElemValidarTXT = gestAlmElements.gestALPEDRCEscTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol3XPath  # Combo
            ElemValidarTXT = gestAlmElements.gestALPEDRCComTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol4XPath  # Precio de venta medio
            ElemValidarTXT = gestAlmElements.gestALPEDRCPVMTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol5XPath  # Coste total de la receta
            ElemValidarTXT = gestAlmElements.gestALPEDRCCTRTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol6XPath  # Beneficio(€)
            ElemValidarTXT = gestAlmElements.gestALPEDRCBenTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol7XPath  # Margen
            ElemValidarTXT = gestAlmElements.gestALPEDRCMarTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCCol8XPath  # Acciones
            ElemValidarTXT = gestElements.gestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I see menu recipes" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see menu recipes --> {}'.format(resStep))
        assert resStep


    @then('I advance page menu recipes')
    def avanzar_pagina_recetas_carta(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I advance page menu recipes')
        resStep = True
        try:
            Pg1 = gestAlmElements.gestAlmRCPg1XPath
            Pg1TXT = gestAlmElements.gestAlmRCPg1TXT
            Mos = gestAlmElements.gestAlmMosXRCXPath
            AvP = gestAlmElements.gestAlmRCAvPXPath
            MP1 = gestAlmElements.gestAlmMos15TXT
            MP2 = gestAlmElements.gestAlmMos16TXT
            MP3 = gestAlmElements.gestAlmMos17TXT
            MP4 = gestAlmElements.gestAlmMos18TXT
            MP5 = gestAlmElements.gestAlmMos19TXT
            ElemValidar = avanzar_pagina(resStep, pagina_gestAlm, Pg1, Pg1TXT, Mos, AvP, MP1, MP2, MP3, MP4, MP5)
        except Exception as e:
            logger.error('Algún elemento en "I advance page menu recipes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
            logger.error(resStep)
        logger.error(resStep)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I advance page menu recipes --> {}'.format(resStep))
        assert resStep

    @then('I turn back page menu recipes')
    def retroceder_recetas_carta(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I turn back page menu recipes')
        resStep = True
        try:
            Pg5 = gestAlmElements.gestAlmRCPg5XPath
            Pg5TXT = gestAlmElements.gestAlmRCPg5TXT
            Mos = gestAlmElements.gestAlmMosXRCXPath
            ReP = gestAlmElements.gestAlmRCRePXPath
            MP1 = gestAlmElements.gestAlmMos1TXT
            MP2 = gestAlmElements.gestAlmMos2TXT
            MP3 = gestAlmElements.gestAlmMos3TXT
            MP4 = gestAlmElements.gestAlmMos4TXT
            MP5 = gestAlmElements.gestAlmMos5TXT
            ElemValidar = retroceder_pagina(resStep, pagina_gestAlm, Pg5, Pg5TXT, Mos, ReP, MP1, MP2, MP3, MP4,MP5)
        except Exception as e:
            logger.error('Algún elemento en "I turn back page menu recipes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I turn back page menu recipes --> {}'.format(resStep))
        assert resStep

    @then('I export menu recipes')
    def exporto_recetas_carta(self):
        pagina_gestAlm = self.driver
        if self.navegator == 'edge':
            deshabilitar_nueva_ventana_edge(pagina_gestAlm)
        logger.debug('INICIO STEP: I export menu recipes')
        resStep = True
        try:
            exporto = exportar(resStep, pagina_gestAlm)
            self.ficexp = exporto[0]
            resStep = exporto[1]
            nombreficorig = self.ficexp[
                            27:97]  # nombre original del fichero sin hora ni extension, Ej: Relación de productos de carta y escandallos_20250529_10122369
            logger.debug('El nombreficorig es ' + nombreficorig)
            self.ficheroRC = gestAlmElements.gestAlmExpFRCTXT + self.ficexp[
                                                                  88:111]  # Nombre fichero completo, ej: Relación de productos de carta y escandallos_20250529_09511922.xlsx
            logger.debug('El nombre de ficheroRecetaCarta es '+ self.ficheroRC)
            nombre = gestAlmElements.gestAlmExpDesLRCTXT  # Relación%20de%20productos%20de%20carta%20y%20escandallos_
            resStep = ficheroExp(resStep, pagina_gestAlm, nombre, nombreficorig, self.ficheroRC)
        except Exception as e:
            logger.error(
                'Algún elemento en "I export menu recipes" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I export menu recipes --> {}'.format(resStep))
        assert resStep

    @then('I open menu recipes file')
    def abrir_fichero_recetas_carta(self):
        logger.debug('INICIO STEP: I open menu recipes file')
        resStep = True
        try:
            logger.debug('Abrir fichero')
            primeraLinea = gestAlmElements.gestAlmExpFRCTXT + ' (Global)'
            logger.debug(primeraLinea)
            resStep = abrirFichero(resStep, primeraLinea, self.ficheroRC)
        except Exception as e:
            logger.error('Algún elemento en "I open menu recipes file" no encontrado: {}'.format(resStep, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I open menu recipes file --> {}'.format(resStep))
        assert resStep

    @step('I search a product')
    def buscar_recetas_carta(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I search a product')
        resStep = True
        try:
            logger.debug('Hacer busqueda de producto de carta')
            ElemValidar = gestAlmElements.gestALPEDRCBusInput  # Buscar
            WebDriverWait(pagina_gestAlm, 15).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
            ElemValidarValor = gestAlmElements.gestAlmMPBAIngValor
            rellenarCampo(pagina_gestAlm, ElemValidar, ElemValidarValor)
            time.sleep(2)
            logger.debug('Resultados de busqueda de producto')
            ElemValidar = gestAlmElements.gestALPEDRCResCol1XPath  # 1/3 Alhambra Reserva
            ElemValidarTXT = gestAlmElements.gestAlMERAPResUlt2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResCol2XPath  # 1/3 Alhambra Reserva
            ElemValidarTXT = gestAlmElements.gestAlMERAPResUlt2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResCol3XPath  # 3.63636 €
            ElemValidarTXT = gestAlmElements.gestALPEDRCResCol3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResCol4XPath  # '1.12250 €
            ElemValidarTXT = gestAlmElements.gestALPEDRCResCol4TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResCol5XPath  # 2.51386 €
            ElemValidarTXT = gestAlmElements.gestALPEDRCResCol5TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResCol6XPath  # 69.13 %'
            ElemValidarTXT = gestAlmElements.gestALPEDRCResCol6TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResColX1XPath  # P Alhambra Reservar
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResColX2XPath  # P Alhambra Reservar
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResColX3XPath  # 0.00000 €
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResColX4XPath  # 0.00000 €
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResColX5XPath  # 0.00000 €
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCResColX6XPath  # 0.00 %
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX6TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep

            logger.debug('Resultados de busqueda de producto después de ordenar por Margen')
            ElemValidar = gestAlmElements.gestALPEDRCOrdXPath  # Ordenar por margen
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestALPEDRCOrdColO1XPath  # 83.51 %
            ElemValidarTXT = gestAlmElements.gestALPEDRCOrdColO1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCOrdColO2XPath  # 83.51 %
            ElemValidarTXT = gestAlmElements.gestALPEDRCOrdColO1TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCOrdColO3XPath  # 69.13 %
            ElemValidarTXT = gestAlmElements.gestALPEDRCOrdColO3TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCOrdColO4XPath  # 0.00 %
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX6TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCOrdColO5XPath  # 0.00 %
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX6TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCOrdColO6XPath  # 0.00 %
            ElemValidarTXT = gestAlmElements.gestALPEDRCResColX6TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
        except Exception as e:
            logger.error('Algún elemento en "I search a product" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I search a product --> {}'.format(resStep))
        assert resStep

    @step("I edit a product's recipe")
    def buscar_recetas_carta(self):
        pagina_gestAlm = self.driver
        logger.debug("INICIO STEP: I edit a product's recipe")
        resStep = True
        try:
            logger.debug('Editar producto de carta')
            ElemValidar = gestAlmElements.gestALPEDRCEdP1XPath  # Editar
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestALPEDRCEdP1TitXPath # EDITAR RECETA
            ElemValidarTXT = gestAlmElements.gestALPEDRCEdP1TitTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCEdP1NomXPath # Nombre*
            ElemValidarTXT = gestElements.gestNom2TXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCEdP1EscXPath # Escandallo
            ElemValidarTXT = gestAlmElements.gestALPEDRCEscTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCEdP1NomInput  # Alhambra Especial 33cl DELIVERY
            ElemValidarTXT = gestAlmElements.gestALPEDRCEdP1NomValor
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCEdP1EscInput
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestAlmElements.gestALPEDRCEdP1EscValor  # 1/2 TOSTADA MIXTA
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            ElemValidar = gestAlmElements.gestALPEDRCEdP1OKXPath  # Aceptar
            ElemValidarTXT = gestElements.gestAOKTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            ElemValidar = gestAlmElements.gestALPEDRCEdP1KOXPath  # Cancelar
            ElemValidarTXT = gestElements.gestKOTXT
            resStep = obtenerTextos(resStep, pagina_gestAlm, ElemValidar, ElemValidarTXT) & resStep
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            resStep = True & resStep
        except Exception as e:
            logger.error('Algún elemento en "I edit a product´s recipe" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug("FIN STEP: I edit a product's recipe --> {}".format(resStep))
        assert resStep