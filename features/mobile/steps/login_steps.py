from behave import given, when, then
from mobile.pages.login_page import LoginPage
from mobile.pages.restaurant_page import RestaurantPage
from mobile.data.users import USERS
from mobile.data.restaurants import RESTAURANTS


@given("la app está abierta")
def step_impl(context):
    assert context.driver is not None


# -----------------------------
# LOGIN
# -----------------------------
@when('hago login con usuario "{user}"')
def step_impl(context, user):

    credentials = USERS[user]

    login = LoginPage(context.driver)

    login.enter_email(credentials["email"])
    login.enter_password(credentials["password"])
    login.click_activate_terminal()


# -----------------------------
# RESTAURANTE
# -----------------------------
@when('selecciono el restaurante "{restaurant_key}"')
def step_impl(context, restaurant_key):

    restaurant_name = RESTAURANTS[restaurant_key]

    restaurant_page = RestaurantPage(context.driver)
    restaurant_page.select_restaurant(restaurant_name)


# -----------------------------
# ASSERT
# -----------------------------
@then("entro en la app")
def step_impl(context):
    assert context.driver is not None