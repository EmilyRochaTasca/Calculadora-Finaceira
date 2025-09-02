"""
Módulo para cálculos financeiros básicos.
"""

def calcular_juros_simples(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula o montante final de um investimento com base na fórmula de juros simples.

    Esta função aplica a taxa de juros sobre o capital inicial durante o
    período especificado e retorna a soma do capital com os juros acumulados.

    A fórmula utilizada é: M = C * (1 + (i * t)), onde:
      - M = Montante final
      - C = Capital inicial
      - i = Taxa de juros (em formato decimal)
      - t = Tempo

    Args:
        capital_inicial (float): O valor do capital inicial a ser investido.
            Ex: 1000.00
        taxa_anual (float): A taxa de juros anual em formato percentual.
            Ex: 5 para 5%
        tempo_anos (float): O período do investimento, em anos. Pode ser fracionado.
            Ex: 2.5 para dois anos e meio.

    Returns:
        float: O montante final (capital + juros), arredondado para 2 casas decimais.

    Raises:
        ValueError: Se qualquer um dos argumentos (capital, taxa, tempo)
            for um valor negativo.

    Example:
        >>> calcular_juros_simples(1000.00, 5.0, 2.0)
        1100.00
        >>> calcular_juros_simples(2500.00, 3.5, 10.0)
        3375.00
    """
  # Validação de tipos: apenas int ou float
    if not isinstance(capital_inicial, (int, float)):
        raise TypeError("Todos os parâmetros devem ser números (int ou float).")
    if not isinstance(taxa_anual, (int, float)):
        raise TypeError("Todos os parâmetros devem ser números (int ou float).")
    if not isinstance(tempo_anos, (int, float)):
        raise TypeError("Todos os parâmetros devem ser números (int ou float).")

    # Validação de valores não-negativos
    if capital_inicial < 0 or taxa_anual < 0 or tempo_anos < 0:
        raise ValueError("O principal, a taxa e o tempo devem ser valores não-negativos.")

    # Cálculo do montante com juros simples
    montante = capital_inicial * (1 + (taxa_anual / 100) * tempo_anos)

    return round(montante, 2)
      


def calcular_juros_compostos(capital_investido:float, taxa_juros:float, tempo:int) -> tuple:
    # Validação do capital investido
    if not isinstance(capital_investido, (int, float)):
        raise ValueError("O capital investido deve ser um número (int ou float).")
    if capital_investido < 0:
        raise ValueError("O capital investido não pode ser negativo.")

    # Validação da taxa de juros
    if not isinstance(taxa_juros, (int, float)):
        raise ValueError("A taxa de juros deve ser um número (int ou float).")
    if taxa_juros < 0:
        raise ValueError("A taxa de juros não pode ser negativa.")

    # Validação do tempo
    if not isinstance(tempo, (int, float)):
        raise ValueError("O tempo deve ser um número (int ou float).")
    if tempo < 0:
        raise ValueError("O tempo não pode ser negativo.")

    # Cálculo dos juros compostos
    montante = capital_investido * (1 + taxa_juros / 100) ** tempo
    juros = montante - capital_investido
    
    return juros, montante




def calcular_diferenca_juros(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula a diferença de juros entre o cálculo do montante de juros composto e o montante de juros simples,
    dado um capital inicial, uma taxa de juros anual e um período de tempo.

    Args:
        capital_inicial (float): O valor do capital inicial. Deve ser um número não negativo.
        taxa_anual (float): A taxa de juros anual em porcentagem (ex: 5 para 5%). Deve ser um número não negativo.
        tempo_anos (float): O tempo do investimento em anos. Deve ser um número não negativo.

    Returns:
        float: A diferença entre o montante com juros compostos e o montante com juros simples, arredondado para 2 casas decimais.

    Raises:
        TypeError: Se qualquer argumento não for número (int ou float).
        ValueError: Se qualquer argumento for número negativo.
    """

    # Verifica se todos os parâmetros são do tipo numérico (int ou float)
    if not isinstance(capital_inicial, (int, float)):
        raise TypeError("capital_inicial deve ser um número (int ou float).")
    if not isinstance(taxa_anual, (int, float)):
        raise TypeError("taxa_anual deve ser um número (int ou float).")
    if not isinstance(tempo_anos, (int, float)):
        raise TypeError("tempo_anos deve ser um número (int ou float).")

    # Verifica se os valores são não negativos
    if capital_inicial < 0:
        raise ValueError("capital_inicial não pode ser negativo.")
    if taxa_anual < 0:
        raise ValueError("taxa_anual não pode ser negativo.")
    if tempo_anos < 0:
        raise ValueError("tempo_anos não pode ser negativo.")

    # Calcula o montante com juros simples
    montante_juros_simples = calcular_juros_simples(capital_inicial, taxa_anual, tempo_anos)

    # Calcula o montante com juros compostos
    _, montante_juros_compostos = calcular_juros_compostos(capital_inicial, taxa_anual, tempo_anos)

    # Calcula a diferença entre os dois montantes
    diferenca = montante_juros_compostos - montante_juros_simples

    # Retorna a diferença arredondada para 2 casas decimais
    return round(diferenca, 2)
