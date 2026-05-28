from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):

    options = webdriver.ChromeOptions()

    mobile_emulation = {
        "deviceMetrics": {
            "width": 820,
            "height": 1180,
            "pixelRatio": 2.0
        },
        "userAgent": (
            "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/14.0 Mobile/15A5341f Safari/604.1"
        )
    }

    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()