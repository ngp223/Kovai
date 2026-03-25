# app/steps/gestion_restaurantes_steps.py

import time
import logging
from behave import when, then
from app.pageobjects_app import GESTION_RESTAURANTES_BTN, TITULO_GESTION_RESTAURANTES
from appium.webdriver.common.appiumby import AppiumBy

logger = logging.getLogger('WebLogs')


class GestionRestaurantesSteps:

    @when('I click to gestion restaurantes')
    def click_user_gestion_restaurantes(self):
        logger.debug('INICIO STEP: I click to gestion restaurantes')

        if self.context.platform == "web":
            # Aquí puedes llamar al step web original
            pass
        elif self.context.platform == "app":
            try:
                el = self.context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=GESTION_RESTAURANTES_BTN)
                el.click()
                logger.debug('Botón "Gestión Restaurantes" clicado en la app')
                resStep = True
            except Exception as e:
                logger.error('Botón "Gestión Restaurantes" no encontrado en la app: {}'.format(e))
                resStep = False
            time.sleep(2)
            self.context.statusScenario = self.context.statusScenario & resStep
            assert resStep

    @then('I see gestion de restaurantes')
    def see_gestion_restaurantes(self):
        logger.debug('INICIO STEP: I see gestion de restaurantes')
        resStep = True

        if self.context.platform == "web":
            # Mantén tu código Selenium original aquí
            pass
        elif self.context.platform == "app":
            try:
                el = self.context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=TITULO_GESTION_RESTAURANTES)
                resStep = el.is_displayed()
                logger.debug('Pantalla "Gestión de Restaurantes" visible en la app --> {}'.format(resStep))
            except Exception as e:
                logger.error('Pantalla "Gestión de Restaurantes" no encontrada en la app: {}'.format(e))
                resStep = False

        self.context.statusScenario = self.context.statusScenario & resStep
        assert resStep
        logger.debug('FIN STEP: I see gestion de restaurantes --> {}'.format(resStep))