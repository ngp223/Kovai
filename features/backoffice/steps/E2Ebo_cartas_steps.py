from behave import then
import time

@then("accedo a cartas")
def step(context):
    context.cartas_page.open_cartas()

@then("creo una nueva carta")
def step(context):
    context.carta_name = f"carta_{int(time.time())}"
    context.cartas_page.create(context.carta_name)

@then("la carta aparece en el listado")
def step(context):
    assert context.cartas_page.exists_item(context.carta_name)

@then('cambio al restaurante "{restaurante}"')
def step(context, restaurante):
    context.cartas_page.change_restaurant(restaurante)

@then("asigno la carta creada como carta maestra")
def step(context):
    context.cartas_page.assign_master_card(context.carta_name)

@then("la carta queda asignada")
def step(context):
    context.cartas_page.verify_assigned(context.carta_name)

@then("cierro la ventana de asignar carta")
def step(context):
    context.cartas_page.close_assign_modal()

@then("la carta aparece marcada por defecto")
def step(context):
    context.cartas_page.verify_default_card(context.carta_name)


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
    
@then("escaneo la carta con IA")
def step_scan_card(context):
    context.cartas_page.open_scan_card()
    context.cartas_page.upload_card_image(r"C:\Users\Nerea QA\Desktop\foto_menu_ej.jpg")
    context.cartas_page.scan_card()