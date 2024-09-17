**Trecho 9 (Média Complexidade): Verificar se uma lista está ordenada em ordem crescente.**

def esta_ordenada(dados):

  """Verifica se uma lista está ordenada em ordem crescente."""

  for i in range(len(dados) - 1):

    if dados[i] > dados[i + 1]:

      return False

  return True