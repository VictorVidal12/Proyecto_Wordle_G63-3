from tkinter import Tk, Button, Entry, Label, messagebox
from tkinter import Frame, StringVar
from wordle.logica.Codigo import Wordle

class Interfaz(Frame):
    def __init__(self, master, nombre: str):
            super().__init__(master)
            self.fila = 0
            self.verde = '#19C065'
            self.naranjado = '#E3B30E'
            self.gris = '#8F8E8C'
            self.texto = StringVar()
            self.texto.trace("w", lambda *args: self.limitar(self.texto))
            self.create_widgets()
            self.palabra_aleatoria() # contiene la palabra aleatoria, la debe de tomar desde codigo

        def create_widgets(self):
            self.frame_titulo = Frame(self.master, bg='black', width=400, height=100)
            self.frame_titulo.grid_propagate(0)
            self.frame_titulo.grid(column=0, row=0, sticky='snew')
            self.frame_cuadros = Frame(self.master, bg='black', width=400, height=350)
            self.frame_cuadros.grid_propagate(0)
            self.frame_cuadros.grid(column=0, row=1, sticky='snew')
            self.frame_control = Frame(self.master, bg='black', width=400, height=100)
            self.frame_control.grid_propagate(0)
            self.frame_control.grid(column=0, row=2, sticky='snew')

            Label(self.frame_titulo, bg='black', fg='white', text='WORDLE',
                  font=('Arial', 25, 'bold')).pack(side='top')

            self.signal = Label(self.frame_control, bg='black', fg='white', text='Señal',
                                font=('Arial', 12))
            self.signal.pack(side='left', expand=True)

            self.palabra = Entry(self.frame_control, font=('Arial', 15), justify='center',
                                 textvariable=self.texto, fg='black', highlightcolor="green2", highlightthickness=2,
                                 width=7)
            self.palabra.pack(side='left', expand=True)

            self.enviar = Button(self.frame_control, text='Enviar', bg='gray50', activebackground='green2',
                                 fg='white', font=('Arial', 12, 'bold'), command=self.verificar_palabra)
            self.enviar.pack(side='left', expand=True)

            self.limpiar = Button(self.frame_control, text='⌫', bg='gray50', activebackground='green2',
                                  fg='white', font=('Arial', 12, 'bold'), width=4, command=lambda: self.texto.set(''))
            self.limpiar.pack(side='left', expand=True)


