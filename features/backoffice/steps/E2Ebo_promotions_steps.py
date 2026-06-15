from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

from features.backoffice.pages.E2Ebo_promotions_page import PromotionsPage_bo


@then("accedo a promociones")
def step_open_promotions(context):

    context.promotions_page = PromotionsPage_bo(context.driver)
    context.promotions_page.open_promotions()


@then("creo una nueva promoción")
def step_create_promotion(context):

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    context.promotion_name = f"Promoción QA {timestamp}"

    context.promotions_page.create_promotion(
        context.promotion_name
    )


@then("la promoción aparece en el listado")
def step_check_promotion(context):

    promotion_locator = (
        By.XPATH,
        f"//*[contains(text(),'{context.promotion_name}')]"
    )

    element = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(promotion_locator)
    )

    assert element.is_displayed(), (
        f"No se encontró la promoción {context.promotion_name}"
    )