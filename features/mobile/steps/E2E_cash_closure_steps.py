from behave import when, then
from features.mobile.pages.E2E_cash_closure_page import CashClosurePage


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


# 🧠 FECHA (OBLIGATORIA)
@when("guardo la fecha del último cierre")
def step_impl(context):
    context.last_closure_date = context.cash.get_last_closure_date()
    print("🧠 Fecha cierre:", context.last_closure_date)


# 💰 IMPORTANTE (OBLIGATORIO)
@when("guardo el importe del último cierre")
def step_impl(context):
    context.last_closure_amount = context.cash.get_last_closure_amount()
    print("💰 Importe cierre:", context.last_closure_amount)