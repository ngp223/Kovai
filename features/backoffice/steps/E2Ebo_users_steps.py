from behave import then
from datetime import datetime
from features.backoffice.pages.E2Ebo_users_page import UsersPage_bo

@then("accedo a usuarios")
def step_open_users(context):
    context.users_page=UsersPage_bo(context.driver)
    context.users_page.open_users()

@then("creo un nuevo usuario")
def step_create_user(context):
    timestamp=datetime.now().strftime("%d%m%Y_%H%M%S")
    context.selected_role=context.users_page.select_random_role()
    context.user_name=f"{context.selected_role}QA {timestamp}"
    context.modified_user_name=f"{context.user_name} 987654"
    context.users_page.create_user(context.user_name)

@then("el usuario aparece en el listado")
def step_user_exists(context):
    context.users_page.wait_user_in_list(context.user_name)

@then("modifico el usuario")
def step_modify_user(context):
    context.users_page.modify_user(context.user_name,context.modified_user_name)
    context.user_name=context.modified_user_name

@then("elimino el usuario")
def step_delete_user(context):
    context.users_page.delete_user(context.user_name)

@then("el usuario no aparece en el listado")
def step_user_not_exists(context):
    context.users_page.wait_user_gone(context.user_name)