import sys
import os
import re
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../..")
)

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


APP_PACKAGE = "com.svacasv.kovapos"


def before_all(context):

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.udid = "HA2ATXGT"

    options.app_package = APP_PACKAGE
    options.app_activity = "com.svacasv.kovapos.MainActivity"

    # Mantiene datos entre escenarios
    # El login y limpieza de sesión lo controla cada test
    options.no_reset = True
    options.full_reset = False

    context.driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )


def before_scenario(context, scenario):

    if not hasattr(context, "driver") or context.driver is None:
        return

    try:
        context.driver.activate_app(APP_PACKAGE)
        print(
            f"[BEFORE_SCENARIO] App abierta: {scenario.name}"
        )

    except Exception as e:
        print("[BEFORE_SCENARIO ERROR]", e)


def after_step(context, step):

    if step.status == "failed":

        screenshots_dir = "screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        clean_name = re.sub(
            r'[^A-Za-z0-9_]',
            '_',
            step.name
        )

        path = os.path.join(
            screenshots_dir,
            f"{clean_name}_{timestamp}.png"
        )

        try:
            context.driver.save_screenshot(path)
            print(
                f"[SCREENSHOT] Guardada: {path}"
            )

        except Exception as e:
            print(
                "[SCREENSHOT ERROR]",
                e
            )


def after_scenario(context, scenario):

    if not hasattr(context, "driver") or context.driver is None:
        return

    try:

        context.driver.terminate_app(APP_PACKAGE)

        print(
            f"[AFTER_SCENARIO] App cerrada: {scenario.name}"
        )

    except Exception as e:
        print(
            "[AFTER_SCENARIO ERROR]",
            e
        )


def after_all(context):

    if hasattr(context, "driver") and context.driver:

        try:
            context.driver.quit()
            print("[AFTER_ALL] Driver cerrado")

        except Exception as e:
            print(
                "[AFTER_ALL ERROR]",
                e
            )
