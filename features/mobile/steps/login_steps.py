from behave import given, when, then

from mobile.pages.login_page import LoginPage
from mobile.data.users import USERS
from mobile.data.restaurants import RESTAURANTS


# -----------------------------
# APP ABIERTA
@given("la app está abierta")
def step_impl(context):
    assert context.driver is not None


# -----------------------------
# LOGIN
@when('hago login con usuario "{user}"')
def step_impl(context, user):

    login = LoginPage(context.driver)

    credentials = USERS[user]

    login.enter_email(credentials["email"])
    login.enter_password(credentials["password"])
    login.click_activate_terminal()


# -----------------------------
# RESTAURANTE
@when('selecciono el restaurante "{restaurant_key}"')
def step_impl(context, restaurant_key):

    login = LoginPage(context.driver)

    restaurant_name = RESTAURANTS[restaurant_key]

    login.select_restaurant(restaurant_name)


# -----------------------------
# USUARIO ADMIN
@when('selecciono el usuario "{role}"')
def step_impl(context, role):

    login = LoginPage(context.driver)

    if role.lower() == "administrador":
        login.select_user_admin()
    else:
        raise ValueError(f"Rol no soportado: {role}")


# -----------------------------
# PIN
@when("introduzco el PIN de acceso")
def step_impl(context):

    login = LoginPage(context.driver)

    login.enter_pin("1234")
    login.click_access()


# -----------------------------
# ENTRADA APP
@when("entro en la app")
def step_impl(context):

    login = LoginPage(context.driver)

    # espera carga mesas
    login.wait_tables_loaded()


# -----------------------------
# ventas
@when("veo ventas")
def step_impl(context):

    login = LoginPage(context.driver)

    login.see_ventas()


# -----------------------------
# MESA B1
@when("selecciono la mesa B1")
def step_impl(context):

    login = LoginPage(context.driver)

    login.select_table_b1()


# -----------------------------
# COMENSALES
@when("selecciono 3 comensales")
def step_impl(context):

    login = LoginPage(context.driver)

    login.select_guests_3()

# -----------------------------
# PRODUCTO PAELLA
@then("selecciono el producto paella")
def step_impl(context):

    login = LoginPage(context.driver)

    login.select_product_paella()