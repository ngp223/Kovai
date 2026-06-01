import sys
import os
import re
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if root_path not in sys.path:
    sys.path.insert(0, root_path)

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

    print("STEP:", step.name, "STATUS:", step.status)

    if step.status == "failed":

        screenshots_dir = "screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # limpiar nombre del step
        clean_name = re.sub(
            r'[^A-Za-z0-9_]',
            '_',
            step.name
        )

        screenshot_name = f"{clean_name}_{timestamp}.png"

        path = os.path.join(screenshots_dir, screenshot_name)

        if context.driver:
            context.driver.save_screenshot(path)
            print(f"\n📸 Screenshot guardado: {path}")

def after_all(context):

    if context.driver:
        context.driver.quit()
        