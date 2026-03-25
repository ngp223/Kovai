import time
import logging.handlers
from behave import then,step
from selenium.webdriver.common.by import By

logger = logging.getLogger('WebLogs')


@step('I click the footer aviso legal')
def click_footer_aviso_legal(self):
    linea_footer = self.driver
    linea_footer.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    logger.debug('INICIO STEP: I click the footer aviso legal')
    try:
        linea_footer.find_element(by=By.LINK_TEXT, value="AVISO LEGAL").click()
        logger.debug('Elemento "I click the footer aviso legal" encontrado')
        resStep = True
    except Exception as e:
        logger.error('Elemento "the footer aviso legal" no encontrado')
        resStep = False
    time.sleep(2)
    self.statusScenario = self.statusScenario & resStep
    logger.debug('FIN STEP: I click the footer aviso legal --> {}'.format(resStep))
    assert resStep


@step('I click the footer politica privacidad')
def click_footer_politica_privacidad(self):
    linea_footer = self.driver
    linea_footer.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    logger.debug('INICIO STEP: I click the footer politica privacidad')
    try:
        linea_footer.find_element(by=By.LINK_TEXT, value="POLÍTICA DE PRIVACIDAD").click()
        logger.debug('Elemento "the footer politica privacidad" encontrado')
        resStep = True
    except Exception as e:
        logger.error('Elemento "the footer politica privacidad" no encontrado')
        resStep = False
    time.sleep(2)
    self.statusScenario = self.statusScenario & resStep
    logger.debug('FIN STEP: I click the footer politica privacidad --> {}'.format(resStep))
    assert resStep


@step('I click the footer politica cookies')
def click_footer_politica_cookies(self):
    linea_footer = self.driver
    linea_footer.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    logger.debug('INICIO STEP: I click the footer politica cookies')
    try:
        linea_footer.find_element(by=By.LINK_TEXT, value="POLÍTICA DE COOKIES").click()
        logger.debug('Elemento "the footer politica cookies" encontrado')
        resStep = True
    except Exception as e:
        logger.error('Elemento "the footer politica cookies" no encontrado')
        resStep = False
    time.sleep(2)
    self.statusScenario = self.statusScenario & resStep
    logger.debug('FIN STEP: I click the footer politica cookies --> {}'.format(resStep))
    assert resStep


