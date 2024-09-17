**Trecho 8 (Média Complexidade): Contar a frequência de cada palavra em um texto.**

def contar_palavras(texto):

  """Conta a frequência de cada palavra em um texto."""

  palavras = texto.lower().split()

  frequencia = {}

  for palavra in palavras:

    if palavra in frequencia:

      frequencia[palavra] += 1

    else:

      frequencia[palavra] = 1

  return frequencia