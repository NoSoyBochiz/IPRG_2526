import json

nom_fitxer = "estudiant.json"

try:
    # Llegir el fitxer JSON
    with open(nom_fitxer, "r", encoding="utf-8") as fitxer:
        estudiant = json.load(fitxer)

    print("Dades actuals de l'estudiant:")
    print(estudiant)

    # Afegir una nova assignatura
    nova_assignatura = input("Introdueix una nova assignatura: ")

    # Comprovem que existeixi la clau 'assignatures'
    if "assignatures" in estudiant:
        estudiant["assignatures"].append(nova_assignatura)
    else:
        estudiant["assignatures"] = [nova_assignatura]

    # Guardar els canvis al mateix fitxer JSON
    with open(nom_fitxer, "w", encoding="utf-8") as fitxer:
        json.dump(estudiant, fitxer, indent=4, ensure_ascii=False)

    print("\nFitxer JSON actualitzat correctament.")

except FileNotFoundError:
    print("Error: El fitxer JSON no existeix.")
except json.JSONDecodeError:
    print("Error: El fitxer no té un format JSON vàlid.")
except PermissionError:
    print("Error: No tens permisos per accedir al fitxer.")
except Exception as e:
    print(f"Error inesperat: {e}")