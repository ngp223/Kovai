from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from features.backoffice.pages.base_page import BasePage


class DevicesPage_bo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    DEVICES_MENU = ( By.XPATH,"//a[@href='/devices']")
    RESTAURANT_SELECT = (By.CSS_SELECTOR,"select._filterSelect_1qr2a_136")

    def open_devices(self):
        self.wait_visible(self.DEVICES_MENU)
        self.click(self.DEVICES_MENU)

    def select_restaurant(self, restaurant_name):
        select_element = self.wait_visible( self.RESTAURANT_SELECT)
        select = Select(select_element)
        if restaurant_name == "Todos los restaurantes":
            select.select_by_value("")
        else:
            select.select_by_visible_text(restaurant_name)

    def device_exists(self, device_id):
        locator = (By.XPATH,f"//*[contains(text(),'{device_id}')]")
        return self.exists(locator,timeout=10)