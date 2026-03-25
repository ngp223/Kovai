import time
import unittest
import logging
from behave import then
from selenium.webdriver.common.by import By
from pageobjects import GestionRestaurantes, HomeUser
from commons import obtenerTextos


logger = logging.getLogger('WebLogs')
gestResElements = GestionRestaurantes.GestionRestaurantes()
homeUserElements = HomeUser.HomeUser()


class gestionRestaurantes(unittest.TestCase):
    @then('I see gestion de restaurantes')
    def see_gestion_restaurantes(self):
        pagina_gestRes = self.driver
        logger.debug('INICIO STEP: I see gestion de restaurantes')
        resStep = True
        try:
            ElemValidar = gestResElements.titPagGestResXPath
            ElemValidarTXT = gestResElements.titPagGestResTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            logger.warning("Titulo de gestion de restaurantes --> {}".format(resStep))
            ElemValidar = gestResElements.nomPagGestRes
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_gestRes.title + ' --> ' + format(ElemValidar == pagina_gestRes.title))
            resStep = (ElemValidar == pagina_gestRes.title) & resStep
            logger.warning("Nombre de la pagina abierta --> {}".format(resStep))
            logger.debug(gestResElements.url + ' lo comparo con: ' + pagina_gestRes.current_url + ' --> ' + format(gestResElements.url == pagina_gestRes.current_url))
            resStep = (gestResElements.url == pagina_gestRes.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "gestion de restaurantes" no encontrado --> {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see gestion de restaurantes --> {}'.format(resStep))
        assert resStep

    @then('I see menu lateral de restaurantes')
    def see_menu_lateral_restaurantes(self):
        pagina_gestRes = self.driver
        logger.debug('INICIO STEP: I see menu lateral de restaurantes')
        resStep = True
        try:
            ElemValidar = gestResElements.latPagGestTerXPath
            ElemValidarTXT = gestResElements.latPagGestTerTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestZonXPath
            ElemValidarTXT = gestResElements.latPagGestZonTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestCarXPath
            ElemValidarTXT = gestResElements.latPagGestCarTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestSubXPath
            ElemValidarTXT = gestResElements.latPagGestSubTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestProXPath
            ElemValidarTXT = gestResElements.latPagGestProTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestGruXPath
            ElemValidarTXT = gestResElements.latPagGestGruTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestComXPath
            ElemValidarTXT = gestResElements.latPagGestComTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestObsXPath
            ElemValidarTXT = gestResElements.latPagGestObsTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestAccXPath
            ElemValidarTXT = gestResElements.latPagGestAccTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestTarXPath
            ElemValidarTXT = gestResElements.latPagGestTarTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestModXPath
            ElemValidarTXT = gestResElements.latPagGestModTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestResXPath
            ElemValidarTXT = gestResElements.latPagGestResTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestAleXPath
            ElemValidarTXT = gestResElements.latPagGestAleTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestAl2XPath
            ElemValidarTXT = gestResElements.latPagGestAl2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestCarXPath
            ElemValidarTXT = gestResElements.latPagGestCarTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestProXPath
            ElemValidarTXT = gestResElements.latPagGestProTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestPr2XPath
            ElemValidarTXT = gestResElements.latPagGestPr2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestInvXPath
            ElemValidarTXT = gestResElements.latPagGestInvTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestFesXPath
            ElemValidarTXT = gestResElements.latPagGestFesTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestImpXPath
            ElemValidarTXT = gestResElements.latPagGestImpTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestRsmXPath
            ElemValidarTXT = gestResElements.latPagGestRsmTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestTpvXPath
            ElemValidarTXT = gestResElements.latPagGestTpvTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestTicXPath
            ElemValidarTXT = gestResElements.latPagGestTicTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestAvaXPath
            ElemValidarTXT = gestResElements.latPagGestAvaTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestAjuXPath
            ElemValidarTXT = gestResElements.latPagGestAjuTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.latPagGestCamXPath
            ElemValidarTXT = gestResElements.latPagGestCamTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
        except Exception as e:
            logger.error('Algún elemento en "menu lateral de restaurantes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see menu lateral de restaurantes --> {}'.format(resStep))
        assert resStep


    @then('I manage restaurantes')
    def manage_restaurantes(self):
        pagina_gestRes = self.driver
        logger.debug('INICIO STEP: I manage restaurantes')
        resStep = True
        try:
            ElemValidar = homeUserElements.menuGlobXPath # GLOBAL
            ElemValidarTXT = homeUserElements.menuGlobTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            pagina_gestRes.find_element(by=By.XPATH, value='//*[@id="restaurant_list"]/div[9]/h4').is_displayed()

            # selecciono restaurante
            ElemValidar = gestResElements.latPagGestRSeXPath
            ElemValidarTXT = gestResElements.latPagGestRSeTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()

            # con restaurante seleccionado página central
            ElemValidar = gestResElements.titPagGestResXPath # LISTADO DE TERMINALES
            ElemValidarTXT = gestResElements.titPagGestResTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)

            # con restaurante seleccionado, página principal
            ElemValidar = gestResElements.pgpPagGestTIcXPath
            ElemValidarTXT = gestResElements.pgpPagGestTIcTXT
            #resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            logger.debug('no localizo icono')

            # validación campos de terminales 1,2
            ElemValidar = gestResElements.pgpPagGestTS1XPath
            ElemValidarTXT = gestResElements.pgpPagGestTS1TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTP1XPath
            ElemValidarTXT = gestResElements.pgpPagGestTP1TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTC1XPath
            ElemValidarTXT = gestResElements.pgpPagGestTC1TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTc1XPath
            ElemValidarTXT = gestResElements.pgpPagGestTc1TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTD1XPath
            ElemValidarTXT = gestResElements.pgpPagGestTD1TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTS2XPath
            ElemValidarTXT = gestResElements.pgpPagGestTS2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTP2XPath
            ElemValidarTXT = gestResElements.pgpPagGestTP2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTC2XPath
            ElemValidarTXT = gestResElements.pgpPagGestTC2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTc2XPath
            ElemValidarTXT = gestResElements.pgpPagGestTc2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestTD2XPath
            ElemValidarTXT = gestResElements.pgpPagGestTD2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)

            ### operaciones entre terminales 1,2
            # Cambio de terminal principal de 1 a 2
            ElemValidar = gestResElements.pgpPagGestTP2XPath
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()

            # Valido que deshabilitar terminal 2, al hacer click NO cambia de valor
            ElemValidar = gestResElements.pgpPagGestTD2class
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()
            valorstatus2 = pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar)
            status_T2 = valorstatus2.get_attribute("class")
            if 'fa fa-square-o' in status_T2:
                logger.debug('OK. El terminal 2 no se puede deshabilitar')
                resStep = True & resStep
            else:
                logger.debug('ERROR. El terminal principal se puede desactivar.')
                resStep = False & resStep
            logger.debug(resStep)
            # Valido que deshabilitar terminal 1, al hacer click cambia de valor
            ElemValidar = gestResElements.pgpPagGestTD1class
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()
            valorstatus1 = pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar)
            status_T1 = valorstatus1.get_attribute("class")
            if 'fa fa-check-square-o' in status_T1:
                logger.debug('OK. El terminal 1 se puede deshabilitar')
                resStep = True & resStep
            else:
                logger.debug('ERROR. El terminal no principal NO se puede desactivar.')
                resStep = False & resStep
            logger.debug(resStep)

            # elementos terminales moviles
            ElemValidar = gestResElements.pgpPagGestRTMIXPath
            ElemValidarTXT = gestResElements.pgpPagGestRTMITXT
            #resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            # no consigo validar el icono

            ElemValidar = gestResElements.pgpPagGestRTMXPath
            ElemValidarTXT = gestResElements.pgpPagGestRTMTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGestRTMC1XPath
            ElemValidarTXT = gestResElements.pgpPagGestRTMC1TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGesRTMD1Xpath
            ElemValidarTXT = gestResElements.pgpPagGesRTMD1TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGesRTMC2Xpath
            ElemValidarTXT = gestResElements.pgpPagGesRTMC2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            ElemValidar = gestResElements.pgpPagGesRTMD2Xpath
            ElemValidarTXT = gestResElements.pgpPagGesRTMD2TXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)

            ### operaciones en terminales moviles 1,2
            # Habilito terminal 2 y activo terminal del cobro 2
            ElemValidar = gestResElements.pgpPagGesRTMD2Xpath
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()
            ElemValidar = gestResElements.pgpPagGesRTMC2Xpath
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()
            #valido que el estado del terminal de cobro 2 ha cambiado
            ElemValidar = gestResElements.pgpPagGesRTMC2_class
            valorstatusTM2 = pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar)
            status_TM2 = valorstatusTM2.get_attribute("class")
            if 'fa fa-square-o' in status_TM2:
                logger.debug('OK. El terminal de cobro de movil 2 esta activado')
                resStep = True & resStep
            else:
                logger.debug('ERROR. El terminal de cobro de movil 2 NO esta activado')
                resStep = False & resStep

            # elementos Terminales Kitchen Display
            ElemValidar = gestResElements.pgpPagGestRTKXPath
            ElemValidarTXT = gestResElements.pgpPagGestRTKTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)

            # guardar cambios
            ElemValidar = gestResElements.guaPagGestResXPath
            ElemValidarTXT = gestResElements.guaPagGestResTXT
            resStep = obtenerTextos(resStep, pagina_gestRes, ElemValidar, ElemValidarTXT)
            # pagina_gestRes.find_element(by=By.ID, value='saveChanges').click()
            # no guardo porque se descolocan todos los terminales y para las comprobaciones no es necesario
            time.sleep(1)

        except Exception as e:
            logger.error('Algún elemento en "manage restaurantes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I manage restaurantes --> {}'.format(resStep))
        assert resStep
