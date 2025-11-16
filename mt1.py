# Importamos los módulos necesarios
from tkinter import *  # Para crear la interfaz gráfica
import math  # Para realizar cálculos matemáticos
import matplotlib.pyplot as plt  # Para generar gráficas

# Configuración de la ventana principal
window = Tk()  # Inicializa la ventana
window.title("Proyecto de probabilidad")  # Establece el título
window.geometry('700x400')  # Configura las dimensiones de la ventana

# Etiquetas y entradas para el ingreso de datos
lbl_instrucciones = Label(window, text="Ingresa xi:", font=("Arial Bold", 12))  # Texto para ingresar valores xi
lbl_instrucciones.grid(column=0, row=0)  # Posición de la etiqueta

entrada_xi = Entry(window, width=100)  # Entrada para los valores xi
entrada_xi.grid(column=0, row=1)  # Posición de la entrada

lbl_instrucciones = Label(window, text="Ingresa pi:", font=("Arial Bold", 12))  # Texto para ingresar valores pi
lbl_instrucciones.grid(column=0, row=2)  # Posición de la etiqueta

entrada_pi = Entry(window, width=100)  # Entrada para las probabilidades pi
entrada_pi.grid(column=0, row=3)  # Posición de la entrada

# Etiquetas para mostrar resultados
lbl_resultado1 = Label(window, text="Esperanza matemática = ", font=("Arial Bold", 12))  # Resultado esperanza matemática
lbl_resultado1.grid(column=0, row=5) # Posición de la salida

# Función que realiza los cálculos y genera la gráfica
def funcion1():
    # Obtención y procesamiento de los datos ingresados
    x = entrada_xi.get()  # Valores xi ingresados
    xi = x.split()  # Se convierten en lista
    fx = entrada_pi.get()  # Probabilidades pi ingresadas
    pi = fx.split()  # Se convierten en lista

    em1 = 0  # Inicialización de la esperanza matemática

    # Cálculo de la esperanza matemática o ejecucion de la formula
    for termino1 in range(len(xi)):
        x1 = xi[termino1]  # Toma cada valor xi
        p1 = pi[termino1]  # Toma la probabilidad pi correspondiente
        var1 = float(x1) * float(p1)  # Producto de xi y pi
        em1 += var1  # Suma acumulativa
    lbl_resultado1.configure(text=f"Esperanza matemática = {em1}")  # Muestra el resultado


# Botón para ejecutar la función
btn_accion1 = Button(window, text="Resolver", command=funcion1)
btn_accion1.grid(column=0, row=4)  # Posición del botón

# Bucle principal de la ventana
window.mainloop()
