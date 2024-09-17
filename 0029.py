**Trecho 29 (Média Complexidade): Converter um número decimal para binário.**

def decimal_para_binario(numero):

  """Converte um número decimal para binário."""

  if numero == 0:

    return "0"

  binario = ""

  while numero > 0:

    resto = numero % 2

    binario = str(resto) + binario

    numero //= 2

  return binario