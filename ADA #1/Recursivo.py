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

    #O(n²)
    def _insertar_recursivo(self, nodo, numero, letra):
        if nodo is None:
            return Nodo(numero, letra)
        if numero < nodo.numero:
            nuevo_nodo = Nodo(numero, letra)
            nuevo_nodo.siguiente = nodo
            return nuevo_nodo
        else:
            nodo.siguiente = self._insertar_recursivo(nodo.siguiente, numero, letra)
            return nodo
        
    #O(n) 
    def insertar_letra(self, letra_nueva, posicion):
        self.cabeza = self._insertar_letra_recursivo(self.cabeza, letra_nueva, posicion, 0)

    #O(n²)
    def _insertar_letra_recursivo(self, nodo, letra_nueva, posicion, indice_actual):
        if nodo is None:
            return Nodo(indice_actual, letra_nueva)
        
        if nodo.siguiente is None:
            nuevo_nodo = Nodo(nodo.numero + 1, letra_nueva)
            nodo.siguiente = nuevo_nodo
            return nodo
        
        if indice_actual == posicion:
            if letra_nueva <= nodo.letra:
                nuevo_nodo = Nodo(nodo.numero, nodo.letra)
                nuevo_nodo.siguiente = nodo.siguiente
                nodo.letra = letra_nueva
                nodo.siguiente = nuevo_nodo
            else:
                nuevo_nodo = Nodo(nodo.numero + 1, letra_nueva)
                nuevo_nodo.siguiente = nodo.siguiente
                nodo.siguiente = nuevo_nodo
            return nodo
        
        nodo.siguiente = self._insertar_letra_recursivo(nodo.siguiente, letra_nueva, posicion, indice_actual + 1)
        return nodo

    #O(n)
    def imprimir(self):
        self._imprimir_recursivo(self.cabeza)
        print()

    #O(n²)
    def _imprimir_recursivo(self, nodo):
        if nodo is None:
            return
        print(f"({nodo.numero}, {nodo.letra})", end=" -> ")
        self._imprimir_recursivo(nodo.siguiente)

    #O(n)
    def obtener_letra(self, numero):
        return self._obtener_letra_recursivo(self.cabeza, numero)

    #O(n)
    def _obtener_letra_recursivo(self, nodo, numero):
        if nodo is None or nodo.numero >= numero:
            return None  
        if nodo.siguiente and nodo.siguiente.numero > numero:
            return nodo.letra
        return self._obtener_letra_recursivo(nodo.siguiente, numero)

    #O(n)
    def insertar_nuevo_elemento(self, numero, letra, posicion):
        self.cabeza = self._insertar_nuevo_elemento_recursivo(self.cabeza, numero, letra, posicion)

    #O(n²)
    def _insertar_nuevo_elemento_recursivo(self, nodo, numero, letra, posicion):
        if nodo is None:
            return Nodo(numero, letra)
        
        letra_existente = self.obtener_letra(numero)
        if letra_existente is not None:
            self.insertar(numero, letra_existente)
        
        return self._insertar_letra_recursivo(nodo, letra, posicion, 0)

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
posicion = int(input("Ingrese la posición para la nueva letra: "))
print("\n")

lista.insertar_nuevo_elemento(numero, letra, posicion)

print("Lista después de insertar el número y la letra:")
lista.imprimir()