from behave import then
import time

@then("accedo a promociones")
def step(context):
    context.promotions_page.open_promotions()

@then("creo una nueva promoción")
def step(context):
    name = f"promo_{int(time.time())}"
    context.promotion_name = name
    context.promotions_page.create(name)

@then("la promoción aparece en el listado")
def step(context):
    assert context.promotions_page.exists_item(context.promotion_name)

@then("borro la promoción creada")
def step(context):
    context.promotions_page.delete_promotion(context.promotion_name)

@then("la promoción no aparece en el listado")
def step(context):
    context.promotions_page.wait_item_gone(context.promotion_name)