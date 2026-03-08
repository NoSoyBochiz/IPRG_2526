suma = 0
comptador = 0

print("Introdueix números (un negatiu per a parar, o major de 100 per a tallar):")

while True:
    num = int(input("Introdueix un número: "))

    # Si és major que 100, finalitza immediatament
    if num > 100:
        print("Número major que 100 detectat. Finalitzant...")
        break

    # Si és negatiu, acaba el programa normalment
    if num < 0:
        break

    # Si és 0, l'ignorem i tornem a començar el bucle
    if num == 0:
        continue

    # Si és un número vàlid (positiu i <= 100)
    suma += num
    comptador += 1

print("--- Resultats ---")
print(f"S'han introduït {comptador} números vàlids (sense comptar els zeros).")
print(f"La suma total és: {suma}")