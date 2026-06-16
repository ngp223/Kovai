from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from features.backoffice.pages.E2Ebo_users_page import UsersPage_bo


@then("accedo a usuarios")
def step_open_users(context):
    context.users_page = UsersPage_bo(context.driver)
    context.users_page.open_users()


@then("creo un nuevo usuario")
def step_create_user(context):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    # Guardamos el rol seleccionado desde el Page Object
    context.selected_role = context.users_page.select_random_role()

    # Creamos el nombre del usuario correctamente formateado
    context.user_name = f"{context.selected_role}QA {timestamp}"

    # Creamos el usuario en la UI
    context.users_page.create_user(context.user_name)


@then("el usuario aparece en el listado")
def step_check_user(context):
    user_locator = (
        By.XPATH,
        f"//*[contains(text(),'{context.user_name}')]"
    )

    element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(user_locator)
    )

    assert element.is_displayed(), f"No se encontró el usuario {context.user_name}"