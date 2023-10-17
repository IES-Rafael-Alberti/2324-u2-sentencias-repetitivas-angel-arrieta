import pytest
from src.Ej_0_2 import example


@pytest.mark.parametrize(
    "inEjemplo, outMensaje",
    [
        ("Referencia1", "Hola"),
        ("Referencia2", "Saludos")
    ]
)


def test_example(inEjemplo, outMensaje):
    assert example(inEjemplo) == outMensaje