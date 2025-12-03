num = int(input("Introdueix un número: "))
count = 0
while num != 0:
    count += 1
    num = int(input("Introdueix un altre número: "))
print(f"S'han introduït {count} números positius.")