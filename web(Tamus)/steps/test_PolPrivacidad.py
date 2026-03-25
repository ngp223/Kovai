import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import PolPrivacidad

logger = logging.getLogger('WebLogs')
politicaPrivacidadElements = PolPrivacidad.PolPrivacidad()


class PoliticaPrivacidad(unittest.TestCase):

    @when('I click to politica privacidad')
    def click_politica_privacidad(self):
        pagina_politicaPrivacidad = self.driver
        logger.debug('INICIO STEP: I click to politica privacidad')
        pagina_politicaPrivacidad.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            ElemValidar = politicaPrivacidadElements.opPPrLink
            pagina_politicaPrivacidad.find_element(by=By.LINK_TEXT, value=ElemValidar).is_displayed()
            pagina_politicaPrivacidad.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Politica Privacidad" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Politica Privacidad" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Politica Privacidad --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then('I see page politica privacidad')
    def see_politica_privacidad(self):
        pagina_politicaPrivacidad = self.driver
        logger.debug('INICIO STEP: I see page politica privacidad')
        pagina_politicaPrivacidad.switch_to.window(pagina_politicaPrivacidad.window_handles[1])
        time.sleep(3)
        try:
            ElemValidar = politicaPrivacidadElements.primeraLineaPPrXPath
            title = pagina_politicaPrivacidad.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = politicaPrivacidadElements.primeraLineaPPrTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de politica privacidad --> {}".format(resStep))
            ElemValidar = politicaPrivacidadElements.nombrepesPPr
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_politicaPrivacidad.title + ' --> ' + str(
                ElemValidar == pagina_politicaPrivacidad.title))
            resStep = (ElemValidar == pagina_politicaPrivacidad.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(politicaPrivacidadElements.url + ' lo comparo con: ' + pagina_politicaPrivacidad.current_url + ' --> ' + str(
                politicaPrivacidadElements.url == pagina_politicaPrivacidad.current_url))
            resStep = (politicaPrivacidadElements.url == pagina_politicaPrivacidad.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see page politica privacidad" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page politica privacidad --> {}'.format(resStep))
        assert resStep
