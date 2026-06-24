from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from random import choice
from features.backoffice.pages.E2Ebo_categories_page import CategoriesPage_bo


@then("accedo a categorías")
def step_open_categories(context):
    context.categories_page = CategoriesPage_bo(context.driver)
    context.categories_page.open_categories()


@then("creo una nueva categoría")
def step_create_category(context):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    tipo_categoria = choice(["Ensalada","Carne","Pescado","Pasta"])
    context.category_name = (f"Categoría QA {tipo_categoria} {timestamp}")
    context.categories_page.create_category(context.category_name)


@then("la categoría aparece en el listado")
def step_check_category(context):
    category_locator = (By.XPATH,f"//*[contains(text(),'{context.category_name}')]")
    element = WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located(category_locator))
    assert element.is_displayed(), (f"No se encontró la categoría {context.category_name}")