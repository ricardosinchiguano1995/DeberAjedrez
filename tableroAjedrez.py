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

