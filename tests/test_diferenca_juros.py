import pytest
from calculadora_financeira import calcular_diferenca_juros



# Teste com valores válidos
def test_valores_validos():
    assert calcular_diferenca_juros(1000, 5, 2) == 2.5

def test_todos_zeros ():
    assert calcular_diferenca_juros (0,0,0) ==0.0

def  test_juros_e_tempo_zero ():
    assert calcular_diferenca_juros(1000,0,0) == 0.0

def test_tempo_zero():
    assert calcular_diferenca_juros(1000, 5, 0) == 0.0

def test_taxa_zero():
    assert calcular_diferenca_juros(1000, 0, 5) == 0.0

def test_numero_decimal():
    assert calcular_diferenca_juros(1500.50, 4.5, 3.2) == 34.57

# Testes com entradas inválidas
def test_entrada_string():
    with pytest.raises(ValueError,match="Valor Inválido"):
           calcular_diferenca_juros("ola", 5, 2)


def test_capital_negativo():
    with pytest.raises(ValueError,match="Valor Inválido"):
        calcular_diferenca_juros(-1000,5,2)

def test_taxa_negativa ():
        with pytest.raises(ValueError,match="Valor Inválido"):
             calcular_diferenca_juros(1000,-5,2)

def test_tempo_negativo ():
     with pytest.raises(ValueError,match="Valor Inválido"):
          calcular_diferenca_juros(1000,5,-2)
