def crea_tablero(fila, columna):
    salida = []    
    for i in range(columna):
        lista2 = []
        for j in range(fila):
            lista2.append(0)
        salida.append(lista2)
    return salida



def juega (tablero, columna, ficha):
    '''
    elegir la columna del tablero
    recorrer la columna de atrás a adelante
    al encontrar el primer 0 pones la ficha
    '''

    c = tablero[columna]

    indice = len(c)-1
    while indice >= 0:
        if c[indice] == 0:
            c[indice] = ficha
            break
        indice -= 1