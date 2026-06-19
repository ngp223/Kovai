from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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


@then("borro el menu creado")
def step_delete_menu(context):
    context.menus_page.delete_menu(context.menu_name)


@then("el menu no aparece en el listado")
def step_check_deleted(context):

    locator = (By.XPATH, f"//*[contains(text(),'{context.menu_name}')]")

    WebDriverWait(context.driver, 10).until(
        lambda d: len(d.find_elements(*locator)) == 0
    )

    assert len(context.driver.find_elements(*locator)) == 0