import time
import logging
import random
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobjects import GestionAlmacen, GestionFacturacion, GestionUsuarios, GestionVentas, Common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('WebLogs')
gestAlmElements = GestionAlmacen.GestionAlmacen()
gestFacElements = GestionFacturacion.GestionFacturacion()
gestUsuElements = GestionUsuarios.GestionUsuarios()
gestVenElements = GestionVentas.GestionVentas()
gestElements = Common.Common()

def deshabilitar_nueva_ventana_edge(pagina_gestAlm):
    logger.debug('Deshabilitar que abra el fichero Office en el navegador')
    pagina_gestAlm.get("edge://settings/downloads#All")
    time.sleep(1)
    pagina_gestAlm.find_element(by=By.XPATH,
                             value='//*[@id="section_downloads"]/div[2]/div/div[3]/div/div[1]/div[2]/div/div/input').click()
    pagina_gestAlm.back() # flecha hacia atrás, retrocede


def obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT):
    pagina.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
    title = pagina.find_element(by=By.XPATH, value=ElemValidar).text
    resStep = (ElemValidarTXT == title) & resStep
    logger.info(ElemValidarTXT + ' mi variable la comparo con el título ' + title + ' --> ' + format(ElemValidarTXT == title))
    time.sleep(2)
    return resStep


def obtenerParteCampo(resStep, pagina, ElemValidar, ElemValidarTXT, ini, fin):
    pagina.find_element(by=By.XPATH, value=ElemValidar).is_displayed()
    campo = pagina.find_element(by=By.XPATH, value=ElemValidar).text
    title = campo[ini:fin]
    logger.debug ('La parte extraida es '+ title)
    resStep = (ElemValidarTXT == title) & resStep
    logger.info(ElemValidarTXT + ' mi variable la comparo con el título ' + title + ' --> ' + format(ElemValidarTXT == title))
    time.sleep(2)
    return resStep


def obtenerTextosByID(resStep, pagina, ElemValidar, ElemValidarTXT):
    pagina.find_element(by=By.ID, value=ElemValidar).is_displayed()
    title = pagina.find_element(by=By.ID, value=ElemValidar).text
    resStep = (ElemValidarTXT == title) & resStep
    logger.info(ElemValidarTXT + ' mi variable la comparo con el título ' + title + ' --> ' + format(ElemValidarTXT == title))
    return resStep


def obtenerClase(resStep, pagina, ElemValidar, ElemValidarCLASS):
    pagina.find_element(by=By.CSS_SELECTOR, value=ElemValidar).is_displayed()
    ElemCLASS = pagina.get_attribute("class")
    resStep = (ElemValidarCLASS == ElemCLASS) & resStep
    logger.info(ElemValidarCLASS + ' mi variable la comparo con el título ' + ElemCLASS + ' --> ' + format(ElemValidarCLASS == ElemCLASS))
    return resStep


def rellenarCampo(pagina, ElemValidar, ElemValidarValor):
    pagina.find_element(by=By.XPATH, value=ElemValidar).clear()
    pagina.find_element(by=By.XPATH, value=ElemValidar).send_keys(ElemValidarValor)
    pagina.find_element(by=By.XPATH, value=ElemValidar).send_keys(Keys.TAB)
    logger.debug('El ' + ElemValidar + ' es rellenado con ' + ElemValidarValor)


def columnas_GA(resStep, pagina):
    logger.debug('8 columnas')
    ElemValidar = gestAlmElements.gestAlmMCo1XPath # Ref.
    ElemValidarTXT = gestElements.gestReferencia3TXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestAlmElements.gestAlmMCo2XPath # Proveedor
    ElemValidarTXT = gestElements.gestProvTXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestAlmElements.gestAlmMCo3XPath
    ElemValidarTXT = gestAlmElements.gestAlmMCoCIFTXT # CIF
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestAlmElements.gestAlmMCo4XPath
    ElemValidarTXT = gestAlmElements.gestAlmMCoTelTXT # Teléfono
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestAlmElements.gestAlmMCo5XPath
    ElemValidarTXT = gestAlmElements.gestAlmMCoEmaTXT # Email
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestAlmElements.gestAlmMCo6XPath
    ElemValidarTXT = gestAlmElements.gestAlmMCoDTOTXT # Desc. albarán
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestAlmElements.gestAlmMCo7XPath
    ElemValidarTXT = gestAlmElements.gestAlmMCoRapTXT # Rappel
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestAlmElements.gestAlmMCo8XPath
    ElemValidarTXT = gestElements.gestAccTXT # Acciones
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    return resStep


def columnas_GF(resStep, pagina):  # Columnas Gestión Facturación
    logger.debug('8 columnas')
    ElemValidar = gestFacElements.gestFacMCo1XPath
    ElemValidarTXT = gestFacElements.gestFacMCoNIFTXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestFacElements.gestFacMCo2XPath
    ElemValidarTXT = gestFacElements.gestFacMCoNomTXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestFacElements.gestFacMCo3XPath
    ElemValidarTXT = gestFacElements.gestFacMCoEmaTXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestFacElements.gestFacMCo4XPath
    ElemValidarTXT = gestFacElements.gestFacMCoTelTXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestFacElements.gestFacMCo5XPath
    ElemValidarTXT = gestFacElements.gestFacMCoCiuTXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    ElemValidar = gestFacElements.gestFacMCo6XPath
    ElemValidarTXT = gestFacElements.gestFacMCoAccTXT
    resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
    return resStep


def crear_rol(resStep, pagina):
    logger.info('INICIO STEP:I create a rol')
    ElemValidar = gestUsuElements.gestUsuRolCreID
    pagina.find_element(by=By.ID, value=ElemValidar).click()
    try:
        ElemValidar = gestUsuElements.gestUsuCreRolTitXPath
        ElemValidarTXT = gestUsuElements.gestUsuCreRolTitTXT
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        ElemValidar = gestUsuElements.gestUsuCreRolNomXPath
        ElemValidarTXT = gestUsuElements.gestUsuCreRolNomTXT
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        ElemValidar = gestUsuElements.gestUsuCreRolNomInput
        newrol = gestUsuElements.gestUsuCreRolNomValor + format(random.randint(1, 100))
        pagina.find_element(by=By.XPATH, value=ElemValidar).send_keys(newrol)
        ElemValidar = gestUsuElements.gestUsuCreRolCloXPath
        ElemValidarTXT = gestUsuElements.gestUsuCreRolCloTXT
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        ElemValidar = gestUsuElements.gestUsuCreRolCloInput
        pagina.find_element(by=By.XPATH, value=ElemValidar).click()
        time.sleep(2)
        ElemValidar = gestUsuElements.gestUsuCreRolKOXPath  # Cancelar
        ElemValidarTXT = gestUsuElements.gestUsuCreRolKOTXT
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        ElemValidar = gestUsuElements.gestUsuCreRolOKXPath  # Aceptar
        ElemValidarTXT = gestUsuElements.gestUsuCreRolOKTXT
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        pagina.find_element(by=By.XPATH, value=ElemValidar).click()  # Acepto
    except Exception as e:
        logger.error('Algún elemento en "I create a rol" no encontrado --> {}'.format(ElemValidar, e))
        resStep = False
    return newrol, resStep


def exportar(resStep, pagina):
    try:
        ElemValidar = gestElements.gestExpID # Exportar
        WebDriverWait(pagina, 60).until(EC.visibility_of_element_located((By.ID, ElemValidar)))
        pagina.find_element(by=By.ID, value=ElemValidar).click()
        time.sleep(2)
        ElemValidar = gestElements.gestExpOKXPath
        ElemValidarTXT = gestElements.gestExpOKTXT # EXPORTACIÓN EXITOSA
        WebDriverWait(pagina, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)

        logger.debug('Comprobación del nombre del fichero')
        ElemValidar = gestElements.gestDesXPath # DESCARGAR
        WebDriverWait(pagina, 30).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        ElemValidarTXT = gestElements.gestDesTXT
        time.sleep(2)
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        ficexp = pagina.find_element(by=By.XPATH, value=ElemValidar).get_attribute("href")
        logger.info ('el nombre del fichero es ' + ficexp)
    except Exception as e:
        logger.error('Algún elemento en "exportar" no encontrado: {}'.format(ElemValidar, e))
        resStep = False
    return ficexp, resStep


def exportar_sinboton(resStep, pagina):
    try:
        ElemValidar = gestElements.gestExpOKXPath
        ElemValidarTXT = gestElements.gestExpOKTXT  # EXPORTACIÓN EXITOSA
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)

        logger.debug('Comprobacion del nombre del fichero')
        ElemValidar = gestElements.gestDesXPath
        WebDriverWait(pagina, 60).until(EC.visibility_of_element_located((By.XPATH, ElemValidar)))
        ElemValidarTXT = gestElements.gestDesTXT  # DESCARGAR
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        ficexp = pagina.find_element(by=By.XPATH, value=ElemValidar).get_attribute("href")
    except Exception as e:
        logger.error('Algún elemento en "exportar" no encontrado: {}'.format(ElemValidar, e))
        resStep = False
    return ficexp, resStep


def ficheroExp(resStep, pagina, nombre, nombreficorig, fichero):
    try:
        nombrefic = nombre + time.strftime("%Y%m%d")  # por ej: nombre calculado = Listado%20de%20unidades + fecha
        logger.debug('Los nombres comparados son, nombregenerado y nombreoriginal: '+ nombrefic + ' y ' + nombreficorig)
        if nombrefic == nombreficorig:
            logger.debug('Fichero exportado con el nombre: ' + fichero)
            resStep = True & resStep
        else:
            logger.debug('Fichero exportado con nombre diferente a: ' + fichero)
            resStep = False
        logger.debug('Descargar')
        ElemValidar = gestElements.gestDesXPath
        pagina.find_element(by=By.XPATH, value=ElemValidar).click()
        time.sleep(2)
        resStep = True & resStep
    except Exception as e:
        logger.error('Algún elemento en "ficheroExp" no encontrado: {}'.format(ElemValidar, e))
        resStep = False
    return resStep


def abrirFichero(resStep, primeraLinea, fichero):
    try:
        # to load the workbook with its path
        ficheroloc = gestElements.gestdirDes + fichero
        logger.info('Fichero a abrir ' + ficheroloc)
        ElemValidar = openpyxl.load_workbook(ficheroloc)
        logger.debug('fichero ' + ficheroloc + ' localizado')
        # to identify active worksheet
        s = ElemValidar.active
        # to identify the cell
        c1 = s.cell(row=1, column=1)
        if primeraLinea in c1.value:
            logger.debug(primeraLinea + ' esta en el título del ' + ficheroloc)
            resStep = True & resStep
        else:
            logger.debug(primeraLinea + ' NO esta en el título del ' + ficheroloc)
            resStep = False
        # to retrieve the cell value and print
    except Exception as e:
        logger.error('Algún elemento en "abrirFichero" no encontrado: {}'.format(ElemValidar, e))
        resStep = False
    return resStep


def avanzar_pagina (resStep, pagina, Pg1, Pg1TXT, Mos, AvP, MP1, MP2, MP3, MP4, MP5):
    try:
        logger.debug('Pulso avanzar')
        ElemValidar = Pg1  # Valida que está en la página 1
        ElemValidarTXT = Pg1TXT
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        pagina.find_element(by=By.XPATH, value=Pg1).click()
        time.sleep(2)
        ElemValidar = Mos
        logger.info(Mos)
        ElemValidarTXT = MP1
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text
        resStep = (Mostrando == ElemValidarTXT) & resStep
        pagina.find_element(by=By.XPATH, value=AvP).click()
        time.sleep(2)
        ElemValidarTXT = MP2
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text
        resStep = (Mostrando == ElemValidarTXT) & resStep
        pagina.find_element(by=By.XPATH, value=AvP).click()
        time.sleep(2)
        ElemValidarTXT = MP3
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text
        resStep = (Mostrando == ElemValidarTXT) & resStep
        pagina.find_element(by=By.XPATH, value=AvP).click()
        time.sleep(2)
        ElemValidarTXT = MP4
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text
        pagina.find_element(by=By.XPATH, value=AvP).click()
        resStep = (Mostrando == ElemValidarTXT) & resStep
        time.sleep(2)
        ElemValidarTXT = MP5
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text
        resStep = (Mostrando == ElemValidarTXT) & resStep
        time.sleep(2)
    except Exception as e:
        logger.error('Algún elemento en avanzar pagina no encontrado: {}'.format(ElemValidar, e))
        resStep = False
    return resStep


def retroceder_pagina (resStep, pagina, Pg5, Pg5TXT, Mos, ReP, MP1, MP2, MP3, MP4, MP5):
    try:
        logger.debug('Retrocedo en la 5')
        ElemValidar = Pg5  # Valida estar en la página 5
        ElemValidarTXT = Pg5TXT
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        pagina.find_element(by=By.XPATH, value=ElemValidar).click()
        time.sleep(2)
        ElemValidar = Mos
        ElemValidarTXT = MP5  # Mostrando del81al100de...proveedores
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text  # actualiza el valor de mostrando
        resStep = (Mostrando == ElemValidarTXT) & resStep
        pagina.find_element(by=By.XPATH, value=ReP).click()
        time.sleep(2)
        ElemValidarTXT = MP4
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text # actualiza el valor de mostrando
        resStep = (Mostrando == ElemValidarTXT) & resStep
        pagina.find_element(by=By.XPATH, value=ReP).click()
        time.sleep(2)
        ElemValidarTXT = MP3
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text # actualiza el valor de mostrando
        resStep = (Mostrando == ElemValidarTXT) & resStep
        pagina.find_element(by=By.XPATH, value=ReP).click()
        time.sleep(3)
        ElemValidarTXT = MP2
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text # actualiza el valor de mostrando
        resStep = (Mostrando == ElemValidarTXT) & resStep
        pagina.find_element(by=By.XPATH, value=ReP).click()
        time.sleep(2)
        ElemValidarTXT = MP1
        resStep = obtenerTextos(resStep, pagina, ElemValidar, ElemValidarTXT)
        Mostrando = pagina.find_element(by=By.XPATH, value=ElemValidar).text # actualiza el valor de mostrando
        resStep = (Mostrando == ElemValidarTXT) & resStep
        time.sleep(2)
    except Exception as e:
        logger.error('Algún elemento en retroceder_pagina no encontrado: {}'.format(ElemValidar, e))
        resStep = False
    return resStep

