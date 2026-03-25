import time
import unittest
import logging.handlers
from behave import then, when
from selenium.webdriver.common.by import By
from pageobjects import PolCookies

logger = logging.getLogger('WebLogs')
politicaCookiesElements = PolCookies.PolCookies()


class PoliticaCookies(unittest.TestCase):

    @when('I click to politica cookies')
    def click_politica_cookies(self):
        pagina_politicaCookies = self.driver
        logger.debug('INICIO STEP: I click to politica cookies')
        pagina_politicaCookies.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            ElemValidar = politicaCookiesElements.opPCoLink
            pagina_politicaCookies.find_element(by=By.LINK_TEXT, value=ElemValidar).is_displayed()
            pagina_politicaCookies.find_element(by=By.LINK_TEXT, value=ElemValidar).click()
            logger.warning('Elemento "I click to Politica Cookies" encontrado')
            resStep = True
        except Exception as e:
            logger.error('Elemento "I click to Politica Cookies" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click to Politica Cookies --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I click to politica cookies')
        assert resStep

    @then('I see page politica cookies')
    def see_politica_cookies(self):
        pagina_politicaCookies = self.driver
        logger.debug('INICIO STEP: I see page politica cookies')
        pagina_politicaCookies.switch_to.window(pagina_politicaCookies.window_handles[1])
        time.sleep(3)
        try:
            ElemValidar = politicaCookiesElements.primeraLineaPCoXPath
            title = pagina_politicaCookies.find_element(by=By.XPATH, value=ElemValidar).text
            ElemValidar = politicaCookiesElements.primeraLineaPCoTXT
            logger.debug(ElemValidar + ' lo comparo con: ' + title + ' --> ' + format(ElemValidar))
            resStep = (title == ElemValidar)
            logger.warning("Primer texto de politica cookies --> {}".format(resStep))
            ElemValidar = politicaCookiesElements.nombrepesPCo
            logger.debug(ElemValidar + ' lo comparo con: ' + pagina_politicaCookies.title + ' --> ' + str(
                ElemValidar == pagina_politicaCookies.title))
            resStep = (ElemValidar == pagina_politicaCookies.title) & resStep
            logger.warning("Nombre de la pestaña abierta --> {}".format(resStep))
            logger.debug(politicaCookiesElements.url + ' lo comparo con: ' + pagina_politicaCookies.current_url + ' --> ' + str(
                politicaCookiesElements.url == pagina_politicaCookies.current_url))
            resStep = (politicaCookiesElements.url == pagina_politicaCookies.current_url) & resStep
            logger.warning("URL --> {}".format(resStep))
            time.sleep(2)
        except Exception as e:
            logger.error('Algún elemento "I see page politica cookies" no encontrado: {}'.format(ElemValidar, e))
            resStep = False
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I see page politica cookies --> {}'.format(resStep))
        assert resStep
