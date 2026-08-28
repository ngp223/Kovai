from behave import then,when
from features.mobile.pages.E2E_categories_page import CategoriesPage

@when('accedo a las categorías')
def step_impl(context):
    context.categories = CategoriesPage(context.driver)
    context.categories.acceder_categorias()

@then('creo una categoría')
def step_impl(context):
    context.categories.crear_categoria()

@then('creo el rol')
def step_impl(context):
    context.categories.crear_rol()

@then('la categoría aparece listada')
def step_impl(context):
    context.categories.esperar_categoria_creada()

@then('modifico la categoría creada')
def step_impl(context):
    context.categories.modificar_categoria()
    
@then('la categoría modificada aparece listada')
def step_impl(context):
    context.categories.comprobar_categoria_modificada()


@then('elimino esa categoría')
def step_impl(context):
    context.categories.eliminar_categoria()

@then('elimino el rol creado')
def step_impl(context):
    context.categories.eliminar_rol()


