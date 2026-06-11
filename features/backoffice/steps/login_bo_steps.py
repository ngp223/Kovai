from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when("hago login con credenciales válidas")
def step_login_bo(context):

    # reutiliza el mismo step
    context.execute_steps("""
        Given el usuario "admin@demo.com" está logueado
    """)

@then("entro al dashboard")
def step_dashboard_bo(context):

    titulo = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[text()='Panel de Control']")
        )
    )

    assert titulo.is_displayed()