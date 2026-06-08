from behave import when, then
from features.mobile.pages.E2E_menus_types_page import CardsPage


@when("accedo al módulo de cartas")
def step_impl(context):

    context.cards_page = CardsPage(context.driver)
    context.cards_page.open_cards()


@then("creo una nueva carta con datos válidos")
def step_impl(context):

    context.cards_page.create_new_card()