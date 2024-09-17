**Trecho 4 (Média Complexidade): Verificar se uma string é um palíndromo.**

def eh_palindromo(texto):

  """Verifica se uma string é um palíndromo."""

  texto = texto.lower().replace(" ", "")

  return texto == texto[::-1]