def contar_palabras(texto):
    return len(texto.split())
def test_contar_palabras_basico():
    assert contar_palabras("hola mundo") == 2
def test_contar_palabras_vacio():
    assert contar_palabras("") == 0
def test_contar_palabras_una():
    assert contar_palabras("python") == 1