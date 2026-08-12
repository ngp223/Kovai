from behave import when, then
from features.mobile.pages.E2E_tablesmap_page import TablesMapPage

@when("accedo a las mesas")
def step_impl(context):
    context.tablemap=TablesMapPage(context.driver)
    context.tablemap.open_tablesmap()

@then("creo tarifa")
def step_impl(context):
    context.tablemap.crear_tarifa()

@then("creo zona")
def step_impl(context):
    context.tablemap.crear_zona()

@then("selecciono la zona")
def step_impl(context):
    context.tablemap.seleccionar_zona_creada()

@then("creo la mesa")
def step_impl(context):
    context.tablemap.crear_mesa()

@then("la mesa se muestra en el mapa")
def step_impl(context):
    context.tablemap.esperar_mesa_creada()

@then("muevo la mesa creada")
def step_impl(context):
    context.tablemap.mover_mesa_creada()

@then("borro la mesa creada")
def step_impl(context):
    context.tablemap.borrar_mesa()

@then("borro la zona")
def step_impl(context):
    context.tablemap.borrar_zona()

@then("borro la tarifa")
def step_impl(context):
    context.tablemap.borrar_tarifa()
