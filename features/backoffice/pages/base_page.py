from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, WebDriverException
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=15, retry=3, js_fallback=True):
        last = None
        for i in range(retry):
            try:
                el = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                el.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException, WebDriverException) as e:
                last = e
                time.sleep(0.3 * (i + 1))
                if js_fallback:
                    try:
                        el = self.driver.find_element(*locator)
                        self.driver.execute_script("arguments[0].click();", el)
                        return
                    except:
                        pass
        raise TimeoutException(f"click failed {locator}") from last

    def fill(self, locator, value, timeout=15, clear=True):
        el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        if clear:
            el.clear()
        el.send_keys(str(value))

    def wait_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def exists(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False