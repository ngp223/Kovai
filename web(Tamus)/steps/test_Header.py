import time
import unittest
import logging
import logging.config
import logging.handlers
from behave import step, then
from selenium.webdriver.common.by import By
from pageobjects import Headers


logger = logging.getLogger('WebLogs')
headersElements = Headers.Headers()


class publicHeader(unittest.TestCase):

    @step('I click header usuarios')
    def click_header_usuarios(self):
        logger.debug('INICIO STEP: I click header usuarios')
        header = self.driver
        ElemValidar = headersElements.headUsuXPath
        try:
            header.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click header usuarios" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click header usuarios" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click header usuarios --> {}'.format(resStep))
        assert resStep

    @step('I click header servicios')
    def click_header_servicios(self):
        logger.debug('INICIO STEP: I click header servicios')
        header = self.driver
        ElemValidar = headersElements.headSerXPath
        try:
            header.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click header servicios" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click header servicios no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click header servicios --> {}'.format(resStep))
        assert resStep

    @then('I see header usuarios')
    def see_header_usuarios(self):
        header = self.driver
        logger.debug('INICIO STEP: I see header usuarios')
        try:
            header.find_element(by=By.PARTIAL_LINK_TEXT, value="RESTAURANTES")
            header.find_element(by=By.LINK_TEXT, value="CAFETERÍAS")
            header.find_element(by=By.LINK_TEXT, value="BARES-PUBS")
            header.find_element(by=By.LINK_TEXT, value="HOTELES")
            header.find_element(by=By.LINK_TEXT, value="EVENTOS")
            logger.debug('Elementos encontrados')
            resStep = True
        except Exception as e:
            logger.error('Elemento no encontrado')
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see header usuarios --> {}'.format(resStep))
        assert resStep

    @then('I see header servicios')
    def see_header_servicios(self):
        header = self.driver
        logger.debug('INICIO STEP: I see header servicios')
        try:
            header.find_element(by=By.XPATH,
                                value="/html/body/div[1]/div[1]/header/div/div/div/div/div[2]/div/div/nav/div[3]/div/div/div/a/div/span[2]").click()
            txt_servicios = header.find_element(by=By.XPATH,
                                                value="/html/body/div[1]/div[1]/header/div/div/div/div/div[2]/div/div/nav/div[3]/div/div/div/div/div/div/div/div[1]/div/p").text
            logger.debug(
                'El software TAMUS te ofrece una variedad de servicios que te facilitarán el trabajo día a día.' + txt_servicios + ' > ' + str(
                    txt_servicios == 'El software TAMUS te ofrece una variedad de servicios que te facilitarán el trabajo día a día.'))
            header.find_element(by=By.LINK_TEXT, value="EQUIPOS TPV")
            header.find_element(by=By.LINK_TEXT, value="PAGO QR")
            header.find_element(by=By.LINK_TEXT, value="DESDE LA NUBE")
            header.find_element(by=By.LINK_TEXT, value="INTEGRACIONES")
            header.find_element(by=By.LINK_TEXT, value="TAKE AWAY")
            logger.debug('Elementos encontrados')
            resStep = True
        except Exception as e:
            logger.error('Elemento no encontrado')
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see rest of the items --> {}'.format(resStep))
        assert resStep

    @then('I see rest of the items')
    def see_header_rest_of_items(self):
        header = self.driver
        logger.debug('INICIO STEP: I see rest of the items')
        try:
            header.find_element(by=By.LINK_TEXT, value="TARIFAS")
            header.find_element(by=By.LINK_TEXT, value="CLIENTES")
            header.find_element(by=By.LINK_TEXT, value="CÓMO FUNCIONA")
            header.find_element(by=By.LINK_TEXT, value="NOSOTROS")
            header.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/header/div/div/div/div/div[2]/div/div/nav/div[8]/div/div/div/a")
            logger.debug('Elementos encontrados')
            resStep = True
        except Exception as e:
            logger.error('Elemento no encontrado')
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see rest of the items --> {}'.format(resStep))
        assert resStep

