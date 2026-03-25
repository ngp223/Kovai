import logging
import time
import unittest

from behave import given, when, then, step
from selenium.webdriver.common.by import By
from pageobjects import RememberPassword, Login

loginElemnents = Login.Login()
remPassElements = RememberPassword.RemPass()
confPassElements = RememberPassword.ConfirmRemPass()

logger = logging.getLogger('WebLogs')


class RememberPass(unittest.TestCase):
    @step('I go into the remember password page')
    def click_remember_password(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I go into the remember password page')
        try:
            ElemValidar = loginElemnents.forgotpassID
            remPassLink = pagina_Login.find_element(by=By.ID, value=loginElemnents.forgotpassID)
            remPassLink.click()
            # Validar que estoy en la página de remember password
            ElemValidar = pagina_Login.current_url
            logger.warning('Texto a validar: ' + confPassElements.url + ' validado con: ' + pagina_Login.current_url + ' > ' + str(
                pagina_Login.current_url == confPassElements.url))
            resStep = pagina_Login.current_url == confPassElements.url
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug("Finalizado: click on remember password")
        logger.debug('FIN STEP: I go into the remember password page --> {}'.format(resStep))
        time.sleep(5)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step("I see the remember password page")
    def see_remember_password_page(self):
        pagina_RemPass = self.driver
        logger.debug('INICIO STEP: I see the remember password page')
        try:
            ElemValidar = remPassElements.subtitle
            subtitle = pagina_RemPass.find_element(by=By.XPATH, value=remPassElements.subtitleXPath).text
            logger.warning('Texto a validar: ' + remPassElements.subtitle + ' validado con: ' + subtitle + ' > ' + str(
            remPassElements.subtitle == subtitle))
            resStep = (remPassElements.subtitle == subtitle)
            ElemValidar = remPassElements.mailXPath
            pagina_RemPass.find_element(by=By.XPATH, value=remPassElements.mailXPath).is_displayed()
            ElemValidar = remPassElements.btnConfirmID
            pagina_RemPass.find_element(by=By.ID, value=remPassElements.btnConfirmID).is_displayed()
            ElemValidar = remPassElements.btnBackID
            pagina_RemPass.find_element(by=By.ID, value=remPassElements.btnBackID).is_displayed()
            ElemValidar = remPassElements.helpID
            pagina_RemPass.find_element(by=By.ID, value=remPassElements.helpID).is_displayed()
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug("Finalizada validación página de remember password")
        logger.debug('FIN STEP: I see the remember password page --> {}'.format(resStep))
        time.sleep(3)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I fill the email and click on remember password")
    def request_remember_password(self):
        pagina_RemPass = self.driver
        logger.debug('INICIO STEP: I fill the email and click on remember password')
        try:
            ElemValidar = remPassElements.mailXPath
            remPassEmail = pagina_RemPass.find_element(by=By.XPATH, value=remPassElements.mailXPath)
            remPassEmail.send_keys('slopez@hi-iberia.es')
            ElemValidar = remPassElements.btnConfirmID
            remPassRecButton = pagina_RemPass.find_element(by=By.ID, value=remPassElements.btnConfirmID)
            remPassRecButton.click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug("Finalizada solicitud de remember password")
        logger.debug('FIN STEP: I fill the email and click on remember password --> {}'.format(resStep))
        time.sleep(3)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step("I see the confirmation recovery page")
    def confirm_recovery_page(self):
        pagina_RemConfPass = self.driver
        logger.debug('INICIO STEP: I see the confirmation recovery page')
        try:
            ElemValidar = confPassElements.subtitle
            subtitle = pagina_RemConfPass.find_element(by=By.XPATH, value=confPassElements.subtitleXPath).text
            logger.warning('Texto a validar: ' + confPassElements.subtitle + ' validado con: ' + subtitle + ' > ' + str(
                confPassElements.subtitle == subtitle))
            resStep = confPassElements.subtitle == subtitle
            ElemValidar = confPassElements.message
            remPassMsgConfirm = pagina_RemConfPass.find_element(by=By.XPATH, value=confPassElements.messageXPath).text
            logger.warning(
                'Texto a validar: ' + confPassElements.message + ' validado con: ' + remPassMsgConfirm + ' > ' + str(
                    confPassElements.message == remPassMsgConfirm))
            resStep = (confPassElements.message == remPassMsgConfirm) & resStep
            ElemValidar = confPassElements.resendEmailID
            pagina_RemConfPass.find_element(by=By.ID, value=confPassElements.resendEmailID).is_displayed()
            ElemValidar = confPassElements.btnBackID
            pagina_RemConfPass.find_element(by=By.ID, value=confPassElements.btnBackID).is_displayed()
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug("Finalizada validación página confirmación remember password")
        logger.debug('FIN STEP: I see the confirmation recovery page --> {}'.format(resStep))
        time.sleep(3)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I click on resend email recovery password")
    def click_on_resend_email(self):
        pagina_RemConfPass = self.driver
        logger.debug('INICIO STEP: I click on resend email recovery password')
        try:
            ElemValidar = confPassElements.resendEmailID
            remPassResendemail = pagina_RemConfPass.find_element(by=By.ID, value=confPassElements.resendEmailID)
            remPassResendemail.click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        # ¿Cómo validar que se envía?
        logger.debug("Finalizado click en Resend Password")
        logger.debug('FIN STEP: I click on resend email recovery password --> {}'.format(resStep))
        time.sleep(3)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I click on back from remember password")
    def click_on_back_confirm_rem_pass(self):
        pagina_RemConfPass = self.driver
        logger.debug('INICIO STEP: I click on back from remember password')
        try:
            ElemValidar = confPassElements.btnBackID
            remPassBackBtn = pagina_RemConfPass.find_element(by=By.ID, value=confPassElements.btnBackID)
            remPassBackBtn.click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        # Confirmar que se vuelve a la ventana de Login
        logger.debug("Finalizado click en Volver - Recovery Password")
        logger.debug('FIN STEP: I click on back from remember password --> {}'.format(resStep))
        time.sleep(3)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I click on back from confirm recovery pass")
    def click_on_back_confirm_recovery_pass(self):
        pagina_RemConfPass = self.driver
        logger.debug('INICIO STEP: I click on back from confirm recovery pass')
        try:
            ElemValidar = confPassElements.btnBackID
            remPassBackBtn = pagina_RemConfPass.find_element(by=By.ID, value=confPassElements.btnBackID)
            remPassBackBtn.click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug("Finalizado click en Volver - Confirm Send Password")
        logger.debug('FIN STEP: I click on back from confirm recovery pass --> {}'.format(resStep))
        time.sleep(3)
        self.statusScenario = self.statusScenario & resStep
        assert resStep
