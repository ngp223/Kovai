from behave import then
from features.backoffice.pages.E2Ebo_logs_page import LogsPage_bo


@then("accedo a logs")
def step_open_logs(context):
    context.logs_page = LogsPage_bo(context.driver)
    context.logs_page.open_logs()


@then("estoy en la página de logs")
def step_check_logs_page(context):
    assert context.logs_page.is_logs_page(), (
        "❌ No estoy en la página de Logs"
    )


@then("filtro por el restaurante Sevilla")
def step_filter_sevilla(context):
    context.logs_page.select_restaurant(
        "Tamus Rooftop Sevilla"
    )


@then("voy a la siguiente página de logs")
def step_next_page(context):
    context.logs_page.go_next_page()


@then("se muestra un id de log")
def step_check_log_id(context):
    assert context.logs_page.log_id_is_displayed(), (
        "❌ No se muestra ningún ID de log"
    )