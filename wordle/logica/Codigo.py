import random
from typing import Union

PALABRAS: list[str] = []


class PalabraOculta:
    def __init__(self):
        self.palabra_oculta: str = PALABRAS[random.randint(0, len(PALABRAS))]

    @staticmethod
    def verificar_palabra(palabra_intento: str):
        if palabra_intento in PALABRAS:
            return True
        else:
            return False

    def comparar_palabras(self, palabra_intento: str):
        if palabra_intento == self.palabra_oculta:
            return True
        else:
            return False

    def retroalimentar(self, palabra_intento: str):
        retroalimentacion = ""
        if not self.comparar_palabras(palabra_intento):
            for i in range(len(self.palabra_oculta)):
                if palabra_intento[i] == self.palabra_oculta[i]:
                    retroalimentacion += "\033[92m" + palabra_intento[i] + "\033[0m "  # Verde
                elif palabra_intento[i] in self.palabra_oculta:
                    retroalimentacion += "\033[93m" + palabra_intento[i] + "\033[0m "  # Amarillo
                else:
                    retroalimentacion += "\033[90m" + palabra_intento[i] + "\033[0m "  # Gris
                print(retroalimentacion)


class Jugador:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.intentos: int = 0
        self.estadisticas: dict[str, int] = {}

    def ingresar_palabra(self, palabra_intento: str) -> Union[str, bool]:
        if PalabraOculta.verificar_palabra(palabra_intento):
            self.intento_realizado()
            return palabra_intento
        else:
            return False

    def intento_realizado(self):
        self.intentos += 1

    def actualizar_estadisticas(self, palabra_intento: str):
        if self.jugador_gano(palabra_intento):
            self.estadisticas[str(self.intentos)] += 1
            self.estadisticas["Partidas ganadas"] += 1
            self.estadisticas["Racha"] += 1
            self.estadisticas["Partidas jugadas"] += 1
        elif self.jugador_perdio(palabra_intento):
            self.estadisticas["Partidas perdidas"] += 1
            self.estadisticas["Racha"] = 0
            self.estadisticas["Partidas jugadas"] += 1

    def jugador_gano(self, palabra_intento: str) -> bool:
        palabra = self.ingresar_palabra(palabra_intento)
        palabra_oculta = PalabraOculta()
        if palabra_oculta.comparar_palabras(palabra):
            return True
        else:
            return False

    def jugador_perdio(self, palabra_intento: str) -> bool:
        return self.intentos == 6 and not self.jugador_gano(palabra_intento)


class Wordle:
    """
    def registrar_jugador(self, nombre: str):
        self.jugador = Jugador(self):
        self.mostrar_estadistica = mostrar

    def iniciar_juego(self, iniciar: bool):
        self.iniciar_juego = iniciar

    def significado_palabra(self):
    """
    pass
