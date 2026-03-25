import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import TakeAway

logger = logging.getLogger('WebLogs')
takeAwayElements = TakeAway.TakeAway()


class takeAway(unittest.TestCase):

    @when('I click to take away')
    def click_takeAway(self):
        pagina_takeAway = self.driver
        logger.debug('INICIO STEP: I click to take away')
        try:
            ElemValidar = takeAwayElements.opTALink
            pagina_takeAway.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to take away" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to take away" no encontrado: {}'.format(ElemValidar, e))
            resStep = False

        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to takeAway --> {}'.format(resStep))
        assert resStep

    @then('I see page take away')
    def Page_takeAway(self):
        pagina_takeAway = self.driver
        logger.debug('INICIO STEP: I see page take away')
        try:
            ElemValidar = takeAwayElements.primeraLineaTAXPath
            title = pagina_takeAway.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = takeAwayElements.primeraLineaTATXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de take away --> {}".format(resStep))
            ElemValidar = takeAwayElements.nombrepesTA
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_takeAway.title + ' > ' + str(
                ElemValidar == pagina_takeAway.title))
            resStep = (ElemValidar == pagina_takeAway.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(takeAwayElements.url + ' lo comparo con: ' + pagina_takeAway.current_url + ' > ' + str(
                takeAwayElements.url == pagina_takeAway.current_url))
            resStep = (takeAwayElements.url == pagina_takeAway.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page take away" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page take away--> {}'.format(resStep))
        assert resStep


