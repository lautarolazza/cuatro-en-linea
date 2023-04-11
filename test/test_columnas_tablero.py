
from src.prototipo import contenido_columna

def test_contenido_columna():
    tablero = [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0]
              ]
    assert [2, 1, 2, 1, 1, 2] == contenido_columna(4, tablero)
