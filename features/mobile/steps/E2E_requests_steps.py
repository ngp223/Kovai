from behave import when, then
from features.mobile.pages.E2E_requests_page import RequestsPage

@when("accedo a peticiones")
def step_impl(context):
    context.requests_page = RequestsPage(context.driver)
    context.requests_page.acceder_peticiones()

@then("creo petición")
def step_impl(context):
    context.requests_page.crear_peticion()

@then("verifico la creación de la petición")
def step_impl(context):
    context.requests_page.comprobar_peticion_creada()

@then("modifico petición")
def step_impl(context):
    context.requests_page.modificar_peticion()

@then("verifico petición modificada")
def step_impl(context):
    context.requests_page.comprobar_peticion_modificada()
