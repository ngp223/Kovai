import time
import unittest
import logging.handlers
from behave import step
from selenium.webdriver.common.by import By

logger = logging.getLogger('WebLogs')


class solicitarLlamada(unittest.TestCase):
    @step('I request call')
    def solicitar_llamada(self):
        pagina_SL = self.driver
        logger.debug('INICIO STEP: I request call')
        pagina_SL.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            ElemValidar = "et_pb_contact_nombre_0"
            pagina_SL.find_element(by=By.ID, value=ElemValidar).send_keys("fake")
            ElemValidar = "et_pb_contact_teléfono_0"
            pagina_SL.find_element(by=By.ID, value=ElemValidar).send_keys("000000000")
            logger.debug("Bajo al final de la pagina y relleno nombre y teléfono")
            ElemValidar = "et_builder_submit_button"
            solicitar = pagina_SL.find_element(by=By.NAME, value=ElemValidar)
            # solicitar.click()
            resStep = True
        except Exception as e:
            logger.error('Algún elemento en "I request call" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I request call --> {}'.format(resStep))
        assert resStep

    @step('I request call contact')
    def solicitar_llamada_contacto(self):
        pagina_SLContacto = self.driver
        logger.debug('INICIO STEP: I request call_contact')
        pagina_SLContacto.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            ElemValidar = "et_pb_contact_nombre_1"
            pagina_SLContacto.find_element(by=By.ID, value=ElemValidar).send_keys("fake")
            ElemValidar = "et_pb_contact_teléfono_1"
            pagina_SLContacto.find_element(by=By.ID, value=ElemValidar).send_keys("000000000")
            logger.debug("Bajo al final de la página y relleno nombre y teléfono")
            ElemValidar = "et_builder_submit_button"
            solicitar = pagina_SLContacto.find_element(by=By.NAME, value=ElemValidar)
            # solicitar.click()
            resStep = True
        except Exception as e:
            logger.error('Algún elemento en "I request call_contact" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I request call_contact --> {}'.format(resStep))
        assert resStep


