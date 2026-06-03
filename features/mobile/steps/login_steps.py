from behave import given

from features.mobile.pages.login_page import LoginPage
from features.mobile.pages.restaurant_page import RestaurantPage
from features.mobile.data.users import USERS
from features.mobile.data.restaurants import RESTAURANTS


@given("la app está abierta")
def step_impl(context):
    assert context.driver is not None

    context.login_page = LoginPage(context.driver)
    context.restaurant_page = RestaurantPage(context.driver)


@given('el usuario "{user}" está logueado en el POS')
def step_impl(context, user):

    credentials = USERS[user]

    lp = context.login_page
    rp = context.restaurant_page

    # LOGIN
    lp.enter_email(credentials["email"])
    lp.enter_password(credentials["password"])
    lp.click_activate_terminal()

    # RESTAURANTE
    restaurant_name = RESTAURANTS["tamusGV"]
    rp.select_restaurant(restaurant_name)

    # USUARIO ADMIN
    lp.select_user_admin()

    # PIN + ACCESO
    lp.enter_pin("1234")
    lp.click_access()

    # ESPERA TPV LISTO
    lp.wait_tables_loaded()


@given("está en la pantalla de ventas")
def step_impl(context):
    from features.mobile.pages.E2E_reservation_pages import ReservationPage

    context.reservation = ReservationPage(context.driver)