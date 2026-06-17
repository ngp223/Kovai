from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from features.backoffice.pages.base_page import BasePage


class SalesPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SALES_MENU = (
        By.XPATH,
        "//a[.//span[normalize-space()='Historial Ventas']]"
    )

    RESTAURANT_SELECT = (
        By.CSS_SELECTOR,
        "select"
    )

    EXPORT_CSV_BTN = (
        By.XPATH,
        "//button[contains(.,'Exportar CSV')]"
    )

    def open_sales(self):

        self.wait_visible(self.SALES_MENU)

        self.click(self.SALES_MENU)

    def select_restaurant(self, restaurant_name):

        select_element = self.wait_visible(
            self.RESTAURANT_SELECT
        )

        Select(select_element).select_by_visible_text(
            restaurant_name
        )

    def export_csv(self):

        self.click(self.EXPORT_CSV_BTN)