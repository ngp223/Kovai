from behave import given
import time
from features.backoffice.pages.login_bo_page import LoginPage_bo
from features.backoffice.pages.restaurant_bo_page import RestaurantPage_bo
from features.backoffice.data.users import USERS
from features.backoffice.data.restaurants import RESTAURANTS
from selenium.webdriver.common.by import By


@given("backoffice está abierta")
def step_impl(context):
    assert context.driver is not None
    context.login_page = LoginPage_bo(context.driver)
    context.restaurant_page = RestaurantPage_bo(context.driver)


@given('el usuario "{user}" está logueado')
def step_impl(context, user):
    credentials = USERS[user]
    lp = context.login_page
    rp = context.restaurant_page

    # LOGIN
    lp.enter_email(credentials["email"])
    lp.enter_password(credentials["password"])
    lp.click_activate_terminal()

    # RESTAURANTE
    restaurant_name = RESTAURANTS["tamusGV"]
    rp.select_restaurant(restaurant_name)

    # USUARIO ADMIN (espera + retry)
    lp.select_user_admin()

    # PIN + ACCESO
    lp.enter_pin("1234")
    lp.click_access()


@given("está en panel de control")
def step_impl(context):

    titulo = context.driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div/div/main/div/div[1]/h1'
    )

    assert titulo.is_displayed(), "No se muestra el título del panel de control"