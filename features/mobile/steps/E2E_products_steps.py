from behave import then,when
from features.mobile.pages.E2E_products_page import ProductsPage

@when('accedo a los productos')
def step_impl(context):
    context.products = ProductsPage(context.driver)
    context.products.acceder_productos()

@then('creo un producto')
def step_impl(context):
    context.products.crear_producto()

@then('el producto aparece listado')
def step_impl(context):
    context.products.esperar_producto_creado()

@then('modifico ese producto')
def step_impl(context):
    context.products.modificar_producto()

@then('el producto modificado aparece listado')
def step_impl(context):
    context.products.comprobar_producto_modificado()

@then('elimino el producto')
def step_impl(context):
    context.products.eliminar_producto()
