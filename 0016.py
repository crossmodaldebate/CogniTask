**Trecho 16 (Alta Complexidade): Implementar uma árvore binária de busca.**

class No:

  """Representa um nó em uma árvore binária de busca."""

  def __init__(self, valor):

    self.valor = valor

    self.esquerda = None

    self.direita = None

class ArvoreBinariaBusca:

  """Implementa uma árvore binária de busca."""

  def __init__(self):

    self.raiz = None

  def inserir(self, valor):

    """Insere um valor na árvore."""

    if self.raiz is None:

      self.raiz = No(valor)

    else:

      self._inserir_recursivo(valor, self.raiz)

  def _inserir_recursivo(self, valor, no_atual):

    """Insere um valor recursivamente na árvore."""

    if valor < no_atual.valor:

      if no_atual.esquerda is None:

        no_atual.esquerda = No(valor)

      else:

        self._inserir_recursivo(valor, no_atual.esquerda)

    else:

      if no_atual.direita is None:

        no_atual.direita = No(valor)

      else:

        self._inserir_recursivo(valor, no_atual.direita)

  def buscar(self, valor):

    """Busca um valor na árvore."""

    if self.raiz is None:

      return False

    else:

      return self._buscar_recursivo(valor, self.raiz)

  def _buscar_recursivo(self, valor, no_atual):

    """Busca um valor recursivamente na árvore."""

    if valor == no_atual.valor:

      return True

    elif valor < no_atual.valor and no_atual.esquerda is not None:

      return self._buscar_recursivo(valor, no_atual.esquerda)

    elif valor > no_atual.valor and no_atual.direita is not None:

      return self._buscar_recursivo(valor, no_atual.direita)

    else:

      return False