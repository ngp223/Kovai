from behave import when, then
from features.mobile.pages.E2E_tickets_history_page import TicketsHistoryPage
from features.utils.tickets_store import load_ticket


@when("accedo al historial de tickets")
def step_impl(context):

    context.tickets_history = TicketsHistoryPage(context.driver)
    context.tickets_history.open_tickets_history()


@then("veo el historial de tickets")
def step_impl(context):

    saved_ticket = load_ticket()

    if saved_ticket:

        print(
            f" Buscando ticket guardado: "
            f"{saved_ticket['date']} - {saved_ticket['amount']}"
        )

        found = context.tickets_history.find_ticket(
            saved_ticket["date"],
            saved_ticket["amount"]
        )

        assert found, (
            f" No encontrado ticket "
            f"{saved_ticket['date']} - {saved_ticket['amount']}"
        )

    else:

        latest_date = context.tickets_history.get_latest_tickets_date(timeout=120)

        assert latest_date is not None, \
            " No se encontró ningún ticket en el historial"

        context.latest_ticket_date = latest_date