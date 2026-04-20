import json
import csv
import os
import shutil

fitxer_json = "estudiants.json"
fitxer_csv = "estudiants.csv"
directori_antincs = "fitxers_antincs"

try:
    # 1. Llegir el fitxer JSON
    with open(fitxer_json, "r", encoding="utf-8") as f:
        estudiants = json.load(f)

    if not isinstance(estudiants, list):
        raise ValueError("El fitxer JSON no conté una llista d'estudiants.")

    # 2. Demanar dades del nou estudiant
    nom = input("Introdueix el nom: ")
    edat = int(input("Introdueix l'edat: "))
    nota = float(input("Introdueix la nota: "))
    assignatures = input("Introdueix les assignatures (separades per comes): ")
    llista_assignatures = [a.strip() for a in assignatures.split(",")]

    nou_estudiant = {
        "nom": nom,
        "edat": edat,
        "nota": nota,
        "assignatures": llista_assignatures
    }

    # 3. Afegir el nou estudiant
    estudiants.append(nou_estudiant)

    # 4. Guardar de nou al fitxer JSON
    with open(fitxer_json, "w", encoding="utf-8") as f:
        json.dump(estudiants, f, indent=4, ensure_ascii=False)

    print("Fitxer JSON actualitzat correctament.")

    # 5. Comprovar si el CSV ja existeix i moure'l
    if os.path.exists(fitxer_csv):
        if not os.path.exists(directori_antincs):
            os.mkdir(directori_antincs)
        shutil.move(fitxer_csv, os.path.join(directori_antincs, fitxer_csv))
        print("Fitxer CSV anterior mogut a 'fitxers_antincs'.")

    # 6. Crear el nou fitxer CSV
    with open(fitxer_csv, "w", encoding="utf-8", newline="") as f:
        escriptor = csv.writer(f)
        escriptor.writerow(["nom", "edat", "nota", "assignatures"])

        for e in estudiants:
            escriptor.writerow([
                e["nom"],
                e["edat"],
                e["nota"],
                ", ".join(e["assignatures"])
            ])

    print("Fitxer CSV creat correctament.")

except FileNotFoundError:
    print("Error: El fitxer JSON no existeix.")
except PermissionError:
    print("Error: No tens permisos per accedir a algun fitxer.")
except json.JSONDecodeError:
    print("Error: El fitxer JSON no té un format vàlid.")
except ValueError as e:
    print(f"Error de dades: {e}")
except Exception as e:
    print(f"Error inesperat: {e}")