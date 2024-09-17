**Trecho 21 (Média Complexidade): Implementar um algoritmo de busca em largura em um grafo.**

from collections import deque

def busca_em_largura(grafo, inicio):

  """Implementa um algoritmo de busca em largura em um grafo."""

  visitados = set([inicio])

  fila = deque([inicio])

  while fila:

    no_atual = fila.popleft()

    print(no_atual)  # Ou realize alguma operação com o nó atual

    for vizinho in grafo[no_atual]:

      if vizinho not in visitados:

        visitados.add(vizinho)

        fila.append(vizinho)