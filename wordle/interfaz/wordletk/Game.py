from tkinter import Tk, Button, Entry, Label, messagebox
from wordle.logica.Codigo import Wordle

"""
Se deben enlazar las excepciones con la aplicación, los excepciones que están
creados en WordleErrors.

También se debe de organizar la estética del programa
"""


class Tablero:
    def __init__(self, palabra_correcta):
        self.num_intentos = 0
        self.matriz = []
        self.palabra_correcta = palabra_correcta
        self.llenar_matriz()

    def llenar_matriz(self):
        for i in range(6):
            self.matriz.append(["_" for _ in range(5)])

    def actualizar_tablero(self, palabra):
        while self.num_intentos < 6:
            if palabra == self.palabra_correcta:
                for i, letra in enumerate(palabra):
                    self.matriz[self.num_intentos][i] = letra
                self.num_intentos = 6
                return
            else:
                for i, letra in enumerate(palabra):
                    if letra == self.palabra_correcta[i]:
                        self.matriz[self.num_intentos][i] = letra
                    elif letra in self.palabra_correcta:
                        self.matriz[self.num_intentos][i] = letra.lower()
                    else:
                        self.matriz[self.num_intentos][i] = letra
                self.num_intentos += 1


class WordleGame:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Wordle")
        self.ventana.configure(bg="white")
        self.wordle = Wordle(nombre="")  # hay que hacer que reciba el nombre el login debería de hacerse en esta
        # misma código
        self.wordle.palabraoculta = self.wordle.PalabraOculta() # no reconoce la clase PalabraOculta()

        for i in range(11):
            self.ventana.rowconfigure(i, weight=1)
        for j in range(5):
            self.ventana.columnconfigure(j, weight=1)

        self.palabra_oculta = self.wordle.palabraoculta
        self.tablero = Tablero(self.palabra_oculta)

        self.etiqueta = Label(ventana, text="WORDLE", font=("Arial", 16))
        self.etiqueta.grid(row=0, column=0, columnspan=5, sticky="nsew")

        self.etiqueta_palabra = Label(ventana, text="Ingresa una palabra de 5 letras:",
                                      font=("Arial", 12))
        self.etiqueta_palabra.grid(row=1, column=0, columnspan=5, sticky="nsew")

        self.entrada_palabra = Entry(ventana, font=("Arial", 12))
        self.entrada_palabra.grid(row=2, column=0, columnspan=5, sticky="nsew")

        self.boton_adivinar = Button(ventana, text="Adivinar", command=self.adivinar_palabra, font=("Courier", 12))
        self.boton_adivinar.grid(row=3, column=0, columnspan=5, sticky="nsew")

        self.etiqueta_error = Label(ventana, text="", fg="red", font=("Arial", 12))
        self.etiqueta_error.grid(row=4, column=0, columnspan=5, sticky="nsew")

        self.etiqueta_tablero = Label(ventana, text="", font=("Arial", 16))
        self.etiqueta_tablero.grid(row=11, column=0, columnspan=5, sticky="nsew")

        self.tablero_labels = []
        for i in range(6):
            fila_labels = []
            for j in range(5):
                label = Label(ventana, text="", width=2, height=1, font=("Arial", 16),
                              relief="solid", borderwidth=1)
                label.grid(row=i + 5, column=j, sticky="nsew")
                fila_labels.append(label)
            self.tablero_labels.append(fila_labels)

    def adivinar_palabra(self):
        palabra = self.entrada_palabra.get()
        if len(palabra) == 5 and palabra.isalpha() and palabra.islower():
            self.etiqueta_error.config(text="")
            self.tablero.actualizar_tablero(palabra)
            self.actualizar_tablero()
            if "".join(self.tablero.matriz[self.tablero.num_intentos - 1]) == self.palabra_oculta:
                self.etiqueta_tablero.config(text="¡Has adivinado la palabra!")
                guardar_resultado(self.palabra_oculta, palabra, "Victoria")
            elif self.tablero.num_intentos == 6:
                self.etiqueta_tablero.config(
                    text=f"¡Agotaste tus intentos! La palabra correcta era: {self.palabra_oculta}")
        else:
            self.etiqueta_error.config(text="Por favor, ingresa una palabra válida")

    def actualizar_tablero(self):
        for i in range(6):
            for j in range(5):
                letra = self.tablero.matriz[i][j]
                label = self.tablero_labels[i][j]
                if letra == "_":
                    label.config(text=letra, bg="white")
                elif letra == self.palabra_oculta[j]:
                    label.config(text=letra, bg="green")
                elif letra in self.palabra_oculta:
                    label.config(text=letra, bg="yellow")
                else:
                    label.config(text=letra, bg="white")


def guardar_resultado(palabra_correcta, palabra_ingresada, resultado):
    with open("historial_juegos.txt", "a") as file:
        file.write(
            f"Palabra correcta: {palabra_correcta}, Palabra ingresada: {palabra_ingresada}, Resultado: {resultado}\n")


if __name__ == "__main__":
    ventana = Tk()
    ventana.configure(bg="white")
    juego = WordleGame(ventana)
    ventana.mainloop()
