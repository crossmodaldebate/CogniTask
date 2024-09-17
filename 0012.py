**Trecho 12 (Alta Complexidade): Implementar uma pilha utilizando uma lista.**

class Pilha:

  """Implementa uma pilha utilizando uma lista."""

  def __init__(self):

    self.itens = []

  def empilhar(self, item):

    """Adiciona um item ao topo da pilha."""

    self.itens.append(item)

  def desempilhar(self):

    """Remove e retorna o item do topo da pilha."""

    if not self.esta_vazia():

      return self.itens.pop()

    else:

      return None

  def esta_vazia(self):

    """Verifica se a pilha está vazia."""

    return len(self.itens) == 0