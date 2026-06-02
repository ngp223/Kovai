from behave import when, then

@when('selecciono la mesa "{table}"')
def step_impl(context, table):
    context.login.select_table_b1()

@when("selecciono comensales")
def step_impl(context):
    context.login.select_guests()
    context.login.click_accept_guests()

@when("selecciono el producto")
def step_impl(context):
    context.login.select_product_paella()

@when("añado el producto al pedido")
def step_impl(context):
    context.login.click_add_product()

@when("aumento la cantidad del producto")
def step_impl(context):
    context.login.increase_product()

@when("realizo el pago")
def step_impl(context):
    context.login.click_realizar_pago()

@when("confirmo el pago")
def step_impl(context):
    context.login.click_confirmar_pago()

@then("finalizo el pedido")
def step_impl(context):
    context.login.click_finalizar()
    