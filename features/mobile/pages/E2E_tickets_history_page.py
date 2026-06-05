from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time
import re


class TicketsHistoryPage:

    HISTORIAL_TICKETS = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Historial de Tickets"]'
    )

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(by, locator)
        )
        element.click()

    def open_tickets_history(self):
        self.click(*self.HISTORIAL_TICKETS)

    def get_latest_tickets_date(self, timeout=120):

        end_time = time.time() + timeout
        latest_date = None

        while time.time() < end_time:

            try:
                # 🔥 Más estable: evitar WebElements (evita StaleElementReferenceException)
                source = self.driver.page_source

                # Formato ES: 04/06/2026
                for match_es in re.findall(r'\d{2}/\d{2}/\d{4}', source):
                    try:
                        dt = datetime.strptime(match_es, "%d/%m/%Y")
                        if not latest_date or dt > latest_date:
                            latest_date = dt
                    except Exception:
                        pass

                # Formato EN: Jun 5, 2026 (sin hora)
                for match_en in re.findall(r'[A-Za-z]{3} \d{1,2}, \d{4}', source):
                    try:
                        dt = datetime.strptime(match_en, "%b %d, %Y")
                        if not latest_date or dt > latest_date:
                            latest_date = dt
                    except Exception:
                        pass

            except Exception:
                pass

            if latest_date:
                return latest_date.strftime("%d/%m/%Y")

            time.sleep(2)

        return None

    def find_ticket(self, expected_date, expected_amount):

        source = self.driver.page_source

        return (
            expected_date in source
            and expected_amount in source
        )