**Trecho 27 (Média Complexidade): Encontrar a mediana de uma lista de números.**

def mediana(dados):

  """Encontra a mediana de uma lista de números."""

  dados_ordenados = sorted(dados)

  n = len(dados_ordenados)

  if n % 2 == 0:

    return (dados_ordenados[n // 2 - 1] + dados_ordenados[n // 2]) / 2

  else:

    return dados_ordenados[n // 2]