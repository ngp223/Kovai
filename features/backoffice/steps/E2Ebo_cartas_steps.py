from behave import then
import time

@then("accedo a cartas")
def step(context):
    context.cartas_page.open_cartas()

@then("creo una nueva carta")
def step(context):
    name = f"carta_{int(time.time())}"
    context.carta_name = name
    context.cartas_page.create(name)

@then("la carta aparece en el listado")
def step(context):
    assert context.cartas_page.exists_item(context.carta_name)

@then("edito la carta creada")
def step(context):
    context.cartas_page.edit_carta(context.carta_name)

@then('modifico la descripción de la carta con "{texto}" y la fecha')
def step(context, texto):
    context.cartas_page.modify_description(f"{texto} {time.strftime('%d/%m/%Y')}")

@then("guardo los cambios de la carta")
def step(context):
    context.cartas_page.save_changes()

@then("confirmo la modificación de la carta")
def step(context):
    context.cartas_page.confirm_changes()

@then("borro la carta creada")
def step(context):
    context.cartas_page.delete_carta(context.carta_name)

@then("la carta no aparece en el listado")
def step(context):
    context.cartas_page.wait_item_gone(context.carta_name)