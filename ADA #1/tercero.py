class Nodo:
    # O(1)
    def __init__(self, numero, letra):
        self.numero = numero
        self.letra = letra
        self.siguiente = None

class ListaEnlazada:
    # O(1)
    def __init__(self):
        self.cabeza = None

    # O(n)
    def insertar(self, numero, letra):
        nuevo_nodo = Nodo(numero, letra)
        if self.cabeza is None or numero < self.cabeza.numero:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.numero <= numero:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    # O(1)
    def insertar_letra_inicio(self, letra_nueva):
        if self.cabeza is not None:
            self.cabeza.letra = letra_nueva

    # O(n)
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(f"({actual.numero}, {actual.letra})", end=" -> ")
            actual = actual.siguiente
        print()

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
print()

numero = int(input("Ingrese un número: "))
letra = input("Ingrese una letra: ")
print()

lista.insertar(numero, 'A')  

lista.insertar_letra_inicio(letra)

print("Lista después de insertar el número y la letra:")
lista.imprimir()