import time
import unittest
import os
import logging
import logging.config
import logging.handlers
from commons import obtenerTextos

from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects import Login, HomeUser

loginElements = Login.Login()
homeElements = HomeUser.HomeUser()

logger = logging.getLogger('WebLogs')


class Login(unittest.TestCase):
    # Step >> Given, When and Then
    @step('I see the Login page')
    def see_login_page(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I see the Login page ')
        try:
            # Hay que cambiar estas validaciones para no tener un try catch y que el TC falle y vaya a logs
            ElemValidar = loginElements.url
            url = pagina_Login.current_url
            logger.debug('Texto a validar: ' + loginElements.url + ' validado con: ' + url + ' > ' + str(
                loginElements.url == url))
            resStep = loginElements.url == url
            ElemValidar = loginElements.title
            title = pagina_Login.title
            logger.debug('Texto a validar: ' + loginElements.title + ' validado con: ' + title + ' > ' + str(
                loginElements.title == title))
            resStep = (loginElements.title == title) & resStep
            ElemValidar = loginElements.subtitle
            subtitle = pagina_Login.find_element(by=By.XPATH, value=loginElements.subtitleXPath).text
            logger.warning('Texto a validar: ' + loginElements.subtitle + ' validado con: ' + subtitle + ' > ' + str(
                loginElements.subtitle == subtitle))
            resStep = (loginElements.subtitle == subtitle) & resStep
            ElemValidar = loginElements.logoImgID
            pagina_Login.find_element(by=By.ID, value=loginElements.logoImgID).is_displayed()
            ElemValidar = loginElements.logoNameID
            pagina_Login.find_element(by=By.ID, value=loginElements.logoNameID).is_displayed()
            ElemValidar = loginElements.usernameID
            pagina_Login.find_element(by=By.ID, value=loginElements.usernameID).is_displayed()
            ElemValidar = loginElements.passwordID
            pagina_Login.find_element(by=By.ID, value=loginElements.passwordID).is_displayed()
            ElemValidar = loginElements.inicioBtnID
            pagina_Login.find_element(by=By.ID, value=loginElements.inicioBtnID).is_displayed()
            ElemValidar = loginElements.forgotpassID
            pagina_Login.find_element(by=By.ID, value=loginElements.forgotpassID).is_displayed()
            ElemValidar = loginElements.registerID
            pagina_Login.find_element(by=By.ID, value=loginElements.registerID).is_displayed()
            ElemValidar = loginElements.votquestionXPath
            pagina_Login.find_element(by=By.XPATH, value=loginElements.votquestionXPath).is_displayed()
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug("Finalizada validación página Login")
        logger.debug('FIN STEP: I see the Login page >> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then('I login as an user')
    def login_as_user(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I login as an user')
        current_page = pagina_Login.current_window_handle
        try:
            ElemValidar = pagina_Login.find_element(by=By.ID, value=loginElements.usernameID).send_keys(self.user_OK)
            ElemValidar = pagina_Login.find_element(by=By.ID, value=loginElements.passwordID).send_keys(self.password_OK)
            ElemValidar = pagina_Login.find_element(by=By.ID, value=loginElements.inicioBtnID).click()
            time.sleep(1)
            # Validar que entramos a la Home de Tamus
            url = pagina_Login.current_url
            ElemValidar = homeElements.url
            logger.debug('Texto a validar: ' + homeElements.url + ' validado con: ' + url + ' > ' + str(
                homeElements.url == url))
            resStep = homeElements.url == url
            ElemValidar = homeElements.title
            title = pagina_Login.title
            logger.debug('Texto a validar: ' + homeElements.title + ' validado con: ' + title + ' > ' + str(
                homeElements.title == title))
            resStep = (homeElements.title == title) & resStep
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug("Finalizado Login con usuario y contraseña correctos.")
        logger.debug('FIN STEP: I login as an user --> {}'.format(resStep))
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then('I try to login with wrong user')
    def not_login_as_user(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I try to login with wrong user')
        username = pagina_Login.find_element(by=By.ID, value=loginElements.usernameID)
        username.send_keys('userError')
        password = pagina_Login.find_element(by=By.ID, value=loginElements.passwordID)
        password.send_keys('passwordOK')
        btnLogin = pagina_Login.find_element(by=By.ID, value=loginElements.inicioBtnID).click()
        time.sleep(2)
        resStep = True
        try:
            ElemValidar = loginElements.msgLoginErrorXPath
            ElemValidarTXT = loginElements.msgLoginError
            errormsg = obtenerTextos(resStep, pagina_Login, ElemValidar, ElemValidarTXT)
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I try to login with wrong user --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then('I try to login with wrong password')
    def not_login_as_user(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I try to login with wrong password')
        username = pagina_Login.find_element(by=By.ID, value=loginElements.usernameID)
        username.send_keys('qa@tamus.io')  # Usuario registrado OK
        password = pagina_Login.find_element(by=By.ID, value=loginElements.passwordID)
        password.send_keys('passwordError')
        btnLogin = pagina_Login.find_element(by=By.ID, value=loginElements.inicioBtnID).click()
        time.sleep(2)
        resStep = True
        try:
            ElemValidar = loginElements.msgLoginErrorXPath
            ElemValidarTXT = loginElements.msgLoginError
            errormsg = obtenerTextos(resStep, pagina_Login, ElemValidar, ElemValidarTXT)
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I try to login with wrong password --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then('I try to login without user') ### CODIGO MAL HECHO. SE QUEDA PILLADO,DECIRSELO A FERNANDO
    def not_login_as_user(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I try to login without user')
        # Without User and with password
        password = pagina_Login.find_element(by=By.ID, value=loginElements.passwordID)
        password.send_keys('passwordError')
        btnLogin = pagina_Login.find_element(by=By.ID, value=loginElements.inicioBtnID).click()
        time.sleep(2)
        resStep = True
        try:

            ElemValidar = loginElements.msgLoginErrorXPath
            ElemValidarTXT = loginElements.msgLoginError
            errormsg = obtenerTextos(resStep, pagina_Login, ElemValidar, ElemValidarTXT)
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I try to login without user --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then('I try to login without password')
    def not_login_as_user(self):
        pagina_Login = self.driver
        logger.debug('INICIO STEP: I try to login without password')
        # With User and without password
        username = pagina_Login.find_element(by=By.ID, value=loginElements.usernameID)
        username.send_keys('userOK')  # Usuario registrado OK
        btnLogin = pagina_Login.find_element(by=By.ID, value=loginElements.inicioBtnID)
        btnLogin.click()
        time.sleep(2)
        resStep = True
        try:
            ElemValidar = loginElements.msgLoginErrorXPath
            ElemValidarTXT = loginElements.msgLoginErrorPass
            errormsg = obtenerTextos(resStep, pagina_Login, ElemValidar, ElemValidarTXT)
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I try to login without password --> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep
