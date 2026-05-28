from behave import given, when, then
from features.backoffice.pages.login_page import LoginPage


@given("que abro el login")
def step_open(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when("hago login con credenciales válidas")
def step_login(context):
    context.login_page.login(
        "admin@demo-restaurante.com",
        "admin123"
    )


@then("entro al dashboard")
def step_dashboard(context):
    assert context.login_page.is_logged_in()