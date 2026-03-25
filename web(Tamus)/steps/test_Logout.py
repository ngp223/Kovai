import time
import unittest
import os
import logging
import logging.config
import logging.handlers

from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects import Login, HomeUser

loginElemnents = Login.Login()
homeElements = HomeUser.HomeUser()

logger = logging.getLogger('WebLogs')


class Logout(unittest.TestCase):
    # Step >> Given, When and Then
    @step('I click on logout')
    def see_home_user_page(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I click on logout')
        try:
            # Desplegamos y pulsamos 'Cerrar sesión'
            ElemValidar = homeElements.userSubDropXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubDropXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubClosID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubClosID).click()
            logger.debug('Pulsamos Cerrar sesión')
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on logout >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep
