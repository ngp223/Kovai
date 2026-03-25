import re
import pandas as pd

input_file = "/web(Tamus)\\features\\GestionAlmacen.feature"
output_file = "../Testscases/Testcases_gestionalmacen.xlsx"

rows = []

current_id = ""
summary = ""
steps = []

translations = {
    "I click to gestion almacen": "Hago clic en gestión de almacén",
    "I see gestion de almacen": "Veo gestión de almacén",
    "I see menu lateral de almacen": "Veo el menú lateral de almacén",
    "I manage almacen": "Gestiono el almacén",
    "I click products": "Hago clic en productos",
    "I click catalogs": "Hago clic en catálogos",
    "I click ingredients": "Hago clic en ingredientes",
    "I click materias primas categories": "Hago clic en categorías de materias primas",
    "I click materias primas units": "Hago clic en unidades de materias primas",
    "I click orders": "Hago clic en pedidos",
    "I click menu recipes": "Hago clic en recetas de carta",
    "I click delivery notes(in)": "Hago clic en albaranes de entrada",
    "I click delivery notes(out)": "Hago clic en albaranes de salida",
    "I click external purchases": "Hago clic en compras externas",
    "I click client order": "Hago clic en pedidos de clientes",
    "I click transfers and departures": "Hago clic en traspasos y salidas",
    "I click the inventory": "Hago clic en inventario",
    "I click the store": "Hago clic en almacén",
    "I export providers": "Exporto proveedores",
    "I export products": "Exporto productos",
    "I export catalogs": "Exporto catálogos",
    "I export ingredients": "Exporto ingredientes",
    "I export categories": "Exporto categorías",
    "I export units": "Exporto unidades",
    "I export orders": "Exporto pedidos",
    "I export inventories": "Exporto inventarios",
    "I export transfers and departures": "Exporto traspasos y salidas",
    "I export imbalances": "Exporto descuadres",
}

def translate(step):
    return translations.get(step, step)

with open(input_file, encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if line.startswith("#") or line == "":
            continue

        if line.startswith("@"):
            current_id = line.split()[0].replace("@", "")

        if line.startswith("Scenario:"):
            if steps:
                numbered = "\n".join([f"{i+1}. {s}" for i, s in enumerate(steps)])
                rows.append([current_id, summary, numbered])
                steps = []

            match = re.search(r"\] (.*)", line)
            summary = match.group(1) if match else ""

        if line.startswith(("When ", "Then ", "And ")):
            step = re.sub(r"^(When|Then|And)\s+", "", line)
            step = translate(step)
            steps.append(step)

if steps:
    numbered = "\n".join([f"{i+1}. {s}" for i, s in enumerate(steps)])
    rows.append([current_id, summary, numbered])

df = pd.DataFrame(rows, columns=["ID", "Summary", "Pasos"])
df.to_excel(output_file, index=False)

print(f"Archivo generado: {output_file}")