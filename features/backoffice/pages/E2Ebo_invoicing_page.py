from selenium.webdriver.common.by import By
from datetime import datetime
from features.backoffice.pages.base_page import BasePage


class InvoicingSeriesPage(BasePage):

    INVOICING_MENU = (
        By.XPATH,
        "//a[@href='/invoicing']"
    )

    SERIES_TAB = (
        By.XPATH,
        "//button[.//text()[contains(.,'Series')]]"
    )

    NEW_SERIES_BTN = (
        By.XPATH,
        "//button[contains(.,'+ Nueva Serie')]"
    )

    SERIE_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: FS']"
    )

    SERIE_PREFIX_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: FS-2026-']"
    )

    CREATE_BTN = (
        By.XPATH,
        "//button[@type='submit' and contains(.,'Crear')]"
    )

    def open_invoicing(self):
        self.click(self.INVOICING_MENU)

    def open_series(self):
        self.click(self.SERIES_TAB)

    def create_series(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        name = f"SerieQA{timestamp}"
        prefix = f"SerieQA-{timestamp}-"

        self.click(self.NEW_SERIES_BTN)

        self.fill(self.SERIE_NAME_INPUT, name)
        self.fill(self.SERIE_PREFIX_INPUT, prefix)

        #self.click(self.CREATE_BTN)
        # Se queda comentada la creación hasta que se pueda eliminar.

        return name, prefix