import sys
from typing import Optional
from wordle.logica.Codigo import Wordle, Jugador, PalabraOculta


class UIConsola:
    def __init__(self):
        self.wordle: Optional[Wordle] = None
        self.jugador: Optional[Jugador] = None
        self.palabraoculta: Optional[PalabraOculta] = None
        self.opciones = {
            "1": self.iniciar_juego,
            "0": self.salir
        }

    @staticmethod
    def instrucciones():
        banner = "WORDLE"
        print(banner)
        print("El juego consiste en tratar de adivinar la palabra de 5 letras en 5 intentos")
        print("Solo serán validas palabras que se encuentren en nuestra base de datos")
        print("Si ingresas una palabra que no es correcta el juego te retroalimentará de la siguiente forma:")
        # continuar mostrando la palabra
        print("Buena suerte jugando")

    @staticmethod
    def mostrar_menu():
        titulo = " WORDLE "
        print(f"\n{titulo:_^30}")
        print("1. Iniciar nuevo juego")
        print("0. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        print("WORDLE")
        self.registrar_jugador()
        while True:
            self.instrucciones()
            print("\n")
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def registrar_jugador(self):
        nombre: str = input("Escriba su nombre: ")
        self.wordle = Wordle(nombre=nombre)
        self.jugador = Jugador(nombre=nombre)
        self.palabraoculta = PalabraOculta()

    def iniciar_juego(self): # NO ESTÁ COMPLETA TIENE MUCHOS ERRORES
        intento_palabra: str = input("ingrese la palabra: ")
        verificar_palabra = self.palabraoculta.verificar_palabra(palabra_intento=intento_palabra)
        while not self.wordle.jugador_perdio(palabra_intento=intento_palabra):
            if verificar_palabra:
                self.jugador.ingresar_palabra(palabra_intento=intento_palabra)
            else:
                print(f"La palabra {intento_palabra} no está permitida")
                break
        self.palabraoculta.retroalimentar(palabra_intento=intento_palabra)
        if self.wordle.jugador_gano(palabra_intento=intento_palabra):
            print(f"Felicitaciones, has adivinado correctamente la palabra ")
            self.wordle.actualizar_estadisticas(palabra_intento=intento_palabra)
            self.mostrar_menu_final()
        elif self.wordle.jugador_perdio(palabra_intento=intento_palabra):
            print(f"No has adivinado correctamente la palabra")
            self.wordle.actualizar_estadisticas(palabra_intento=intento_palabra)
            self.mostrar_menu_final()

    def mostrar_menu_final(self):
        palabra: str = self.palabraoculta.palabra_oculta
        partidas_jugadas: int = self.jugador.estadisticas["Partidas jugadas"]
        partidas_ganadas: int = self.jugador.estadisticas["Partidas ganadas"]
        partidas_perdidas: int = self.jugador.estadisticas["Partidas perdidas"]
        racha: int = self.jugador.estadisticas["Racha"]

        print(f"La palabra del día es {palabra}")
        print("Estadísticas: ")
        print(f"Partidas jugadas {partidas_jugadas}")
        print(f"Partidas ganadas {partidas_ganadas}")
        print(f"Partidas perdidas {partidas_perdidas}")
        print(f"Racha {racha}")

    @staticmethod
    def salir():
        print("Gracias por jugar, vuelva pronto")
        sys.exit(0)
