import pytest
from calculadora_financeira import calcular_juros_compostos


# Teste com valor inválido
def test_calcular_juros_entrada_invalida():
    with pytest.raises(ValueError, match="O capital investido deve ser um número"):
        calcular_juros_compostos("ola", 10, 5)

# Teste com entrada básica
def test_calcular_juros_entrada_basica():
    juros, montante = calcular_juros_compostos(200, 10, 5)
    assert round(juros, 2) == 122.10
    assert round(montante, 2) == 322.10


# Teste com valor inválido na taxa de juros
def test_calcular_juros_juros_invalido():
    with pytest.raises(ValueError, match="A taxa de juros deve ser um número"):
        calcular_juros_compostos(100, "oi", 5)

# Teste com numero negativo na capital
def test_calcular_capital_numero_negativo():
    with pytest.raises(ValueError, match="O capital investido não pode ser negativo."):
        calcular_juros_compostos(-100, 10, 5)


# Tete com numero negativo no juros
def test_calcular_juros_numero_negativo():
    with pytest.raises(ValueError, match="A taxa de juros não pode ser negativa."):
        calcular_juros_compostos(100, -10, 5)

# Teste com o tempo (string)
def test_calcular_juros_tempo_string():
    with pytest.raises(ValueError, match="O tempo deve ser um número"):
        calcular_juros_compostos(100, 10, "alex")

# Teste com numero negativo
def test_calcular_juros_tempo_negativo():
    with pytest.raises(ValueError, match="O tempo não pode ser negativo."):
        calcular_juros_compostos(100, 10, -1)

# Testando com tudo 0
def test_calcular_juros_tudo_zero_erro():
    with pytest.raises(ValueError, match="não podem ser zero"):
        calcular_juros_compostos(0, 0, 0)

# Teste com string (Deve ser int ou float)
def test_calcular_juros_capital_invalido_fail():
    # Aqui a função levanta "O capital investido deve ser um número (int ou float)."
    # mas o match não bate, então o teste vai FALHAR de propósito.
    with pytest.raises(ValueError, match="Mensagem errada"):
        calcular_juros_compostos("ola", 10, 5)

# Teste com valor entrada básica
def test_fail_entrada_basica():
    juros, montante = calcular_juros_compostos(200, 10, 5)
    assert round(juros, 2) == 999.99
    assert round(montante, 2) == 111.11

# Teste com taxa de juros inválida
def test_fail_taxa_invalida():
    with pytest.raises(ValueError, match="Taxa inválida qualquer"):
        calcular_juros_compostos(100, "oi", 5)


# Teste com  a capital  negativa
def test_fail_capital_negativo():
    with pytest.raises(ValueError, match="Capital não pode ser menor que zero!!!"):
        calcular_juros_compostos(-100, 10, 5)

# Teste com taxa de juros negativa
def test_fail_taxa_negativa():
    with pytest.raises(ValueError, match="Taxa errada"):
        calcular_juros_compostos(100, -10, 5)

# Test com tempo negativo
def test_fail_tempo_negativo():
    with pytest.raises(ValueError, match="tempo negativo errado"):
        calcular_juros_compostos(100, 10, -1)