**Trecho 13 (Média Complexidade): Encontrar o segundo maior valor em uma lista de números.**

def encontrar_segundo_maior(dados):

  """Encontra o segundo maior valor em uma lista de números."""

  if len(dados) < 2:

    return None

  maior = max(dados[0], dados[1])

  segundo_maior = min(dados[0], dados[1])

  for i in range(2, len(dados)):

    if dados[i] > maior:

      segundo_maior = maior

      maior = dados[i]

    elif dados[i] > segundo_maior and dados[i] != maior:

      segundo_maior = dados[i]

  return segundo_maior