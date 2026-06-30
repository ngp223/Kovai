from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.backoffice.pages.base_page import BasePage
import time


class TablesPage_bo(BasePage):

    TABLES_MENU = (By.XPATH, "//a[@href='/tables']")
    RESTAURANT_SELECT = (By.TAG_NAME, "select")

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

    def __init__(self, driver):
        super().__init__(driver)
        self.current_table = None

    # ---------------- NAV ----------------

    def open_tables(self):
        self.wait_visible(self.TABLES_MENU)
        self.click(self.TABLES_MENU)

    def select_restaurant(self):
        select = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RESTAURANT_SELECT)
        )
        Select(select).select_by_visible_text("Tamus Rooftop Sevilla")
        time.sleep(2)

    # ---------------- CREATE ----------------

    def create_table(self):

        tables_before = len(self.driver.find_elements(*self.TABLE))

        try:
            btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.FIRST_TABLE_BTN)
            )
        except TimeoutException:
            btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.RECTANGULAR_BTN)
            )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        time.sleep(0.5)

        self.driver.execute_script(
            "arguments[0].click();",
            btn
        )

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self.TABLE)) == tables_before + 1
        )

        self.current_table = self.driver.find_elements(*self.TABLE)[-1]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            self.current_table
        )

        time.sleep(1)

    # ---------------- MOVE ----------------

    def move_table(self):

        table = self.current_table

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            table
        )

        time.sleep(0.5)

        ActionChains(self.driver) \
            .move_to_element(table) \
            .click_and_hold() \
            .move_by_offset(-100, -80) \
            .pause(1) \
            .release() \
            .perform()

        time.sleep(2)

        # 🔥 re-captura la última mesa (la movida sigue siendo la última)
        self.current_table = self.driver.find_elements(*self.TABLE)[-1]

    # ---------------- DELETE ----------------

    def delete_table(self):

        table = self.current_table

        delete_btn = table.find_element(*self.DELETE_BTN)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete_btn
        )

        time.sleep(0.5)

        self.driver.execute_script(
            "arguments[0].click();",
            delete_btn
        )

        time.sleep(1)

        try:
            confirm = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(.,'Confirmar') or contains(.,'Eliminar')]")
                )
            )
            self.driver.execute_script("arguments[0].click();", confirm)
        except TimeoutException:
            pass

    # ---------------- WAIT ----------------

    def wait_table_created(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.current_table)
        )

    def wait_table_deleted(self):
        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(self.current_table)
        )