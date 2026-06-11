from behave import given, when, then
from selenium.webdriver.common.by import By
from features.backoffice.pages.login_bo_page import LoginPage_bo
from features.backoffice.data.users import USERS

@when('hago login con credenciales válidas')
def step_login_admin(context):

    user = USERS["admin"]

    page = LoginPage_bo(context.driver)

    page.login_bo(
        user["email"],
        user["password"]
    )


@then("entro al panel de control")
def step_panel_de_control(context):

    title = context.driver.find_element(By.XPATH, "//h1")

    assert title.text == "Panel de Control"
    