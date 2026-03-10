class Nodo:
  def __init__(self, data):
    self.data = data
    self.next = None


class comandos:

  def __init__(self):
    self.head = None


  def insertar_final(self, data):

    nuevo_nodo = Nodo(data)

    if self.head is None:
      self.head = nuevo_nodo
      return

    nodo_actual = self.head

    while nodo_actual.next:
      nodo_actual = nodo_actual.next

    nodo_actual.next = nuevo_nodo


  def insertar_antes(self, data, val):

    nuevo_nodo = Nodo(data)

    if self.head is None:
      return

    if self.head.data == val:
      nuevo_nodo.next = self.head
      self.head = nuevo_nodo
      return

    nodo_actual = self.head

    while nodo_actual.next and nodo_actual.next.data != val:
      nodo_actual = nodo_actual.next

    if nodo_actual.next:
      nuevo_nodo.next = nodo_actual.next
      nodo_actual.next = nuevo_nodo


  def insertar_despues(self, data, val):

    nuevo_nodo = Nodo(data)
    nodo_actual = self.head

    while nodo_actual:

      if nodo_actual.data == val:
        nuevo_nodo.next = nodo_actual.next
        nodo_actual.next = nuevo_nodo
        return

      nodo_actual = nodo_actual.next


  def eliminar_primero(self):

    if self.head is None:
      return

    self.head = self.head.next


  def eliminar_ultimo(self):

    if self.head is None:
      return

    if self.head.next is None:
      self.head = None
      return

    nodo_actual = self.head

    while nodo_actual.next.next:
      nodo_actual = nodo_actual.next

    nodo_actual.next = None


  def buscar(self, val):

    nodo_actual = self.head

    while nodo_actual:
      if nodo_actual.data == val:
        return True

      nodo_actual = nodo_actual.next

    return False


  def contar(self):

    nodo_actual = self.head
    cont = 0

    while nodo_actual:
      cont += 1
      nodo_actual = nodo_actual.next

    return cont

