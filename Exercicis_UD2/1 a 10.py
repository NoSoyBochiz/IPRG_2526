#Ejercici 1.
temperatura= float(input("Passam la temperatura"))
nuvolat = input("Esta nuvolat? (si/s)")

if nuvolat.lower() == "si" or nuvolat.lower() == "s":
    nuvolat = true
else:
    nuvolat = False

if(temperatura<=0):
     if (nuvolat):
        print("Fa un fred polar!")
elif temperatura >=0 and temperatura <=15:
     if (nuvolat):
        print("Fa fred i el dia està trist.")
     else:
        print("Fa fresquet pero el sol alegra el dia")
elif temperatura >=16 and temperatura <=25:
     if (nuvolat):
        print("Temperatura agradable, pero potser ploga")
     else:
        print("Dia perfecte per a passejar")
elif temperatura >35:
    if (nuvolat):
        print("Calor i humitat... combinació infernal!")
    else:
         print("Fa un calor que fon les pedres")



#Ejercici 2.
print("Classificador d'alumnes per edat i assistència")

n = int(input("Quants alumnes vols processar? "))
i = 0 #Començaba per 1, per tant el ultim element no el tractaba

while i < n:
    nom = input("Nom: ")
    edat = input("Edat: ")
    assist = input("Assistència (S/N): ").lower()

    if edat < 12:
        categoria = "infantil"
    elif edat > 12 and edat < 18:
        categoria = "adolescent"
    elif edat >= 19 and edat < 65: #he cambiat el 18 per 19 per evitar erorrs amb la categoria Adolescent
        categoria = "adult"
    else:
        categoria = "jubilat"

    if assist == "S": #He cambiat les opcions de s/si per S per a que s'execute el codi
        estat = "present"
    else:
        estat = "absent"

    print(nom, "-", categoria, "-", estat)
    i = i + 1


#Ejercici 3.
num = int(input("Introdueix un número: "))
count = 0
while num != 0:
    count += 1
    num = int(input("Introdueix un altre número: "))
print(f"S'han introduït {count} números positius.")


#Ejercici 4.
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


#Ejercici 5.
num = int(input("Introdueix un número: "))
count = 0
while num != 0:
    count += 1
    num = int(input("Introdueix un altre número: "))
print(f"S'han introduït {count} números positius.")
#Resolt en classe

#Ejercici 6.
num = int(input("Introdueix un número: "))
count = 0
while num != 0:
    count += 1
    num = int(input("Introdueix un altre número: "))
    if num>100:
        break
print(f"S'han introduït {count} números positius.")

#Ejercici 7.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#Ejercici 8
try:
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    resultat = num1 / num2
    print(f"El resultat de la divisió és: {resultat}")
except ZeroDivisionError:
    print("Error: Eres tonto")