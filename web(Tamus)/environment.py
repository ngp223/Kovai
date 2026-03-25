import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from conf.LoadConfig import load_config, load_config_logging, load_data

logger = logging.getLogger('WebLogs')


def before_all(context):
    load_config(context)
    load_data(context)
    logger.warning('---- SETUP CONFIG ----')

    # Plataforma de ejecución: "web" o "app"
    context.platform = "app"  # Cambia a "web" para Selenium, "app" para Appium


def before_feature(context, feature):
    load_config_logging(context, feature)
    logger.info('---- SETUP CONFIG FEATURE ----')
    logger.info('INICIO FEATURE: {}'.format(str(feature)))


def after_feature(context, feature):
    logger.info('FIN FEATURE: {}'.format(str(feature)))


def before_scenario(context, scenario):
    context.statusScenario = False

    if context.platform == "web":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {
            "download.default_directory": 'C:\\Users\\ngome\\Downloads\\',
            "safebrowsing.enabled": True,
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        })
        try:
            context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            logger.debug('Última versión de Chrome instalada')
        except Exception:
            options_edge = EdgeOptions()
            options_edge.add_argument("--start-maximized")
            context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options_edge)
            logger.debug('Chrome no disponible, se usa Edge')

    elif context.platform == "app":
        from appium import webdriver as appium_webdriver
        from app.pageobjects_app import APP_PACKAGE, APP_ACTIVITY

        desired_caps = {
            "platformName": "Android",
            "platformVersion": "12",
            "deviceName": "MiTablet",
            "appPackage": APP_PACKAGE,
            "appActivity": APP_ACTIVITY,
            "automationName": "UiAutomator2"
        }

        context.driver = appium_webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        logger.debug('Driver Appium inicializado para Android')

    context.statusScenario = True
    logger.info('INICIO SCENARIO: {}'.format(str(scenario)))


def after_scenario(context, scenario):
    status = 'PASSED' if context.statusScenario else 'FAILED'
    logger.info('FIN SCENARIO: {} >> ESTADO: {}'.format(str(scenario), status))

    if hasattr(context, 'driver'):
        context.driver.quit()
        logger.warning('---- DRIVER CLOSED ----')