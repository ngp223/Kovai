from behave import then
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.backoffice.pages.E2Ebo_cartas_page import CartasPage_bo


@then("accedo a cartas")
def step_open_cartas(context):
    context.cartas_page = CartasPage_bo(context.driver)
    context.cartas_page.open_cartas()


@then("creo una nueva carta")
def step_create_carta(context):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    context.carta_name = f"Carta QA {timestamp}"

    context.cartas_page.create_carta(context.carta_name)


@then("borro la carta creada")
def step_delete_carta(context):
    context.cartas_page.delete_carta(context.carta_name)


@then("la carta no aparece en el listado")
def step_check_deleted(context):

    locator = (By.XPATH, f"//*[contains(text(),'{context.carta_name}')]")

    WebDriverWait(context.driver, 15).until(
        EC.invisibility_of_element_located(locator)
    )