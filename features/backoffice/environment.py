import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from features.backoffice.pages.E2Ebo_cartas_page import CartasPage_bo
from features.backoffice.pages.E2Ebo_menus_page import MenusPage_bo
from features.backoffice.pages.E2Ebo_promotions_page import PromotionsPage_bo


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # -----------------------------
    # DESCARGAS (CSV / FILES)
    # -----------------------------
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    # -----------------------------
    # DRIVER
    # -----------------------------
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # ❌ No implicit waits (usas explícitos correctamente)
    context.driver.implicitly_wait(0)

    # -----------------------------
    # CONTEXT GLOBAL
    # -----------------------------
    context.download_dir = download_dir
    context.debug_mode = True

    # -----------------------------
    # PAGE OBJECTS (NO TOCAR NOMBRES)
    # -----------------------------
    context.cartas_page = CartasPage_bo(context.driver)
    context.menus_page = MenusPage_bo(context.driver)
    context.promotions_page = PromotionsPage_bo(context.driver)


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        if scenario.status == "failed":
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_path = os.path.join(screenshots_dir, f"{scenario.name}.png")
            context.driver.save_screenshot(file_path)
            print(f"📸 Screenshot guardado: {file_path}")

        context.driver.quit()