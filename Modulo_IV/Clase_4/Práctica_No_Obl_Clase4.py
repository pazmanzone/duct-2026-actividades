def contar_palabras(texto):
    palabras = texto.split()
    print(f"DEBUG: texto recibido = '{texto}'")
    print(f"DEBUG: cantidad de palabras = {len(palabras)}")
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        print(f"DEBUG: procesando '{palabra}', frecuencia actual = {frecuencias.get(palabra, 0)}")
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    print(f"DEBUG: resultado final = {frecuencias}")
    return frecuencias