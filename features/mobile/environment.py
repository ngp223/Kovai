from appium import webdriver
from appium.options.android import UiAutomator2Options


def before_all(context):

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.udid = "HA2ATXGT"

    options.app_package = "com.svacasv.kovapos"
    options.app_activity = "com.svacasv.kovapos.MainActivity"

    options.no_reset = True
    options.full_reset = False

    context.driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )


def after_all(context):

    if context.driver:
        context.driver.quit()