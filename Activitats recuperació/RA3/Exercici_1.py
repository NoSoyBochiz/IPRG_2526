# Demanem l'edat i la convertim a un número sencer
edat = int(input("Quina edat tens? "))

# Comprovem primer si és menor d'edat
if edat < 18:
    print("No pot conduir")
else:
    # Si té 18 o més, demanem si té carnet
    tinc_carnet = input("Tens carnet de conduir? (S/N): ").upper()
    
    if tinc_carnet == "S":
        print("Pot conduir legalment")
    else:
        print("És major d'edat però no pot conduir")