import sys
from wordle.logica.Codigo import Wordle, PalabraOculta


class UIConsola:
    def __init__(self):
        self.wordle = None
        self.opciones = {
            "1": self.iniciar_juego,
            "0": self.salir
        }

    @staticmethod
    def instrucciones():
        print("El juego consiste en tratar de adivinar la palabra de 5 letras en 6 intentos.")
        print("Solo serán válidas palabras que se encuentren en nuestra base de datos.")
        print("Si ingresas una palabra que no es correcta el juego te retroalimentará.")

    @staticmethod
    def mostrar_menu():
        print("\n----- MENU -----")
        print("1. Iniciar nuevo juego")
        print("0. Salir")
        print("----------------")

    @staticmethod
    def salir():
        print("Gracias por jugar, ¡vuelve pronto!")
        sys.exit(0)

    def registrar_jugador(self):
        nombre = input("Escribe tu nombre: ")
        self.wordle = Wordle(nombre=nombre)

    def reiniciar_juego(self):
        self.wordle.jugador.intentos = 0
        self.wordle.palabraoculta = PalabraOculta()
        self.iniciar_juego()

    def iniciar_juego(self):
        while self.wordle.jugador.intentos < 6:
            palabra_intento = input(f"\nIntento #{self.wordle.jugador.intentos + 1}\nIngresa tu intento: ").lower()

            if not self.wordle.palabraoculta.verificar_palabra(palabra_intento):
                print(f"La palabra {palabra_intento} no es válida.")
                continue

            self.wordle.jugador.ingresar_palabra(palabra_intento)
            if not self.wordle.palabraoculta.comparar_palabras(palabra_intento):
                self.wordle.palabraoculta.retroalimentar(palabra_intento)
                continue

            elif self.wordle.jugador_gano(palabra_intento):
                print(f"\n¡Felicidades! Has adivinado la palabra secreta: {self.wordle.palabraoculta.palabra_oculta}")
                self.wordle.actualizar_estadisticas(palabra_intento)
                self.mostrar_menu_final()
                break

        if self.wordle.jugador.intentos == 6:
            print(f"\n¡Has agotado tus intentos! La palabra secreta era: {self.wordle.palabraoculta.palabra_oculta}")
            self.wordle.actualizar_estadisticas("Perdiste")
            self.mostrar_menu_final()

    def mostrar_menu_final(self):
        print(f"\nEstadísticas de {self.wordle.jugador.nombre}:")
        print("Partidas jugadas:", self.wordle.jugador.estadisticas["Partidas jugadas"])
        print("Partidas ganadas:", self.wordle.jugador.estadisticas["Partidas ganadas"])
        print("Partidas perdidas:", self.wordle.jugador.estadisticas["Partidas perdidas"])
        print("Racha actual:", self.wordle.jugador.estadisticas["Racha"])
        print("Mejor racha:", self.wordle.jugador.estadisticas["Mejor racha"])
        print("Partidas ganadas por intentos:")
        print("#1:", self.wordle.jugador.estadisticas["1"])
        print("#2:", self.wordle.jugador.estadisticas["2"])
        print("#3:", self.wordle.jugador.estadisticas["3"])
        print("#4:", self.wordle.jugador.estadisticas["4"])
        print("#5:", self.wordle.jugador.estadisticas["5"])
        print("#6:", self.wordle.jugador.estadisticas["6"])

        opciones = str(input("¿Deseas volver a jugar? Sí(s), No(n): "))
        if opciones == "s":
            self.reiniciar_juego()
        elif opciones == "n":
            self.salir()

    def ejecutar_app(self):
        print("-----WORDLE-----")
        self.registrar_jugador()
        while True:
            print("\n----------------")
            self.instrucciones()
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")
