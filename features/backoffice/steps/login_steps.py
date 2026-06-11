from behave import given, when, then
from features.backoffice.pages.login_bo_page import LoginPage_bo


@given("que abro el login")
def step_open_bo(context):
    context.login_page = LoginPage_bo(context.driver)
    context.login_page.open_bo()


@when("hago login con credenciales válidas")
def step_login_bo(context):
    context.login_page.login_bo(
        "admin@demo-restaurante.com",
        "admin123"
    )


@then("entro al dashboard")
def step_dashboard_bo(context):
    assert context.login_page.is_logged_in_bo()
