from behave import given
from mobile.pages.E2E_reservation_pages import ReservationPage
from mobile.data.users import USERS
from mobile.data.restaurants import RESTAURANTS


@given("la app está abierta")
def step_impl(context):
    assert context.driver is not None
    context.login = ReservationPage(context.driver)


@given('el usuario "{user}" está logueado en el POS')
def step_impl(context, user):

    credentials = USERS[user]

    context.login.enter_email(credentials["email"])
    context.login.enter_password(credentials["password"])
    context.login.click_activate_terminal()

    restaurant_name = RESTAURANTS["tamusGV"]
    context.login.select_restaurant(restaurant_name)

    context.login.select_user_admin()

    context.login.enter_pin("1234")
    context.login.click_access()

    context.login.wait_tables_loaded()


@given("está en la pantalla de ventas")
def step_impl(context):
    context.login.see_ventas()