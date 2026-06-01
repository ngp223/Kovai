from behave import given, when, then
from mobile.pages.E2E_reservation_pages import ReservationPage
from mobile.data.users import USERS
from mobile.data.restaurants import RESTAURANTS

@given("la app está abierta")
def step_impl(context):
    assert context.driver is not None
    context.login = ReservationPage(context.driver)

@when('hago login con usuario "{user}"')
def step_impl(context, user):

    credentials = USERS[user]
    context.login.enter_email(credentials["email"])
    context.login.enter_password(credentials["password"])
    context.login.click_activate_terminal()

@when('selecciono el restaurante "{restaurant_key}"')
def step_impl(context, restaurant_key):

    restaurant_name = RESTAURANTS[restaurant_key]
    context.login.select_restaurant(restaurant_name)

@when('selecciono el usuario "{role}"')
def step_impl(context, role):

    if role.lower() == "administrador":
        context.login.select_user_admin()
    else:
        raise ValueError(f"Rol no soportado: {role}")

@when("introduzco el PIN de acceso")
def step_impl(context):

    context.login.enter_pin("1234")
    context.login.click_access()

@when("entro en la app")
def step_impl(context):
    context.login.wait_tables_loaded()

@when("veo ventas")
def step_impl(context):
    context.login.see_ventas()

@when('selecciono la mesa "{table}"')
def step_impl(context, table):
    context.login.select_table_b1()

@when("selecciono comensales")
def step_impl(context):
    context.login.select_guests()
    context.login.click_accept_guests()

@then("selecciono el producto")
def step_impl(context):
    context.login.select_product_paella()

@then("añado el producto al pedido")
def step_impl(context):
    context.login.click_add_product()

@then("aumento la cantidad del producto")
def step_impl(context):
    context.login.increase_product()

@then("realizo el pago")
def step_impl(context):
    context.login.click_realizar_pago()

@then("confirmo el pago")
def step_impl(context):
    context.login.click_confirmar_pago()

@then("finalizo el pedido")
def step_impl(context):
    context.login.click_finalizar()