import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # ❌ Quitar implicit wait (mezclar waits es mala práctica)
    context.driver.implicitly_wait(0)

    context.debug_mode = True


def after_scenario(context, scenario):

    if scenario.status == "failed":

        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        file_path = os.path.join(
            screenshots_dir,
            f"{scenario.name}.png"
        )

        context.driver.save_screenshot(file_path)
        print(f"📸 Screenshot guardado: {file_path}")

    context.driver.quit()