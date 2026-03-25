import time
import unittest
import logging.handlers
from behave import when
from selenium.webdriver.common.by import By
from pageobjects import HomeUser

logger = logging.getLogger('WebLogs')
homeUserElements = HomeUser.HomeUser()


class Header_user(unittest.TestCase):
    @when('I click to gestion restaurantes')
    def click_user_gestion_restaurantes(self):
        pagina_gestRes = self.driver
        logger.debug('INICIO STEP: I click to gestion restaurantes')
        ElemValidar = homeUserElements.gestResXPath
        try:
            pagina_gestRes.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click to gestion restaurantes" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to gestion de restaurantes" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to gestion de restaurantes --> {}'.format(resStep))
        assert resStep

    @when('I click to gestion almacen')
    def click_user_gestion_almacen(self):
        pagina_gestAlm = self.driver
        logger.debug('INICIO STEP: I click to gestion almacen')
        ElemValidar = homeUserElements.gestAlmXPath
        try:
            pagina_gestAlm.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click to gestion almacen" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to gestion almacen" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to gestion almacen --> {}'.format(resStep))
        assert resStep

    @when('I click to gestion ventas')
    def click_user_gestion_ventas(self):
        pagina_gestVen = self.driver
        logger.debug('INICIO STEP: I click to gestion ventas')
        ElemValidar = homeUserElements.gestVenXPath
        try:
            pagina_gestVen.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click to gestion ventas" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to gestion ventas no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to gestion ventas --> {}'.format(resStep))
        assert resStep

    @when('I click to gestion facturacion')
    def click_user_gestion_facturacion(self):
        pagina_gestFac = self.driver
        logger.debug('INICIO STEP: I click to gestion facturacion')
        ElemValidar = homeUserElements.gestFacXPath
        try:
            pagina_gestFac.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click to gestion facturacion" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to gestion facturacion" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to gestion facturacion --> {}'.format(resStep))
        assert resStep

    @when('I click to gestion usuarios')
    def click_user_gestion_usuarios(self):
        pagina_gestUsu = self.driver
        logger.debug('INICIO STEP: I click to gestion usuarios')
        ElemValidar = homeUserElements.gestUsuXPath
        try:
            pagina_gestUsu.find_element(by=By.XPATH, value=ElemValidar).click()
            logger.debug('Elemento "I click to gestion usuarios" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to gestion usuarios no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to gestion usuarios --> {}'.format(resStep))
        assert resStep
