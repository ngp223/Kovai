import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Restaurantes

logger = logging.getLogger('WebLogs')
restaurantesElements = Restaurantes.Restaurantes()


class Restaurantes(unittest.TestCase):

    @when('I click to restaurantes')
    def click_restaurantes(self):
        pagina_Restaurantes = self.driver
        logger.debug('INICIO STEP: I click to restaurantes')
        try:
            ElemValidar = restaurantesElements.opResLink
            pagina_Restaurantes.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Restaurantes" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Restaurantes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Restaurantes--> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to restaurantes')
        assert resStep

    @then('I see page restaurantes')
    def page_restaurantes(self):
        pagina_Restaurantes = self.driver
        logger.debug('INICIO STEP: I see page restaurantes')
        try:
            ElemValidar = restaurantesElements.primeraLineaResXPath
            title = pagina_Restaurantes.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = restaurantesElements.primeraLineaResTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de restaurantes --> {}".format(resStep))
            ElemValidar = restaurantesElements.nombrepesRes
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Restaurantes.title + ' --> ' + str(ElemValidar == pagina_Restaurantes.title))
            resStep = (ElemValidar == pagina_Restaurantes.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(restaurantesElements.url + ' lo comparo con: ' + pagina_Restaurantes.current_url + ' --> '
                         + str(restaurantesElements.url == pagina_Restaurantes.current_url))
            resStep = (restaurantesElements.url == pagina_Restaurantes.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page restaurantes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page restaurantes --> {}'.format(resStep))
        assert resStep