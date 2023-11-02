import tkinter as tk
from tkinter import Tk
from wordle.interfaz.wordletk.Game import WordleGame


if __name__ == "__main__":
    def iniciar_juego():
        on_closing()
        ventana_2 = Tk()
        ventana_2.configure(bg="white")
        juego = WordleGame(ventana_2)
        ventana_2.mainloop()


    def on_closing():
        ventana_1.destroy()


    ventana_1 = Tk()
    ventana_1.geometry("500x500")

    label = tk.Label(ventana_1,
                     text="¡Bienvenido a WORDLE!")  # Se debe agregar el boton para registro y que guarde el nombre
    label.pack(pady=100, padx=100)
    start_button = tk.Button(ventana_1, text="Iniciar juego", command=iniciar_juego)
    start_button.pack()
    close_button = tk.Button(ventana_1, text="Cerrar", command=on_closing)
    close_button.pack()

    ventana_1.mainloop()
