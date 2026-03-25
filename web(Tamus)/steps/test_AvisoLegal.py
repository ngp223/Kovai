import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import AvisoLegal

logger = logging.getLogger('WebLogs')
avisoLegalElements = AvisoLegal.AvisoLegal()


class AvisoLegal(unittest.TestCase):

    @when('I click to aviso legal')
    def click_aviso_legal(self):
        pagina_avisoLegal = self.driver
        logger.debug('INICIO STEP: I click to aviso legal')
        pagina_avisoLegal.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            ElemValidar = avisoLegalElements.opALeLink
            pagina_avisoLegal.find_element(by=By.LINK_TEXT, value=ElemValidar).is_displayed()
            pagina_avisoLegal.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            time.sleep(2)
            logger.warning('Elemento "I click to AvisoLegal" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to AvisoLegal" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to AvisoLegal --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to aviso legal')
        assert resStep

    @then('I see page aviso legal')
    def see_aviso_legal(self):
        pagina_avisoLegal = self.driver
        logger.debug('INICIO STEP: I see page aviso legal')
        pagina_avisoLegal.switch_to.window(pagina_avisoLegal.window_handles[1])
        time.sleep(3)
        try:
            ElemValidar = avisoLegalElements.primeraLineaALeXPath
            title = pagina_avisoLegal.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = avisoLegalElements.primeraLineaALeTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de aviso legal --> {}".format(resStep))
            ElemValidar = avisoLegalElements.nombrepesALe
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_avisoLegal.title + ' --> '
                         + str(ElemValidar == pagina_avisoLegal.title))
            resStep = (ElemValidar == pagina_avisoLegal.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(avisoLegalElements.url + ' lo comparo con: ' + pagina_avisoLegal.current_url + ' --> '
                         + str(avisoLegalElements.url == pagina_avisoLegal.current_url))
            resStep = (avisoLegalElements.url == pagina_avisoLegal.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento en "I see page aviso legal" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page aviso legal --> {}'.format(resStep))
        assert resStep
