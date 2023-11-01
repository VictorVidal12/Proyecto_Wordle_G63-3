import ast
import random
import requests
from typing import Union
from wordle.logica.WordleErrors import WordleError, InvalidWordError, LenError, NotFoundWordError


# Uso de la api para obtener las palabras
def palabra_aleatoria():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    palabras_wordle = [plb['word'] for _ in range(50) if (
        response := requests.get(api_url, headers={'X-Api-Key': '74w5GflDZj4lbxnx3l7Lrg==129rRPt1vTEb5hdg'})) and (
                           plb := ast.literal_eval(response.text)) and len(plb['word']) == 5]
    return palabras_wordle


PALABRAS: list[str] = palabra_aleatoria()

class PalabraOculta:
    def __init__(self):
        self.palabra_oculta: str = PALABRAS[random.randint(0, len(PALABRAS) - 1)]

    @staticmethod
    def verificar_palabra():
        return Jugador.ingresar_palabra in PALABRAS

    def comparar_palabras(self, palabra_intento: str) -> bool:
        return palabra_intento == self.palabra_oculta

    def retroalimentar(self, palabra_intento: str):
        retroalimentacion = ""
        for i in range(len(self.palabra_oculta)):
            if palabra_intento[i] == self.palabra_oculta[i]:
                retroalimentacion += "\033[92m" + palabra_intento[i] + "\033[0m "  # Verde
            elif palabra_intento[i] in self.palabra_oculta:
                retroalimentacion += "\033[93m" + palabra_intento[i] + "\033[0m "  # Amarillo
            else:
                retroalimentacion += "\033[90m" + palabra_intento[i] + "\033[0m "  # Gris
        print(retroalimentacion)
        if not self.comparar_palabras(palabra_intento):
            for i in range(len(self.palabra_oculta)):
                if palabra_intento[i] == self.palabra_oculta[i]:
                    retroalimentacion += "\033[92m" + palabra_intento[i] + "\033[0m "  # Verde
                elif palabra_intento[i] in self.palabra_oculta:
                    retroalimentacion += "\033[93m" + palabra_intento[i] + "\033[0m "  # Amarillo
                else:
                    retroalimentacion += "\033[90m" + palabra_intento[i] + "\033[0m "  # Gris
            print(retroalimentacion)

    def significado(self):
        api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(self.palabra_oculta)
        response = requests.get(api_url, headers={'X-Api-Key': '74w5GflDZj4lbxnx3l7Lrg==129rRPt1vTEb5hdg'})
        significado = ast.literal_eval(response.text)
        return significado['definition']


class Jugador:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.intentos: int = 0
        self.estadisticas: dict[str, int] = {"Partidas ganadas": 0, "Partidas perdidas": 0, "Partidas jugadas": 0,
                                             "Racha": 0, "Mejor racha": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                                             "6": 0}

    def intento_realizado(self):
        self.intentos += 1

    def ingresar_palabra(self, palabra_intento: str) -> Union[str, bool]:
        if PalabraOculta.verificar_palabra():
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
            self.jugador.estadisticas[str(self.jugador.intentos)] += 1
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
