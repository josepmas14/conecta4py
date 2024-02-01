def crea_tablero(cols, rows):
    res = []    
    for i in range(cols):
        res2 = []
        for j in range(rows):
            res2.append(0)
        res.append(res2)
    return res


board=(crea_tablero(6,7))
print(board)
board[5][2]=1
print(board)

def busca_hueco(columna):
    '''
    Buscar la ultima posicion vacía de la columna del tablero
    '''
    res = 5
    for i in range(len(board[0])-1):
        if board[i][columna]!=0:
            res = i-1
    return res

print (busca_hueco(2))