from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("la app está abierta")
def step_impl(context):

    wait = WebDriverWait(context.driver, 30)

    # Esperar cualquier elemento del login estable
    wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "Activar Terminal")
        )
    )


@when('introduzco email "{email}"')
def step_impl(context, email):

    wait = WebDriverWait(context.driver, 10)

    email_field = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
        )
    )

    email_field.clear()          # 👈 LIMPIA CAMPO
    email_field.send_keys(email)


@when('introduzco password "{password}"')
def step_impl(context, password):

    wait = WebDriverWait(context.driver, 10)

    password_field = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
        )
    )

    password_field.clear()       # 👈 LIMPIA CAMPO
    password_field.send_keys(password)


@when("pulso activar terminal")
def step_impl(context):

    wait = WebDriverWait(context.driver, 10)

    button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Activar Terminal"]')
        )
    )

    button.click()


@then("entro en la app")
def step_impl(context):
    assert context.driver is not None