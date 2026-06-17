import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    download_dir = os.path.join(os.getcwd(), "downloads")

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    options.add_experimental_option("prefs", prefs)

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    context.driver.implicitly_wait(10)

    context.download_dir = download_dir

    # debug ON/OFF
    context.debug_mode = True


def after_scenario(context, scenario):

    if scenario.status == "failed":

        screenshots_dir = os.path.join(os.getcwd(), "screenshots")

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        file_path = os.path.join(
            screenshots_dir,
            f"{scenario.name}.png"
        )

        context.driver.save_screenshot(file_path)

        print(f"📸 Screenshot guardado: {file_path}")

    if hasattr(context, "driver"):
        context.driver.quit()