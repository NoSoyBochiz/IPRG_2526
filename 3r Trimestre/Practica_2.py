# UD4 - Pràctica 2: Matrius

#Tenim una matriu amb la temperatura de la setmana en tres ciutats. Cada fila és un dia i cada columna és una ciutat. 
import numpy as np

temperatures = np.array([
    [18, 20, 17],
    [19, 21, 18],
    [17, 19, 16],
    [22, 24, 20],
    [21, 23, 19],
    [15, 22, 18],
    [18, 20, 17]
])

# Exercici 1 - Seleccionar elements

print(temperatures)
print(temperatures[4, 1])
print(temperatures[3, 0])

# Exercici 2 - Seleccionar files i/o columnes

print(temperatures[:, 2])
print(temperatures[0, :])
print(temperatures[0:2, :])
print(temperatures[2:5, 0])

# Exercici 3 - Filtratge

print(temperatures[temperatures < 18])
print(temperatures[temperatures > 20])
print(temperatures[temperatures == 19])