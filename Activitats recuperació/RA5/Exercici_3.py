import csv
import os

# 0. Obtindre la ruta automática del archiu CSV
# Detecta la carpeta on resideix Exercici_3.py
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_lectura = os.path.join(directorio_actual, "alumnes.csv")
ruta_escritura = os.path.join(directorio_actual, "alumnes_nou.csv")

alumnes = []

try:
    # 1. Llegir el fitxer CSV
    # Añadimos encoding="utf-8" para evitar problemas con acentos
    with open(ruta_lectura, "r", encoding="utf-8") as fitxer:
        lector = csv.reader(fitxer)
        for fila in lector:
            alumnes.append(fila)

    # 2. Mostrar les dades
    print("Dades dels alumnes:")
    for alumne in alumnes:
        print(alumne)

    # 3. Demanar dades d'un nou alumne
    nom = input("Nom: ")
    edat = input("Edat: ")
    nota = input("Nota: ")

    alumnes.append([nom, edat, nota])

    # 4. Guardar en un nou fitxer
    with open(ruta_escritura, "w", newline="", encoding="utf-8") as fitxer_nou:
        escriptor = csv.writer(fitxer_nou)
        escriptor.writerows(alumnes)

    print(f"Nou alumne afegit correctament en {os.path.basename(ruta_escritura)}")

except FileNotFoundError:
    print(f"Error: el fitxer alumnes.csv no existeix en: {ruta_lectura}")

except Exception as e:
    print(f"Ha sorgit un error inesperat: {e}")