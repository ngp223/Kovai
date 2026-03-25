import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import DesdeLaNube

logger = logging.getLogger('WebLogs')
desdeLaNubeElements = DesdeLaNube.DesdeLaNube()


class DesdeLaNube(unittest.TestCase):

    @when('I click to desde la nube')
    def click_desde_la_nube(self):
        pagina_DesdeLaNube = self.driver
        logger.debug('INICIO STEP: I click to desde la nube')
        ElemValidar = desdeLaNubeElements.opDLNLink
        try:
            pagina_DesdeLaNube.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.debug('Elemento "I click to desde la nube" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to desde la nube" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to desde la nube --> {}'.format(resStep))
        assert resStep

    @then('I see page desde la nube')
    def see_desde_la_nube(self):
        pagina_DesdeLaNube = self.driver
        logger.debug('INICIO STEP: I see page desde la nube')
        try:
            ElemValidar = desdeLaNubeElements.primeraLineaDLNXPath
            title = pagina_DesdeLaNube.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = desdeLaNubeElements.primeraLineaDLNTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de desde la nube --> {}".format(resStep))
            ElemValidar = desdeLaNubeElements.nombrepesDLN
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_DesdeLaNube.title + ' --> ' + str(
                ElemValidar == pagina_DesdeLaNube.title))
            resStep = (ElemValidar == pagina_DesdeLaNube.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(desdeLaNubeElements.url + ' lo comparo con: ' + pagina_DesdeLaNube.current_url + ' --> ' + str(
                desdeLaNubeElements.url == pagina_DesdeLaNube.current_url))
            resStep = (desdeLaNubeElements.url == pagina_DesdeLaNube.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page desde la nube" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page desde la nube --> {}'.format(resStep))
        assert resStep

