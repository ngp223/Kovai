from datetime import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from features.backoffice.pages.base_page import BasePage


class TablesPage_bo(BasePage):

    TABLES_MENU = (By.XPATH, "//a[@href='/tables']")
    RESTAURANT_SELECT = (By.TAG_NAME, "select")

    NEW_RATE_BTN = (By.XPATH, "//button[contains(.,'+ Nueva Tarifa')]")
    RATE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Ej: Tarifa Terraza 10%']")
    CREATE_RATE_BTN = (By.XPATH, "//button[@type='submit' and contains(.,'Crear')]")

    NEW_ZONE_BTN = (By.XPATH, "//button[contains(.,'+ Nueva Zona')]")
    ZONE_NAME_INPUT = (By.XPATH, "//input[@type='text']")
    CREATE_ZONE_BTN = (By.XPATH, "//button[@type='submit' and contains(.,'Crear')]")
    ZONE_SELECT = (By.XPATH, "//select[contains(@class,'_filterSelect_')]")

    FIRST_TABLE_BTN = (
        By.XPATH,
        "//button[contains(normalize-space(),'Añadir primera mesa') or contains(normalize-space(),'Anadir primera mesa')]"
    )

    RECTANGULAR_BTN = (
        By.XPATH,
        "//button[contains(@title,'rectangular') or contains(.,'Rectangular')]"
    )

    TABLE = (
        By.XPATH,
        "//div[contains(@class,'_table_')][.//button[@title='Eliminar mesa']]"
    )

    DELETE_BTN = (
        By.XPATH,
        ".//button[@title='Eliminar mesa']"
    )

    CONTINUE_BTN = (
        By.XPATH,
        "//button[contains(.,'Continuar')]"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.current_table = None
        self.zone_name = None
        self.rate_name = None

    def open_tables(self):
        self.click(self.TABLES_MENU)
        time.sleep(2)

    def select_restaurant(self):
        Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    self.RESTAURANT_SELECT
                )
            )
        ).select_by_visible_text(
            "Tamus Rooftop Sevilla"
        )
        time.sleep(3)

    def create_rate(self):
        self.rate_name = f"TarifaQA_{datetime.now():%Y%m%d_%H%M%S}"

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.NEW_RATE_BTN
            )
        ).click()

        inp = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.RATE_NAME_INPUT
            )
        )

        inp.send_keys(self.rate_name)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.CREATE_RATE_BTN
            )
        ).click()

        time.sleep(3)

        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    self.CONTINUE_BTN
                )
            ).click()
        except TimeoutException:
            pass

        time.sleep(3)

    def create_zone(self):
        self.zone_name = f"ZonaQA_{datetime.now():%Y%m%d_%H%M%S}"

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.NEW_ZONE_BTN
            )
        ).click()

        inp = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.ZONE_NAME_INPUT
            )
        )

        inp.send_keys(self.zone_name)

        selects = self.driver.find_elements(
            By.TAG_NAME,
            "select"
        )

        for element in selects:
            try:
                select = Select(element)
                for option in select.options:
                    if self.rate_name in option.text:
                        select.select_by_visible_text(
                            option.text
                        )
                        break
            except:
                continue

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.CREATE_ZONE_BTN
            )
        ).click()

        time.sleep(4)

    def select_created_zone(self):
        Select(
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    self.ZONE_SELECT
                )
            )
        ).select_by_visible_text(
            self.zone_name
        )

        time.sleep(3)

    def create_table(self):
        before = len(
            self.driver.find_elements(*self.TABLE)
        )

        try:
            btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    self.FIRST_TABLE_BTN
                )
            )
        except TimeoutException:
            btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    self.RECTANGULAR_BTN
                )
            )

        self.driver.execute_script(
            "arguments[0].click();",
            btn
        )

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self.TABLE)) == before + 1
        )

        self.current_table = self.driver.find_elements(
            *self.TABLE
        )[-1]

        time.sleep(2)

    def wait_table_created(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(
                self.current_table
            )
        )

    def move_table(self):
        ActionChains(self.driver)\
            .move_to_element(self.current_table)\
            .click_and_hold()\
            .move_by_offset(-100, -80)\
            .release()\
            .perform()

        time.sleep(3)

    def delete_table(self):
        self.current_table.find_element(
            *self.DELETE_BTN
        ).click()

        time.sleep(2)

        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(.,'Eliminar')]"
                    )
                )
            ).click()
        except TimeoutException:
            pass

        time.sleep(3)

    def wait_table_deleted(self):
        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(
                self.current_table
            )
        )

    def delete_rate(self):
        rate = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//span[normalize-space()='{self.rate_name}']"
                )
            )
        )

        container = rate.find_element(
            By.XPATH,
            "./ancestor::div[.//button[@title='Eliminar']][1]"
        )

        delete_button = container.find_element(
            By.XPATH,
            ".//button[@title='Eliminar']"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

        confirm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class,'_confirmButton_') and normalize-space()='Eliminar']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            confirm
        )

        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(rate)
        )

    def delete_zone(self):
        zone = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//span[normalize-space()='{self.zone_name}']"
                )
            )
        )

        container = zone.find_element(
            By.XPATH,
            "./ancestor::div[.//button[@title='Eliminar']][1]"
        )

        delete_button = container.find_element(
            By.XPATH,
            ".//button[@title='Eliminar']"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

        confirm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class,'_confirmButton_') and normalize-space()='Eliminar']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            confirm
        )

        time.sleep(3)