import tkinter as tk


def on_closing():
    ventana.destroy()


ventana = tk.Tk()
ventana.geometry("500x500")

label = tk.Label(ventana, text="¡Bienvenido a WORDLE!")
label.pack(pady=100, padx=100)

button = tk.Button(ventana, text="Cerrar", command=on_closing)
button.pack()

ventana.mainloop()
