import time
from pathlib import Path

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
    context.sales_page.select_restaurant("Tamus Rooftop Sevilla")


@then("exporto el CSV")
def step_export_csv(context):
    download_dir = Path(context.download_dir)
    context.csvs_before = {f.name for f in download_dir.glob("*.csv")}
    context.sales_page.export_csv()


@then("se descarga y valido el fichero CSV")
def step_validate_csv(context):
    download_dir = Path(context.download_dir)
    timeout = 30
    start = time.time()
    latest_file = None

    print("⏳ Esperando CSV...")

    while time.time() - start < timeout:
        csv_files = list(download_dir.glob("*.csv"))
        crdownload = list(download_dir.glob("*.crdownload"))

        new_csvs = [f for f in csv_files if f.name not in context.csvs_before]

        if new_csvs and not crdownload:
            latest_file = max(new_csvs, key=lambda f: f.stat().st_mtime)
            break

        time.sleep(1)

    assert latest_file is not None, "❌ No se detectó un CSV nuevo"

    print(f"\n📂 CSV: {latest_file}")

    df = pd.read_csv(latest_file, sep=None, engine="python")

    print("\n📊 DATA:")
    print(df.head())

    assert "Ticket" in df.columns, "❌ Falta columna Ticket"
    assert "Total" in df.columns, "❌ Falta columna Total"

    ticket = 3
    expected_value = "32.77"

    ticket_row = df[df["Ticket"] == ticket]

    assert not ticket_row.empty, f"❌ No existe el Ticket {ticket}"

    actual_value = str(ticket_row.iloc[0]["Total"]).strip()

    print("\n🔎 VALIDACIÓN:")
    print(f"Ticket:   {ticket}")
    print(f"Expected: {expected_value}")
    print(f"Actual:   {actual_value}")

    show_debug_overlay(
        context.driver,
        f"""
        <b>CSV VALIDATION</b><br>
        Ticket: {ticket}<br>
        Expected: {expected_value}<br>
        Actual: {actual_value}<br><br>
        <b>{'✅ OK' if actual_value == expected_value else '❌ FAIL'}</b>
        """
    )

    time.sleep(5)

    assert actual_value == expected_value, (
        f"❌ El Ticket {ticket} tiene Total={actual_value} y se esperaba {expected_value}"
    )

    context.csv_file = str(latest_file)
    context.df = df
