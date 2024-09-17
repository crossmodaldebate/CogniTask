**Trecho 11 (Alta Complexidade): Implementar uma fila utilizando uma lista.**

class Fila:

  """Implementa uma fila utilizando uma lista."""

  def __init__(self):

    self.itens = []

  def enfileirar(self, item):

    """Adiciona um item ao final da fila."""

    self.itens.append(item)

  def desenfileirar(self):

    """Remove e retorna o item do início da fila."""

    if not self.esta_vazia():

      return self.itens.pop(0)

    else:

      return None

  def esta_vazia(self):

    """Verifica se a fila está vazia."""

    return len(self.itens) == 0