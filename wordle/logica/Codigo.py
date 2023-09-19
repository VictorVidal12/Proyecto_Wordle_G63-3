VERDE = "\033[0;32m]"
AMARILLO = "\033[0;33m]"
GRIS = "\033[0;30m]"


class PalabraOculta:
    pass


class Jugador:
    pass


class Wordle:
    def registrar_jugador(self, nombre: str):
        self.jugador = Jugador()  # se registra el jugador

    def mostrar_estadistica(self, mostrar: bool):
        self.mostrar_estadistica = mostrar

    def iniciar_juego(self, iniciar: bool):
        self.iniciar_juego = iniciar

    def significado_palabra(self):
        pass
