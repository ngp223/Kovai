from behave import then
import time

@then("accedo a menus")
def step(context):
    context.menus_page.open_menus()

@then("creo un nuevo menu")
def step(context):
    name = f"menu_{int(time.time())}"
    context.menu_name = name
    context.menus_page.create(name)

@then("el menu aparece en el listado")
def step(context):
    assert context.menus_page.exists_item(context.menu_name)

@then("borro el menu creado")
def step(context):
    context.menus_page.delete_menu(context.menu_name)

@then("el menu no aparece en el listado")
def step(context):
    context.menus_page.wait_item_gone(context.menu_name)