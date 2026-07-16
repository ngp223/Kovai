from behave import then
from features.backoffice.pages.E2Ebo_tables_page import TablesPage_bo

@then("accedo a mesas")
def step_open(context):
    context.tables_page=TablesPage_bo(context.driver)
    context.tables_page.open_tables()

@then("selecciono el restaurante Tamus Rooftop Sevilla")
def step_restaurant(context):
    context.tables_page.select_restaurant()

@then("creo una tarifa")
def step_rate(context):
    context.tables_page.create_rate()

@then("creo una zona")
def step_zone(context):
    context.tables_page.create_zone()

@then("selecciono la zona creada")
def step_zone_select(context):
    context.tables_page.select_created_zone()

@then("creo una mesa")
def step_table(context):
    context.tables_page.create_table()

@then("la mesa aparece en el mapa")
def step_table_check(context):
    context.tables_page.wait_table_created()

@then("muevo la mesa")
def step_move(context):
    context.tables_page.move_table()

@then("elimino la mesa")
def step_delete(context):
    context.tables_page.delete_table()

@then("la mesa no aparece en el mapa")
def step_deleted(context):
    context.tables_page.wait_table_deleted()

@then("elimino la tarifa")
def step_rate_delete(context):
    context.tables_page.delete_rate()

@then("elimino la zona")
def step_zone_delete(context):
    context.tables_page.delete_zone()