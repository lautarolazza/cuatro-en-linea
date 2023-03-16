def soltar_ficha(columna, tablero, secuencia):
    ficha = 1
    for i in range(len(secuencia)):
        columna = secuencia[i]
        for fila in range(6, 0, -1):
            if tablero[fila - 1][columna - 1] == 0:
                tablero[fila - 1][columna - 1] = ficha
                ficha = 2 if ficha == 1 else 1
                break
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero: 
        for elemento in fila:
            print(elemento, end=' ')
        print()

tablero = [
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0]   
              ]
ficha = "9"
columna = 0
secuencia = [1, 2, 3, 1]

soltar_ficha(columna, tablero, secuencia)

imprimir_tablero(tablero)