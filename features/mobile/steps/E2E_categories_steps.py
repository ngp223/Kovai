from behave import then
from features.mobile.pages.E2E_categories_page import CategoriesPage


@then('accedo a las categorías')
def step_impl(context):
    context.categories=CategoriesPage(context.driver)
    context.categories.acceder_categorias()


@then('creo una categoría')
def step_impl(context):
    context.categories.crear_categoria()


@then('la categoría aparece listada')
def step_impl(context):
    context.categories.esperar_categoria_creada()


@then('elimino esa categoría')
def step_impl(context):
    context.categories.eliminar_categoria()


@then('la categoría no aparece listada')
def step_impl(context):
    context.categories.comprobar_categoria_no_aparece()


@then('creo el rol')
def step_impl(context):
    context.categories.crear_rol()


@then('elimino el rol creado')
def step_impl(context):
    context.categories.eliminar_rol()


@then('el rol no aparece listado')
def step_impl(context):
    context.categories.comprobar_rol_no_aparece()

