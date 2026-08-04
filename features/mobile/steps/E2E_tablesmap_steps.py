from behave import when, then
from features.mobile.pages.E2E_tablesmap_page import TablesMapPage


@when("accedo a las mesas")
def step_impl(context):
    context.tablemap = TablesMapPage(context.driver)
    context.tablemap.open_tablemap()


@then("creo tarifa")
def step_impl(context):
    context.tablemap.crear_tarifa()


@then("creo zona")
def step_impl(context):
    context.tablemap.crear_zona()


@then("borro la zona")
def step_impl(context):
    context.tablemap.borrar_zona()


@then("borro la tarifa")
def step_impl(context):
    context.tablemap.borrar_tarifa()
