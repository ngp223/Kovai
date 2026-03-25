import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By

logger = logging.getLogger('WebLogs')


class ajustesCookies(unittest.TestCase):
    @when('I click the ajustes cookies')
    def click_ajustes_cookies(self):
        pagina_ajCoo = self.driver
        logger.debug('INICIO STEP: I click the ajustes cookies')
        try:
            pagina_ajCoo.find_element(by=By.XPATH, value='/html/body/button/span[1]').click()
            logger.debug('Elemento "the footer politica cookies" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "the footer politica cookies" no encontrado')
            resStep = False
        time.sleep(2)
        logger.debug('FIN STEP: I click the ajustes cookies --> {}'.format(resStep))
        assert resStep

    @then('I see the ajustes cookies')
    def see_ajustes_cookies(self):
        pagina_ajCoo = self.driver
        logger.debug('INICIO STEP: I see the ajustes cookies')
        try:
            # --> no me reconoce el path conmpleto, dejo el parcial
            activar_todo = pagina_ajCoo.find_element(by=By.XPATH,
                                                     value="//*[@id='moove_gdpr_cookie_modal']/div/div[2]/div[3]/div/button[1]")
            guardar_ajustes = pagina_ajCoo.find_element(by=By.XPATH,
                                                        value="//*[@id='moove_gdpr_cookie_modal']/div/div[2]/div[3]/div/button[2]")
            logger.debug('Elemento "activar_todo" encontrado')
            logger.debug('Elemento "guardar_ajustes" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "activar_todo/guardar_ajustes" no encontrado')
            resStep = False
        time.sleep(2)
        logger.debug('FIN STEP: I click the ajustes cookies --> {}'.format(resStep))
        assert resStep




