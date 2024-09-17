**Trecho 17 (Média Complexidade): Encontrar o elemento que aparece mais vezes em uma lista.**

def elemento_mais_frequente(dados):

  """Encontra o elemento que aparece mais vezes em uma lista."""

  frequencia = {}

  for elemento in dados:

    if elemento in frequencia:

      frequencia[elemento] += 1

    else:

      frequencia[elemento] = 1

  mais_frequente = None

  maior_frequencia = 0

  for elemento, freq in frequencia.items():

    if freq > maior_frequencia:

      mais_frequente = elemento

      maior_frequencia = freq

  return mais_frequente