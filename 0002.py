**Trecho 2 (Baixa Complexidade): Encontrar o maior valor em uma lista de números.**

def encontrar_maior(dados):

  """Encontra o maior valor em uma lista de números."""

  if len(dados) == 0:

    return None

  maior = dados[0]

  for valor in dados:

    if valor > maior:

      maior = valor

  return maior