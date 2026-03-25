import logging
import logging.config
import logging.handlers
import time
import unittest
import os
import configparser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from behave import given, when, then, step
from pageobjects import HomeUser

homeElements = HomeUser.HomeUser()

logger = logging.getLogger('WebLogs')

class Setup(unittest.TestCase):

    @given('I visit the main page in web')
    def visit_main_page_web(self):
        logger.debug('INICIO STEP: I visit the main page in web')
        page = self.driver
        try:
            page.get(self.environment)
            logger.debug('Se abre navegador con Tamus')
            resStep = True
        except Exception as e:
            logger.error('Error en apertura de navegador con Tamus. Error --> {}'.format(e))
            resStep = False
        # Añadir navegador
        logger.debug('FIN STEP: I visit the main page in web >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep
