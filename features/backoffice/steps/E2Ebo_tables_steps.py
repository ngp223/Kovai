from behave import then
from features.backoffice.pages.E2Ebo_tables_page import TablesPage_bo


@then("accedo a mesas")
def step_open_tables(context):
    context.tables_page=TablesPage_bo(context.driver)
    context.tables_page.open_tables()


@then("selecciono el restaurante Tamus Rooftop Sevilla")
def step_select_restaurant(context):
    context.tables_page.select_restaurant()


@then("creo una mesa")
def step_create_table(context):
    context.tables_page.create_table()


@then("la mesa aparece en el mapa")
def step_check_table(context):
    context.tables_page.wait_table_created()


@then("elimino la mesa")
def step_delete_table(context):
    context.tables_page.delete_table()


@then("la mesa no aparece en el mapa")
def step_check_deleted(context):
    context.tables_page.wait_table_deleted()
    
    
@then("muevo la mesa")
def step_move_table(context):
    context.tables_page.move_table()