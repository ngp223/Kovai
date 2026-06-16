from selenium.webdriver.common.by import By

from features.backoffice.pages.base_page import BasePage


class CategoriesPage_bo(BasePage):

    CATEGORIES_MENU = (
        By.XPATH,
        "//a[@href='/categories']"
    )

    NEW_CATEGORY_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Nueva Categoría')]"
    )

    CATEGORY_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Ej: Bebidas']"
    )

    CREATE_BTN = (
        By.XPATH,
        "//button[@type='submit' and contains(normalize-space(),'Crear')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open_categories(self):

        self.wait_visible(self.CATEGORIES_MENU)

        self.click(self.CATEGORIES_MENU)

    def create_category(self, category_name):

        self.click(self.NEW_CATEGORY_BTN)

        self.fill(
            self.CATEGORY_NAME_INPUT,
            category_name
        )

        self.click(self.CREATE_BTN)