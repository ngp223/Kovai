import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Bares

logger = logging.getLogger('WebLogs')
baresElements = Bares.Bares()


class Bares(unittest.TestCase):

    @when('I click to bares')
    def click_bares(self):
        pagina_Bares = self.driver
        logger.debug('INICIO STEP: I click to bares')
        try:
            ElemValidar = baresElements.opBarLink
            pagina_Bares.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Bares" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Bares" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Bares --> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to bares')
        assert resStep

    @then('I see page bares')
    def see_bares(self):
        pagina_Bares = self.driver
        logger.debug('INICIO STEP: I see page bares')
        try:
            ElemValidar = baresElements.primeraLineaBarXPath
            title = pagina_Bares.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = baresElements.primeraLineaBarTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de bares --> {}".format(resStep))
            ElemValidar = baresElements.nombrepesBar
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Bares.title + ' > ' + str(
                ElemValidar == pagina_Bares.title))
            resStep = (ElemValidar == pagina_Bares.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(baresElements.url + ' lo comparo con: ' + pagina_Bares.current_url + ' > ' + str(
                baresElements.url == pagina_Bares.current_url))
            resStep = True
        except Exception as e:
            logger.error('Algún elemento en "I see page bares" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page bares --> {}'.format(resStep))
        assert resStep
