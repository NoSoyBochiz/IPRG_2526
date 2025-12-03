elements = ["poma", "pera", "taronja", "plàtan"]

try:
    posicio = int(input("Introdueix una posició (0-3): "))
    element = elements[posicio]
    print(f"L'element a la posició {posicio} és: {element}")

except IndexError:
    print("Error: la posició indicada no existeix a la llista.")

except ValueError:
    print("Error: cal introduir un número enter.")

finally:
    print("Operació finalitzada.")