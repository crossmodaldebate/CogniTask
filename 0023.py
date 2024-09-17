**Trecho 23 (Alta Complexidade): Implementar um algoritmo de ordenação rápida (quicksort).**

def quicksort(dados):

  """Implementa um algoritmo de ordenação rápida (quicksort)."""

  if len(dados) <= 1:

    return dados

  pivo = dados[len(dados) // 2]

  menores = [x for x in dados if x < pivo]

  iguais = [x for x in dados if x == pivo]

  maiores = [x for x in dados if x > pivo]

  return quicksort(menores) + iguais + quicksort(maiores)