from googletrans import Translator
import os
import re

translator = Translator()

features_folder = r"C:\Users\Nerea QA\Documents\HI\PROYECTOS\TAMUS\Auto-TAMUS\web\features"
traducciones_folder = r"C:\Users\Nerea QA\Documents\HI\PROYECTOS\TAMUS\Auto-TAMUS\app\traducciones"
os.makedirs(traducciones_folder, exist_ok=True)

for feature_file in os.listdir(features_folder):
    if not feature_file.endswith(".feature"):
        continue

    feature_name = os.path.splitext(feature_file)[0]
    translation_dict = {}
    with open(os.path.join(features_folder, feature_file), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith(("When ", "Then ", "And ")):
                step_text = re.sub(r"^(When|Then|And)\s+", "", line)
                try:
                    translation = translator.translate(step_text, src='en', dest='es').text
                except Exception:
                    translation = step_text  # fallback a texto original si falla
                translation_dict[step_text] = translation

    # Guardar diccionario
    dict_file = os.path.join(traducciones_folder, f"{feature_name}_translations.py")
    with open(dict_file, "w", encoding="utf-8") as f_out:
        f_out.write(f"translations = {translation_dict}\n")
    print(f"Diccionario generado: {dict_file}")