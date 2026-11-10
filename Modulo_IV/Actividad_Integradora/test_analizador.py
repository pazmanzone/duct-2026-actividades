from analizador import contar_frecuencias
def test_frecuencias_basico():
    resultado = contar_frecuencias("palabras mercado palabras")
    assert resultado["palabras"] == 2
    assert resultado["mercado"] == 1
def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}
def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Palabras palabras PALABRAS")
    assert resultado["palabras"] == 3