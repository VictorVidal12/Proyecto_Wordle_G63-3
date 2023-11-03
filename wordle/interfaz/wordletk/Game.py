from tkinter import Tk, Button, Entry, Label
from wordle.logica.Codigo import Wordle
from wordle.logica.WordleErrors import InvalidWordError, LenError, NotFoundWordError
import matplotlib.pyplot as plt

"""
Se deben enlazar las excepciones con la aplicación, los excepciones que están
creados en WordleErrors.

También se debe de organizar la estética del programa
"""


class Tablero:
    def __init__(self, palabra_oculta):
        self.num_intentos = 0
        self.matriz = []
        self.palabra_oculta = palabra_oculta
        self.llenar_tablero()

    def llenar_tablero(self):
        for i in range(6):
            self.matriz.append(["_" for _ in range(5)])

    def actualizar_tablero(self, palabra):
        if self.num_intentos < 6:
            if palabra == self.palabra_oculta:
                for i, letra in enumerate(palabra):
                    self.matriz[self.num_intentos][i] = letra
                self.num_intentos = 6
                return
            else:
                for i, letra in enumerate(palabra):
                    if letra == self.palabra_oculta[i]:
                        self.matriz[self.num_intentos][i] = letra
                    elif letra in self.palabra_oculta:
                        self.matriz[self.num_intentos][i] = letra.lower()
                    else:
                        self.matriz[self.num_intentos][i] = letra
                self.num_intentos += 1


class Game:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Wordle")
        self.ventana.configure(bg="white")
        self.wordle = Wordle(nombre="")
        self.wordle.palabraoculta = self.wordle.palabraoculta
        self.wordle.jugador = self.wordle.jugador

        for i in range(11):
            self.ventana.rowconfigure(i, weight=1)
        for j in range(5):
            self.ventana.columnconfigure(j, weight=1)

        self.palabraOculta = self.wordle.palabraoculta
        self.tablero = Tablero(self.palabraOculta.palabra_oculta)

        self.etiqueta = Label(ventana, text="WORDLE UDEM", font=("Arial", 16))
        self.etiqueta.grid(row=0, column=0, columnspan=5, sticky="nsew")

        self.etiqueta_palabra = Label(ventana, text="Ingresa una palabra de 5 letras:",
                                      font=("Arial", 12))
        self.etiqueta_palabra.grid(row=1, column=0, columnspan=5, sticky="nsew")

        self.entrada_palabra = Entry(ventana, font=("Arial", 12))
        self.entrada_palabra.grid(row=2, column=0, columnspan=5, sticky="nsew")

        self.boton_ingresar = Button(ventana, text="Ingresar palabra", command=self.ingresar_palabra,
                                     font=("Arial", 12))
        self.boton_ingresar.grid(row=3, column=0, columnspan=5, sticky="nsew")

        self.error = Label(ventana, text="", fg="red", font=("Arial", 12))
        self.error.grid(row=4, column=0, columnspan=5, sticky="nsew")

        self.etiqueta_tablero = Label(ventana, text="", font=("Arial", 16))
        self.etiqueta_tablero.grid(row=11, column=0, columnspan=5, sticky="nsew")

        self.boton_estadisticas = Button(ventana, text="Estadisticas", command=self.estadisticas, font=("Arial", 16))
        self.boton_estadisticas.grid(row=12, column=1, columnspan=5, sticky="nsew")

        self.boton_significado = Button(ventana, text="Significado", command=self.palabraOculta.significado,
                                        font=("Arial", 16))
        self.boton_significado.grid(row=13, column=1, columnspan=5, sticky="nsew")

        self.tablero_labels = []
        for i in range(6):
            fila_labels = []
            for j in range(5):
                label = Label(ventana, text="", width=2, height=1, font=("Arial", 16),
                              relief="solid", borderwidth=1)
                label.grid(row=i + 5, column=j, sticky="nsew")
                fila_labels.append(label)
            self.tablero_labels.append(fila_labels)

    def ingresar_palabra(self):
        palabra = self.entrada_palabra.get()

        try:
            if len(palabra) != 5 or not palabra.isalpha() or not palabra.islower():
                raise LenError("Por favor, ingresa una palabra valida")

            self.error.config(text="")

            self.tablero.actualizar_tablero(palabra)
            self.actualizar_tablero()

            if "".join(self.tablero.matriz[self.tablero.num_intentos - 1]) == self.palabraOculta.palabra_oculta:
                self.etiqueta_tablero.config(text="¡Has adivinado la palabra!")
            elif self.tablero.num_intentos == 6:
                self.etiqueta_tablero.config(
                    text=f"¡Agotaste tus intentos! La palabra correcta era: {self.palabraOculta.palabra_oculta}")

        except (LenError, InvalidWordError, NotFoundWordError) as e:
            self.error.config(text=str(e))

    def actualizar_tablero(self):
        for i in range(6):
            for j in range(5):
                letra = self.tablero.matriz[i][j]
                label = self.tablero_labels[i][j]
                if letra == "_":
                    label.config(text=letra, bg="white")
                elif letra == self.palabraOculta.palabra_oculta[j]:
                    label.config(text=letra, bg="green")
                elif letra in self.palabraOculta.palabra_oculta:
                    label.config(text=letra, bg="yellow")
                else:
                    label.config(text=letra, bg="white")

    # Método que grafica las estadisticas del juego:
    def estadisticas(self):
        stats: list[int] = [self.wordle.jugador.estadisticas["Partidas ganadas"],
                            self.wordle.jugador.estadisticas["Partidas perdidas"],
                            self.wordle.jugador.estadisticas["Partidas jugadas"],
                            self.wordle.jugador.estadisticas["Racha"], self.wordle.jugador.estadisticas["Mejor racha"]]
        etiquetas: list[str] = ["Partidas ganadas", "Partidas perdidas", "Partidas Jugadas", "Racha Actual",
                                "Mejor Racha"]
        fig, ax = plt.subplots()
        ax.barh(etiquetas, width=stats)
        plt.show()


if __name__ == "__main__":
    ventana = Tk()
    ventana.configure(bg="white")
    juego = Game(ventana)
    ventana.mainloop()
