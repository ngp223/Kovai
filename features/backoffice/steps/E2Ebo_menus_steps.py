from behave import when, then
import time

@when("accedo a menus")
def step(context):
    context.menus_page.open_menus()

@when("creo un nuevo menu")
def step(context):
    name = f"menu_{int(time.time())}"
    context.menu_name = name
    context.menus_page.create(name)

@when("modifico el menu y añado platos")
def step(context):
    context.menus_page.modify_menu(context.menu_name)

@then("el menu aparece con 3 productos")
def step(context):
    assert context.menus_page.check_products(context.menu_name, 3), \
        f"El menú {context.menu_name} no tiene 3 productos"

@when("borro el menu creado")
def step(context):
    context.menus_page.delete_menu(context.menu_name)

@then("el menu no aparece en el listado")
def step(context):
    context.menus_page.wait_item_gone(context.menu_name)
