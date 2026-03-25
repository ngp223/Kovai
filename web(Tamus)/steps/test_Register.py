import time
import unittest
import logging.handlers
from behave import step, then, when
from selenium.webdriver.common.by import By
from pageobjects import Login, Cookies

logger = logging.getLogger('WebLogs')
loginElemnents = Login.Login()
cookiesElemnents = Cookies.Cookies()


class Register(unittest.TestCase):
    @step('I click register to web')
    def registrar(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP:  I click register to web')
        try:
            ElemValidar = loginElemnents.registerID
            pagina_Login.find_element(by=By.ID, value=ElemValidar).click()
            logger.debug('Elemento encontrado')
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click register to Web --> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP:I click register to web')
        assert resStep

    @step('I accept cookies')
    def accept_cookies(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I accept cookies')
        current_page = pagina_Login.current_url
        try:
            ElemValidar = cookiesElemnents.buttonCookiesXpath
            pagina_Login.find_element(by=By.XPATH, value=ElemValidar).click()
            time.sleep(2)
            logger.debug('Elemento encontrado en la pagina ' + current_page)
            resStep = True
        except Exception as e:
            logger.error("buttonCookiesXpath no encontrado: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I accept Cookies --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then('Do register')
    def registro(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: Do register')
        time.sleep(2)
        logger.debug('FIN STEP: Do register')









