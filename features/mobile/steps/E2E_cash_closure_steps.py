from behave import when, then
from features.mobile.pages.cash_closure_page import CashClosurePage


@when("accedo al cierre de caja")
def step_impl(context):
    context.cash = CashClosurePage(context.driver)
    context.cash.open_cash_closure()


@when("abro normal declarado")
def step_impl(context):
    context.cash.open_declared_section()


@when("copio el esperado primero")
def step_impl(context):
    context.cash.copy_expected_first()


@when("copio el esperado segundo")
def step_impl(context):
    context.cash.copy_expected_second()


@when("hago scroll hasta finalizar cierre")
def step_impl(context):
    context.cash.scroll_to_finalize()


@then("realizo el cierre de caja")
def step_impl(context):
    context.cash.finalize_closure()
