**Trecho 20 (Alta Complexidade): Implementar um algoritmo de Dijkstra para encontrar o caminho mais curto em um grafo.**

import heapq

def dijkstra(grafo, inicio, fim):

  """Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto em um grafo."""

  distancias = {no: float('inf') for no in grafo}

  distancias[inicio] = 0

  predecessores = {}

  fila_prioridade = [(0, inicio)]

  while fila_prioridade:

    distancia_atual, no_atual = heapq.heappop(fila_prioridade)

    if no_atual == fim:

      break

    if distancia_atual > distancias[no_atual]:

      continue

    for vizinho, peso in grafo[no_atual].items():

      nova_distancia = distancia_atual + peso

      if nova_distancia < distancias[vizinho]:

        distancias[vizinho] = nova_distancia

        predecessores[vizinho] = no_atual

        heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

  return distancias, predecessores