from behave import then
from features.mobile.pages.E2E_modifiers_page import ModifiersPage

@then('accedo a los modificadores')
def step_impl(context):
    context.modifiers = ModifiersPage(context.driver)
    context.modifiers.acceder_modificadores()

@then('creo un modificador')
def step_impl(context):
    context.modifiers.crear_modificador()

@then('el modificador aparece listado')
def step_impl(context):
    context.modifiers.esperar_modificador_creado()

@then('modifico el modificador')
def step_impl(context):
    context.modifiers.modificar_modificador()

@then('el modificador modificado aparece listado')
def step_impl(context):
    context.modifiers.comprobar_modificador_modificado()

@then('elimino el modificador')
def step_impl(context):
    context.modifiers.eliminar_modificador()
