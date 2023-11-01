from tkinter import Tk, Button, Entry, Label, messagebox
from tkinter import Frame
#from wordle.logica.Codigo import PalabraOculta, Jugador, Wordle


class Casilla(Frame):
    def __init__(self, master, fila, columna):
        super().__init__()
        self.estado = "vacia"
        self.frame = Frame(master, width=50, height=50, bg="white", borderwidth=1, relief="solid")
        self.frame.grid(row=fila, column=columna)
        self.label = Label(self.frame, text="", font=("Arial", 24))
        self.label.pack(expand=True)

    def cambiar_estado(self, estado):
        self.estado = estado
        colores = {"vacia": "white", "correcta": "green", "incorrecta": "red"}
        self.frame.configure(bg=colores[estado])

    def establecer_letra(self, letra):
        self.label.configure(text=letra)

class Tablero:
    def __init__(self, filas, columnas):
        self.tablero = Tk()
        self.tablero.title(f"Tablero Wordle {filas}x{columnas}")
        self.casillas = [[Casilla(self.tablero, i, j) for j in range(columnas)] for i in range(filas)]

    def iniciar(self):
        self.tablero.mainloop()

tablero = Tablero(5, 6)
tablero.iniciar()



class InterfazJuego(Frame):
    pass