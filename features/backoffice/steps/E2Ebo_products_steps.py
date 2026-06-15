from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

from features.backoffice.pages.E2Ebo_products_page import ProductsPage_bo


@then("accedo a productos")
def step_open_products(context):

    context.products_page = ProductsPage_bo(context.driver)
    context.products_page.open_products()


@then("creo un nuevo producto")
def step_create_product(context):

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    context.product_name = f"Nuevo producto QA {timestamp}"

    context.products_page.create_product(
        context.product_name
    )


@then("el producto aparece en el listado")
def step_check_product(context):

    product_locator = (
        By.XPATH,
        f"//*[contains(text(),'{context.product_name}')]"
    )

    element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(product_locator)
    )

    assert element.is_displayed(), (
        f"No se encontró el producto {context.product_name}"
    )