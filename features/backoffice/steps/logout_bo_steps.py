from behave import then

from features.backoffice.pages.logout_bo_page import LogoutPage_bo


@then("hago logout")
def step_logout(context):

    logout_page = LogoutPage_bo(context.driver)
    logout_page.logout()