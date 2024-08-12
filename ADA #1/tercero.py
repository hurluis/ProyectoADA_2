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

    # O(n)
    def insertar_letra(self, letra_nueva, posicion):
        if self.cabeza is None:
            return  # Lista vacía, no se puede insertar

        if posicion == 0:
            self.cabeza.letra = letra_nueva
            return

        actual = self.cabeza
        indice_actual = 0

        while actual and indice_actual < posicion:
            actual = actual.siguiente
            indice_actual += 1

        if actual:
            actual.letra = letra_nueva
        else:
            print(f"La posición {posicion} está fuera de rango.")


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
posicion= int(input("la posicion en la que desea poner la letra: "))
print()

lista.insertar(numero, 'A')  

lista.insertar_letra(letra, posicion)

print("Lista después de insertar el número y la letra:")
lista.imprimir()