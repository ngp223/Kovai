from behave import when, then
from features.mobile.pages.E2E_promotions_page import PromotionsPage


@when('accedo a las promociones')
def step_impl(context):
    context.promotions = PromotionsPage(context.driver)
    context.promotions.acceder_promociones()

@then('creo una promoción')
def step_impl(context):
    context.promotions.crear_promocion()

@then('la promoción aparece listado')
def step_impl(context):
    context.promotions.esperar_promocion_creada()

@then('modifico la promoción')
def step_impl(context):
    context.promotions.modificar_promocion()

@then('la promoción modificada aparece listado')
def step_impl(context):
    context.promotions.comprobar_promocion_modificada()

@then('elimino la promoción')
def step_impl(context):
    context.promotions.eliminar_promocion()
