from behave import when, then
from features.mobile.pages.E2E_menus_page import MenusPage


@when("accedo al módulo de menús")
def step_impl(context):
    context.menus_page = MenusPage(context.driver)
    context.menus_page.open_menus()


@when("creo un menú con datos válidos")
def step_impl(context):
    context.menus_page.create_menu()


@then("el menú se crea correctamente")
def step_impl(context):
    assert context.menus_page.nombre_menu_creado is not None


@then("borro el menú creado")
def step_impl(context):
    context.menus_page.delete_menu()


@then("el menú se elimina correctamente")
def step_impl(context):
    context.menus_page.open_menus()
    assert not context.menus_page.menu_exists()

