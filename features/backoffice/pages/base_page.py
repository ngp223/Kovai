from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=15):

        last_exception = None

        for _ in range(3):
            try:
                element = WebDriverWait(self.driver, timeout).until(
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

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(str(value))

    def wait_visible(self, locator, timeout=15):

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=15):

        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_invisible(self, locator, timeout=15):

        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def get_text(self, locator, timeout=15):

        return self.wait_visible(locator, timeout).text

    def scroll_down(self, pixels=600):

        self.driver.execute_script(
            f"window.scrollBy(0,{pixels});"
        )

    def scroll_to_element(self, locator, timeout=15):

        element = self.wait_visible(locator, timeout)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        return element