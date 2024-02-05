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

def esta_llena(tablero, columna):
    '''
    recorremos todos los elementos de la columna
    si algún elemento es 0, res es falso
    si todos los elementos son diferents de 0, res es verdadero
    '''
    c = tablero[columna]
    return 0 not in c

#def victoria_vertical(tablero):
#    victoria = False
#    i = 0
#    while (i<=(len(tablero)-1)) and victoria == False:
#        j = 0
#        while (j<=(len(tablero[i])-4)):
#            if(tablero[i][j]==tablero[i][j+1] and tablero[i][j]==tablero[i][j+2] and tablero[i][j]==tablero[i][j+3]) and tablero[i][j]!=0:
#                victoria = True
#            j+=1
#        i+=1
#    return victoria

def victoria_vertical_col(tablero, pos_columna,ficha):
    contador_iguales = 0
    columna = tablero[pos_columna]
    ix = 0
    while ix < len(columna):
        if columna[ix] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0
        
        if contador_iguales == 4:
            return True
        ix += 1
    return False

def victoria_horizontal_fila(tablero, pos_fila, ficha):
    contador_iguales = 0

    for columna in tablero:
        if columna[pos_fila] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0
        
        if contador_iguales == 4:
            return True
    return False


def victoria (tablero, ficha):
    '''
    Obtener el número de columnas de mi tablero
    iterar robre range(num_columnas)
    para cada columna, devolver True si es true
    si es false ir a la siguiente
    '''
    num_cols = len(tablero)
    num_filas = len(tablero[0])
    for num_col in range(num_cols):
        
        if victoria_vertical_col(tablero,num_col,ficha):
            return True
    for num_fila in range(num_filas):
        if victoria_horizontal_fila(tablero,num_fila,ficha):
            return True
    return False
        

#def victoria_horizontal(tablero):
#    victoria = False 
#
#    i = 0
#    while i < len(tablero) - 3:
#        j = 0
#        while j < len(tablero[0]):
#            if tablero[i][j] == tablero[i + 1][j] == tablero[i + 2][j] == tablero[i + 3][j] and tablero[i][j] != 0:
#                victoria = True
#            j += 1
#        i += 1
#
#    return victoria
