from behave import when, then
from selenium.webdriver.common.by import By
from features.backoffice.pages.E2Ebo_cartas_page import CartasPage_bo
from features.backoffice.data.users import USERS
from features.backoffice.pages.login_bo_page import LoginPage_bo


@when("la web está abierta")
def step_open(context):
    context.driver.get("https://kovai.hi-iberia.es/login")


@when("el usuario está logueado")
def step_login(context):

    user = USERS["admin"]

    page = LoginPage_bo(context.driver)
    page.login_bo(user["email"], user["password"])


@then("accedo a cartas")
def step_open_cartas(context):

    context.cartas_page = CartasPage_bo(context.driver)
    context.cartas_page.open_cartas()


@then("creo una nueva carta")
def step_create_carta(context):

    context.carta_name = "Carta Ejemplo QA"

    context.cartas_page.create_carta(context.carta_name)


@then("la carta aparece en el listado")
def step_check_carta(context):

    element = context.driver.find_element(
        By.XPATH,
        f"//*[contains(text(),'{context.carta_name}')]"
    )

    assert element.is_displayed(), "La carta no aparece en el listado"