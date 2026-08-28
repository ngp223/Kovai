from behave import then,when
from features.mobile.pages.E2E_users_page import UsersPage

@when('accedo a usuariostab')
def step_impl(context):
    context.users=UsersPage(context.driver)
    context.users.acceder_usuarios()

@then('creo un nuevo usuariotab')
def step_impl(context):
    context.users.crear_usuario()
    #context.users.esperar_usuario_creado()

@then('elimino el usuariotab')
def step_impl(context):
    context.users.eliminar_usuario()

@then('el usuario no aparece en el listadotab')
def step_impl(context):
    context.users.comprobar_usuario_no_aparece()