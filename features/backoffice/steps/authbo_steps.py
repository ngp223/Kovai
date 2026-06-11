from behave import given
from features.backoffice.pages.login_bo_page import LoginPage_bo


@given('la web está abierta')
def step_open_bo(context):
    context.driver.get("https://kovai.hi-iberia.es/login")


@given('el usuario "{user}" está logueado')
def step_login_background(context, user):

    page = LoginPage_bo(context.driver)
    page.login_bo(user, "admin123")