**Trecho 19 (Média Complexidade): Verificar se duas strings são anagramas.**

def sao_anagramas(texto1, texto2):

  """Verifica se duas strings são anagramas."""

  texto1 = texto1.lower().replace(" ", "")

  texto2 = texto2.lower().replace(" ", "")

  return sorted(texto1) == sorted(texto2)