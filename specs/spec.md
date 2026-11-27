# Especificación

## Contexto

La plataforma web ofrece cursos lúdicos para niños. El MVP se centra en el curso de Geografía de Colombia y en la mecánica Memoria de parejas. Sus usuarios son docentes y niños; el niño entra con el código de la clase, un alias y un avatar, sin correo electrónico.

## Historias de usuario

### H1. El docente gestiona las actividades del curso.

Como docente, quiero gestionar las actividades del curso, para disponer de preguntas del curso en las partidas.

**Criterios de aceptación**

- Dado que se registra una actividad, cuando se consulta su contenido, entonces agrupa un mínimo de 5 preguntas del curso.
- Dado que una actividad contiene una pregunta, cuando se consulta la pregunta, entonces tiene un enunciado, 3 o 4 opciones y una sola respuesta correcta.

### H2. La plataforma inicia con contenido del curso.

Como niño, quiero encontrar contenido del curso al iniciar, para poder comenzar una actividad.

**Criterios de aceptación**

- Dada una base de datos vacía, cuando se inicia la aplicación, entonces carga una clase de ejemplo, 3 actividades de 5 preguntas del curso y 3 niños ficticios.
- Dada una base de datos que ya contiene datos, cuando se inicia la aplicación, entonces no vuelve a cargar el contenido inicial de ejemplo.

### H3. El niño entra con el código de la clase, su alias y un avatar.

Como niño, quiero identificar mi clase, mi alias y mi avatar, para entrar a la plataforma sin usar correo electrónico.

**Criterios de aceptación**

- Dado el código de una clase, cuando el niño entra a esa clase, entonces puede elegir su alias entre los niños de esa clase.
- Dado que el niño elige un avatar, cuando confirma su selección, entonces el valor guardado es uno de estos seis: `colibri`, `tortuga`, `delfin`, `jaguar`, `buho` o `rana`.

### H4. El niño resuelve una actividad y sabe de inmediato si acertó.

Como niño, quiero responder las preguntas de una actividad y recibir el resultado de cada respuesta, para saber si acerté.

**Criterios de aceptación**

- Dada una pregunta de una actividad, cuando el niño la responde, entonces puede elegir entre 3 o 4 opciones y solo una opción es correcta.
- Dada una opción seleccionada, cuando el niño responde, entonces la plataforma indica si acertó o falló en ese momento.

### H5. La plataforma aplica la regla de la mecánica.

Como niño, quiero jugar con parejas de preguntas y respuestas, para practicar el contenido del curso mediante Memoria de parejas.

**Criterios de aceptación**

- Dada una partida, cuando se muestra el tablero, entonces contiene 6 parejas (12 cartas), cada una formada por el enunciado de una pregunta y su respuesta correcta.
- Dado el contador de fallos de una pareja para un niño, cuando se voltea una de sus cartas sin formar esa pareja, entonces el contador aumenta en 1; cuando el niño descubre la pareja al primer intento, entonces el contador disminuye en 1 sin bajar de 0.
- Dadas las parejas registradas para un niño, cuando comienza la siguiente partida, entonces se usan las 6 con más fallos y, en caso de empate, se priorizan en el orden en que fueron creadas.

### H6. El docente consulta el progreso de cada niño.

Como docente, quiero consultar el progreso de cada niño, para conocer sus resultados en las actividades del curso.

**Criterios de aceptación**

- Dada una actividad que un niño termina, cuando se registra el intento, entonces guarda los aciertos, el total de preguntas, la duración en segundos y la fecha.
- Dado un intento, cuando se calcula el porcentaje de aciertos, entonces el resultado es aciertos dividido por el total de preguntas y multiplicado por 100.
- Dado el progreso de un niño, cuando se calculan sus métricas, entonces el tiempo de juego es la suma de las duraciones de sus intentos y las actividades completadas se cuentan sin repetir.

## Requisitos funcionales

| Código | Requisito | Historia |
| --- | --- | --- |
| RF1 | Cada actividad agrupa al menos 5 preguntas del curso; cada pregunta tiene un enunciado, 3 o 4 opciones y una sola respuesta correcta. | H1 |
| RF2 | Si la base de datos está vacía al iniciar la aplicación, cargar una clase de ejemplo, 3 actividades de 5 preguntas y 3 niños ficticios; no cargar esos datos si ya existen datos en la base. | H2 |
| RF3 | Permitir que el niño entre con el código de clase, elija su alias de la lista de niños de esa clase y seleccione uno de los avatares `colibri`, `tortuga`, `delfin`, `jaguar`, `buho` o `rana`, sin correo electrónico. | H3 |
| RF4 | Al responder una pregunta, indicar si la respuesta elegida es correcta o incorrecta. | H4 |
| RF5 | Registrar un intento al terminar una actividad con aciertos, total de preguntas, duración en segundos y fecha; calcular el porcentaje de aciertos como aciertos / total de preguntas × 100. | H6 |
| RF6 | Mostrar una partida con 6 parejas (12 cartas) de enunciado y respuesta correcta; mantener el contador de fallos por pareja y niño según la regla de la mecánica, y elegir las 6 parejas con más fallos para la siguiente partida, empatando por orden de creación. | H5 |
| RF7 | Calcular el tiempo de juego como la suma de las duraciones de los intentos y contar las actividades completadas sin repetir. | H6 |

## Requisitos no funcionales

| Código | Requisito | Cómo se verifica |
| --- | --- | --- |
| RNF1 | La aplicación web expone sus endpoints y reglas de negocio de forma consistente para el curso Geografía de Colombia y la mecánica Memoria de parejas sin requerir correo electrónico para el niño. | Pruebas de aceptación automatizadas con `pytest` y verificación de endpoints en la API. |
| RNF2 | El código y las rutas de la aplicación cumplen las reglas de estilo y calidad definidas en el proyecto. | Ejecución de `ruff check .` y pruebas unitarias/de aceptación sin errores. |

## Casos límite

- Si la base de datos no está vacía al iniciar, no se vuelve a cargar el contenido inicial.
- El contador de fallos de una pareja no puede disminuir por debajo de 0.
- Si varias parejas tienen el mismo número de fallos, se conserva su orden de creación al priorizarlas.
- Una actividad completada se cuenta una sola vez en la métrica de actividades completadas, aunque tenga más de un intento.

## Fuera de alcance

- Cualquier tipo de actividad distinto de preguntas con 3 o 4 opciones y una respuesta correcta, incluidos los demás tipos indicados en el encargo.
- Autenticación con correo electrónico o contraseña para los niños.

## Criterios de terminado

- Están definidas las seis historias H1–H6 y cada una tiene al menos dos criterios verificables en formato Dado/Cuando/Entonces.
- Las actividades usan preguntas con 3 o 4 opciones y una sola respuesta correcta.
- El contenido inicial, la entrada del niño, la regla de Memoria de parejas, el registro de intentos y las métricas del docente cumplen los criterios de aceptación descritos.

## Dudas abiertas

| Duda | Supuesto |
| --- | --- |
| No se dispone de `specs/dudas-encargo.md` en el paquete consultado; se toman únicamente las definiciones confirmadas en `specs/respuestas-cliente.md`. | Se mantiene la estructura de la tabla con la columna `Supuesto` sin añadir supuestos no confirmados del cliente. |