from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
from random import choice

from features.backoffice.pages.E2Ebo_modifiers_page import ModifiersPage_bo


@then("accedo a modificadores")
def step_open_modifiers(context):

    context.modifiers_page = ModifiersPage_bo(context.driver)
    context.modifiers_page.open_modifiers()


@then("creo un nuevo grupo de modificadores")
def step_create_modifier_group(context):

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    descripcion = choice([
        "Chuletón",
        "Chuleta",
        "Solomillo"
    ])

    context.group_name = (
        f"Grupo QA {descripcion} {timestamp}"
    )

    context.modifiers_page.create_modifier_group(
        context.group_name
    )


@then("el grupo de modificadores aparece en el listado")
def step_check_modifier_group(context):

    group_locator = (
        By.XPATH,
        f"//*[contains(text(),'{context.group_name}')]"
    )

    element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(group_locator)
    )

    assert element.is_displayed(), (
        f"No se encontró el grupo {context.group_name}"
    )