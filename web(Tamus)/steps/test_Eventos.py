import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Eventos

logger = logging.getLogger('WebLogs')
eventosElements = Eventos.Eventos()


class Eventos(unittest.TestCase):

    @when('I click to eventos')
    def click_eventos(self):
        pagina_Eventos = self.driver
        logger.debug('INICIO STEP: I click to eventos')
        ElemValidar = eventosElements.opEveLink
        try:
            pagina_Eventos.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.debug('Elemento "I click to eventos" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to eventos" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to eventos--> {}'.format(resStep))
        assert resStep

    @then('I see page eventos')
    def see_eventos(self):
        pagina_Eventos = self.driver
        logger.debug('INICIO STEP: I see page eventos')
        try:
            ElemValidar = eventosElements.primeraLineaEveXPath
            title = pagina_Eventos.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = eventosElements.primeraLineaEveTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de Eventos --> {}".format(resStep))
            ElemValidar = eventosElements.nombrepesEve
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Eventos.title + ' --> ' + str(
                ElemValidar == pagina_Eventos.title))
            resStep = (ElemValidar == pagina_Eventos.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(eventosElements.url + ' lo comparo con: ' + pagina_Eventos.current_url + ' --> ' + str(
                eventosElements.url == pagina_Eventos.current_url))
            resStep = (eventosElements.url == pagina_Eventos.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page eventos" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page eventos --> {}'.format(resStep))
        assert resStep
