from behave import then
from features.backoffice.pages.E2Ebo_tax_config_page import TaxConfigPage


@then("accedo a configuración fiscal")
def step_open_tax_config(context):
    context.tax_config_page = TaxConfigPage(context.driver)
    context.tax_config_page.open_tax_config()


@then("estoy en la página de configuración fiscal")
def step_check_tax_config_page(context):
    assert context.tax_config_page.is_page_displayed(), (
        "No se ha accedido a la página de Configuración Fiscal"
    )