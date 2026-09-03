from behave import given
from features.mobile.pages.login_page import LoginPage

@given("la app está abierta")
def step_impl(context):
    assert context.driver is not None
    context.login_page = LoginPage(context.driver)

@given('el usuario "{user}" está logueado en el POS')
def step_impl(context, user):
    context.login_page.login(user)
