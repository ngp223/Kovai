from behave import then
from datetime import datetime
from random import choice
from selenium.webdriver.common.by import By
from features.backoffice.pages.E2Ebo_modifiers_page import ModifiersPage_bo


@then("accedo a modificadores")
def step_open_modifiers(context):
    context.modifiers_page = ModifiersPage_bo(context.driver)
    context.modifiers_page.open_modifiers()


@then("creo un nuevo grupo de modificadores")
def step_create_modifier_group(context):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    descripcion = choice(["Chuletón","Chuleta","Solomillo"])
    context.group_name = f"Grupo QA {descripcion} {timestamp}"
    context.modifiers_page.create_modifier_group(context.group_name)


@then("el grupo de modificadores aparece en el listado")
def step_check_modifier_group(context):
    assert context.modifiers_page.exists_item(context.group_name)


@then("elimino el grupo de modificadores")
def step_delete_modifier_group(context):
    context.modifiers_page.delete_modifier_group(context.group_name)


@then("el grupo de modificadores no aparece en el listado")
def step_check_deleted_modifier_group(context):
    context.modifiers_page.wait_item_gone(context.group_name)