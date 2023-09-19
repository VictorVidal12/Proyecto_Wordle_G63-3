class PalabraOculta:
    pass


class Jugador:
    pass


class Wordle:
    def registrar_jugador(self,nombre: str):
        self.nombre_jugador = nombre

    def mostrar_estadistica(self, mostrar : bool):
        self.mostrar_estadistica = mostrar

    def iniciar_juego(self,iniciar: bool):
        self.iniciar_juego = iniciar

    def significado_palabra(self):
        pass
