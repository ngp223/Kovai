import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import ComoFunciona

logger = logging.getLogger('WebLogs')
ComoFuncionaElements = ComoFunciona.ComoFunciona()


class ComoFunciona(unittest.TestCase):

    @when('I click to como funciona')
    def click_como_funciona(self):
        pagina_ComoFunciona = self.driver
        logger.debug('INICIO STEP: I click to como funciona')
        ElemValidar = ComoFuncionaElements.opCFuLink
        try:
            pagina_ComoFunciona.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.debug('Elemento "I click to como funciona" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to como funciona" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to como funciona --> {}'.format(resStep))
        assert resStep

    @then('I see page como funciona')
    def see_como_funciona(self):
        pagina_ComoFunciona = self.driver
        logger.debug('INICIO STEP: I see page como funciona')
        try:
            ElemValidar = ComoFuncionaElements.primeraLineaCFuXPath
            title = pagina_ComoFunciona.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = ComoFuncionaElements.primeraLineaCFuTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de como funciona --> {}".format(resStep))
            ElemValidar = ComoFuncionaElements.nombrepesCFu
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_ComoFunciona.title + ' --> ' + str(
                ElemValidar == pagina_ComoFunciona.title))
            resStep = (ElemValidar == pagina_ComoFunciona.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(ComoFuncionaElements.url + ' lo comparo con: ' + pagina_ComoFunciona.current_url + ' --> ' + str(
                ComoFuncionaElements.url == pagina_ComoFunciona.current_url))
            resStep = (ComoFuncionaElements.url == pagina_ComoFunciona.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page como funciona" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page como funciona --> {}'.format(resStep))
        assert resStep


