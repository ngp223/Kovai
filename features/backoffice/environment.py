import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    context.driver.implicitly_wait(0)    # ❌ No implicit waits
    context.download_dir = download_dir
    context.debug_mode = True


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        file_path = os.path.join(screenshots_dir,f"{scenario.name}.png")
        context.driver.save_screenshot(file_path)
        print(f"📸 Screenshot guardado: {file_path}")
    context.driver.quit()