from behave import then

@then("intento crear una carta sin nombre")
def step(context):
    context.cartas_page.create_without_name()

@then("aparece el mensaje de nombre obligatorio")
def step(context):
    context.cartas_page.verify_name_required_message()
