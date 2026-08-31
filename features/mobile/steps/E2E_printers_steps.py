from behave import when, then
from features.mobile.pages.E2E_printers_page import PrintersPage

@when("accedo a las impresoras")
def step_impl(context):
    context.printers = PrintersPage(context.driver)
    context.printers.acceder_impresoras()

@then("modifico campos")
def step_impl(context):
    context.printers.modificar_campos()
    context.printers.aplicar_cambios()

@then("los campos han sido modificados")
def step_impl(context):
    context.printers.comprobar_campos_modificados()

@then("los campos han sido restablecidos")
def step_impl(context):
    context.printers.restablecer_campos()
    context.printers.comprobar_campos_restablecidos()
