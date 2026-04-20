elements = ["poma", "pera", "taronja", "plàtan"]

seleccio = None

try:
    posicio = input("Introdueix una posició (0-3): ")
    
    posicio = int(posicio)
    
    assert 0 <= posicio <= 3, "Error: la posició ha d’estar entre 0 i 3."
    
    seleccio = elements[posicio]
    print(f"L'element a la posició {posicio} és: {seleccio}")

except ValueError:
    print("Error: has d'introduir un número enter.")

except AssertionError as e:
    print(e)

finally:
    print("Comprovació finalitzada.")
    print(f"Llista de treball: {elements}")
    print(f"La selecció final és: {seleccio}")