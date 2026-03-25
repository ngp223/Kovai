import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Integraciones

logger = logging.getLogger('WebLogs')
integracionesElements = Integraciones.Integraciones()


class Integraciones(unittest.TestCase):

    @when('I click to integraciones')
    def click_integraciones(self):
        pagina_Integraciones = self.driver
        logger.debug('INICIO STEP: I click to integraciones')
        ElemValidar = integracionesElements.opIntLink
        try:
            pagina_Integraciones.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Integraciones" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Integraciones" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Integraciones--> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to integraciones')
        assert resStep

    @then('I see page integraciones')
    def see_integraciones(self):
        pagina_Integraciones = self.driver
        logger.debug('INICIO STEP: I see page integraciones')
        resStep = True
        try:
            ElemValidar = integracionesElements.primeraLineaIntXPath
            title = pagina_Integraciones.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = integracionesElements.primeraLineaIntTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de integraciones --> {}".format(resStep))
            ElemValidar = integracionesElements.nombrepesInt
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Integraciones.title + ' --> ' + str(
                ElemValidar == pagina_Integraciones.title))
            resStep = (ElemValidar == pagina_Integraciones.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(integracionesElements.url + ' lo comparo con: ' + pagina_Integraciones.current_url + ' --> ' + str(
                integracionesElements.url == pagina_Integraciones.current_url))
            resStep = (integracionesElements.url == pagina_Integraciones.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page integraciones" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page integraciones --> {}'.format(resStep))
        assert resStep

