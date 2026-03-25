import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Nosotros

logger = logging.getLogger('WebLogs')
nosotrosElements = Nosotros.Nosotros()


class Nosotros(unittest.TestCase):

    @when('I click to nosotros')
    def click_nosotros(self):
        pagina_Nosotros = self.driver
        logger.debug('INICIO STEP: I click to nosotros')
        try:
            ElemValidar = nosotrosElements.opNosLink
            pagina_Nosotros.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Nosotros" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Nosotros" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Nosotros--> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to nosotros')
        assert resStep

    @then('I see page nosotros')
    def see_nosotros(self):
        pagina_Nosotros = self.driver
        logger.debug('INICIO STEP: I see page nosotros')
        resStep = True
        try:
            ElemValidar = nosotrosElements.primeraLineaNosXPath
            title = pagina_Nosotros.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = nosotrosElements.primeraLineaNosTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de nosotros --> {}".format(resStep))
            ElemValidar = nosotrosElements.nombrepesNos
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Nosotros.title + ' --> ' + str(
                ElemValidar == pagina_Nosotros.title))
            resStep = (ElemValidar == pagina_Nosotros.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(nosotrosElements.url+ ' lo comparo con: ' + pagina_Nosotros.current_url + ' --> ' + str(
                nosotrosElements.url== pagina_Nosotros.current_url))
            resStep = (nosotrosElements.url== pagina_Nosotros.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algun elemento en "I see page nosotros" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page nosotros --> {}'.format(resStep))
        assert resStep

