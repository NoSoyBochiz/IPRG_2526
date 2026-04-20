import csv

fitxer_origen = "estudiants.csv"
fitxer_desti = "estudiants_modificat.csv"

try:
    # Llegir el fitxer CSV
    with open(fitxer_origen, "r", encoding="utf-8", newline="") as fitxer:
        lector = csv.reader(fitxer)
        dades = list(lector)

    print("Contingut del fitxer CSV:")
    for fila in dades:
        print(fila)

    # Afegir una nova fila amb dades de l'usuari
    nom = input("\nIntrodueix el nom: ")
    edat = input("Introdueix l'edat: ")
    nota = input("Introdueix la nota: ")

    nova_fila = [nom, edat, nota]
    dades.append(nova_fila)

    # Escriure les dades modificades en un nou fitxer CSV
    with open(fitxer_desti, "w", encoding="utf-8", newline="") as fitxer:
        escriptor = csv.writer(fitxer)
        escriptor.writerows(dades)

    print(f"\nDades guardades correctament a '{fitxer_desti}'.")

except FileNotFoundError:
    print("Error: El fitxer CSV no existeix.")
except PermissionError:
    print("Error: No tens permisos per accedir al fitxer.")
except csv.Error:
    print("Error: El fitxer no és un CSV vàlid.")
except Exception as e:
    print(f"Error inesperat: {e}")