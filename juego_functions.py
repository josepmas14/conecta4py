def crea_tablero(fila, columna):
    salida = []    
    for i in range(columna):
        lista2 = []
        for j in range(fila):
            lista2.append(0)
        salida.append(lista2)
    return salida

print(crea_tablero(4,3))