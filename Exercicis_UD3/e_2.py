fitxers_origen = ["fitxer1.txt", "fitxer2.txt", "fitxer3.txt"]

# Nom del fitxer de destinació
fitxer_desti = "fitxer_concatenat.txt"

try:
    # Obrim el fitxer de destinació en mode escriptura
    with open(fitxer_desti, "w", encoding="utf-8") as desti:
        
        # Recorrem cada fitxer d'origen
        for nom_fitxer in fitxers_origen:
            try:
                # Obrim i llegim el fitxer d'origen
                with open(nom_fitxer, "r", encoding="utf-8") as origen:
                    contingut = origen.read()
                    desti.write(contingut + "\n")

                print(f"Fitxer '{nom_fitxer}' concatenat correctament.")

            except FileNotFoundError:
                print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
            except PermissionError:
                print(f"Error: No tens permisos per llegir '{nom_fitxer}'.")

    print(f"\nTots els fitxers possibles s'han concatenat a '{fitxer_desti}'.")

except PermissionError:
    print("Error: No tens permisos per crear o escriure el fitxer de destinació.")
except Exception as e:
    print(f"Error inesperat: {e}")