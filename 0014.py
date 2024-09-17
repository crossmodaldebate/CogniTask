**Trecho 14 (Baixa Complexidade): Calcular a soma dos dígitos de um número.**

def soma_digitos(numero):

  """Calcula a soma dos dígitos de um número."""

  soma = 0

  while numero > 0:

    digito = numero % 10

    soma += digito

    numero //= 10

  return soma