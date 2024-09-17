**Trecho 28 (Baixa Complexidade): Calcular a distância euclidiana entre dois pontos.**

import math

def distancia_euclidiana(x1, y1, x2, y2):

  """Calcula a distância euclidiana entre dois pontos."""

  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)