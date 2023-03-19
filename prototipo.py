import sys

def validar_secuencia(secuencia):
    for num in secuencia:
        if num > 7:
            print(f"El número {num} no es un número válido, los números de las columnas donde se sueltan las fichas deben ser menores que 7")
            sys.exit()
    return None

def contenido_columna(numero_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[numero_columna - 1]
        columna.append(celda)
    return columna

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
ficha = 0
columna = 0
secuencia = [1, 2, 3, 1, 3, 4, 5]

validar_secuencia(secuencia)
soltar_ficha(columna, tablero, secuencia)
imprimir_tablero(tablero)

print(contenido_columna(1, tablero))