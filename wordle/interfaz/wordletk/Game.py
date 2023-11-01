from tkinter import Tk, Button, Entry, Label, messagebox
from tkinter import Frame
#from wordle.logica.Codigo import PalabraOculta, Jugador, Wordle


class Casilla(Frame):
    def __init__(self, master, fila, columna):
        super().__init__()
        self.estado = "vacia"  # Puede ser "vacia", "correcta" o "incorrecta"
        self.frame = Frame(master, width=50, height=50, bg="white", borderwidth=1, relief="solid")
        self.frame.grid(row=fila, column=columna)
        self.label = Label(self.frame, text="", font=("Arial", 24))
        self.label.pack(expand=True)
        self.letra_correcta = ""



class InterfazJuego(Frame):
    pass