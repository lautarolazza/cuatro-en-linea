from src.prototipo import soltar_ficha, tablero_vacio

def test_soltar_ficha():
    tablero = tablero_vacio()
    secuencia = [1, 1, 1, 1, 1, 1]

    tablero = soltar_ficha(1, tablero, secuencia)

    assert tablero == [
        [2, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0]
    ]

    secuencia = [5, 5, 5, 5, 5, 5]
    tablero = soltar_ficha(1, tablero, secuencia)

    assert tablero == [
        [2, 0, 0, 0, 2, 0, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [2, 0, 0, 0, 2, 0, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [2, 0, 0, 0, 2, 0, 0],
        [1, 0, 0, 0, 1, 0, 0]
    ]

