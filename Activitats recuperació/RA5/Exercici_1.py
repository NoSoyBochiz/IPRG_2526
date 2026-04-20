try:
    # 1. Demanar dades a l'usuari
    nom = input("Introdueix el teu nom: ")
    edat = input("Introdueix la teua edat: ")

    # 2. Guardar les dades en el fitxer
    with open("usuari.txt", "w") as fitxer:
        fitxer.write("Nom: " + nom + "\n")
        fitxer.write("Edat: " + edat + "\n")

except PermissionError:
    print("Error: no tens permís per escriure en el fitxer.")

# 3. Llegir el fitxer i mostrar-lo
try:
    with open("usuari.txt", "r") as fitxer:
        contingut = fitxer.read()
        print("\nContingut del fitxer:")
        print(contingut)

except FileNotFoundError:
    print("Error: el fitxer no existeix.")
except PermissionError:
    print("Error: no tens permís per llegir el fitxer.")

# 4. Afegir ciutat al final del fitxer
try:
    ciutat = input("Introdueix la teua ciutat: ")

    with open("usuari.txt", "a") as fitxer:
        fitxer.write("Ciutat: " + ciutat + "\n")

    print("Ciutat afegida correctament.")

except PermissionError:
    print("Error: no tens permís per modificar el fitxer.")