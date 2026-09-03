from behave import when, then
from features.mobile.pages.E2E_settings_page import SettingsPage

@when("accedo a ajustes")
def step_impl(context):
    context.settings_page = SettingsPage(context.driver)
    context.settings_page.acceder_ajustes()

@then("cambio el idioma a ingles")
def step_impl(context):
    context.settings_page.cambiar_idioma()

@then("cambio el aspecto a oscuro")
def step_impl(context):
    context.settings_page.cambiar_aspecto()

@then("cambio el tamaño de texto a grande")
def step_impl(context):
    context.settings_page.cambiar_accesibilidad()

@then("verifico que el texto aumenta de tamaño")
def step_impl(context):
    context.settings_page.comprobar_tamano_texto()

@then("cierro sesión")
def step_impl(context):
    context.settings_page.cerrar_sesion()