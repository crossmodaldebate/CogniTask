**Trecho 6 (Alta Complexidade): Implementar um algoritmo de ordenação por mesclagem.**

def ordenacao_por_mesclagem(dados):

  """Implementa um algoritmo de ordenação por mesclagem."""

  if len(dados) <= 1:

    return dados

  meio = len(dados) // 2

  esquerda = ordenacao_por_mesclagem(dados[:meio])

  direita = ordenacao_por_mesclagem(dados[meio:])

  return mesclar(esquerda, direita)

def mesclar(esquerda, direita):

  """Mescla duas listas ordenadas em uma única lista ordenada."""

  resultado = []

  i = 0

  j = 0

  while i < len(esquerda) and j < len(direita):

    if esquerda[i] < direita[j]:

      resultado.append(esquerda[i])

      i += 1

    else:

      resultado.append(direita[j])

      j += 1

  resultado += esquerda[i:]

  resultado += direita[j:]

  return resultado