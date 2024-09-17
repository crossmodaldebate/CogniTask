**Trecho 10 (Baixa Complexidade): Calcular o fatorial de um número.**

def calcular_fatorial(n):

  """Calcula o fatorial de um número."""

  if n == 0:

    return 1

  else:

    return n * calcular_fatorial(n - 1)