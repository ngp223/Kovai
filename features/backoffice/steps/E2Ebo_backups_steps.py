import os
import time
import json
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


@then("descargo la copia de respaldo")
def step_download_backup(context):
    context.backups_page.download_backup(context.backup_text)


@then("el fichero de respaldo es válido")
def step_validate_backup(context):
    download_dir=context.download_dir
    timeout=30
    start=time.time()
    latest_file=None

    while time.time()-start < timeout:
        files=os.listdir(download_dir)
        json_files=[f for f in files if f.endswith(".json")]
        crdownload=[f for f in files if f.endswith(".crdownload")]
        if json_files and not crdownload:
            latest_file=max(
                json_files,
                key=lambda f: os.path.getctime(os.path.join(download_dir,f))
            )
            break
        time.sleep(1)

    assert latest_file is not None,"❌ No se descargó el JSON del backup"

    file_path=os.path.join(download_dir,latest_file)

    with open(file_path,"r",encoding="utf-8") as f:
        data=json.load(f)

    assert "createdAt" in data,"❌ Falta createdAt en el backup"

    created_at=data["createdAt"]
    assert created_at is not None and len(created_at)>0,"❌ createdAt vacío"

    context.backup_file=file_path


@then("elimino la copia de respaldo")
def step_delete_backup(context):
    context.backups_page.delete_backup(context.backup_text)


@then("la copia no aparece en el listado")
def step_check_deleted_backup(context):
    context.backups_page.wait_backup_gone(context.backup_text)