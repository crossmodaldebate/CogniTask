**Trecho 1 (Baixa Complexidade): Cálculo da média de uma lista de números.**

def calcular_media(dados):

  """Calcula a média de uma lista de números."""

  if len(dados) == 0:

    return 0

  return sum(dados) / len(dados)