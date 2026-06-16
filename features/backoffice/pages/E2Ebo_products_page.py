from selenium.webdriver.common.by import By

from features.backoffice.pages.base_page import BasePage


class ProductsPage_bo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PRODUCTS_MENU = (
        By.XPATH,
        "//*[@id='root']/div/div/aside/nav/a[4]"
    )

    NUEVO_PRODUCT_BTN = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/header/div[2]/button"
    )

    NOMBRE_INPUT = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/form/div[1]/div[2]/input"
    )

    CREAR_BTN = (
        By.XPATH,
        "//*[@id='root']/div/div/div/main/div/div[3]/div/form/div[2]/button[2]"
    )

    def open_products(self):
        self.click(self.PRODUCTS_MENU)

    def create_product(self, nombre):

        self.click(self.NUEVO_PRODUCT_BTN)

        self.fill(self.NOMBRE_INPUT, nombre)

        self.scroll_down(800)

        self.click(self.CREAR_BTN)