# PART 1: Creació i escriptura amb mode 'w'

fitxer = open("prueba.txt", "w", encoding="utf-8")
fitxer.write("Primera línia\n")
fitxer.close()

fitxer = open("prueba.txt", "w", encoding="utf-8")
fitxer.write("Segona línia\n")
fitxer.close()
# El contingut anterior s'esborra perquè el mode 'w' sobreescriu el fitxer


# PART 2: Creació exclusiva amb mode 'x'

try:
    fitxer = open("prueba.txt", "x", encoding="utf-8")
    fitxer.write("Tercera línia\n")
    fitxer.close()
except FileExistsError:
    print("Error: El fitxer ja existeix (FileExistsError).")

# Si s'esborra el fitxer i es torna a executar aquest bloc,
# el fitxer es crearà correctament sense error


# PART 3: Afegir contingut amb mode 'a'

fitxer = open("prueba.txt", "a", encoding="utf-8")
fitxer.write("Quarta línia\n")
fitxer.close()

fitxer = open("prueba.txt", "a", encoding="utf-8")
fitxer.write("Cinquena línia\n")
fitxer.write("Sisena línia\n")
fitxer.close()


# PART 4: Llegir i tancar fitxers

fitxer = open("prueba.txt", "r", encoding="utf-8")
contingut = fitxer.read()
fitxer.close()

print("Contingut final del fitxer:")
print(contingut)

# Prova d'obrir un fitxer que no existeix
try:
    fitxer = open("no_existeix.txt", "r")
except FileNotFoundError:
    print("Error: El fitxer no existeix (FileNotFoundError).")