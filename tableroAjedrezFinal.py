
# PROGRAMA QUE SIMULA UN TABLERO DE AJEDREZ
# REALIZADO POR: Alcivar Inca y Ricardo Sinchiguano
from Tkinter import *
ventana= Tk() # Creamos un objeto Tk
ventana.title("TABLERO AJEDREZ") # Titulo de la ventana
canvas = Canvas(ventana, width=642, height=642)
canvas.pack()
color =1
alto=2
# Dos ciclos for para crear los cuadrados y pintarlos de acuerdo a su posicion
for i in range (8):
	ancho=2
	for j in range (8):
		if color % 2 == 0:
			canvas.create_rectangle(ancho, alto, (ancho + 80),(alto + 80), fill= 'black')
		else:
			canvas.create_rectangle(ancho, alto, (ancho + 80),(alto + 80))
		ancho= ancho+80
		color = color +1
	color = color +1
	alto=alto+80
ventana.mainloop()

