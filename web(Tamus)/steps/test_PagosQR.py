import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import PagosQR

logger = logging.getLogger('WebLogs')
pagosQRElements = PagosQR.PagosQR()


class PagosQR(unittest.TestCase):

    @when('I click to pagos qr')
    def click_pagosQR(self):
        pagina_PagosQR = self.driver
        logger.debug('INICIO STEP: I click to pagosQR')
        try:
            ElemValidar = pagosQRElements.opPQRLink
            pagina_PagosQR.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to PagosQR" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to PagosQR" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to PagosQR--> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('INICIO STEP: I click to pagosQR')
        assert resStep

    @then('I see page pagos qr')
    def see_pagosQR(self):
        pagina_PagosQR = self.driver
        logger.debug('INICIO STEP: I see page pagos qr')
        try:
            ElemValidar = pagosQRElements.primeraLineaPQRXPath
            title = pagina_PagosQR.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = pagosQRElements.primeraLineaPQRTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de pagos qr --> {}".format(resStep))
            ElemValidar = pagosQRElements.nombrepesPQR
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_PagosQR.title + ' --> ' + str(
                ElemValidar == pagina_PagosQR.title))
            resStep = (ElemValidar == pagina_PagosQR.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(pagosQRElements.url + ' lo comparo con: ' + pagina_PagosQR.current_url + ' --> ' + str(
                pagosQRElements.url == pagina_PagosQR.current_url))
            resStep = (pagosQRElements.url == pagina_PagosQR.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page pagos qr" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page pagos qr --> {}'.format(resStep))
        assert resStep
