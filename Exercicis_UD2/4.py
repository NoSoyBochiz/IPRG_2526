suma = 0
comptador_parells = 0

for i in range(1, 7):
    if i % 2 == 0:
        suma = suma + i
        comptador_parells = comptador_parells + 1
    else:
        suma = suma - 1
    print("Resultat final:"+str(1))
    print("suma ="+str(suma))
    print("comptador_parells ="+str(comptador_parells))

print("Resultat final:")
print("suma =", suma)
print("comptador_parells =", comptador_parells)
#1ra iteracció (i = 1) Condició = f Valor de suma = -1 Valor de contador = 0
#2na iteracció (i = 2) Condició = t Valor de suma = 1 Valor de contador = 1
#3ra iteracció (i = 3) Condició = f Valor de suma = 0 Valor de contador = 1
#4ta iteracció (i = 4) Condició = t Valor de suma = 4 Valor de contador = 2
#5ra iteracció (i = 5) Condició = f Valor de suma = 3 Valor de contador = 2
#6ra iteracció (i = 6) Condició = t Valor de suma = 9 Valor de contador = 3