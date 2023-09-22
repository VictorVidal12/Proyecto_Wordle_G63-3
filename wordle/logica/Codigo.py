import random
from typing import Union

PALABRAS: list[str] = ["piton", "comer", "trata", "zarza", "camus", "cello", "lapiz", "diera", "zarpa", "mango",
                       "cebra", "mansa", "perro", "trenz", "calar", "largo", "tiara", "azote", "cacao", "lucha",
                       "trama", "coche", "grifo", "barco"]


class PalabraOculta:
    def __init__(self):
        self.palabra_oculta: str = PALABRAS[random.randint(0, len(PALABRAS) - 1)]

    @staticmethod
    def verificar_palabra(palabra_intento: str) -> bool:
        if palabra_intento in PALABRAS:
            return True
        else:
            return False

    def comparar_palabras(self, palabra_intento: str) -> bool:
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
        self.estadisticas: dict[str, int] = {"Partidas ganadas": 0, "Partidas perdidas": 0, "Partidas jugadas": 0,
                                             "Racha": 0, "Mejor racha": 0}

    def intento_realizado(self):
        self.intentos += 1

    def ingresar_palabra(self, palabra_intento: str) -> Union[str, bool]:
        if PalabraOculta.verificar_palabra(palabra_intento):
            self.intento_realizado()
            return palabra_intento
        else:
            return False


class Wordle:
    def __init__(self, nombre: str):
        self.jugador: Jugador = Jugador(nombre)
        self.palabraoculta: PalabraOculta = PalabraOculta()

    def jugador_gano(self, palabra_intento: str) -> bool:
        if self.palabraoculta.comparar_palabras(palabra_intento):
            return True
        else:
            return False

    def jugador_perdio(self, palabra_intento: str) -> bool:
        return self.jugador.intentos == 6 and not self.jugador_gano(palabra_intento)

    def actualizar_estadisticas(self, palabra_intento: str):
        if self.jugador_gano(palabra_intento):
            # self.jugador.estadisticas[str(self.jugador.intentos)] += 1
            self.jugador.estadisticas["Partidas ganadas"] += 1
            self.jugador.estadisticas["Racha"] += 1
            self.jugador.estadisticas["Partidas jugadas"] += 1
            if self.jugador.estadisticas["Racha"] >= self.jugador.estadisticas["Mejor racha"]:
                self.jugador.estadisticas["Mejor racha"] = self.jugador.estadisticas["Racha"]
        elif self.jugador_perdio(palabra_intento):
            self.jugador.estadisticas["Partidas perdidas"] += 1
            self.jugador.estadisticas["Racha"] = 0
            self.jugador.estadisticas["Partidas jugadas"] += 1
            if self.jugador.estadisticas["Racha"] > self.jugador.estadisticas["Mejor racha"]:
                self.jugador.estadisticas["Mejor racha"] = self.jugador.estadisticas["Racha"]
