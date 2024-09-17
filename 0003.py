**Trecho 3 (Média Complexidade): Ordenar uma lista de números em ordem crescente.**

def ordenar_lista(dados):

  """Ordena uma lista de números em ordem crescente."""

  for i in range(len(dados)):

    for j in range(i + 1, len(dados)):

      if dados[i] > dados[j]:

        dados[i], dados[j] = dados[j], dados[i]

  return dados