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

    # =========================================================
    # CLICK (ULTRA ROBUSTO)
    # =========================================================
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
                            "arguments[0].click();", element
                        )
                        return
                    except Exception:
                        pass

        raise TimeoutException(
            f"[BasePage] No se pudo clicar el elemento: {locator}"
        ) from last_exception

    # =========================================================
    # FILL (INPUTS ROBUSTOS)
    # =========================================================
    def fill(self, locator, value, timeout=15, clear=True):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        self._safe_scroll_into_view(element)

        if clear:
            element.clear()

        element.send_keys(str(value))

    # =========================================================
    # WAITS BÁSICOS
    # =========================================================
    def wait_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_present(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_invisible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    # =========================================================
    # STATE CHECK
    # =========================================================
    def exists(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    # =========================================================
    # SCROLL
    # =========================================================
    def scroll_down(self, pixels=800):
        self.driver.execute_script(
            f"window.scrollBy(0,{pixels});"
        )

    def scroll_to_element(self, locator, timeout=15):
        element = self.wait_present(locator, timeout)
        self._safe_scroll_into_view(element)
        return element

    def _safe_scroll_into_view(self, element):
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )
        except Exception:
            pass

    # =========================================================
    # SHORT WAIT (NO HARDCODED SLEEP)
    # =========================================================
    def _wait_short(self, seconds):
        time.sleep(seconds)