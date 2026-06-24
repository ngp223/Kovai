from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from features.backoffice.pages.E2Ebo_menus_page import MenusPage_bo


@then("accedo a menus")
def step_open_menus(context):
    context.menus_page = MenusPage_bo(context.driver)
    context.menus_page.open_menus()


@then("creo un nuevo menu")
def step_create_menu(context):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    context.menu_name = f"Menu QA {timestamp}"
    context.menus_page.create_menu(context.menu_name)


@then("el menu aparece en el listado")
def step_check(context):
    locator = (By.XPATH,f"//*[contains(normalize-space(),'{context.menu_name}')]")
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(locator))


@then("borro el menu creado")
def step_delete(context):
    context.menus_page.delete_menu(context.menu_name)


@then("el menu no aparece en el listado")
def step_check_deleted(context):
    locator = (By.XPATH, f"//*[contains(text(),'{context.menu_name}')]")
    WebDriverWait(context.driver, 15).until(EC.invisibility_of_element_located(locator))