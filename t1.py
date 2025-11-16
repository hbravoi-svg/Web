from sympy.geometry import Point, Segment

import time #Se importa la biblioteca time para medir la velocidad de dibujo de cada trazo.
import math #Se importa la biblioteca math para llamar directamente el valor de la variable phi.
import matplotlib.pyplot as plt


puntos = [] #Se crea una lista vacia llamada puntos.
m = 0 #Se crea una variable m para crear un conjunto de puntos.

while m < 2 * math.pi: #Con el bucle mientras se crea 12 puntos y se aniade los puntos a mi lista puntos.
    P = Point(4 * math.cos(m), 4 * math.sin(m))
    P.size = 4
    puntos.append(P)
    m = m + math.pi / 6

# Crear la gráfica
plt.figure(figsize=(6, 6))
plt.axis("equal")

# Dibujar los puntos
for (x, y) in puntos:
    plt.plot(x, y, 'bo')  # 'bo' para puntos azules

for j in range(0, 12): #Con el bucle para o for se crea la grafica.
    for i in range(1, 12):
        # Extraer coordenadas de los puntos
        x_values = [puntos[i][0], puntos[j][0]]
        y_values = [puntos[i][1], puntos[j][1]]
        plt.plot(x_values, y_values, 'g-', alpha=0.5)  # 'g-' para líneas verdes con transparencia

# Mostrar la gráfica
plt.title("12 puntos en una circunferencia y sus conexiones")
plt.show()
