from behave import when, then

from features.mobile.pages.E2E_reservation_pages import ReservationPage
from features.mobile.pages.logout_page import LogoutPage


@when("está en la pantalla de ventas")
def step_impl(context):
    context.reservation = ReservationPage(context.driver)


@when('selecciono la mesa "{table}"')
def step_impl(context, table):
    context.reservation.select_table_b1()


@when("selecciono comensales")
def step_impl(context):
    context.reservation.select_guests()
    context.reservation.click_accept_guests()


@when("selecciono el producto")
def step_impl(context):
    context.reservation.select_product_paella()


@when("añado el producto al pedido")
def step_impl(context):
    context.reservation.click_add_product()


@when("aumento la cantidad del producto")
def step_impl(context):
    context.reservation.increase_product()


@when("realizo el pago")
def step_impl(context):
    context.reservation.click_realizar_pago()


@when("confirmo el pago")
def step_impl(context):
    context.reservation.click_confirmar_pago()


@then("finalizo el pedido")
def step_impl(context):
    context.reservation.click_finalizar()


@then("salgo del modo TPV")
def step_impl(context):
    LogoutPage(context.driver).exit_pos_mode()