<<<<<<< HEAD
# PROGRAMA QUE SIMULA UN TABLERO DE AJEDRE
from Tkinter import *
# Creamos un objeto Tk
ventana= Tk()
ventana.title("TABLERO AJEDREZ")

canvas = Canvas(ventana, width=642, height=642)
canvas.pack()
color =1
alto=2
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
=======
# PROGRAMA QUE SIMULA UN TABLERO DE AJEDREZ
from tkinter import *
ventana=Tk()
ventana.title("TABLERO AJEDREZ")
canva=Canvas(ventana, width=500 ,height=500)
canva.pack()
for i in range (0,10):
	for j in range(0,10):
		canva.create_rectangle((20+(i*30),(50+(j*30)),30, 30)
ventana.mainloop()

>>>>>>> origin/master
