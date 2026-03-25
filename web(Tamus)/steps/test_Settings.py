import time
import unittest
import logging.handlers

from behave import given, when, then, step
from selenium.webdriver.common.by import By

from pageobjects import HomeUser, Settings

homeElements = HomeUser.HomeUser()
settingsElements = Settings.Settings()

logger = logging.getLogger('WebLogs')


class Settings(unittest.TestCase):
    @step('I click on settings')
    def click_on_settings(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I click on settings')
        try:
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubDropXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubDropXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            logger.debug('Pulsamos Ajustes')
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on settings >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step("I see the settings page")
    def see_settings_page(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the settings page')
        try:
            url = pagina_settings.current_url
            ElemValidar = settingsElements.url
            logger.warning('Texto a validar: ' + ElemValidar + ' validado con: ' + url + ' > ' + str(
                ElemValidar == url))
            resStep = ElemValidar == url
            ElemValidar = settingsElements.title
            title = pagina_settings.title
            logger.warning('Texto a validar: ' + ElemValidar + ' validado con: ' + title + ' > ' + str(
                ElemValidar == title))
            resStep = (ElemValidar == title) & resStep
            ElemValidar = settingsElements.subtitleTXT
            subtitle = pagina_settings.find_element(by=By.XPATH, value=settingsElements.subtitleXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + subtitle + ' > ' + str(
                    ElemValidar == subtitle))
            resStep = (ElemValidar == subtitle) & resStep
            # Albaran entrada pendiente
            ElemValidar = settingsElements.inPendSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.inPendSettingXPath).is_displayed()
            ElemValidar = settingsElements.imgInPendSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.imgInPendSettingXPath).is_displayed()
            ElemValidar = settingsElements.optInPendSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingXPath).is_displayed()
            ElemValidar = settingsElements.inPendSettingTXT
            albEntrPte = pagina_settings.find_element(by=By.XPATH, value=settingsElements.inPendSettingXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + albEntrPte + ' > ' + str(
                    ElemValidar == albEntrPte))
            resStep = (ElemValidar == albEntrPte) & resStep
            # Albaran salida pendiente
            ElemValidar = settingsElements.dePendSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.dePendSettingXPath).is_displayed()
            ElemValidar = settingsElements.imgDePendSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.imgDePendSettingXPath).is_displayed()
            ElemValidar = settingsElements.optDePendSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDePendSettingXPath).is_displayed()
            ElemValidar = settingsElements.dePendSettingTXT
            albSalPte = pagina_settings.find_element(by=By.XPATH, value=settingsElements.dePendSettingXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + albSalPte + ' > ' + str(
                    ElemValidar == albSalPte))
            resStep = (ElemValidar == albSalPte) & resStep

            # Albaran entrada rechazado
            ElemValidar = settingsElements.inRejSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.inRejSettingXPath).is_displayed()
            ElemValidar = settingsElements.imgInRejSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.imgInRejSettingXPath).is_displayed()
            ElemValidar = settingsElements.optInPendSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInRejSettingXPath).is_displayed()
            ElemValidar = settingsElements.inRejSettingTXT
            albEntrRej = pagina_settings.find_element(by=By.XPATH, value=settingsElements.inRejSettingXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + albEntrRej + ' > ' + str(
                    ElemValidar == albEntrRej))
            resStep = (ElemValidar == albEntrRej) & resStep
            # Albaran salida rechazado
            ElemValidar = settingsElements.deRejSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.deRejSettingXPath).is_displayed()
            ElemValidar = settingsElements.imgDeRejSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.imgDeRejSettingXPath).is_displayed()
            ElemValidar = settingsElements.optDeRejSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDeRejSettingXPath).is_displayed()
            ElemValidar = settingsElements.deRejSettingTXT
            albSalRej = pagina_settings.find_element(by=By.XPATH, value=settingsElements.deRejSettingXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + albSalRej + ' > ' + str(
                    ElemValidar == albSalRej))
            resStep = (ElemValidar == albSalRej) & resStep
            # Stock bajo en almacén
            ElemValidar = settingsElements.lowStoSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.lowStoSettingXPath).is_displayed()
            ElemValidar = settingsElements.imgLowStoSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.imgLowStoSettingXPath).is_displayed()
            ElemValidar = settingsElements.optLowStoSettingXPath
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optLowStoSettingXPath).is_displayed()
            ElemValidar = settingsElements.lowStoSettingTXT
            stockLow = pagina_settings.find_element(by=By.XPATH, value=settingsElements.lowStoSettingXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + stockLow + ' > ' + str(
                    ElemValidar == stockLow))
            resStep = (ElemValidar == stockLow) & resStep
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the settings page >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I activate the option incoming delivery pending")
    def activate_incoming_delivery_pending(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I activate the option incoming delivery pending')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optInPendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingXPath).is_displayed()
            # Comprobamos si está seleccionado, si no > Se selecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optInPendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor: # Está seleccionada
                logger.debug('Opción activada.')
            else:  # No está seleccionada -> Se selecciona
                logger.debug('Activamos la opción.')
                ElemValidar = settingsElements.optInPendSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingXPath).click()
            time.sleep(2)
            # Recargamos la página
            #pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I activate the option incoming delivery pending >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I activate the option departure delivery pending")
    def activate_departure_delivery_pending(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I activate the option departure delivery pending')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optDePendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDePendSettingXPath).is_displayed()
            # Comprobamos si está seleccionado, si no > Se selecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDePendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:  # Está seleccionada
                logger.debug('Opción activada.')
            else:  # No está seleccionada -> Se selecciona
                logger.debug('Activamos la opción.')
                ElemValidar = settingsElements.optDePendSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDePendSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I activate the option departure delivery pending >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I activate the option incoming delivery rejected")
    def activate_incoming_delivery_rejected(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I activate the option incoming delivery rejected')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optInRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInRejSettingXPath).is_displayed()
            time.sleep(2)
            # Comprobamos si está seleccionado, si no > Se selecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optInRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:  # Está seleccionada
                logger.debug('Opción activada.')
            else:  # No está seleccionada -> Se selecciona
                logger.debug('Activamos la opción.')
                ElemValidar = settingsElements.optInRejSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInRejSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I activate the option incoming delivery rejected >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I activate the option departure delivery rejected")
    def activate_departure_delivery_rejected(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I activate the option departure delivery rejected')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optDeRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDeRejSettingXPath).is_displayed()
            # Comprobamos si está seleccionado, si no > Se selecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDeRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:  # Está seleccionada
                logger.debug('Opción activada.')
            else:  # No está seleccionada -> Se selecciona
                logger.debug('Activamos la opción.')
                ElemValidar = settingsElements.optDeRejSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDeRejSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I activate the option departure delivery rejected >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I activate the option low stock")
    def activate_low_stock(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I activate the option low stock')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optLowStoSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optLowStoSettingXPath).is_displayed()
            # Comprobamos si está seleccionado, si no > Se selecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optLowStoSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:  # Está seleccionada
                logger.debug('Opción activada.')
            else:  # No está seleccionada -> Se selecciona
                logger.debug('Activamos la opción.')
                ElemValidar = settingsElements.optLowStoSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optLowStoSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True

        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I activate the option low stock >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option incoming delivery pending actived")
    def see_incoming_delivery_pending_actived(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option incoming delivery pending actived')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            time.sleep(2)
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optInPendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingXPath).is_displayed()
            # Validamos si está seleccionado, si no -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:
                logger.debug('Opción activada.')
                resStep = True
            else:
                logger.debug('Opción no activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option incoming delivery pending actived >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option departure delivery pending actived")
    def see_departure_delivery_pending_actived(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option departure delivery pending actived')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            time.sleep(2)
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optDePendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDePendSettingXPath).is_displayed()
            # Validamos si está seleccionado, si no -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDePendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:
                logger.debug('Opción activada.')
                resStep = True
            else:
                logger.debug('Opción no activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False

        logger.debug('FIN STEP: I see the option departure delivery pending actived >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option incoming delivery rejected actived")
    def see_incoming_delivery_rejected_actived(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option incoming delivery rejected actived')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            time.sleep(2)
            logger.debug('Desplegamos el drop')
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            time.sleep(2)
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optInRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInRejSettingXPath).is_displayed()
            # Validamos si está seleccionado, si no -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optInRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:
                logger.debug('Opción activada.')
                resStep = True
            else:
                logger.debug('Opción no activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option incoming delivery rejected actived >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option departure delivery rejected actived")
    def see_departure_delivery_rejected_actived(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option departure delivery rejected actived')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optDeRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDeRejSettingXPath).is_displayed()
            # Validamos si está seleccionado, si no -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDeRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:
                logger.debug('Opción activada.')
                resStep = True
            else:
                logger.debug('Opción no activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option departure delivery rejected actived >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option low stock actived")
    def see_low_stock_actived(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option low stock actived')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            time.sleep(2)
            logger.debug('Desplegamos el drop')
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            time.sleep(2)
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optLowStoSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optLowStoSettingXPath).is_displayed()
            # Validamos si está seleccionado, si no -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optLowStoSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-not-empty' in switch_valor:
                logger.debug('Opción activada.')
                resStep = True
            else:
                logger.debug('Opción no activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option low stock actived >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option incoming delivery pending deactivated")
    def see_incoming_delivery_pending_deactivated(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option incoming delivery pending deactivated')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            time.sleep(2)
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción no está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optInPendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingXPath).is_displayed()
            # Validamos si no está seleccionado, si lo está -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optInPendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:
                logger.debug('Opción no activada.')
                resStep = True
            else:
                logger.debug('Opción activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option incoming delivery pending deactivated >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option departure delivery pending deactivated")
    def see_departure_delivery_pending_deactivated(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option departure delivery pending deactivated')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            time.sleep(2)
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción no está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optDePendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDePendSettingXPath).is_displayed()
            # Validamos si no está seleccionado, si lo está -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDePendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:
                logger.debug('Opción no activada.')
                resStep = True
            else:
                logger.debug('Opción activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option departure delivery pending deactivated >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option incoming delivery rejected deactivated")
    def see_incoming_delivery_rejected_deactivated(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option incoming delivery rejected deactivated')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            time.sleep(2)
            logger.debug('Desplegamos el drop')
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            time.sleep(2)
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción no está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optInRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInRejSettingXPath).is_displayed()
            # Validamos si no está seleccionado, si lo está -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optInRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:
                logger.debug('Opción no activada.')
                resStep = True
            else:
                logger.debug('Opción activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option incoming delivery rejected deactivated >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option departure delivery rejected deactivated")
    def see_departure_delivery_rejected_deactivated(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option departure delivery rejected deactivated')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción no está activa
            ElemValidar = ('Elemento no activo: ', settingsElements.optDeRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDeRejSettingXPath).is_displayed()
            # Validamos si no está seleccionado, si lo está -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDeRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:
                logger.debug('Opción no activada.')
                resStep = True
            else:
                logger.debug('Opción activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option departure delivery rejected deactivated >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @then("I see the option low stock deactivated")
    def see_low_stock_deactived(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I see the option low stock deactived')
        try:
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            time.sleep(2)
            # Desplegamos y pulsamos 'Settings'
            ElemValidar = homeElements.userSubUserNameXPath
            pagina_settings.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            logger.debug('Desplegamos el drop')
            time.sleep(2)
            ElemValidar = homeElements.userSubAjuID
            pagina_settings.find_element(by=By.ID, value=homeElements.userSubAjuID).click()
            logger.debug('Pulsamos Ajustes')
            # Validamos que la opción está deactiva
            ElemValidar = ('Elemento no activo: ', settingsElements.optLowStoSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optLowStoSettingXPath).is_displayed()
            # Validamos si está deseleccionado, si no -> Error
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optLowStoSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:
                logger.debug('Opción desactivada.')
                resStep = True
            else:
                logger.debug('Opción activada --> Failed')
                resStep = False
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the option low stock deactived >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I deactivate the option incoming delivery pending")
    def deactivate_incoming_delivery_pending(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I deactivate the option incoming delivery pending')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optInPendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingXPath).is_displayed()
            # Comprobamos si no está seleccionado, si no > Se elimina la selección
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optInPendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor: # Está deseleccionada
                logger.debug('Opción desactivada.')
            else:  # No está seleccionada -> Se deselecciona
                logger.debug('Desactivamos la opción.')
                ElemValidar = settingsElements.optInPendSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInPendSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I deactivate the option incoming delivery pending >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I deactivate the option departure delivery pending")
    def deactivate_departure_delivery_pending(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I deactivate the option departure delivery pending')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optDePendSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDePendSettingXPath).is_displayed()
            # Comprobamos si no está seleccionado, si no > Se deselecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDePendSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:  # Está deseleccionada
                logger.debug('Opción deactivada.')
            else:  # No está seleccionada -> Se deselecciona
                logger.debug('Desactivamos la opción.')
                ElemValidar = settingsElements.optDePendSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDePendSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I deactivate the option departure delivery pending >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep


    @when("I deactivate the option incoming delivery rejected")
    def deactivate_incoming_delivery_rejected(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I deactivate the option incoming delivery rejected')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optInRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInRejSettingXPath).is_displayed()
            time.sleep(2)
            # Comprobamos si está deseleccionado, si no > Se deselecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optInRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:  # Está deseleccionada
                logger.debug('Opción deactivada.')
            else:  # No está deseleccionada -> Se deselecciona
                logger.debug('Desactivamos la opción.')
                ElemValidar = settingsElements.optInRejSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optInRejSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I deactivate the option incoming delivery rejected >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @when("I deactivate the option departure delivery rejected")
    def deactivate_departure_delivery_rejected(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I deactivate the option departure delivery rejected')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optDeRejSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDeRejSettingXPath).is_displayed()
            # Comprobamos si está deseleccionado, si no > Se deselecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optDeRejSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:  # Está deseleccionada
                logger.debug('Opción deactivada.')
            else:  # No está seleccionada -> Se deselecciona
                logger.debug('Desativamos la opción.')
                ElemValidar = settingsElements.optDeRejSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optDeRejSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I deactivate the option departure delivery rejected >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep
    @when("I deactivate the option low stock")
    def deactivate_low_stock(self):
        pagina_settings = self.driver
        logger.debug('INICIO STEP: I deactivate the option low stock')
        time.sleep(2)
        try:
            # Validamos que la opción está visible
            ElemValidar = ('Elemento no activo: ', settingsElements.optLowStoSettingXPath)
            pagina_settings.find_element(by=By.XPATH, value=settingsElements.optLowStoSettingXPath).is_displayed()
            # Comprobamos si está deseleccionado, si no > Se deselecciona
            toogle_switch = pagina_settings.find_element(by=By.XPATH,
                                                         value=settingsElements.optLowStoSettingInputClassXPath)
            switch_valor = toogle_switch.get_attribute("class")
            logger.debug('El valor del input_class es : {}'.format(switch_valor))
            if 'ng-empty' in switch_valor:  # Está deseleccionada
                logger.debug('Opción desactivada.')
            else:  # No está deseleccionada -> Se deselecciona
                logger.debug('Desactivamos la opción.')
                ElemValidar = settingsElements.optLowStoSettingXPath
                pagina_settings.find_element(by=By.XPATH, value=settingsElements.optLowStoSettingXPath).click()
            # Recargamos la página
            pagina_settings.find_element(by=By.ID, value=homeElements.logoID).click()
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I deactivate the option low stock >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep