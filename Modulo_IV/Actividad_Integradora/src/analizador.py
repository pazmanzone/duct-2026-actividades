import string
from pathlib import Path

import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_TEXTO = BASE_DIR / "data" / "texto_integradora.txt"
RUTA_GRAFICO = BASE_DIR / "outputs" / "grafico_frecuencias.png"


STOP_WORDS = {
    "el", "la", "los", "las", "de", "del", "y", "a", "en", "un", "una",
    "que", "es", "por", "con", "no", "se", "su", "al", "lo", "como",
}



def tokenizar(texto):
    """
    Convierte el texto a minusculas, quita los signos de puntuacion
    y lo separa en una lista de palabras (tokens).

    Parametros:
        texto (str): texto crudo a procesar

Retorna:
        list[str]: lista de tokens limpios
    """
    texto = texto.lower()

    for signo in string.punctuation:
        texto = texto.replace(signo, "")   
    return texto.split()


def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra del texto,
    excluyendo las stopwords.

    Parámetros:
        texto (str): texto que se desea analizar.

    Retorna:
        dict: diccionario con cada palabra y su frecuencia.
    """
    palabras_texto = tokenizar(texto)

    frecuencias = {}

    for palabra in palabras_texto:
        if palabra not in STOP_WORDS:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias



def analizar_y_visualizar(ruta=RUTA_TEXTO, top_n=10):
    """
    Lee un archivo de texto, cuenta la frecuencia de cada palabra
    y genera un grafico de barras horizontales con las top_n
    palabras mas frecuentes.

    Parametros:
        ruta (str): ruta al archivo de texto a analizar
        top_n (int): cantidad de palabras a graficar

    """
    # 1. Abrir y leer el archivo de texto

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

    except (FileNotFoundError, PermissionError):
        print("No se pudo acceder al archivo. Verifique que la ruta sea correcta y que tenga permisos de lectura.")
        return 

    # 2. Contar la frecuencia de cada palabra
    
    frecuencias_sin_stopwords = contar_frecuencias(texto)

    # 3. Obtener las top_n palabras mas frecuentes

    top10 = sorted(frecuencias_sin_stopwords.items(), key=lambda x: x[1], reverse=True)[:top_n]

    palabras = [palabra for palabra, frecuencia in top10]
    valores = [frecuencia for palabra, frecuencia in top10]

    # 4. Generar el grafico de barras horizontales

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color='skyblue')
    plt.title(f"Top {top_n} palabras de contenido mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabras")

    # 5. Guardar el grafico como imagen y mostrarlo

    RUTA_GRAFICO.parent.mkdir(exist_ok=True)
    plt.savefig(RUTA_GRAFICO)
    plt.show()