**Trecho 26 (Alta Complexidade): Implementar um algoritmo de Kruskal para encontrar a árvore geradora mínima em um grafo.**

class Subconjunto:

  def __init__(self, pai, rank):

    self.pai = pai

    self.rank = rank

def encontrar(subconjuntos, i):

  """Encontra o conjunto ao qual o elemento i pertence."""

  if subconjuntos[i].pai != i:

    subconjuntos[i].pai = encontrar(subconjuntos, subconjuntos[i].pai)

  return subconjuntos[i].pai

def unir(subconjuntos, x, y):

  """Une os conjuntos aos quais os elementos x e y pertencem."""

  raiz_x = encontrar(subconjuntos, x)

  raiz_y = encontrar(subconjuntos, y)

  if subconjuntos[raiz_x].rank < subconjuntos[raiz_y].rank:

    subconjuntos[raiz_x].pai = raiz_y

  elif subconjuntos[raiz_x].rank > subconjuntos[raiz_y].rank:

    subconjuntos[raiz_y].pai = raiz_x

  else:

    subconjuntos[raiz_y].pai = raiz_x

    subconjuntos[raiz_x].rank += 1

def kruskal(grafo):

  """Implementa o algoritmo de Kruskal para encontrar a árvore geradora mínima em um grafo."""

  arestas = []

  for u in grafo:

    for v, peso in grafo[u].items():

      arestas.append((peso, u, v))

  arestas.sort()

  arvore = []

  subconjuntos = [Subconjunto(i, 0) for i in range(len(grafo))]

  for peso, u, v in arestas:

    if encontrar(subconjuntos, u) != encontrar(subconjuntos, v):

      arvore.append((u, v, peso))

      unir(subconjuntos, u, v)

  return arvore