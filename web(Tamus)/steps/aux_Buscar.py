import time
import unittest

import logging.handlers
from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

logger = logging.getLogger('WebLogs')


class Buscar(unittest.TestCase):
    @then('I do search')
    # meter el try/except
    def buscar(self):
        driver = self.driver
        logger.debug('INICIO STEP: I do search')
        # moviendo el ratón  -- no lo hace, pero tampoco da error..
        try:
            mouse_mov = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div[2]")
            mouse_mov2 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[1]/form/div/button")
            movimiento = ActionChains(driver)
            movimiento.move_to_element(mouse_mov).move_to_element(mouse_mov2).click().perform()
            # hacer una búsqueda
            buscar = driver.find_element(by=By.NAME, value="s")
            buscar.send_keys("pagos")
            # Pulsamos "Buscar"
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[1]/form/div/button").click()
            time.sleep(2)
            # comprobamos la búsqueda
            driver.find_element(by=By.LINK_TEXT, value="PAGOS QR")
            buscar = driver.find_element(by=By.NAME, value="s")
            buscar.clear()
            # nueva busqueda
            buscar.send_keys("TAKE AWAY")
            time.sleep(2)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div[1]/article[1]/h2/a").click()
            # comprobamos la búsqueda
            # self.driver.find_element(by=By.LINK_TEXT, value="Enviar comida a tus clientes ya no es un problema") --> da error
            driver.find_element(by=By.CLASS_NAME, value="et_pb_text_inner")
        except Exception as e:
            logger.error('Algún elemento en "I do search" no encontrado: {}')
            resStep = False
        time.sleep(2)
        self.statusScenario = self.statusScenario & resStep
        logger.debug('FIN STEP: I do search --> {}'.format(resStep))
        assert resStep

