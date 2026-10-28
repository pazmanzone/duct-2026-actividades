import numpy as np
numeros = np.array([1, 2, 3, 4, 5])
print(numeros)  
print(numeros * 2)
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
a + b          # 11 22 33       suma elemento a elemento
a - b          # 9 18 27        resta
a * b          # 10 40 90       multiplicación
np.mean(a)     # 20.0             promedio
np.sum(a)      # 60               suma total
np.max(a)      # 30               valor maximo
np.min(a)      # 10               valor minimo
np.std(a)      # 8.16...          desviacion estandar
print (np.mean(a))
print (np.sum(a))
print (np.max(a))
print (np.min(a))
print (np.std(a))


import pandas as pd
datos = {
    "nombre": ["Maria", "Juan", "Ana"],
    "idioma": ["espanol", "ingles", "portugues"],
    "nivel": [8, 6, 7]
}
df = pd.DataFrame(datos)
print(df)


df = pd.read_csv("corpus.csv")
print(df.head())     # muestra las primeras 5 filas
df.shape             # (3, 3)   filas x columnas
df.columns           # nombre de las columnas
df.dtypes            # tipo de dato de cada columna
df.describe()        # estadisticas resumidas de las columnas numericas
df.info()            # resumen general: tipos, nulos, memoria
print(df.shape)      
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.info())


import matplotlib.pyplot as plt
palabras = ["sol", "luna", "mar", "cielo", "estrella"]
frecuencias = [45, 32, 60, 28, 15]
plt.bar(palabras, frecuencias)
plt.title("Frecuencia de palabras")
plt.xlabel("Palabra")
plt.ylabel("Frecuencia")
plt.show()


import seaborn as sns
import pandas as pd
df = pd.DataFrame({
    "idioma": ["es", "en", "pt", "fr", "es", "en", "pt"],
    "nivel": [8, 6, 7, 5, 9, 7, 8]

})
sns.boxplot(data=df, x="idioma", y="nivel")
plt.title("Distribucion de niveles por idioma")
plt.show()


import spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp("El analisis de corpus permite estudiar el uso real del lenguaje.")
print(doc)
for token in doc:
    print(f"{token.text:15} {token.pos_:8} {token.dep_:15}")

for token in doc:
    print(f"{token.text:15} {token.lemma_:15}")

    doc = nlp("Gabriel Garcia Marquez escribio en Bogota y Ciudad de Mexico.")
for ent in doc.ents:
    print(f"{ent.text:25} {ent.label_:10}")


from nltk.tokenize import word_tokenize
texto = "El analisis de corpus es fundamental en linguistica computacional."
tokens = word_tokenize(texto)
print(tokens)

from nltk.corpus import stopwords
stop_es = set(stopwords.words('spanish'))

palabras = ["el", "analisis", "de", "corpus", "es", "fundamental"]
filtradas = [p for p in palabras if p not in stop_es]
print(filtradas)

from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("spanish")
print(stemmer.stem("corriendo"))    # corr (no siempre da resultados semanticamente correctos)

print(stemmer.stem("correr"))       # correr

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(["hola mundo", "hola Python"])
print(X)

from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)
print(classifier("El producto es excelente, llegó rápido"))