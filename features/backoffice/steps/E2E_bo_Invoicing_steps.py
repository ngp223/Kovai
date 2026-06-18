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
    context.invoicing_page.create_series()