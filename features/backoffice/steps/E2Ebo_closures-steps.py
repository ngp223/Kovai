from behave import then
from features.backoffice.pages.E2Ebo_closures_page import ClosuresPage_bo


@then("accedo a cierres")
def step_open_closures(context):
    context.closures_page = ClosuresPage_bo(context.driver)
    context.closures_page.open_closures()


@then("cambio al restaurante Tamus Rooftop Sevilla")
def step_change_restaurant(context):
    context.closures_page.select_restaurant("Tamus Rooftop Sevilla")


@then("filtro por Maître Alberto")
def step_filter_employee(context):
    context.closures_page.select_employee("Maître Alberto")


@then("veo el cierre del empleado")
def step_check_closure(context):
    assert context.closures_page.closure_exists("11/05/2026"), "❌ No aparece el cierre esperado"