class Nodo:
    #O(1)
    def __init__(self, numero, letra):
        self.numero = numero
        self.letra = letra
        self.siguiente = None

class ListaEnlazada:
    #O(1)
    def __init__(self):
        self.cabeza = None

    #O(n)
    def insertar(self, numero, letra):
        self.cabeza = self._insertar_recursivo(self.cabeza, numero, letra)

    #O(n)
    def _insertar_recursivo(self, nodo, numero, letra):
        if nodo is None or numero < nodo.numero:
            nuevo_nodo = Nodo(numero, letra)
            nuevo_nodo.siguiente = nodo
            return nuevo_nodo
        else:
            nodo.siguiente = self._insertar_recursivo(nodo.siguiente, numero, letra)
            return nodo
    
    #O(1)
    def insertar_letra(self, letra_nueva):
        if self.cabeza is not None:
            self.cabeza.letra = letra_nueva

    #O(n)
    def imprimir(self):
        self._imprimir_recursivo(self.cabeza)
        print()

    #O(n)
    def _imprimir_recursivo(self, nodo):
        if nodo is None:
            return
        print(f"({nodo.numero}, {nodo.letra})", end=" -> ")
        self._imprimir_recursivo(nodo.siguiente)

lista = ListaEnlazada()

lista.insertar(0, 'A')
lista.insertar(1, 'B')
lista.insertar(3, 'W')
lista.insertar(5, 'X')
lista.insertar(7, 'U')
lista.insertar(8, 'V')
lista.insertar(9, 'R')
lista.insertar(12, 'D')

print("Lista inicial:")
lista.imprimir()
print("\n")

numero = int(input("Ingrese un número: "))
letra = input("Ingrese una letra: ")
print("\n")

lista.insertar(numero, 'A')  

lista.insertar_letra(letra)

print("Lista después de insertar el número y la letra:")
lista.imprimir()