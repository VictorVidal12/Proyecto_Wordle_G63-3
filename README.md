# Proyecto_Wordle_G63-3

# Requisitos 

| Nombre    | R1: Iniciar juego                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Inicia el juego generando una palabra aleatoria de cinco letras                                                                                            |
| Entradas  |                                                                                                                                                            |
| Resultado | 1.El sistema inicia el juego<br/> 2. El sistema muestra las instrucciones del juego <br/> 3. Se genera una palabra oculta aleatoria de cinco letras  <br/> |

|Pasos|Métodos|Responsable|
|---|---|---|
|Iniciar juego| iniciar_juego()->bool|Wordle|
|Mostrar instrucciones| instrucciones(bool)| Wordle|
|Generar palabra oculta|palabra_oculta()|Palabra|

| Nombre    | R2: Gestionar intentos                                                                                                                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema gestiona los intentos del jugador, esto determina si el juego continúa o no                                                                                                                                                                                    |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                          |
| Resultado | 1.Se muestran los intentos realizados<br/>2. El jugador ingresa su palabra<br/>3.Se suma el intento realizado<br/> 4.Si la cantidad de intentos es mayor a 6 se ejecuta el requisito R6 (Finalizar el juego)<br/>5. Si no, se ejecuta el requisito R3 (Verificar palabra) |


| Pasos          | Métodos             | Responsable |
|----------------|---------------------|-------------|
| Sumar intentos | intento_realizado() | Jugador     |

| Nombre    | R3: Verificar palabra                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Se determina si la palabra ingresada es válida                                                                                                                                                                                                                                                                                                                                                |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                                                                                                                                              |
| Resultado | 1.Se verifica que la palabra ingresada esté registrada en la base de datos<br/>2. Si se valida que la palabra si está registrada en la base de datos, se verifica si es igual a la generada por el sistema o si es diferente. <br/>2.1 Si la palabra es igual se ejecuta el requisito R5 (Mostrar resultados) <br/> 2.2 Si la palabra es distinta se ejecuta el requisito R4 (retroalimentar) |

| Pasos             | Métodos                                  | Responsable |
|-------------------|------------------------------------------|-------------|
| Verificar palabra | verificar_palabra(palabra_intento)->bool | Palabra     |
| Comparar palabras | comparar_palabras(palabra_intento)->bool| Palabra |

| Nombre    | R4: Retroalimentar                                                                                                                                                                                                                                                                                                                           |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Se retroalimenta la palabra ingresada por el jugador según sea sí adivinó la letra correcta y está en la misma posición, la adivinó y no se encuentra en la misma posición o si la letra adivinada no hace parte de la palabra oculta                                                                                                        |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                                                                                             |
| Resultado | 1. Las letras correctas y en las mismas posiciones que en la palabra original las marca de verde. <br/> 2. Las letras correctas pero que no tiene posiciones coincidentes las marca de amarillo. <br/> 3. Las letras que no se encuentran en la palabra original se marcan de gris. <br/> 4. Se ejecuta el requisito R2 (Gestionar intentos) |

| Pasos             | Métodos                         | Responsable |
|-------------------|---------------------------------|-------------|
| Retroalimentar    | retroalimentar(palabra_intento) | Palabra     |


| Nombre    | R5: Mostrar resultados                                                                                                                                                                                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  determina los resultados del juego                                                                                                                                                                                                                                    |
| Entradas  |                                                                                                                                                                                                                                                                                   |
| Resultado | 1. Si se adivina la palabra antes de que se acaben los intentos se mostrará un mensaje de victoria <br/>2. Si no llega antes de los 6 intentos se muestra un mensaje de derrota y se muestra cuál era la palabra correcta <br/>3. Se ejecuta el requisito R6 (Finalizar el juego) |

| Pasos           | Métodos                                   | Responsable |
|-----------------|-------------------------------------------|-------------|
| Adivinó palabra | comparar_palabras(palabra_intento)-> list | Palabra     |

| Nombre    | R6: Finalizar juego                                                                                                                                                                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  finaliza el juego                                                                                                                                                                                                                                                          |
| Entradas  |                                                                                                                                                                                                                                                                                        |
| Resultado | 1. Aparece un recuadro con varias informaciones<br/>1.1 Se muestra el significado de la palabra independientemente de si el jugador ganó o no <br/>1.2. Se muestra la opción de iniciar un nuevo juego. <br/> 1.3 Se muestra la opción de ver las estadísticas de las partidas jugadas |

| Pasos                             | Métodos                      | Responsable |
|-----------------------------------|------------------------------|-------------|
| Mostrar significado de la palabra | significado_palabra(palabra) | Wordle      |
| Mostrar estadísticas              | mostrar_estadisticas(bool)   | Wordle      |
|Finalizar juego| finalizar_juego(bool)| Wordle      |
