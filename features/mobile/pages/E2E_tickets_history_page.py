from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from features.utils.tickets_store import load_ticket
import time
import re

class TicketsHistoryPage:
    HISTORIAL_TICKETS = (AppiumBy.XPATH, '//android.widget.TextView[@text="Historial de Tickets"]')

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(by, locator))
        element.click()

    def open_tickets_history(self):
        self.click(*self.HISTORIAL_TICKETS)

    def verify_tickets_history(self):
        saved_ticket = load_ticket()
        if saved_ticket:
            print(f"Buscando ticket guardado: {saved_ticket['date']} - {saved_ticket['amount']}")
            return self.find_ticket(saved_ticket["date"], saved_ticket["amount"])
        latest_date = self.get_latest_tickets_date(timeout=120)
        return latest_date is not None

    def get_latest_tickets_date(self, timeout=120):
        end_time = time.time() + timeout
        latest_date = None
        while time.time() < end_time:
            try:
                source = self.driver.page_source
                for match_es in re.findall(r'\d{2}/\d{2}/\d{4}', source):
                    try:
                        dt = datetime.strptime(match_es, "%d/%m/%Y")
                        if not latest_date or dt > latest_date:
                            latest_date = dt
                    except Exception:
                        pass
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
        return expected_date in source and expected_amount in source
