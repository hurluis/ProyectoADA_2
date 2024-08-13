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

    # O(n²)
    def insertar_letra(self, letra_nueva, posicion):
        if self.cabeza is None:
            return  

        actual = self.cabeza
        indice = 0

        while actual and indice < posicion:
            if indice == posicion - 1:
                prev = actual
            actual = actual.siguiente
            indice += 1

        if actual:
            if letra_nueva <= actual.letra:
                temp_letra = actual.letra
                actual.letra = letra_nueva
                nuevo_nodo = Nodo(actual.numero, temp_letra)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
            else:
                nuevo_nodo = Nodo(actual.numero, letra_nueva)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
        else:
            print(f"La posición {posicion} está fuera de rango.")

    # O(n³)
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
posicion = int(input("La posición en la que desea poner la letra: "))
print("\n")

actual = lista.cabeza
while actual and actual.numero < numero:
    letra_existente = actual.letra
    actual = actual.siguiente
lista.insertar(numero, letra_existente if letra_existente else 'A')

lista.insertar_letra(letra, posicion)

print("Lista después de insertar el número y la letra:")
lista.imprimir()