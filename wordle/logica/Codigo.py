class PalabraOculta:
    pass


class Jugador:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.intentos: int = 0
        self.estadisticas: dict[str, int] = {}

    def ingresar_palabra(self, palabra_intento) -> str:
        if PalabraOculta.verificar_palabra(palabra_intento):
            self.intento_realizado()
            return palabra_intento
        else:
            return f"Palabra no encontrada en el sistema."

    def intento_realizado(self):
        self.intentos += 1

    def actualizar_estadisticas(self):
        if self.jugador_gano():
            self.estadisticas[str(self.intentos)] += 1
            self.estadisticas["Partidas ganadas"] += 1
        else:
            self.estadisticas["Partidas perdidas"] += 1

    def jugador_gano(self) -> bool:
        if PalabraOculta.palabra_encontrada():
            return True
        else:
            return False

    def jugador_perdio(self) -> bool:
        if self.intentos == 6 and not self.jugador_gano():
            return True
        else:
            return False

class Wordle:
    def registrar_jugador(self, nombre: str):
        self.nombre_jugador = nombre

    def mostrar_estadistica(self, mostrar: bool):
        self.mostrar_estadistica = mostrar

    def iniciar_juego(self, iniciar: bool):
        self.iniciar_juego = iniciar

    def significado_palabra(self):
        pass
