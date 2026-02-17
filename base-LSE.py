# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza

			self.cabeza = nuevo_nodo
	#conteo
    def conteo(self):
        contador = 0
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente

        return contador

    #buscador
    def buscar(self, data):
      nodo_actual = self.cabeza

      while nodo_actual is not None:
          if nodo_actual.data == data:
              return True
          nodo_actual = nodo_actual.siguiente

      return False
    

#crear lista
lista = ListaSE()

elementos = int(input("Ingrese la cantidad de elementos que desea agregar en la lista: "))

for i in range(elementos):
  elemento = input("Digite el elemento: ")
  lista.agregarInicio(elemento)
print("Cantidad de nodos en la lista:", lista.conteo())

data=input("Digite el elemento a buscar: ")
if lista.buscar(data):
  print(f"El elemento {data} se encuentra en la lista")
else:
  print(f"El elemento {data} no se encuentra en la lista")
