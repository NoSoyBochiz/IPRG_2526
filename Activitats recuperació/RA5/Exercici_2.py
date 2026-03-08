import json
import os

# 0. Obtindre la ruta automática del archiu JSON
# Aço busca la carpeta on resideix Exercici_2.py
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(directorio_actual, "estudiant.json")

try:
    # 1. Llegir el fitxer JSON
    with open(ruta, "r", encoding="utf-8") as fitxer:
        dades = json.load(fitxer)

    # 2. Demanar nova assignatura
    nova_assignatura = input("Introdueix una nova assignatura: ")

    # 3. Afegir-la a la llista
    dades["assignatures"].append(nova_assignatura)

    # 4. Guardar el fitxer actualitzat
    with open(ruta, "w", encoding="utf-8") as fitxer:
        json.dump(dades, fitxer, indent=4)

    # 5. Missatge d'èxit
    print("L'assignatura s'ha afegit correctament.")

except FileNotFoundError:
    print(f"Error: el fitxer estudiant.json no existeix en la ruta: {ruta}")

except json.JSONDecodeError:
    print("Error: el fitxer JSON té un format incorrecte.")

except Exception as e:
    print(f"Ha sorgit un error inesperat: {e}")