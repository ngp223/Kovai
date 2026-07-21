from behave import then
from features.backoffice.pages.E2Ebo_products_page import ProductsPage_bo

@then("accedo a productos")
def step_open_products(context):
    context.products_page=ProductsPage_bo(context.driver)
    context.products_page.open_products()

@then("modifico el producto")
def step_edit_product(context):
    context.products_page.edit_product("Arroz con Bogavante","Arroz con Bogavantes")

@then("restablezco el producto")
def step_restore_product(context):
    context.products_page.edit_product("Arroz con Bogavantes","Arroz con Bogavante")