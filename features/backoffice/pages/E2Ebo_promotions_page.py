from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from features.backoffice.pages.base_page import BasePage


class PromotionsPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PROMOTIONS_MENU = (
        By.XPATH,
        "//a[@href='/promotions']"
    )

    CREATE_FIRST_PROMOTION_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Crear primera promoción')]"
    )

    NEW_PROMOTION_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Nueva Promoción')]"
    )

    PROMOTION_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: 2x1 en Cervezas']"
    )

    CREATE_PROMOTION_BTN = (
        By.XPATH,
        "//button[@type='submit' and contains(.,'Crear Promoción')]"
    )

    def open_promotions(self):

        self.wait_visible(self.PROMOTIONS_MENU)

        self.click(self.PROMOTIONS_MENU)

    def open_create_promotion_form(self):

        try:

            self.click(
                self.CREATE_FIRST_PROMOTION_BTN,
                timeout=5
            )

        except TimeoutException:

            self.click(
                self.NEW_PROMOTION_BTN,
                timeout=10
            )

    def create_promotion(self, promotion_name):

        self.open_create_promotion_form()

        self.fill(
            self.PROMOTION_NAME_INPUT,
            promotion_name
        )

        self.click(
            self.CREATE_PROMOTION_BTN
        )