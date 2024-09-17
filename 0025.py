**Trecho 25 (Baixa Complexidade): Verificar se uma string é um pangrama (contém todas as letras do alfabeto).**

import string

def eh_pangrama(texto):

  """Verifica se uma string é um pangrama (contém todas as letras do alfabeto)."""

  texto = texto.lower()

  for letra in string.ascii_lowercase:

    if letra not in texto:

      return False

  return True