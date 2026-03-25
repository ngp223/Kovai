import os
import re
import pandas as pd
import importlib.util

# --- CONFIGURACIÓN DE CARPETAS ---
features_folder = "C:\\Users\\Nerea QA\\Documents\\HI\\PROYECTOS\\TAMUS\\Auto-TAMUS\\web\\features"      # Carpeta con los feature
translations_folder = "C:\\Users\\Nerea QA\\Documents\\HI\\PROYECTOS\\TAMUS\\Auto-TAMUS\\App\\traducciones"   # Carpeta con diccionarios de traducción por feature
output_folder = "C:\\Users\\Nerea QA\\Documents\\HI\\PROYECTOS\\TAMUS\\Auto-TAMUS\\App\\Testcases"           # Carpeta donde se generarán los Excel

os.makedirs(output_folder, exist_ok=True)

# --- FUNCIONES ---
def load_translations(feature_name):
    """
    Carga el diccionario de traducción de un feature si existe.
    El archivo debe llamarse translations_<feature_name>.py y contener un dict llamado 'translations'.
    """
    file_path = os.path.join(translations_folder, f"translations_{feature_name.lower()}.py")
    if not os.path.exists(file_path):
        return {}
    spec = importlib.util.spec_from_file_location("translations_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "translations", {})

def translate(step, translations):
    """Traduce un paso usando el diccionario, si no existe deja el original"""
    return translations.get(step, step)

def process_feature(file_path):
    """Procesa un feature y devuelve un DataFrame con Num, ID, Summary y Pasos"""
    feature_name = os.path.splitext(os.path.basename(file_path))[0]
    translations = load_translations(feature_name)

    rows = []
    current_id = ""
    summary = ""
    steps = []

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            if line.startswith("@"):
                current_id = line.split()[0].replace("@", "")
            if line.startswith("Scenario:"):
                # Guardar steps anteriores
                if steps:
                    numbered = "\n".join([f"{i+1}. {s}" for i, s in enumerate(steps)])
                    rows.append([current_id, summary, numbered])
                    steps = []
                match = re.search(r"\] (.*)", line)
                summary = match.group(1) if match else ""
            if line.startswith(("When ", "Then ", "And ")):
                step = re.sub(r"^(When|Then|And)\s+", "", line)
                step = translate(step, translations)
                steps.append(step)
    # Guardar último escenario
    if steps:
        numbered = "\n".join([f"{i+1}. {s}" for i, s in enumerate(steps)])
        rows.append([current_id, summary, numbered])

    # Crear DataFrame con numeración de tests
    df = pd.DataFrame(rows, columns=["ID", "Summary", "Pasos"])
    df.insert(0, "Num", range(1, len(df) + 1))
    return df, feature_name

# --- PROCESAR TODOS LOS FEATURE ---
for feature_file in os.listdir(features_folder):
    if feature_file.endswith(".feature"):
        full_path = os.path.join(features_folder, feature_file)
        df, feature_name = process_feature(full_path)
        output_file = os.path.join(output_folder, f"Testcases_{feature_name}.xlsx")
        df.to_excel(output_file, index=False)
        print(f"Archivo generado: {output_file}")