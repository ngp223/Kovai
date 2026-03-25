import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import EquiposTPV

logger = logging.getLogger('WebLogs')
equiposTPVElements = EquiposTPV.EquiposTPV()


class EquiposTPV(unittest.TestCase):

    @when('I click to equipos tpv')
    def click_equipos_tpv(self):
        pagina_EquiposTPV = self.driver
        logger.debug('INICIO STEP: I click to equipos tpv')
        ElemValidar = equiposTPVElements.opTPVLink
        try:
            pagina_EquiposTPV.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.debug('Elemento "I click to equipos tpv" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to equipos tpv" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to equipos tpv--> {}'.format(resStep))
        assert resStep

    @then('I see page equipos tpv')
    def see_equipos_TPV(self):
        pagina_EquiposTPV = self.driver
        logger.debug('INICIO STEP: I see page equipos tpv')
        try:
            ElemValidar = equiposTPVElements.primeraLineaTPVXPath
            title = pagina_EquiposTPV.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = equiposTPVElements.primeraLineaTPVTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de equipos tpv --> {}".format(resStep))
            ElemValidar = equiposTPVElements.nombrepesTPV
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_EquiposTPV.title + ' --> ' + str(
                ElemValidar == pagina_EquiposTPV.title))
            resStep = (ElemValidar == pagina_EquiposTPV.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(equiposTPVElements.url + ' lo comparo con: ' + pagina_EquiposTPV.current_url + ' --> ' + str(
                equiposTPVElements.url == pagina_EquiposTPV.current_url))
            resStep = (equiposTPVElements.url == pagina_EquiposTPV.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
        except Exception as e:
            logger.error('Algún elemento en "I see page equipos tpv" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page equipos tpv --> {}'.format(resStep))
        assert resStep
