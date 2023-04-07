from src.prototipo import contenido_todas_columnas

def test_contenido_todas_las_columnas():
        tablero = [
            [2, 1, 0, 1, 2, 0, 1],
            [1, 2, 0, 2, 1, 0, 2],
            [2, 1, 0, 1, 2, 0, 1],
            [1, 2, 0, 2, 1, 0, 2],
            [2, 1, 0, 1, 2, 0, 1],
            [1, 2, 0, 2, 1, 0, 2]
              ]
        assert [[2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2], [0, 0, 0, 0, 0, 0], [1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1], [0, 0, 0, 0, 0, 0], [1, 2, 1, 2, 1, 2]] == contenido_todas_columnas(tablero)