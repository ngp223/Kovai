from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from features.backoffice.pages.E2Ebo_cartas_page import CartasPage_bo
from features.backoffice.data.users import USERS
from features.backoffice.pages.login_bo_page import LoginPage_bo


@then("accedo a cartas")
def step_open_cartas(context):
    context.cartas_page = CartasPage_bo(context.driver)
    context.cartas_page.open_cartas()


@then("creo una nueva carta")
def step_create_carta(context):
    timestamp = int(time.time())
    context.carta_name = f"Carta QA {timestamp}"

    context.cartas_page.create_carta(context.carta_name)


@then("la carta aparece en el listado")
def step_check_carta(context):

    carta_locator = (
        By.XPATH,
        f"//*[contains(text(),'{context.carta_name}')]"
    )

    element = WebDriverWait(context.driver, 15).until(
        EC.visibility_of_element_located(carta_locator)
    )

    assert element.is_displayed(), "La carta no aparece en el listado"