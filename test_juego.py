from juego_functions import crea_tablero, juega, esta_llena, victoria_vertical_col

def test_crear_tablero():
    tab = crea_tablero(4,3)

    assert tab == [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def test_anyadir_ficha_a_tablero():
    tab = crea_tablero(4, 3)

    juega(tab, 2, 'x')

    assert tab ==[[0,0,0,0],[0,0,0,0],[0,0,0,'x']]

    juega(tab, 1, 'o')

    assert tab ==[[0,0,0,0],[0,0,0,'o'],[0,0,0,'x']]

def test_comprobar_columna_llena():
    tab = crea_tablero(4,3)
    juega(tab,2,'x')
    juega(tab,2,'x')
    juega(tab,2,'x')
    juega(tab,2,'x')

    assert esta_llena(tab,2) == True


    tab1 = crea_tablero(6,7)
    juega(tab, 2, 1)

def test_victoria_vertical_columna():
    tab = crea_tablero(6,7)


    assert victoria_vertical_col(tab,2,"x") == False
    juega(tab,2,'x')
    assert victoria_vertical_col(tab,2,"x") == False
    juega(tab,2,'x')
    assert victoria_vertical_col(tab,2,"x") == False
    juega(tab,2,'x')
    assert victoria_vertical_col(tab,2,"x") == False
    juega(tab,2,'x')
    assert victoria_vertical_col(tab,2,"x") == True

#def test_victoria_horizontal():
#    tab = [[0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0],
#           ["x",0,0,0,0,0,0],
#           ["x",0,0,0,0,0,0],
#           ["x",0,0,0,0,0,0],
#           ["x",0,0,0,0,0,0]]
#
#    assert victoria_horizontal(tab) == True