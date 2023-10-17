from src.Ej_5_2 import inversion


def test_inversion():
    assert inversion(900, 15, 3) == ("Año 1 -- 1035.0\nAño 2 -- 1190.25\nAño 3 -- 1368.79\n")
