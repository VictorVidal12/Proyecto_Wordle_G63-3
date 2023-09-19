# Proyecto_Wordle_G63-3

# Requisitos 

| Nombre    | R1: Iniciar juego                                                                                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Inicia el juego generando una palabra aleatoria de cinco letras en un tablero 5x6                                                                                                             |
| Entradas  |                                                                                                                                                                                               |
| Resultado | 1.El sistema inicia el juego<br/> 2. Se genera una palabra oculata aleatoria de cinco letras en un tablero 5x6 <br/>3. El sistema muestra al jugador las celdas donde introducirá la palabra. |

|Pasos|Métodos|Responsable|
|---|---|---|
|Iniciar juego| iniciar_juego()->bool|Wordle|
|Generar palabra oculta|palabra_oculta()|Palabra|

| Nombre    | R2: Gestionar intentos                                                                                                                                                                                                                                                   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema gestiona los intentos del jugador, esto determina si el juego continúa o no                                                                                                                                                                                   |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                         |
| Resultado | 1.Se muestran los intentos realizados<br/>2. El jugador ingresa su palabra<br/>3.Se suma el intento realizado<br/> 4.Si la cantidad de intentos es mayor a 6 se ejecuta el requisito R6 (Finalizar el juego)<br/>5. Sino, se ejecuta el requisito R3 (Verificar palabra) |


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

| Nombre    | R4: Retroalimentar                                                                                                                                                                                                                                                                                                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | Se verifica que letras son correctas, si están en su posición o no y si son incorrectas                                                                                                                                                                                                                                                                                                       |
| Entradas  | Palabra ingresada por el jugador                                                                                                                                                                                                                                                                                                                                                              |
| Resultado | 1.Se verifica que la palabra ingresada esté registrada en la base de datos<br/>2. Si se valida que la palabra si está registrada en la base de datos, se verifica si es igual a la generada por el sistema o si es diferente. <br/>2.1 Si la palabra es igual se ejecuta el requisito R5 (Mostrar resultados) <br/> 2.2 Si la palabra es distinta se ejecuta el requisito R4 (retroalimentar) |

| Pasos             | Métodos                         | Responsable |
|-------------------|---------------------------------|-------------|
| Retroalimentar    | retroalimentar(palabra_intento) | Palabra     |


| Nombre    | R5: Mostrar resultados                                                                                                                                                                                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  determina los resultados del juego                                                                                                                                                                                                                                    |
| Entradas  |                                                                                                                                                                                                                                                                                   |
| Resultado | 1. Si se adivina la palabra antes de que se acaben los intentos se msotrará un mensaje de victoria <br/>2. Si no llega antes de los 6 intentos se muestra un mensaje de derrota y se muestra cual era la palabra correcta <br/>3. Se ejecuta el requisito R6 (Finalizar el juego) |

| Pasos           | Métodos                                   | Responsable |
|-----------------|-------------------------------------------|-------------|
| Adivinó palabra | comparar_palabras(palabra_intento)-> list | Palabra     |

| Nombre    | R6: Finalizar juego                                                                                                                                                                                                                                                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumen   | El sistema  finaliza el juego                                                                                                                                                                                                                                                         |
| Entradas  |                                                                                                                                                                                                                                                                                       |
| Resultado | 1. Aparece un recuadro con varias informaciones<br/>1.1 Se muestra el signficado de la palabra independientemente de si el jugador ganó o no <br/>1.2. Se muestra la opción de iniciar un nuevo juego. <br/> 1.3 Se muestra la opción de ver las estadísitcas de las partidas jugadas |

| Pasos                             | Métodos                      | Responsable |
|-----------------------------------|------------------------------|-------------|
| Mostrar significado de la palabra | significado_palabra(palabra) | Wordle      |
| Mostrar estadísticas              | mostrar_estadisticas(bool)   | Wordle      |
|Finalizar juego| finalizar_juego(bool)| Wordle      |
