from src.prototipo import contenido_fila

def test_contenido_fila():
    tablero = [
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0],  
            [1, 2, 1, 2, 1, 2, 1],  
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0]   
              ]
    assert [1, 2, 1, 2, 1, 2, 1] == contenido_fila(3, tablero)
