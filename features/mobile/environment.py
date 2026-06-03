import sys
import os
import re
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options
from features.mobile.pages.logout_page import LogoutPage


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


def before_all(context):

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.udid = "HA2ATXGT"

    options.app_package = "com.svacasv.kovapos"
    options.app_activity = "com.svacasv.kovapos.MainActivity"

    options.no_reset = False
    options.full_reset = False

    context.driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    context.driver.implicitly_wait(10)


def after_step(context, step):

    if step.status == "failed":

        screenshots_dir = "screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        clean_name = re.sub(r'[^A-Za-z0-9_]', '_', step.name)

        path = os.path.join(
            screenshots_dir,
            f"{clean_name}_{timestamp}.png"
        )

        context.driver.save_screenshot(path)


def after_scenario(context, scenario):

    if not hasattr(context, "driver") or context.driver is None:
        return

    try:

        logout = LogoutPage(context.driver)

        try:
            logout.exit_pos_mode()
        except:
            pass

        logout.open_change_user()
        logout.go_back()
        logout.close_company_session()

    except Exception as e:
        print("[AFTER_SCENARIO ERROR]", e)


def after_all(context):
    if context.driver:
        context.driver.quit()