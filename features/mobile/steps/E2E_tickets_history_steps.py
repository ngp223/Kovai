from behave import when, then
from features.mobile.pages.E2E_tickets_history_page import TicketsHistoryPage
from features.utils.tickets_store import load_ticket

@when("accedo al historial de tickets")
def step_impl(context):
    context.tickets_history = TicketsHistoryPage(context.driver)
    context.tickets_history.open_tickets_history()

@then("veo el historial de tickets")
def step_impl(context):
    assert context.tickets_history.verify_tickets_history(), "No se encontró ningún ticket en el historial"

