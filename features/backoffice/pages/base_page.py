from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    WebDriverException
)
from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def exists(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def click(self, locator, timeout=15, retry=3, js_fallback=True):
        last_exception = None
        for attempt in range(retry):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                self._safe_scroll_into_view(element)
                element.click()
                return

            except (
                StaleElementReferenceException,
                ElementClickInterceptedException,
                WebDriverException
            ) as e:
                last_exception = e
                self._wait_short(0.3 * (attempt + 1))
                if js_fallback:
                    try:
                        element = self.driver.find_element(*locator)
                        self.driver.execute_script(
                            "arguments[0].click();",
                            element
                        )
                        return
                    except Exception:
                        pass
        raise TimeoutException(
            f"[BasePage] No se pudo clicar el elemento: {locator}"
        ) from last_exception

    def fill(self, locator, value, timeout=15, clear=True):

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        self._safe_scroll_into_view(element)

        if clear:
            element.clear()
        element.send_keys(str(value))

    def wait_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_present(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_invisible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def _safe_scroll_into_view(self, element):
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )
        except Exception:
            pass

    def _wait_short(self, seconds):
        time.sleep(seconds)

    def delete_by_name(
        self,
        name,
        confirm_button_locator,
        row_xpath=None
    ):
        if row_xpath:
            row_locator = (By.XPATH, row_xpath.format(name=name))
        else:
            row_locator = (
                By.XPATH,
                f"//*[contains(normalize-space(),'{name}')]/ancestor::tr[1]"
            )

        row_element = self.wait_present(row_locator)
        delete_button = row_element.find_element(
            By.XPATH,
            ".//button[contains(@title,'Eliminar') or .//*[name()='svg']]"
        )
        self._safe_scroll_into_view(delete_button)
        try:
            delete_button.click()
        except Exception:
            self.driver.execute_script(
                "arguments[0].click();",
                delete_button
            )
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(confirm_button_locator)
        )
        confirm_button.click()