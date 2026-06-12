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

    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):

    if hasattr(context, "driver"):
        context.driver.quit()