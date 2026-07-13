from behave import then
from datetime import datetime
from features.backoffice.pages.E2Ebo_support_page import SupportPage_bo

@then("accedo a soporte")
def step_open_support(context):
    context.support_page = SupportPage_bo(context.driver)
    context.support_page.open_support()

@then("creo una petición de soporte")
def step_create(context):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    context.support_title = f"Problema QA {timestamp}"
    context.support_description = f"Problema QA {timestamp}"
    context.support_page.create_support_ticket(context.support_title, context.support_description)

@then("la petición aparece en el listado")
def step_list(context):
    context.support_page.wait_ticket_in_list(context.support_title)

@then("cambio el estado a en proceso")
def step_modify(context):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    comment = f"Problema2 QA {timestamp}"
    context.support_page.modify_support_ticket(context.support_title, comment)