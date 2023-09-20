import random

PALABRAS: list[str] = []


class PalabraOculta:
    def __init__(self):
        self.palabra_oculta: str = PALABRAS[random.randint(0, len(PALABRAS))]
    @staticmethod
    def verificar_palabra(self, palabra_intento : str):
        if palabra_intento in PALABRAS:
            return True
        else:
            return False

    def comparar_palabras(self, palabra_intento):
        if palabra_intento == self.palabra_oculta:
            return True
        else:
            return False

    def retroalimentar(self, palabra_intento):
        retroalimentacion = ""
        if  not self.comparar_palabras(palabra_intento):
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

    def ingresar_palabra(self, palabra_intento: str) -> str:
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
        self.nombre_jugador= nombre
        self.jugador = Jugador(self.nombre)
        print(f"Bienvenido, {self.jugador.nombre}.")
        nuevo_juego = input("¿Deseas empezar un nuevo juego? a: si, b: no ")
        if nuevo_juego == "a":
            self.iniciar_juego(True)
        else:
            pass

    def iniciar_juego(self, iniciar: bool):
        self.iniciar_juego = iniciar
        print("adivina la palabra oculta")

        while self.iniciar_juego:
            self.palabra_intento=input("ingresar palabra: ")
            self.jugador.ingresar_palabra()

        #self.mostrar_estadistica = mostrar
        
    """""
    def significado_palabra(self):
        pass
    def mostrar_instrucciones(bool):
        pass
    def finalizar_juego():
        pass
    """



nombre_jugador= input("ingrese su nombre: ")
