import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Tarifas

logger = logging.getLogger('WebLogs')
tarifasElements = Tarifas.Tarifas()


class Tarifas(unittest.TestCase):

    @when('I click to tarifas')
    def click_tarifas(self):
        pagina_Tarifas = self.driver
        logger.debug('INICIO STEP: I click to tarifas')
        try:
            ElemValidar = tarifasElements.opTarLink
            pagina_Tarifas.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to tarifas" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to tarifas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to tarifas')
        assert resStep

    @then('I see page tarifas')
    def Page_Tarifas(self):
        pagina_Tarifas = self.driver
        logger.debug('INICIO STEP: I see page tarifas')
        try:
            ElemValidar = tarifasElements.primeraLineaTarXPath
            title = pagina_Tarifas.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = tarifasElements.primeraLineaTarTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de tarifas --> {}".format(resStep))
            ElemValidar = tarifasElements.nombrepesTar
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Tarifas.title + ' --> ' + str(
                ElemValidar == pagina_Tarifas.title))
            resStep = (ElemValidar == pagina_Tarifas.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(tarifasElements.url + ' lo comparo con: ' + pagina_Tarifas.current_url + ' --> ' + str(
                tarifasElements.url == pagina_Tarifas.current_url))
            resStep = (tarifasElements.url == pagina_Tarifas.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page tarifas" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page tarifas--> {}'.format(resStep))
        assert resStep
