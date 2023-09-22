# Proyecto_Wordle_G63-3

El juego de Wordle consiste en un programa ...

# Requisitos Funcionales

| Nombre    | R1: Iniciar juego                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Inicia el juego generando una palabra aleatoria de cinco letras                                                                                            |
| Entradas  |                                                                                                                                                            |
| Resultado | 1 El sistema inicia el juego<br/> 2 Se registra el jugador con su nombre <br/> 2 El sistema muestra la opción de ver las instrucciones del juego <br/> 3 El sistema muestra la opción de ver las estadisticas del juego<br/> 4 Se genera una palabra oculta aleatoria de cinco letras <br/>5 Se ejecuta el requisito R2 (Turno jugador) |

|Pasos|Métodos|Responsable|
|---|---|---|
|Registrar jugador| registrar_jugador()|Wordle|
|Iniciar juego| iniciar_juego()->bool|Wordle|
|Mostrar instrucciones| instrucciones(bool)| Wordle|
|Generar palabra oculta|palabra_oculta()|PalabraOculta|

| Nombre    | R2: Iniciar turno jugador                                                                                                                                                                                                                                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El jugador hace su jugada, donde debe adivinar la palabra oculta                                                                                                                                                                                   |
| Entradas  |                                                                                                                                                                                                                                          |
| Resultado | 1 El jugador ingresa una palabra de 5 letras<br/>2 la partida se suma a partidas jugadas en las estadísticas del juego<br/> 3 se ejecuta el requisito R3 (Gestionar intentos) |

|Pasos|Métodos|Responsable|
|---|---|---|
|ingresar palabra | ingresar_palabra(palabra_intento: str)-> Union[str, bool] |Jugador|
|sumar partida |actualizar_estadisticas(palabra_intento: str)|Wordle|


| Nombre    | R3: Gestionar intentos                                                                                                                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema gestiona los intentos del jugador, esto determina si el juego continúa o no                                                                                                                                                                                    |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                          |
| Resultado | 1 Se suma el intento realizado a estadísticas del juego<br/> 2 se muestran los intentos realizados <br/> 3 Si la cantidad de intentos es mayor a 6 <br/>3.1 se ejecuta el requisito R6 (Mostrar resultados) <br/> 4 Si no, se ejecuta el requisito R4 (Verificar palabra) |


| Pasos          | Métodos             | Responsable |
|----------------|---------------------|-------------|
| Sumar intentos | intento_realizado() | Jugador     |
| verificar si el numero de intentos es igual a 6 | jugador_perdio(palabra_intento: str)->Bool | Wordle     |


| Nombre    | R4: Verificar palabra                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Se determina si la palabra ingresada es válida                                                                                                                                                                                                                                                                                                                                                |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                                                                                                                                              |
| Resultado | 1 Se verifica que la palabra ingresada esté registrada en la base de datos<br/>2 Si la palabra está registrada en la base de datos <br/>2.1 se verifica si es igual a la generada por el sistema o si es diferente. <br/>2.1.1 Si la palabra es igual se ejecuta el requisito R6 (Mostrar resultados) <br/> 2.1.2 Si la palabra es distinta se ejecuta el requisito R5 (retroalimentar) |

| Pasos             | Métodos                                  | Responsable |
|-------------------|------------------------------------------|-------------|
| Verificar palabra | verificar_palabra(palabra_intento)->bool | PalabraOculta     |
| Comparar palabras | comparar_palabras(palabra_intento)->bool| PalabraOculta |

| Nombre    | R5: Retroalimentar                                                                                                                                                                                                                                                                                                                           |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Se retroalimenta la palabra ingresada por el jugador según si adivino las letras correctas y están en la posición correcta, las adivinó y no se encuentran en la posición correcta o si las letras no hacen parte de la palabra oculta                                                                                                         |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                                                                                             |
| Resultado |  1 las letras correctas en la posición correcta se marcan de verde<br/> 2 Las letras correctas en la posición incorrecta se marcan de amarillo. <br/> 3 Las letras que no se encuentran en la palabra oculta se marcan de gris. <br/> 4 se guardan los resultados de la retroalimentación en la distribución de intentos <br/> 5. Se ejecuta el requisito R3 (Gestionar intentos)|

| Pasos             | Métodos                         | Responsable |
|-------------------|---------------------------------|-------------|
| Retroalimentar    | retroalimentar(palabra_intento) | PalabraOculta     |
| resultados del intento    | actualizar_estadisticas(palabra_intento) | Wordle     |


| Nombre    | R6: Mostrar resultados                                                                                                                                                                                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  determina los resultados del juego                                                                                                                                                                                                                                    |
| Entradas  |                                                                                                                                                                                                                                                                                   |
| Resultado | 1 Si se adivina la palabra antes de que se acaben los intentos se mostrará un mensaje de victoria <br/> 1.1 se suma una partida ganada <br/> 1.2 y la racha suma uno <br/> 2 Si no llega antes de los 6 intentos se muestra un mensaje de derrota <br/> 2.1 se revela la palabra oculta <br/> 2.2 se suma una partida perdida <br/>2.3 y la racha queda en 0 <br/> 3 Se ejecuta el requisito R6 (Finalizar el juego) |

| Pasos           | Métodos                                   | Responsable |
|-----------------|-------------------------------------------|-------------|
| Adivinó palabra | comparar_palabras(palabra_intento)-> list | Palabra     |
| Sumar partidas perdidas | actualizar_estadisticas(palabra_intento: str)| Wordle    |
| Sumar partidas ganadas | actualizar_estadisticas(palabra_intento: str)| Wordle    |


| Nombre    | R7: Finalizar juego                                                                                                                                                                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  finaliza el juego                                                                                                                                                                                                                                                          |
| Entradas  |                                                                                                                                                                                                                                                                                        |
| Resultado | 1 Aparece el menú final <br/>1.1 Se muestra el significado de la palabra independientemente de si el jugador ganó o no <br/>1.2. Se muestra la opción de iniciar un nuevo juego. <br/> 1.3 <br/> Se muestra la opción de salir del juego <br/> 1.4 Se muestra la opción de ver las estadísticas de las partidas jugadas |

| Pasos                             | Métodos                      | Responsable |
|-----------------------------------|------------------------------|-------------|
| Mostrar significado de la palabra | significado_palabra(palabra_oculta) | Wordle      |
| Mostrar estadísticas              | mostrar_estadisticas(bool)   | Wordle      |
| Mostrar menú final              | mostrar_menu_final()   | Wordle      |
|Finalizar juego| salir(bool)| Wordle      |

# Modelo del mundo del problema (UML)
![Diagrama de clases Wordle G63-3 (2)](https://github.com/VictorVidal12/Proyecto_Wordle_G63-3/assets/110042484/c80c5d87-a36d-43a4-a098-cd20da8cc735)


