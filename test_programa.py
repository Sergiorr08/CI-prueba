import pytest
from programa import es_primo  # Reemplaza 'tu_archivo' con el nombre del archivo donde está la función

@pytest.mark.parametrize("numero, esperado", [
    (2, True),    # Caso base: el número primo más pequeño
    (3, True),    # Otro número primo pequeño
    (4, False),   # Número compuesto
    (5, True),    # Primo
    (10, False),  # Número par no primo
    (17, True),   # Número primo
    (19, True),   # Número primo
    (20, False),  # Número compuesto
    (23, True),   # Número primo
    (25, False),  # Cuadrado de un primo (5 * 5)
    (29, True),   # Número primo
    (97, True),   # Primo grande
    (100, False), # Número compuesto grande
    (1, False),   # 1 no es primo
    (0, False),   # 0 no es primo
    (-5, False),  # Números negativos no son primos
    (-11, False)  # Números negativos no son primos
])
def test_es_primo(numero, esperado):
    assert es_primo(numero) == esperado
