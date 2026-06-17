from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from features.backoffice.pages.base_page import BasePage


class ClosuresPage_bo(BasePage):

    # =========================
    # LOCATORS
    # =========================

    CLOSURES_MENU = (
        By.XPATH,
        "//a[@href='/closures']"
    )

    RESTAURANT_SELECT = (
        By.XPATH,
        "//select[option[contains(text(),'Tamus')]]"
    )

    EMPLOYEE_SELECT = (
        By.XPATH,
        "//select[contains(@class,'_filterSelect_')]"
    )

    TABLE_ROWS = (
        By.XPATH,
        "//tbody/tr"
    )

    ANY_CELL = (
        By.XPATH,
        "//tbody/tr/td[1]"
    )

    # =========================
    # WAITS
    # =========================

    def _wait_table_loaded(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.ANY_CELL)
        )

    def _wait_table_refresh(self, old_rows):
        WebDriverWait(self.driver, 20).until(
            lambda d: len(d.find_elements(*self.TABLE_ROWS)) != old_rows
        )

    # =========================
    # ACTIONS
    # =========================

    def open_closures(self):
        self.wait_visible(self.CLOSURES_MENU)
        self.click(self.CLOSURES_MENU)
        self._wait_table_loaded()

    def select_restaurant(self, restaurant_name):
        """
        Cambia el restaurante (select HTML nativo)
        """

        self._wait_table_loaded()
        old_rows = len(self.driver.find_elements(*self.TABLE_ROWS))

        select = Select(
            self.wait_visible(self.RESTAURANT_SELECT)
        )
        select.select_by_visible_text(restaurant_name)

        self._wait_table_refresh(old_rows)

    def select_employee(self, employee_name):
        """
        Filtra por empleado (dependiente del restaurante)
        """

        self._wait_table_loaded()
        old_rows = len(self.driver.find_elements(*self.TABLE_ROWS))

        select_el = self.wait_visible(self.EMPLOYEE_SELECT)
        select_el.click()

        option_locator = (
            By.XPATH,
            f"//option[contains(normalize-space(),'{employee_name}')]"
        )

        option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(option_locator)
        )
        option.click()

        self._wait_table_refresh(old_rows)

    def closure_exists(self, date_text):

        locator = (
            By.XPATH,
            f"//tbody/tr[td[contains(normalize-space(),'{date_text}')]]"
        )

        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False