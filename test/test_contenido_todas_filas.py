from src.prototipo import contenido_todas_filas 

def test_contenido_todas_filas():
        tablero = [
            [2, 1, 0, 1, 2, 0, 1],
            [1, 2, 0, 2, 1, 0, 2],
            [2, 1, 0, 1, 2, 0, 1],
            [1, 2, 0, 2, 1, 0, 2],
            [2, 1, 0, 1, 2, 0, 1],
            [1, 2, 0, 2, 1, 0, 2]
              ]
        assert [[2, 1, 0, 1, 2, 0, 1], [1, 2, 0, 2, 1, 0, 2], [2, 1, 0, 1, 2, 0, 1], [1, 2, 0, 2, 1, 0, 2], [2, 1, 0, 1, 2, 0, 1], [1, 2, 0, 2, 1, 0, 2]] == contenido_todas_filas(tablero)