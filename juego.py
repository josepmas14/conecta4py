

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
        if board[columna][i]!=0:
            res = i-1
    return res

print (busca_hueco(2))