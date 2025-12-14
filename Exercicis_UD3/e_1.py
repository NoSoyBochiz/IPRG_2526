nom_fitxer = "dades_usuari.txt"

try:
    # Demanar dades a l'usuari
    nom = input("Introdueix el teu nom: ")
    edat = input("Introdueix la teva edat: ")

    # Escriure les dades al fitxer (mode escriptura)
    with open(nom_fitxer, "w", encoding="utf-8") as fitxer:
        fitxer.write(f"Nom: {nom}\n")
        fitxer.write(f"Edat: {edat}\n")

    print("\nDades guardades correctament.\n")

    # Llegir el contingut del fitxer
    with open(nom_fitxer, "r", encoding="utf-8") as fitxer:
        contingut = fitxer.read()
        print("Contingut del fitxer:")
        print(contingut)

    # Afegir una nova dada
    ciutat = input("Introdueix la teva ciutat: ")

    # Afegir informació al fitxer (mode afegir)
    with open(nom_fitxer, "a", encoding="utf-8") as fitxer:
        fitxer.write(f"Ciutat: {ciutat}\n")

    print("\nNova dada afegida correctament.")

except FileNotFoundError:
    print("Error: El fitxer no s'ha trobat.")

except PermissionError:
    print("Error: No tens permisos per accedir al fitxer.")

except Exception as e:
    print(f"S'ha produït un error inesperat: {e}")