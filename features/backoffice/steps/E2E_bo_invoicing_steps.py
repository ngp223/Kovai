from behave import then
from features.backoffice.pages.E2Ebo_invoicing_page import InvoicingSeriesPage


@then("accedo a facturacion")
def step_open_invoicing(context):
    context.invoicing_page = InvoicingSeriesPage(context.driver)
    context.invoicing_page.open_invoicing()


@then("accedo a series")
def step_open_series(context):
    context.invoicing_page.open_series()


@then("creo una nueva serie")
def step_create_series(context):
    context.series_name = context.invoicing_page.create_series()


@then("la serie aparece en el listado")
def step_series_exists(context):
    context.invoicing_page.wait_series_in_list(context.series_name)


@then("elimino la serie")
def step_delete_series(context):
    context.invoicing_page.delete_series(context.series_name)


@then("la serie no aparece en el listado")
def step_series_not_exists(context):
    context.invoicing_page.wait_series_gone(context.series_name)