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


class HomeUser(unittest.TestCase):
    @step('I see the Home user page')
    def see_home_user_page(self):
        pagina_homeUser = self.driver
        logger.debug('INICIO STEP: I see the Home user page')
        try:
            ElemValidar = homeElements.url
            url = pagina_homeUser.current_url
            logger.warning('Texto a validar: ' + homeElements.url + ' validado con: ' + url + ' > ' + str(
                homeElements.url == url))
            resStep = (homeElements.url == url)
            logger.debug('Resultado resStep es : {}'.format(resStep))
            ElemValidar = homeElements.title
            title = pagina_homeUser.title
            logger.warning('Texto a validar: ' + homeElements.title + ' validado con: ' + title + ' > ' + str(
                homeElements.title == title))
            resStep = (homeElements.title == title) & resStep
            logger.debug('Resultado resStep es : {}'.format(resStep))
            # Footer Gestión - Elementos
            ElemValidar = homeElements.gestResXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestResXPath).is_displayed()
            ElemValidar = homeElements.gestAlmXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestAlmXPath).is_displayed()
            ElemValidar = homeElements.gestVenXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestVenXPath).is_displayed()
            ElemValidar = homeElements.gestFacXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestFacXPath).is_displayed()
            ElemValidar = homeElements.gestUsuXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestUsuXPath).is_displayed()
            # Footer Gestión - TXT Elementos
            ElemValidar = homeElements.gestResTXT
            gestionRestaurantes = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestResXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.gestResTXT + ' validado con: ' + gestionRestaurantes + ' > ' + str(
                    homeElements.gestResTXT == gestionRestaurantes))
            resStep = (homeElements.gestResTXT == gestionRestaurantes) & resStep
            ElemValidar = homeElements.gestAlmTXT
            gestionAlmacen = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestAlmXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.gestAlmTXT + ' validado con: ' + gestionAlmacen + ' > ' + str(
                    homeElements.gestAlmTXT == gestionAlmacen))
            resStep = (homeElements.gestAlmTXT == gestionAlmacen) & resStep

            ElemValidar = homeElements.gestVenTXT
            gestionVentas = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestVenXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.gestVenTXT + ' validado con: ' + gestionVentas + ' > ' + str(
                    homeElements.gestVenTXT == gestionVentas))
            resStep = (homeElements.gestVenTXT == gestionVentas) & resStep
            ElemValidar = homeElements.gestFacTXT
            gestionFacturas = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestFacXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.gestFacTXT + ' validado con: ' + gestionFacturas + ' > ' + str(
                    homeElements.gestFacTXT == gestionFacturas))
            resStep = (homeElements.gestFacTXT == gestionFacturas) & resStep
            ElemValidar = homeElements.gestUsuTXT
            gestionUsuarios = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.gestUsuXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.gestUsuTXT + ' validado con: ' + gestionUsuarios + ' > ' + str(
                    homeElements.gestUsuTXT == gestionUsuarios))
            resStep = (homeElements.gestUsuTXT == gestionUsuarios) & resStep


            # Footer Usuarios - Elementos & TXT
            ElemValidar = homeElements.userEyeXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userEyeXPath).is_displayed()
            ElemValidar = homeElements.userNotXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotXPath).is_displayed()
            ElemValidar = homeElements.userSubUserNameTXT
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).is_displayed()
            ElemValidar = homeElements.userSubUserNameTXT
            SubUsuarios = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.userSubUserNameTXT + ' validado con: ' + SubUsuarios + ' > ' + str(
                    homeElements.userSubUserNameTXT == SubUsuarios)) ## QA Tamus
            resStep = (homeElements.userSubUserNameTXT == SubUsuarios) & resStep
            ElemValidar = homeElements.userSubImgUserXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubImgUserXPath).is_displayed()
            ElemValidar = homeElements.userSubDropXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubDropXPath).is_displayed()
            # Footer user - Notificaciones - Elementos
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotXPath).click()
            time.sleep(3)
            ElemValidar = homeElements.userNotListID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userNotListID).is_displayed()
            ElemValidar = homeElements.userNotAlertXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAlertXPath).is_displayed()
            ElemValidar = homeElements.userNotImgEvenXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotImgEvenXPath).is_displayed()
            ElemValidar = homeElements.userNotImgAviXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotImgAviXPath).is_displayed()
            ElemValidar = homeElements.userNotEvenXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotEvenXPath).is_displayed()
            ElemValidar = homeElements.userNotImgAviXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotImgAviXPath).is_displayed()
            ElemValidar = homeElements.userNotAviXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAviXPath).is_displayed()
            ElemValidar = homeElements.userNotAllXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAllXPath).is_displayed()
            # Footer user - Notificaciones - TXT
            ElemValidar = homeElements.userNotAlertTXT
            UserNotiAlertas = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAlertXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.userNotAlertTXT + ' validado con: ' + UserNotiAlertas + ' > ' + str(
                    homeElements.userNotAlertTXT == UserNotiAlertas))
            resStep = (homeElements.userNotAlertTXT == UserNotiAlertas) & resStep
            ElemValidar = homeElements.userNotEvenTXT
            UserNotiEventos = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotEvenXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.userNotEvenTXT + ' validado con: ' + UserNotiEventos + ' > ' + str(
                    homeElements.userNotEvenTXT == UserNotiEventos))
            resStep = (homeElements.userNotEvenTXT == UserNotiEventos) & resStep
            ElemValidar = homeElements.userNotAviTXT
            UserNotiAvisos = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAviXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.userNotAviTXT + ' validado con: ' + UserNotiAvisos + ' > ' + str(
                    homeElements.userNotAviTXT == UserNotiAvisos))
            resStep = (homeElements.userNotAviTXT == UserNotiAvisos) & resStep
            ElemValidar = homeElements.userNotAllTXT
            UserNotiAll = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotAllXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.userNotAllTXT + ' validado con: ' + UserNotiAll + ' > ' + str(
                    homeElements.userNotAllTXT == UserNotiAll))
            resStep = (homeElements.userNotAllTXT == UserNotiAll) & resStep
            # Cerramos el desplegable
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userNotXPath).click()
            # Footer user - User top
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubUserNameXPath).click()
            ElemValidar = homeElements.userSubAjuID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubAjuID).is_displayed()
            ElemValidar = homeElements.userSubImgAjuXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubImgAjuXPath).is_displayed()
            ElemValidar = homeElements.userSubCPssID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubCPssID).is_displayed()
            ElemValidar = homeElements.userSubImgPssXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubImgPssXPath).is_displayed()
            ElemValidar = homeElements.userSubClosID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubClosID).is_displayed()
            ElemValidar = homeElements.userSubImgClosXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.userSubImgClosXPath).is_displayed()
            ElemValidar = homeElements.userSubAjuTXT
            userSubAju = pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubAjuID).text
            logger.warning(
                'Texto a validar: ' + homeElements.userSubAjuTXT + ' validado con: ' + userSubAju + ' > ' + str(
                    homeElements.userSubAjuTXT == userSubAju))
            resStep = (homeElements.userSubAjuTXT == userSubAju) & resStep
            ElemValidar = homeElements.userSubCPssTXT
            userSubCPss = pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubCPssID).text
            logger.warning(
                'Texto a validar: ' + homeElements.userSubCPssTXT + ' validado con: ' + userSubCPss + ' > ' + str(
                    homeElements.userSubCPssTXT == userSubCPss))
            resStep = (homeElements.userSubCPssTXT == userSubCPss) & resStep
            ElemValidar = homeElements.userSubClosTXT
            userSubClos = pagina_homeUser.find_element(by=By.ID, value=homeElements.userSubClosID).text
            logger.warning(
                'Texto a validar: ' + homeElements.userSubClosTXT + ' validado con: ' + userSubClos + ' > ' + str(
                    homeElements.userSubClosTXT == userSubClos))
            resStep = (homeElements.userSubClosTXT == userSubClos) & resStep
            # Habilitar - Deshabilitar Menu Lateral
            ElemValidar = homeElements.imgXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.imgXPath).is_displayed()
            ElemValidar = homeElements.menuLatID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.menuLatID).is_displayed()
            # Menu Lateral
            ElemValidar = homeElements.menuGlobXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.menuGlobXPath).is_displayed()
            ElemValidar = homeElements.submenuGlobID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuGlobID).is_displayed()
            ElemValidar = homeElements.submenuNotXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuNotXPath).is_displayed()
            ElemValidar = homeElements.menuGlobTXT
            menuGlob = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.menuGlobXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.menuGlobTXT + ' validado con: ' + menuGlob + ' > ' + str(
                    homeElements.menuGlobTXT == menuGlob))
            resStep = (homeElements.menuGlobTXT == menuGlob) & resStep
            ElemValidar = homeElements.submenuNotTXT
            submenuNot = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuNotXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuNotTXT + ' validado con: ' + submenuNot + ' > ' + str(
                    homeElements.submenuNotTXT == submenuNot))
            resStep = (homeElements.submenuNotTXT == submenuNot) & resStep
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.menuGlobXPath).click()
            ElemValidar = homeElements.submenuGlobTXT
            submenuGlob = pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuGlobID).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuGlobTXT + ' validado con: ' + submenuGlob + ' > ' + str(
                    homeElements.submenuGlobTXT == submenuGlob))
            resStep = (homeElements.submenuGlobTXT == submenuGlob) & resStep
            # Menu Lateral - Listado de restaurantes - según usuario
            ElemValidar = homeElements.submenuLatXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuLatXPath).is_displayed()
            ElemValidar = homeElements.submenuLatRestID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuLatRestID).is_displayed()
            ElemValidar = homeElements.submenuLatTXT
            submenuLat = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuLatXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuLatTXT + ' validado con: ' + submenuLat + ' > ' + str(
                    homeElements.submenuLatTXT == submenuLat))
            resStep = (homeElements.submenuLatTXT == submenuLat) & resStep
            # Restaurantes por usuario -- Al menos hay uno
            ElemValidar = homeElements.submenuLatRest1XPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuLatRest1XPath).is_displayed()
            # Menu Lateral - Listado de obradores - según usuario
            ElemValidar = homeElements.submenuObradXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuObradXPath).is_displayed()
            ElemValidar = homeElements.submenuObrID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuObrID).is_displayed()
            ElemValidar = homeElements.submenuObradTXT
            submenuObrad = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuObradXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuObradTXT + ' validado con: ' + submenuObrad + ' > ' + str(
                    homeElements.submenuObradTXT == submenuObrad))
            resStep = (homeElements.submenuObradTXT == submenuObrad) & resStep
            # Obradores por usuario -- Al menos hay uno
            ElemValidar = homeElements.submenuObr1XPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuObr1XPath).is_displayed()

            # Menu Lateral - Listado de papizza
            ElemValidar = homeElements.submenuPZZXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuPZZXPath).is_displayed()
            ElemValidar = homeElements.submenuPZZID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuPZZID).is_displayed()
            ElemValidar = homeElements.submenuPZZTXT
            submenuPZZ = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuPZZXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuPZZTXT + ' validado con: ' + submenuPZZ + ' > ' + str(
                    homeElements.submenuPZZTXT == submenuPZZ))
            resStep = (homeElements.submenuPZZTXT == submenuPZZ) & resStep

            # Papizza por usuario -- Al menos hay uno
            ElemValidar = homeElements.submenuPZZ1XPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuPZZ1XPath).is_displayed()
            # Menu Lateral - Listado de SantaGloria
            ElemValidar = homeElements.submenuSTGXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuSTGXPath).is_displayed()
            ElemValidar = homeElements.submenuSTGID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuSTGID).is_displayed()
            ElemValidar = homeElements.submenuSTGTXT
            submenuSTG = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuSTGXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuSTGTXT + ' validado con: ' + submenuSTG + ' > ' + str(
                    homeElements.submenuSTGTXT == submenuSTG))
            resStep = (homeElements.submenuSTGTXT == submenuSTG) & resStep
            # SantaGloria por usuario -- Al menos hay uno
            ElemValidar = homeElements.submenuSTG1XPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuSTG1XPath).is_displayed()

            # Menu Lateral - Listado de Vezzo
            ElemValidar = homeElements.submenuVEZXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuVEZXPath).is_displayed()
            ElemValidar = homeElements.submenuVEZID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuVEZID).is_displayed()
            ElemValidar = homeElements.submenuVEZTXT
            submenuVEZ = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuVEZXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuVEZTXT + ' validado con: ' + submenuVEZ + ' > ' + str(
                    homeElements.submenuVEZTXT == submenuVEZ))
            resStep = (homeElements.submenuVEZTXT == submenuVEZ) & resStep
            # Vezzo por usuario -- Al menos hay uno
            ElemValidar = homeElements.submenuVEZ1XPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuVEZ1XPath).is_displayed()

            # Menu Lateral - Listado de Volapié
            ElemValidar = homeElements.submenuVLPXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuVLPXPath).is_displayed()
            ElemValidar = homeElements.submenuVLPID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuVLPID).is_displayed()
            ElemValidar = homeElements.submenuVLPTXT
            submenuVLP = pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuVLPXPath).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuVLPTXT + ' validado con: ' + submenuVLP + ' > ' + str(
                    homeElements.submenuVLPTXT == submenuVLP))
            resStep = (homeElements.submenuVLPTXT == submenuVLP) & resStep
            # Volapié por usuario -- Al menos hay uno
            ElemValidar = homeElements.submenuVLP1XPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuVLP1XPath).is_displayed()

            # Menu Lateral - Franquicias
            ElemValidar = homeElements.submenuFranqID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuFranqID).is_displayed()
            ElemValidar = homeElements.submenuFranqTXT
            submenuFranq = pagina_homeUser.find_element(by=By.ID, value=homeElements.submenuFranqID).text
            logger.warning(
                'Texto a validar: ' + homeElements.submenuFranqTXT + ' validado con: ' + submenuFranq + ' > ' + str(
                    homeElements.submenuFranqTXT == submenuFranq))
            resStep = (homeElements.submenuFranqTXT == submenuFranq) & resStep
            ElemValidar = homeElements.submenuOcuFranqXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuOcuFranqXPath).is_displayed()
            ElemValidar = homeElements.submenuMosFranqXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuMosFranqXPath).is_displayed()
            ElemValidar = homeElements.submenuSolFranqXPath
            pagina_homeUser.find_element(by=By.XPATH, value=homeElements.submenuSolFranqXPath).is_displayed()
            # Panel principal
            ElemValidar = homeElements.panelPpalID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.panelPpalID).is_displayed()
            ElemValidar = homeElements.panelPpaltitleID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.panelPpaltitleID).is_displayed()
            ElemValidar = homeElements.panelPpalMarkID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.panelPpalMarkID).is_displayed()
            ElemValidar = homeElements.panelPpalContID
            pagina_homeUser.find_element(by=By.ID, value=homeElements.panelPpalContID).is_displayed()
        except Exception as e:
            logger.error("Elemento no encontrado: {}. Error: {}".format(ElemValidar, e))
            resStep = False
        logger.debug('FIN STEP: I visit the main page in web >> {}'.format(resStep))
        self.statusScenario = self.statusScenario & resStep
        assert resStep
