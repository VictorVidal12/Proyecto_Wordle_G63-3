# Proyecto_Wordle_G63-3

Wordle es un juego de palabras en el que el jugador debe adivinar una palabra oculta de cinco letras en un número limitado de intentos. El juego proporciona retroalimentación después de cada intento, lo que permite al jugador deducir las letras correctas y su posición dentro de la palabra.

Reglas del juego:

1. Palabra oculta: Al comienzo del juego, se genera aleatoriamente una palabra oculta de cinco letras. Las letras pueden repetirse, lo que significa que una misma letra puede aparecer en diferentes posiciones de la palabra.
2. Intentos: El jugador tiene un número limitado de intentos para adivinar la palabra oculta. Generalmente, se asignan seis intentos, pero este número puede variar según la implementación del juego. Cada palabra que el jugador ingrese, debe ser una palabra válida (debe hacer parte de la base de datos de palabras del juego).
3. Retroalimentación: Después de cada intento, el juego proporciona retroalimentación al jugador. La retroalimentación consiste en indicar cuántas letras del intento son correctas y 
están en la posición correcta (marcadas en verde), cuántas letras son correctas, pero están en una posición incorrecta (marcadas en amarillo) y cuántas letras no hacen parte de la palabra (marcadas en gris).
4. Lógica y deducción: Basándose en la retroalimentación recibida después de cada intento, el jugador debe usar su lógica y deducción para reducir las posibilidades y adivinar la palabra oculta. Al analizar las letras y su posición, se pueden descartar letras incorrectas y buscar patrones para encontrar la solución correcta.
5. Intentos restantes: El juego muestra el número de intentos restantes para motivar al jugador a adivinar la palabra antes de agotar los intentos disponibles.
6. Victoria o derrota: El jugador gana el juego si adivina la palabra oculta dentro de los intentos asignados. En caso contrario, si se agotan todos los intentos sin adivinar correctamente la palabra, se considera una derrota. En este último caso, el juego muestra cual era la palabra correcta.

Al finalizar, el jugador tiene la opción de buscar el significado de la palabra (ya sea que la haya adivinado o no) y de iniciar un nuevo juego.

En cualquier momento, el jugador podrá ver las instrucciones del juego. Además, también deberá tener la opción de ver las estadísticas del juego donde se le mostrará un gráfico con la distribución de los intentos en cada juego realizado.

# Prototipo

https://www.figma.com/proto/fI06NkyY1qP9jk2nMZlaAr/Wordle_G3-3?type=design&node-id=3-38&t=NXi9QRuyWQsNyfQ3-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=4%3A2972&show-proto-sidebar=1&mode=design

# Requisitos Funcionales

| Nombre    | R1: Iniciar juego                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Inicia el juego generando una palabra aleatoria de cinco letras.                                                                                           |
| Entradas  | Nombre del jugador.                                                                                                                                                           |
| Resultado | 1. El sistema inicia el juego.<br/> 2. Se registra el jugador con su nombre.<br/> 3. El sistema muestra la opción de ver las instrucciones del juego.<br/> 4. El sistema muestra la opción de ver las estadisticas del juego.<br/> 5. Se genera una palabra oculta aleatoria de cinco letras.<br/>6. Se ejecuta el requisito R2 (Ingresar palabra). |

|Pasos|Métodos|Responsable|
|---|---|---|
|Registrar jugador| registrar_jugador()|Wordle|
|Iniciar juego| iniciar_juego()->bool|Wordle|
|Mostrar instrucciones| instrucciones(bool)| Wordle|
|Generar palabra oculta|palabra_oculta()|PalabraOculta|

| Nombre    | R2: Ingresar palabra                                                                                                                                                                                                                                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El jugador ingresa una palabra con el fin de adivinar la palabra oculta.                                                                                                                                                                                   |
| Entradas  | Palabra ingresada por el jugador.                                                                                                                                                                                                                                        |
| Resultado | 1. El jugador ingresa una palabra de 5 letras.<br/>2. la partida se suma a partidas jugadas en las estadísticas del juego.<br/> 3. se ejecuta el requisito R3 (Gestionar intentos). |

|Pasos|Métodos|Responsable|
|---|---|---|
|Ingresar palabra | ingresar_palabra(palabra_intento: str)-> Union[str, bool] |Jugador|
|Sumar partida |actualizar_estadisticas(palabra_intento: str)|Wordle|


| Nombre    | R3: Gestionar intentos                                                                                                                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema gestiona los intentos del jugador, esto determina si el juego continúa o no.                                                                                                                                                                                   |
| Entradas  | Palabra ingresada por el jugador.                                                                                                                                                                                                                                          |
| Resultado | 1. Se suma el intento realizado a estadísticas del juego.<br/> 2. se muestran los intentos realizados.<br/> 3. Si la cantidad de intentos es mayor a 6.<br/>3.1 Se ejecuta el requisito R6 (Mostrar resultados).<br/> 4. Si no, se ejecuta el requisito R4 (Verificar palabra).|


| Pasos          | Métodos             | Responsable |
|----------------|---------------------|-------------|
| Sumar intentos | intento_realizado() | Jugador     |
| Verificar si el número de intentos es igual a 6 | jugador_perdio(palabra_intento: str)->Bool | Wordle     |


| Nombre    | R4: Verificar palabra                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Se determina si la palabra ingresada es válida.                                                                                                                                                                                                                                                                                                                                                |
| Entradas  | Palabra ingresada por el jugador.                                                                                                                                                                                                                                                                                                                                                              |
| Resultado | 1. Se verifica que la palabra ingresada esté registrada en la base de datos.<br/>2. Si la palabra está registrada en la base de datos.<br/>2.1 Se verifica si es igual a la generada por el sistema o si es diferente. <br/>2.1.1 Si la palabra es igual se ejecuta el requisito R6 (Mostrar resultados). <br/> 2.1.2 Si la palabra es distinta se ejecuta el requisito R5 (Retroalimentar).|

| Pasos             | Métodos                                  | Responsable |
|-------------------|------------------------------------------|-------------|
| Verificar palabra | verificar_palabra(palabra_intento: str)->bool | PalabraOculta     |
| Comparar palabras | comparar_palabras(palabra_intento: str)->bool| PalabraOculta |

| Nombre    | R5: Retroalimentar                                                                                                                                                                                                                                                                                                                           |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Se retroalimenta la palabra ingresada por el jugador según si adivinó las letras correctas y están en la posición correcta, las adivinó y no se encuentran en la posición correcta o si las letras no hacen parte de la palabra oculta.                                                                                                         |
| Entradas  | Palabra ingresada por el jugador.                                                                                                                                                                                                                                                                                                            |
| Resultado |  1. Las letras correctas en la posición correcta se marcan de verde.<br/> 2. Las letras correctas en la posición incorrecta se marcan de amarillo. <br/> 3. Las letras que no se encuentran en la palabra oculta se marcan de gris. <br/> 4. Se guardan los resultados de la retroalimentación en la distribución de intentos.<br/> 5. Se ejecuta el requisito R3 (Gestionar intentos).|

| Pasos             | Métodos                         | Responsable |
|-------------------|---------------------------------|-------------|
| Retroalimentar    | retroalimentar(palabra_intento: str) | PalabraOculta     |
| Resultados del intento    | actualizar_estadisticas(palabra_intento: str) | Wordle     |


| Nombre    | R6: Mostrar resultados                                                                                                                                                                                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  determina los resultados del juego.                                                                                                                                                                                                                                    |
| Entradas  |                                                                                                                                                                                                                                                                                   |
| Resultado | 1. Si se adivina la palabra antes de que se acaben los intentos se mostrará un mensaje de victoria. <br/> 1.1 Se suma una partida ganada. <br/> 1.2 Se suma uno a la racha. <br/> 2. Si no se adivina la palabra antes de los 6 intentos, se muestra un mensaje de derrota. <br/> 2.1 Se revela la palabra oculta. <br/> 2.2 Se suma una partida perdida. <br/>2.3 y La racha queda en 0. <br/> 3. Se ejecuta el requisito R6 (Finalizar el juego). |

| Pasos           | Métodos                                   | Responsable |
|-----------------|-------------------------------------------|-------------|
| Adivinó palabra | comparar_palabras(palabra_intento: str) -> bool | Palabra     |
| Sumar partidas perdidas | actualizar_estadisticas(palabra_intento: str)| Wordle    |
| Sumar partidas ganadas | actualizar_estadisticas(palabra_intento: str)| Wordle    |


| Nombre    | R7: Finalizar juego                                                                                                                                                                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  finaliza el juego.                                                                                                                                                                                                                                                         |
| Entradas  |                                                                                                                                                                                                                                                                                        |
| Resultado | 1. Aparece el menú final. <br/>1.1 Se muestra el significado de la palabra independientemente de si el jugador ganó o no. <br/>1.2. Se muestra la opción de ver las estadísticas de las partidas jugadas.  <br/> 1.3 Se muestra la opción de iniciar un nuevo juego. <br/> 1.4 Se muestra la opción de salir del juego.|

| Pasos                             | Métodos                      | Responsable |
|-----------------------------------|------------------------------|-------------|
| Mostrar significado de la palabra | significado_palabra(palabra_oculta) | Wordle      |
| Mostrar estadísticas              | mostrar_estadisticas(bool)   | Wordle      |
| Mostrar menú final              | mostrar_menu_final()   | Wordle      |
|Finalizar juego| salir(bool)| Wordle      |

# Modelo del mundo del problema (UML)
![Diagrama de clases Wordle G63-3 (2)](https://github.com/VictorVidal12/Proyecto_Wordle_G63-3/assets/110042484/551be563-bc5f-4e48-aec0-c750f43f3ee5)



