**Trecho 22 (Baixa Complexidade): Calcular o máximo divisor comum (MDC) de dois números.**

def mdc(a, b):

  """Calcula o máximo divisor comum (MDC) de dois números."""

  while b:

    a, b = b, a % b

  return a