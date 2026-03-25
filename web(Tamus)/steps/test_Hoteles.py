import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Hoteles

logger = logging.getLogger('WebLogs')
hotelesElements = Hoteles.Hoteles()


class Hoteles(unittest.TestCase):

    @when('I click to hoteles')
    def click_hoteles(self):
        pagina_Hoteles = self.driver
        logger.debug('INICIO STEP: I click to hoteles')
        try:
            ElemValidar = hotelesElements.opHotLink
            pagina_Hoteles.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Hoteles" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Hoteles" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Hoteles--> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to hoteles')
        assert resStep

    @then('I see page hoteles')
    def see_hoteles(self):
        pagina_Hoteles = self.driver
        logger.debug('INICIO STEP: I see page hoteles')
        try:
            ElemValidar = hotelesElements.primeraLineaHotXPath
            title = pagina_Hoteles.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = hotelesElements.primeraLineaHotTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de hoteles --> {}".format(resStep))
            ElemValidar = hotelesElements.nombrepesHot
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Hoteles.title + ' --> ' + str(
                ElemValidar == pagina_Hoteles.title))
            resStep = (ElemValidar == pagina_Hoteles.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(hotelesElements.url + ' lo comparo con: ' + pagina_Hoteles.current_url + ' --> ' + str(
                hotelesElements.url == pagina_Hoteles.current_url))
            resStep = (hotelesElements.url == pagina_Hoteles.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page hoteles" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page hoteles --> {}'.format(resStep))
        assert resStep
