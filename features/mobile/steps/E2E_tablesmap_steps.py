from behave import when,then
from features.mobile.pages.E2E_tablesmap_page import TablesMapPage


@when("accedo a las mesas")
def step_impl(context):
    context.tablemap = TablesMapPage(context.driver)
    context.tablemap.open_tablemap()

@then("creo tarifa")
def step_creo_tarifa(context):
    TablesMapPage(context.driver).crear_tarifa()


