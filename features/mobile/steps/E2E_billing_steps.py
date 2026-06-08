from behave import when, then
from features.mobile.pages.E2E_billing_page import BillingPage


@when("accedo al módulo de facturación")
def step_impl(context):

    context.billing_page = BillingPage(context.driver)
    context.billing_page.open_billing()


@when("creo una nueva factura con datos válidos")
def step_impl(context):

    context.billing_page.create_new_invoice()


@then("la factura se crea correctamente")
def step_impl(context):

    pass


@then("veo la factura en el listado de facturas")
def step_impl(context):

    pass