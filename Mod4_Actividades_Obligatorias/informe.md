# Informe: Módulo IV, Clase 2

## 1. ¿Qué palabras aparecen en el top 10 de la Secuencia A del Ejercicio 2 pero desaparecen en la Secuencia B? ¿Por qué desaparecen?

Desaparecen las diez palabras del top 10 de la Secuencia A: **"de", "que", "la", "el", "y", "los", "en", "es", "un", "las"**.

Desaparecen porque todas están incluidas en el conjunto `STOP_WORDS`. En la Secuencia B, el condicional `if token not in STOP_WORDS` descarta esas palabras antes de contarlas, por lo que nunca se agregan al diccionario `frecuencias_sin_stopwords`.

Como resultado, el top 10 de la Secuencia B pasa a estar encabezado por palabras con contenido propio del texto: "biblioteca" (27), "libros" (20), "libro" (17), "hexágono" (13) y "hombres" (10). También aparecen "o", "pero", "cada", "todos" y "hay", que son palabras funcionales que no están incluidas en `STOP_WORDS`, por lo que el filtro no las elimina.

## 2. Comparando el Ejercicio 1 con el Ejercicio 2: ¿cambia el resultado por usar `tokenizar()` en lugar de `.split()`? ¿En qué casos se nota la diferencia?

Sí, el resultado cambia, aunque de forma leve:

| Palabra | Ejercicio 1 (`.split()`) | Ejercicio 2 (`tokenizar()`) | Diferencia |
|---|---|---|---|
| que | 104 | 106 | +2 |
| y | 64 | 67 | +3 |
| los | 65 | 66 | +1 |
| un | 38 | 39 | +1 |
| de, la, el, en, es, las | igual | igual | 0 |

`.split()` separa el texto únicamente por espacios, de modo que si un signo de puntuación está pegado a una palabra, el token resultante es distinto. Por ejemplo, `(que` y `que` se cuentan como dos palabras diferentes. La función `tokenizar()` reemplaza por una cadena vacía todos los signos de `string.punctuation`:

```
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

Así, esas variantes se unifican y suman a la palabra correcta.

**Casos concretos del texto:**

- **que:** en "El universo (que otros llaman la Biblioteca)" el token con `.split()` es `(que`.
- **y:** hay casos con paréntesis pegado, como `(y` en "(y no escribió)" y en "(y aun la humilde...)", y un caso seguido de coma (`y,`).

La diferencia también altera el ranking: con `.split()`, "los" (65) queda por encima de "y" (64), mientras que con `tokenizar()` "y" (67) pasa por encima de "los" (66).

## 3. ¿Qué relación encontrás entre la línea que faltaba completar en el Ejercicio 1 y las dos líneas que faltaba completar en el Ejercicio 2? ¿Por qué se repite la misma lógica dos veces en el Ejercicio 2?

La relación es que en ambos ejercicios se trabaja con el mismo archivo de texto, *La biblioteca de Babel*, y en ambos se completa una línea que **guarda el resultado de una operación en una variable**.

**Ejercicio 1.** La línea a completar era la apertura del archivo con la función integrada `open()`, dentro de una sentencia `with`, que lo deja disponible con el nombre `archivo`. Recibe tres parámetros:

- el nombre o ruta del archivo (`"la_biblioteca_de_babel.txt"`),
- el modo de apertura (`"r"`, lectura), que exige que el archivo exista para no generar un error,
- la codificación (`encoding="utf-8"`), para que se lean bien las tildes y los caracteres especiales.

**Ejercicio 2.** Se abre el mismo archivo con el mismo `open()` y su contenido se guarda en la variable `texto` mediante `archivo.read()`. Ese texto se divide en tokens con `tokenizar()` y los tokens se cuentan en dos diccionarios: uno con **todas** las palabras (`frecuencias_todas`) y otro con todas las palabras **menos** las incluidas en `STOP_WORDS` (`frecuencias_sin_stopwords`).

**Por qué la lógica se repite dos veces.** Las dos líneas que faltaba completar en el Ejercicio 2 son la misma operación aplicada a un diccionario distinto:

```python
frecuencias_todas[token] = frecuencias_todas.get(token, 0) + 1
frecuencias_sin_stopwords[token] = frecuencias_sin_stopwords.get(token, 0) + 1
```

El método `.get()` recibe dos parámetros: la clave (`token`) y un valor por defecto (`0`). Devuelve la cantidad de veces que la palabra apareció hasta ese momento, o `0` si es la primera vez que aparece, y a ese valor se le suma 1. La única diferencia entre ambos conteos es que el segundo está dentro de un `if token not in STOP_WORDS`, que deja afuera las palabras vacías.

En ambos casos el bucle `for` no es infinito: termina cuando recorre todos los tokens del texto.

**Conclusión.** En el Ejercicio 1 se asigna a `archivo` el resultado de abrir el archivo, y en el Ejercicio 2 se asigna a cada diccionario el resultado de `.get()`. Es el mismo patrón, guardar el resultado de una operación en una variable, aplicado primero a la lectura del archivo y después al conteo de palabras.

