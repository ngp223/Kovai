from selenium.webdriver.common.by import By
from features.backoffice.pages.base_page import BasePage


class TaxConfigPage(BasePage):

    TAX_CONFIG_MENU = (By.XPATH,"//a[@href='/tax-config']")
    PAGE_TITLE = (By.XPATH,"//span[contains(.,'Configuración Fiscal')]")

    def open_tax_config(self):
        self.click(self.TAX_CONFIG_MENU)

    def is_page_displayed(self):
        element = self.wait_visible(self.PAGE_TITLE)
        return element.is_displayed()