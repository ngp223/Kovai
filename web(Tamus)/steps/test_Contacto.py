import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import Contacto

logger = logging.getLogger('WebLogs')
contactoElements = Contacto.Contacto()


class Contacto(unittest.TestCase):

    @when('I click to contacto')
    def click_contacto(self):
        pagina_Contacto = self.driver
        logger.debug('INICIO STEP: I click to contacto')
        ElemValidar = contactoElements.opConXPath
        try:
            pagina_Contacto.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click to contacto" encontrado')
            time.sleep(3)
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to contacto" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to contacto --> {}'.format(resStep))
        assert resStep

    @then('I see page contacto')
    def see_contacto(self):
        pagina_Contacto = self.driver
        logger.debug('INICIO STEP: I see page contacto')
        try:
            pagina_Contacto.switch_to.window(pagina_Contacto.window_handles[1])
            ElemValidar = contactoElements.primeraLineaConXPath
            title = pagina_Contacto.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = contactoElements.primeraLineaConTXT
            logger.debug(ElemValidar + title + ' --> ' + ElemValidar)
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de contacto --> {}".format(resStep))
            ElemValidar = contactoElements.nombrepesCon
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_Contacto.title + ' --> ' + str(
                ElemValidar == pagina_Contacto.title))
            resStep = (ElemValidar == pagina_Contacto.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(contactoElements.url + ' lo comparo con: ' + pagina_Contacto.current_url + ' --> ' + str(
                contactoElements.url == pagina_Contacto.current_url))
            resStep = (contactoElements.url == pagina_Contacto.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page contacto" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page contacto --> {}'.format(resStep))
        assert resStep
