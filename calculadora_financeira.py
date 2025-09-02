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

      


def calcular_juros_compostos(capital_investido:float, taxa_juros:float, tempo:int) -> tuple:
    return None



def calcular_diferenca_juros(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula a diferença de juros entre o calculo do montante do juros composto e o montante do juros simples a partir de um capital inicial, uma taxa de juros e um período de tempo.

    A fórmula usada para calcular os juros compostos é:
        diferenca_juros = MC - MS
    Onde:
        MC = Montante final do calculo de juros composto
        MS = Montante final do calculo de juros simples

    Parâmetros:
    -----------
    capital_investido : float
        O valor do capital inicial (P). Deve ser um número não negativo.
    
    taxa_juros : float
        A taxa de juros anual (r), expressa em porcentagem (ex: 5 para 5%). Deve ser um número não negativo.

    tempo : float
        O tempo de investimento (t), em anos ou períodos definidos. Deve ser um número não negativo.

    Retorno:
    --------
        float: A diferença entre o montate resultante do calculo do juros composto e o montante do calculo do juros simples, arredondado para 2 casas decimais.
    """
    
    return None