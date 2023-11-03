import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
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
    ventana_1.configure(bg="#212529")

    label = tk.Label(ventana_1,
                     text="¡Bienvenido a WORDLE!")
    label.pack(pady=100, padx=100)

    label_usuario = tk.Label(ventana_1,
                     text="¡Ingresa tu nombre!")
    label_usuario.pack(pady=100, padx=100)
    label_usuario.pack(pady=(ventana_1.winfo_height() // 2 - label_usuario.winfo_height() // 2))
    label_usuario.pack(padx=(ventana_1.winfo_width() // 2 - label_usuario.winfo_width() // 2))
    Nombre = tk.Entry(ventana_1)
    Nombre.pack(pady=10)
    start_button = tk.Button(ventana_1, text="Iniciar juego", command=iniciar_juego)
    start_button.pack()
    close_button = tk.Button(ventana_1, text="Cerrar", command=on_closing)
    close_button.pack()
    ventana_1.mainloop()
