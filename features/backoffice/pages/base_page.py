from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException
)
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=15):
        last_exception = None

        for _ in range(3):
            try:
                element = WebDriverWait(
                    self.driver,
                    timeout
                ).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                return
            except StaleElementReferenceException as e:
                last_exception = e

        raise TimeoutException(
            f"No se pudo clicar el elemento: {locator}"
        ) from last_exception

    def fill(self, locator, value, timeout=15):
        element = WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(str(value))

    def wait_visible(self, locator, timeout=15):
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def scroll_down(self, pixels=800):
        self.driver.execute_script(
            f"window.scrollBy(0,{pixels});"
        )

    def visual_pause(self, seconds=2):
        time.sleep(seconds)

    def exists(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False