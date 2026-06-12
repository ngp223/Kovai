from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

from features.backoffice.pages.E2Ebo_products_page import ProductosPage_bo


@then("accedo a productos")
def step_open_productos(context):

    context.productos_page = ProductosPage_bo(context.driver)
    context.productos_page.open_productos()


@then("creo un nuevo producto")
def step_create_producto(context):

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    context.producto_name = f"Nuevo producto QA {timestamp}"

    context.productos_page.create_producto(
        context.producto_name
    )


@then("el producto aparece en el listado")
def step_check_producto(context):

    producto_locator = (
        By.XPATH,
        f"//*[contains(text(),'{context.producto_name}')]"
    )

    element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(producto_locator)
    )

    assert element.is_displayed(), (
        f"No se encontró el producto {context.producto_name}"
    )