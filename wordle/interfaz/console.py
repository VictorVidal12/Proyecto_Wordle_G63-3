import sys
from wordle.logica.Codigo import Wordle, Jugador, PalabraOculta


class UIConsola:
    def __init__(self):
        self.wordle = None
        self.jugador = None
        self.palabraoculta = None
        self.opciones = {
            "1": self.iniciar_juego,
            "0": self.salir
        }

    @staticmethod
    def instrucciones():
        print("El juego consiste en tratar de adivinar la palabra de 5 letras en 5 intentos.")
        print("Solo serán válidas palabras que se encuentren en nuestra base de datos.")
        print("Si ingresas una palabra que no es correcta el juego te retroalimentará.")

    @staticmethod
    def mostrar_menu():
        print("\n----- MENU -----")
        print("1. Iniciar nuevo juego")
        print("0. Salir")

    def registrar_jugador(self):
        nombre = input("Escribe tu nombre: ")
        self.wordle = Wordle(nombre=nombre)
        self.jugador = Jugador(nombre=nombre)
        self.palabraoculta = PalabraOculta()

    def iniciar_juego(self): # TIENE EL ERROR QUE CUANDO SE ESCRIBE LA PALABRA CORRECTA EL JUEGO NO SE TERMINA
        intentos = 0
        while intentos <= 6:
            palabra_intento = input(f"\nIntentos: {intentos}\nIngresa tu intento: ").lower()

            if not self.palabraoculta.verificar_palabra(palabra_intento):
                print(f"La palabra {palabra_intento} no es válida.")
                continue

            self.jugador.ingresar_palabra(palabra_intento)
            if not self.palabraoculta.comparar_palabras(palabra_intento):
                self.palabraoculta.retroalimentar(palabra_intento)
                continue

            elif self.wordle.jugador_gano(palabra_intento):
                print(f"\n¡Felicidades! Has adivinado la palabra secreta: {self.palabraoculta.palabra_oculta}")
                self.wordle.actualizar_estadisticas(palabra_intento)
                self.mostrar_menu_final()
                break

            intentos += 1

        if intentos > 6:
            print(f"\n¡Has agotado tus intentos! La palabra secreta era: {self.palabraoculta.palabra_oculta}")
            self.wordle.actualizar_estadisticas(palabra_intento)
            self.mostrar_menu_final()

    @staticmethod
    def mostrar_menu_final(self):
        print(f"\nEstadísticas de {self.jugador.nombre}:")
        print(f"Partidas jugadas: {self.jugador.estadisticas['Partidas jugadas']}")
        print(f"Partidas ganadas: {self.jugador.estadisticas['Partidas ganadas']}")
        print(f"Partidas perdidas: {self.jugador.estadisticas['Partidas perdidas']}")
        print(f"Racha: {self.jugador.estadisticas['Racha']}")

    def ejecutar_app(self):
        print("WORDLE")
        self.registrar_jugador()
        while True:
            self.instrucciones()
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    @staticmethod
    def salir():
        print("Gracias por jugar, ¡vuelve pronto!")
        sys.exit(0)
