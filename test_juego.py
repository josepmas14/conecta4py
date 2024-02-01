from juego_functions import crea_tablero

def test_crear_tablero():
    tab = crea_tablero(4,3)

    assert tab == [[0,0,0,0],[0,0,0,0],[0,0,0,0]]