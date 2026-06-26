from behave import then
from features.backoffice.pages.E2Ebo_backups_page import BackupsPage_bo


@then("accedo a backups")
def step_open_backups(context):
    context.backups_page=BackupsPage_bo(context.driver)
    context.backups_page.open_backups()


@then("creo una copia de respaldo")
def step_create_backup(context):
    context.backups_page.create_backup()
    context.backup_text=context.backups_page.get_last_backup_text()


@then("la copia aparece en el listado")
def step_check_backup(context):
    context.backups_page.wait_backup_in_list(context.backup_text)


@then("elimino la copia de respaldo")
def step_delete_backup(context):
    context.backups_page.delete_backup(context.backup_text)


@then("la copia no aparece en el listado")
def step_check_deleted_backup(context):
    context.backups_page.wait_backup_gone(context.backup_text)