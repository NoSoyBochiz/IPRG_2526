#1.1
#Demanar al usuari dos nombres, enter i flotant
a = int(input("Numero enter: "))
b = int(input("Numero flotant: "))

#Operacions aritmetiques
suma = a + b
resta = a - b
multiplicacio = a * b
divisio = a / b
modul = a % b

#Mostrar resultats
print("\n--- Resultats ---")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacio: {multiplicacio}")
print(f"Divisio: {divisio}")
print(f"Modul: {modul}")

#Concatenacio de cadenes
text1 = "El resultat de la suma es "
text2 = str(suma)
missatge = text1 + text2

print("\n--- Concatenacio de text ---")
print(missatge)

#1.2
#Comparar 2 numeros
c = float(input("Primer numero: "))
d = float(input("Segon numero: "))

if a > b:
    print("El primer numero es major al segon")
elif a < b:
    print("El primer numero es menor al segon")
else:
    print("Els dos numeros son iguals")

#2.1
#Llista de estudiants
estudiants = ["Anna", "Marc", "Julia", "Pau", "Laia"]

estudiants.append("Joan")
pirnt("Despres d'afegir un estudiant:", estudiants)

del estudiants [1]
print("Despres d'eliminar el segon estudiant:", estudiants)

#3.1
#Funcio de salutacio
def saluda(nom):
    print(f"Hola, {nom}!")

saluda("Anna")
saluda("Marc")
saluda("Julia")

#3.2
#Area d'un cercle
import math

def area_cercle(radi):
    return math.pi * radi**2

radi = float(input("Introdueix el radi del cercle: "))
print("L'area es:", area_cercle(radi))

#3.3
#Funcio amb valor per defecte

def suma(num1 + num2=5):
    return num1 + num2

print("Suma amb un sol valor:", suma(10))
print("Suma amb dos valors:" suma(10, 3))

#4.1
#Operadors aritmetics i logics

x = 10
y = 5

#operadors aritmetics
print(f"Suma: {x + y}")
print(f"Resta: {x - y}")
print(f"Multiplicacio: {x * y}")
print(f"Divisio: {x / y}")
print(f"Modul: {x % y}")

#operadors de comparacio
print(f"x es mes gran que y? {x > y}")
print(f"x es igual a y? {x == y}")

#operadors logics
condicio = (x > y) and (x % 2 == 0)
print(f"x es mes gran que y i el modul de x es 0= {condicio}")

#4.2
#Operador in i not in

fruits = ["poma", "platan", "taronja", "maduixa", "raim"]

fruit_usuari = input("Introdueix un fruit: ").lower()

if fruit_usuari in fruits:
    print(f"{fruit_usuari} esta a la llista de fruits!")
else:
    print(f"{fruit_usuari} no existeix a la llista.")

#5.1
#Calculadora IMC

pes = float(input("Introdueix el teu pes en kg: "))
altura = float(input("Introdueix la teua altura en metres: "))

imc = pes / (altura ** 2)
print(f"El teu IMC es: {imc:.2f}")

if imc < 18.5:
    print(f"Inferior al pes saludable.")
elif 18.5 <= imc <= 24.9:
    print(f"Pes saludable.")
else:
    print(f"Sobreeiximent de pes.")

#6.1
#Que fa el seguent codi? Descriu en detall el que fa i el resultat que s'obtindria si l'executes amb els valors actuals:

a = [5, 10, 15] # Una llista amb tres nombres
b = 20    #variable b amb valor 20

if 5 in a:     # Comprava si 5 esta en la llista
    b -= 5     # si esta en la llista li resta 5 a "b"
if 10 in a:    # Comprava si 10 esta en la llista
    b -= 10    # si esta en la llista li resta 10 a "b"
if 15 in a:    # Comprava si 15 esta en la llista
    b -= 15    # si esta en la llista li resta 15 a "b"

print(b)       # Mostra el valor final de b el cual sera -10

#6.2
#Que fa el seguent codi? Descriu en detall el que fa i el resultat que s'obtindria si l'executes amb els valors actuals:

a = [5, 10, 15] # Una llista amb tres nombres
b = 20    #variable b amb valor 20

if 5 in a:     # Comprava si 5 esta en la llista
    b -= 5     # si esta en la llista li resta 5 a "b"
elif 10 in a:    # Sols comprova si l'anterior es fals
    b -= 10    
else 15 in a:    # Error sintactic 'else' no pot tindre condicio
    b -= 15    

print(b)       # Mostra el valor final de b el cual sera 15

#6.3
#Que fa el seguent codi? Explica que retornaria si el valor de n es 6:

def factorial(n): 
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(6))

#Defineix una funcio factorial(n) que calcula el factorial d'un numero. si n es 0 retorna 1 (cas base)
#si n es mes gran que 0 multiplica n pel factorial de n-1(recursio) i crida la funcio amb 6 per a imprimir el resultat el cual seria 720

#7.1
#Corregir codi

x = 10
y = 5

if x == y:
    print("Son iguals")
else:
    print("Son diferents")

#7.2
#Corregir codi

llista = [1, 2, 3, 4, 5]
print(llista[4])