import logging.handlers
import time
import unittest
from selenium.webdriver.common.by import By
from behave import given, when, then, step
from pageobjects import HomeUser, Notificaciones

homeElements = HomeUser.HomeUser()
notificElements = Notificaciones.Notificaciones()

logger = logging.getLogger('WebLogs')


class NotifUser(unittest.TestCase):
    @step('I click on alerts notifications')
    def click_on_alerts_notifications(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I click on alerts notifications')
        try:
            logger.debug('Desplegamos el drop de Notificaciones')
            ElemValidar = homeElements.userNotID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userNotID).click()
            logger.debug('Pinchamos en alertas')
            ElemValidar = homeElements.userNotAlertXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAlertXPath).click()
            time.sleep(2)
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on alerts notifications>> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step('I click on events notifications')
    def click_on_events_notifications(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I click on events notifications')
        try:
            logger.debug('Desplegamos el drop de Notificaciones')
            ElemValidar = homeElements.userNotID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userNotID).click()
            time.sleep(2)
            logger.debug('Pinchamos en eventos')
            ElemValidar = homeElements.userNotEvenXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotEvenXPath).click()
            time.sleep(2)
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on events notifications>> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step('I click on notices notifications')
    def click_on_notices_notifications(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I click on notices notifications')
        try:
            logger.debug('Desplegamos el drop de Notificaciones')
            ElemValidar = homeElements.userNotID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userNotID).click()
            time.sleep(2)
            logger.debug('Pinchamos en avisos')
            ElemValidar = homeElements.userNotAviXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAviXPath).click()
            time.sleep(2)
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on notices notifications >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step('I click on all notifications')
    def click_on_all_notifications(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I click on all notifications')
        try:
            logger.debug('Desplegamos el drop de Notificaciones')
            ElemValidar = homeElements.userNotID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userNotID).click()
            time.sleep(2)
            logger.debug ('Pinchamos en Ver Todas >>> # No deja hacer click para ver todas')
            ElemValidar = homeElements.userNotAllXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAllXPath).click()
            time.sleep(2)
            resStep = True
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I click on all notifications >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep

    @step('I see the notifications board')
    def see_notifications_board(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I see the notifications board')
        try:
            # Panel de notificaciones
            ElemValidar = notificElements.panelTablaID
            pagina_homeUser.find_element(by=By.ID, value=notificElements.panelTablaID).is_displayed()
            # Buscar
            ElemValidar = notificElements.panelBuscarXPath
            pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelBoxBuscarXPath).is_displayed()
            ElemValidar = notificElements.panelBuscarTXT
            buscarNotific = pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelBuscarXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + buscarNotific + ' > ' + str(
                    ElemValidar == buscarNotific))
            resStep = (ElemValidar == buscarNotific)
            # Indicativo de notificaciones mostradas  >>> REVISAR COMO SACAR EL CONTEO CUANDO ES > 0
            ElemValidar = notificElements.panelConteoXPath
            pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelConteoXPath).is_displayed()
            ElemValidar = notificElements.panelConteoTXT
            conteoNotif = pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelConteoXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + conteoNotif + ' > ' + str(
                    ElemValidar == conteoNotif))
            resStep = (ElemValidar == conteoNotif) & resStep
            # Columna Fecha
            ElemValidar = notificElements.panelFechaXPath
            pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelFechaXPath).is_displayed()
            ElemValidar = notificElements.panelFechaTXT
            fechaNotif = pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelFechaXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + fechaNotif + ' > ' + str(
                    ElemValidar == fechaNotif))
            resStep = (ElemValidar == fechaNotif) & resStep
            # Columna Mensaje
            ElemValidar = notificElements.panelMsajeXPath
            pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelMsajeXPath).is_displayed()
            ElemValidar = notificElements.panelMsajeTXT
            msajeNotif = pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelMsajeXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + msajeNotif + ' > ' + str(
                    ElemValidar == msajeNotif))
            resStep = (ElemValidar == msajeNotif) & resStep
            # Columna Tipo
            ElemValidar = notificElements.panelTipoXPath
            pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelTipoXPath).is_displayed()
            ElemValidar = notificElements.panelTipoTXT
            tipoNotif = pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelTipoXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + tipoNotif + ' > ' + str(
                    ElemValidar == tipoNotif))
            resStep = (ElemValidar == tipoNotif) & resStep
            # Columna Acciones
            ElemValidar = notificElements.panelAccionesXPath
            pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelAccionesXPath).is_displayed()
            ElemValidar = notificElements.panelAccionesTXT
            accionesNotif = pagina_homeUser.find_element(by=By.XPATH, value=notificElements.panelAccionesXPath).text
            logger.warning(
                'Texto a validar: ' + ElemValidar + ' validado con: ' + accionesNotif + ' > ' + str(
                    ElemValidar == accionesNotif))
            resStep = (ElemValidar == accionesNotif) & resStep
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I see the notifications board >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep