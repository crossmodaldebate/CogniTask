**Trecho 15 (Média Complexidade): Verificar se um número é primo.**

def eh_primo(numero):

  """Verifica se um número é primo."""

  if numero <= 1:

    return False

  for i in range(2, int(numero**0.5) + 1):

    if numero % i == 0:

      return False

  return True