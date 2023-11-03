import random
from wordle.logica.palabras import get_randoms_words_with_meanings
from typing import Union
from wordle.logica.WordleErrors import InvalidWordError, LenError, NotFoundWordError

lista_de_palabras: list[str] = []
random_words = get_randoms_words_with_meanings(5)
for key, value in random_words.items():
    if key == value:
        lista_de_palabras.append(value)
    else:
        continue


class PalabraOculta:
    def __init__(self):
        self.palabra_oculta: str = lista_de_palabras[random.randint(0, len(lista_de_palabras) - 1)]

    def actualizar_lista(self):
        return lista_de_palabras.remove(self.palabra_oculta)

    @staticmethod
    def verificar_palabra():
        return Jugador.ingresar_palabra in lista_de_palabras

    def comparar_palabras(self, palabra_intento: str) -> bool:
        if len(palabra_intento) != 5:
            raise LenError("La palabra debe ser de 5 caracteres")
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
        return random_words[f"{self.palabra_oculta} definition"]


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

        if not isinstance(palabra_intento, str) or not palabra_intento.isalpha():
            raise InvalidWordError("La palabra debe ser una cadena de texto valida.")
        if palabra_intento not in lista_de_palabras:
            raise NotFoundWordError("a palabra no se encuentra en la lista de palabras")

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
