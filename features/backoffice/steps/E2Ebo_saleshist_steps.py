import os
import time
import pandas as pd
from behave import then
from features.backoffice.pages.E2Ebo_saleshist_page import SalesPage_bo
from features.backoffice.utils.debug_overlay import show_debug_overlay


@then("accedo a historial ventas")
def step_open_sales(context):

    context.sales_page = SalesPage_bo(context.driver)
    context.sales_page.open_sales()


@then("selecciono Tamus Rooftop Sevilla")
def step_select_restaurant(context):

    context.sales_page.select_restaurant(
        "Tamus Rooftop Sevilla"
    )


@then("exporto el CSV")
def step_export_csv(context):

    context.sales_page.export_csv()


@then("se descarga y valido el fichero CSV")
def step_validate_csv(context):

    download_dir = context.download_dir

    timeout = 30
    start = time.time()

    latest_file = None

    print("⏳ Esperando CSV...")

    while time.time() - start < timeout:

        files = os.listdir(download_dir)

        csv_files = [f for f in files if f.endswith(".csv")]
        crdownload = [f for f in files if f.endswith(".crdownload")]

        if csv_files and not crdownload:

            latest_file = max(
                csv_files,
                key=lambda f: os.path.getctime(
                    os.path.join(download_dir, f)
                )
            )

            break

        time.sleep(1)

    assert latest_file is not None, "❌ No CSV descargado"

    file_path = os.path.join(download_dir, latest_file)

    print(f"\n📂 CSV: {file_path}")

    df = pd.read_csv(file_path, sep=None, engine="python")

    print("\n📊 DATA:")
    print(df.head())

    assert "Total" in df.columns, "❌ Falta columna Total"

    actual_value = str(df.loc[1, "Total"]).strip()
    expected_value = "32.77"

    print("\n🔎 VALIDACIÓN:")
    print(f"Expected: {expected_value}")
    print(f"Actual:   {actual_value}")

    # =========================
    # VISUAL DEBUG
    # =========================
    show_debug_overlay(
        context.driver,
        f"""
        <b>CSV VALIDATION</b><br>
        Expected: {expected_value}<br>
        Actual: {actual_value}<br>
        <br>
        <b>{'✅ OK' if actual_value == expected_value else '❌ FAIL'}</b>
        """
    )

    time.sleep(5)

    assert actual_value == expected_value, (
        f"❌ Valor incorrecto: {actual_value}"
    )

    context.csv_file = file_path
    context.df = df