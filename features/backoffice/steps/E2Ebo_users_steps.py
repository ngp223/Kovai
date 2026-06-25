from behave import then
from datetime import datetime
from random import choice
from features.backoffice.pages.E2Ebo_categories_page import CategoriesPage_bo

@then("accedo a categorías")
def step_open_categories(context):
    context.categories_page = CategoriesPage_bo(context.driver)
    context.categories_page.open_categories()

@then("creo una nueva categoría")
def step_create_category(context):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    tipo_categoria = choice(["Ensalada","Carne","Pescado","Pasta"])
    context.category_name = f"Categoría QA {tipo_categoria} {timestamp}"
    context.categories_page.create_category(context.category_name)

@then("la categoría aparece en el listado")
def step_check_category(context):
    context.categories_page.wait_category_in_list(context.category_name)

@then("elimino la categoría")
def step_delete_category(context):
    context.categories_page.delete_category(context.category_name)

@then("la categoría no aparece en el listado")
def step_category_not_present(context):
    context.categories_page.wait_category_gone(context.category_name)