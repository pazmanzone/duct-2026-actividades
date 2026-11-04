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
resultado = contar_palabras("Hola mundo hola")
print(resultado)

import spacy
nlp = spacy.load("es_core_news_sm")
def analizar_texto(texto):
    doc = nlp(texto)
    print(f"DEBUG: texto original = '{texto}'")
    print(f"DEBUG: tokens = {[token.text for token in doc]}")
    print(f"DEBUG: lemas = {[token.lemma_ for token in doc]}")
    print(f"DEBUG: POS tags = {[token.pos_ for token in doc]}")
    return doc
doc = analizar_texto("Los gatos duermen en la casa.")

import spacy
nlp = spacy.load("es_core_news_sm")
def procesar_corpus(textos):
    resultados = []
    for texto in textos:
        doc = nlp(texto)
        entidades = [(ent.text, ent.label_) for ent in doc.ents]
        resultados.append(entidades)
    return resultados
textos = ["Juan vive en Buenos Aires", "Maria trabaja en Google"]
resultados = procesar_corpus(textos)
print(resultados)