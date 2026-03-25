import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Cafeterias

logger = logging.getLogger('WebLogs')
cafeteriasElements = Cafeterias.Cafeterias()


class Cafeterías(unittest.TestCase):

    @when('I click to cafeterias')
    def click_cafeterias(self):
        pagina_Cafeterias = self.driver
        logger.debug('INICIO STEP: I click to cafeterias')
        ElemValidar = cafeteriasElements.opCafLink
        try:
            pagina_Cafeterias.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Cafeterías" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Cafeterías" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Cafeterías --> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to cafeterias')
        assert resStep

    @then('I see page cafeterias')
    def see_cafeterias(self):
        pagina_Cafeterias = self.driver
        logger.debug('INICIO STEP: I see page cafeterias')
        try:
            ElemValidar = cafeteriasElements.primeraLineaCafXPath
            title = pagina_Cafeterias.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = cafeteriasElements.primeraLineaCafTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de cafeterias --> {}".format(resStep))
            ElemValidar = cafeteriasElements.nombrepesCaf
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Cafeterias.title + ' > ' + str(
                ElemValidar == pagina_Cafeterias.title))
            resStep = (ElemValidar == pagina_Cafeterias.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(cafeteriasElements.url + ' lo comparo con: ' + pagina_Cafeterias.current_url + ' > ' + str(
                cafeteriasElements.url == pagina_Cafeterias.current_url))
            resStep = (cafeteriasElements.url == pagina_Cafeterias.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page cafeterias" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page cafeterias --> {}'.format(resStep))
        assert resStep