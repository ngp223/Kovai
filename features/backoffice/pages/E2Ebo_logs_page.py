import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from features.backoffice.pages.base_page import BasePage


class LogsPage_bo(BasePage):

    LOGS_MENU = (By.XPATH,"//a[@href='/logs']")
    TITLE = (By.XPATH,"//h1[contains(normalize-space(),'Auditoría')]")
    RESTAURANT_SELECT = (By.XPATH,"//select[contains(@class,'_filterSelect_')]")
    NEXT_PAGE_BTN = (By.XPATH,"//button[contains(.,'Siguiente')]")
    ANY_LOG_ID = (By.XPATH,"//div[contains(text(),'ID:')]")

    def open_logs(self):
        self.click(self.LOGS_MENU)

    def is_logs_page(self):
        try:
            self.wait_visible(self.TITLE, timeout=10)
            return True
        except TimeoutException:
            return False

    def select_restaurant(self, restaurant_name):
        select_el = self.wait_visible(self.RESTAURANT_SELECT)
        Select(select_el).select_by_visible_text(restaurant_name)
        time.sleep(2)

    def go_next_page(self):
        self.click(self.NEXT_PAGE_BTN)
        time.sleep(2)

    def log_id_is_displayed(self):
        try:
            self.wait_visible(self.ANY_LOG_ID, timeout=10)
            return True
        except TimeoutException:
            return False