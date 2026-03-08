elements = ["roig", "verd", "blau", "groc"]

try:
    # Demanem la posició (pot llançar ValueError si no és un enter)
    posicio = int(input("Introdueix una posició (0-3): "))

    # Utilitzem assert per a comprovar el rang
    # Si la condició és falsa, llança un AssertionError
    assert 0 <= posicio <= 3, "La posició ha d'estar entre 0 i 3"

    # Si tot és correcte, mostrem l'element
    print(f"L'element a la posició {posicio} és: {elements[posicio]}")

except ValueError:
    print("Error: Has d'introduir un número enter vàlid.")

except AssertionError as e:
    print(f"Error de rang: {e}")

finally:
    # Aquest bloc s'executa sempre, hi haja error o no
    print("Procés finalitzat.")