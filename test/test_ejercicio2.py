from src.ejercicio2 import significado_fruta

def test_significado_fruta():
    cadena = [1,2,3]
    resultado = significado_fruta(cadena)

    assert resultado == cadena