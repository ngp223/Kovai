import time
import unittest
import logging.handlers
import cv2

from behave import given, when, then, step
from selenium.webdriver.common.by import By

from pageobjects import HomeUser, ChangePass

homeElements = HomeUser.HomeUser()
changePassElements = ChangePass.ChangePass()

logger = logging.getLogger('WebLogs')


class ChangePass(unittest.TestCase):
    @step('I click on change password')
    def click_on_change_password(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I click on change password')
        try:
            # Desplegamos y pulsamos 'ChangePassword'
            ElemValidar = homeElements.userSubDropXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubDropXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubCPssID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubCPssID).click()
            logger.debug('Pulsamos Change Password')
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on change password >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the change password option")
    def see_change_password_option(self):
        pagina_changePass = self.driver
        logger.debug('INICIO STEP: I see the change password option')
        try:
            ElemValidar = changePassElements.title
            title = pagina_changePass.find_element(by=By.XPATH, value=changePassElements.titlePath).text
            logger.warning('Texto a validar: ' + ElemValidar + ' validado con: ' + title + ' > ' + str(
                ElemValidar == title))
            resStep = ElemValidar == title
            ElemValidar = changePassElements.closeXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.closeXPath).is_displayed()
            # Contraseña Actual
            ElemValidar = changePassElements.passActTXT
            passActual = pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passActTXTXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + passActual + ' > ' + str(
                    ElemValidar == passActual))
            resStep = (ElemValidar == passActual) & resStep
            ElemValidar = changePassElements.passActBoxXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passActBoxXPath).is_displayed()
            # Contraseña nueva
            ElemValidar = changePassElements.passNewTXT
            passActual = pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passNewTXTXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + passActual + ' > ' + str(
                    ElemValidar == passActual))
            resStep = (ElemValidar == passActual) & resStep
            ElemValidar = changePassElements.passNewBoxXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passNewBoxXPath).is_displayed()
            # Repetir contraseña nueva
            ElemValidar = changePassElements.passRepNewTXT
            passActual = pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passRepNewTXTXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + passActual + ' > ' + str(
                    ElemValidar == passActual))
            resStep = (ElemValidar == passActual) & resStep
            ElemValidar = changePassElements.passRepNewBoxXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passRepNewBoxXPath).is_displayed()
            # Botón cancelar y aceptar
            ElemValidar = changePassElements.btnChangeXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.btnChangeXPath).is_displayed()
            ElemValidar = changePassElements.btnCancelXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.btnCancelXPath).is_displayed()
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the change password option >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I fill out all data")
    def fill_out_all_data(self):
        pagina_changePass = self.driver
        logger.debug('INICIO STEP: I fill out all data')
        try:
            # Rellenamos password antigua y nueva
            ElemValidar = changePassElements.passActBoxXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passActBoxXPath).send_keys(
                "Actual_Password")
            ElemValidar = changePassElements.passNewBoxXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passNewBoxXPath).send_keys(
                self.changePass)
            ElemValidar = changePassElements.passRepNewBoxXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passRepNewBoxXPath).send_keys(
                self.changePass)
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I fill out all data >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step("I click on confirm button")
    def click_on_confirm_button(self):
        pagina_changePass = self.driver
        logger.debug('INICIO STEP: I click on confirm button')
        try:
            ElemValidar = changePassElements.btnChangeXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.btnChangeXPath).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on confirm button >> {}'.format(resStep))
        time.sleep(5)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when('I fill out with {actPass} {newPass} {confNewPass} wrong data')
    def fill_out_empty_data(self, actPass, newPass, confNewPass):
        pagina_changePass = self.driver
        logger.debug('INICIO STEP: I fill out with wrong data')
        try:
            # Dejamos algún campo vacío >> 'Los campos seleccionados son obligatorios.'
            logger.debug('Ejecución con {}, {} y {}'.format(actPass, newPass, confNewPass))
            if actPass != 'None':
                ElemValidar = changePassElements.passActBoxXPath
                pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passActBoxXPath).send_keys(
                    actPass)
            if newPass != 'None':
                ElemValidar = changePassElements.passNewBoxXPath
                pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passNewBoxXPath).send_keys(
                    newPass)
            if confNewPass != 'None':
                ElemValidar = changePassElements.passRepNewBoxXPath
                pagina_changePass.find_element(by=By.XPATH, value=changePassElements.passRepNewBoxXPath).send_keys(
                    confNewPass)
            time.sleep(3)
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I fill out with wrong data >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see message error {msgeError}")
    def see_message_error(self, msgeError):
        pagina_changePass = self.driver
        logger.debug('INICIO STEP: I see message error {}'.format(msgeError))
        try:
            ElemValidar = msgeError
            msageError = pagina_changePass.find_element(by=By.XPATH, value=changePassElements.msgeErrorXPath).text
            logger.warning('Texto a validar: ' + ElemValidar + ' validado con: ' + msageError + ' > ' + str(
                ElemValidar == msageError))
            resStep = ElemValidar == msageError
            if resStep is False:
                pagina_changePass.find_element(by=By.XPATH, value=changePassElements.msgeErrorXPath).screenshot(
                self.outputs + str(str(time.strftime("%Y%m%d_%H:%M:%S"))) + 'ERROR_CHAPASS_' + msageError + '.png')
            time.sleep(3)
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see message error {} >> {}'.format(msgeError, resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step("I click on cancel button change password")
    def click_on_cancel_button_change_password(self):
        pagina_changePass = self.driver
        logger.debug('INICIO STEP: I click on cancel button')
        try:
            ElemValidar = changePassElements.btnCancelXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.btnCancelXPath).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on cancel button >> {}'.format(resStep))
        time.sleep(5)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step("I click on close change password")
    def click_on_close_button_change_password(self):
        pagina_changePass = self.driver
        logger.debug('INICIO STEP: I click on close change password')
        try:
            ElemValidar = changePassElements.closeXPath
            pagina_changePass.find_element(by=By.XPATH, value=changePassElements.closeXPath).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on close change password >> {}'.format(resStep))
        time.sleep(5)
        self.statusScenario = self.statusScenario & resStep
        assert resStep
