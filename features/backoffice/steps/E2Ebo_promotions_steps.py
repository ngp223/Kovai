from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from features.backoffice.pages.E2Ebo_promotions_page import PromotionsPage_bo


@then("accedo a promociones")
def step_open_promotions(context):
    context.promotions_page = PromotionsPage_bo(context.driver)
    context.promotions_page.go_to_promotions()


@then("creo una nueva promoción")
def step_create(context):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    context.promotion_name = f"Promoción QA {timestamp}"

    context.promotions_page.create_promotion(context.promotion_name)
    context.promotions_page.close_continue_modal_if_present()
    context.promotions_page.go_to_promotions()


@then("la promoción aparece en el listado")
def step_check(context):
    locator = (By.XPATH,f"//*[contains(normalize-space(),'{context.promotion_name}')]")
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located(locator))


@then("borro la promoción creada")
def step_delete(context):
    context.promotions_page.delete_promotion(context.promotion_name)


@then("la promoción no aparece en el listado")
def step_not_present(context):
    locator = (
        By.XPATH,
        f"//*[contains(normalize-space(),'{context.promotion_name}')]"
    )

    WebDriverWait(context.driver, 20).until(
        EC.invisibility_of_element_located(locator)
    )