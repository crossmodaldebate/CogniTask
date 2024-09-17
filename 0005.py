**Trecho 5 (Alta Complexidade): Implementar um algoritmo de busca binária em uma lista ordenada.**

def busca_binaria(dados, valor):

  """Implementa um algoritmo de busca binária em uma lista ordenada."""

  inicio = 0

  fim = len(dados) - 1

  while inicio <= fim:

    meio = (inicio + fim) // 2

    if dados[meio] == valor:

      return meio

    elif dados[meio] < valor:

      inicio = meio + 1

    else:

      fim = meio - 1

  return -1