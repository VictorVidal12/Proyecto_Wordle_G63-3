import random


class PalabraOculta:
    def __init__(self):
        self.palabra: list = self.palabra_oculta()

    def palabra_oculta(self):
        palabras = ["", ""]
        return random.choice(palabras)

    def verificar_palabra(self, palabra_intento):
        if palabra_intento in self.palabra_oculta():
            return True
        else:
            return False

    def comparar_palabras(self, palabra_intento):
        if palabra_intento == self.palabra:
            pass
        # se debe llamar jugador gano
        else:
            self.retroalimentar(palabra_intento)

    def retroalimentar(self, palabra_intento):
        retroalimentacion = ""
        for i in range(len(self.palabra)):
            if palabra_intento[i] == self.palabra[i]:
                retroalimentacion += "\033[92m" + palabra_intento[i] + "\033[0m "  # Verde
            elif palabra_intento[i] in self.palabra:
                retroalimentacion += "\033[93m" + palabra_intento[i] + "\033[0m "  # Amarillo
            else:
                retroalimentacion += "\033[90m" + palabra_intento[i] + "\033[0m "  # Gris
            print(retroalimentacion)


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
