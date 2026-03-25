import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Clientes

logger = logging.getLogger('WebLogs')
clientesElements = Clientes.Clientes()


class Clientes(unittest.TestCase):

    @when('I click to clientes')
    def click_clientes(self):
        pagina_Clientes = self.driver
        logger.debug('INICIO STEP: I click to clientes')
        ElemValidar = clientesElements.opCliLink
        try:
            pagina_Clientes.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.debug('Elemento "I click to clientes" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to clientes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to clientes --> {}'.format(resStep))
        assert resStep

    @then('I see page clientes')
    def see_clientes(self):
        pagina_Clientes = self.driver
        logger.debug('INICIO STEP: I see page clientes')
        try:
            ElemValidar = clientesElements.primeraLineaCliXPath
            title = pagina_Clientes.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = clientesElements.primeraLineaCliTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de clientes --> {}".format(resStep))
            ElemValidar = clientesElements.nombrepesCli
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Clientes.title + ' > ' + str(
                ElemValidar == pagina_Clientes.title))
            resStep = (ElemValidar == pagina_Clientes.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(clientesElements.url + ' lo comparo con: ' + pagina_Clientes.current_url + ' > ' + str(
                clientesElements.url == pagina_Clientes.current_url))
            resStep = (clientesElements.url == pagina_Clientes.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page clientes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page clientes --> {}'.format(resStep))
        assert resStep

