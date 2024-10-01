class Nodo:
    def __init__(self, coeficiente, grado):
        self.coeficiente = coeficiente
        self.grado = grado
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, coeficiente, grado):
        nuevo_nodo = Nodo(coeficiente, grado)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.coeficiente}x^{actual.grado}", end=" ")
            if actual.siguiente:
                print("+", end=" ")
            actual = actual.siguiente
        print()

    def sumar_mismos_grados(self):
        grado_dict = {}
        actual = self.cabeza
        while actual:
            if actual.grado in grado_dict:
                grado_dict[actual.grado] += actual.coeficiente
            else:
                grado_dict[actual.grado] = actual.coeficiente
            actual = actual.siguiente
        
        self.cabeza = None
        for grado, coeficiente in grado_dict.items():
            if coeficiente != 0:  # Ignorar coeficientes cero
                self.agregar(coeficiente, grado)

class Polinomio:
    def __init__(self):
        self.listas_por_grado = {}  # Diccionario para almacenar listas enlazadas

    def esta_vacio(self):
        return len(self.listas_por_grado) == 0

    def dividir_polinomio(self, polinomio):
        terminos = polinomio.replace(" ", "").replace("-", "+-").split("+")
        for termino in terminos:
            if 'x^' in termino:
                coeficiente, grado = termino.split("x^")
                grado = int(grado)
            elif 'x' in termino:
                coeficiente = termino[:-1]
                grado = 1
            else:
                coeficiente = termino
                grado = 0

            coeficiente = int(coeficiente) if coeficiente else 1
            if grado not in self.listas_por_grado:
                self.listas_por_grado[grado] = ListaEnlazada()
            self.listas_por_grado[grado].agregar(coeficiente, grado)

    def agregar_al_final(self, nuevo_polinomio):
        for grado, lista in nuevo_polinomio.listas_por_grado.items():
            if grado not in self.listas_por_grado:
                self.listas_por_grado[grado] = lista
            else:
                actual = self.listas_por_grado[grado].cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = lista.cabeza

    def organizar_heap(self):
        self.listas_por_grado = dict(sorted(self.listas_por_grado.items(), key=lambda item: item[0], reverse=True))

    def imprimir(self):
        polinomio_str = ""
        for grado in sorted(self.listas_por_grado.keys(), reverse=True):
            lista = self.listas_por_grado[grado]
            actual = lista.cabeza
            while actual:
                polinomio_str += f"{actual.coeficiente}x^{actual.grado} "
                if actual.siguiente:
                    polinomio_str += "+ "
                actual = actual.siguiente
        print(polinomio_str.strip())  # Eliminar espacios innecesarios al final

    def imprimir_original(self):
        polinomio_original = ""
        for grado in sorted(self.listas_por_grado.keys()):
            lista = self.listas_por_grado[grado]
            actual = lista.cabeza
            while actual:
                if polinomio_original:
                    polinomio_original += " + "
                polinomio_original += f"{actual.coeficiente}x^{actual.grado}"
                actual = actual.siguiente
        print(polinomio_original)
    def sumar_mismos_grados(self):
        for lista in self.listas_por_grado.values():
            lista.sumar_mismos_grados()

    def reconstruir_polinomio(self, listas_por_grado):
        nuevo_polinomio = Polinomio()
        for grado in sorted(listas_por_grado.keys()):
            lista = listas_por_grado[grado]
            actual = lista.cabeza
            while actual:
                nuevo_polinomio.agregar_al_final(nuevo_polinomio)
                nuevo_polinomio.agregar(actual.coeficiente, grado)
                actual = actual.siguiente
        return nuevo_polinomio


# # Uso del programa
# ordenar = Polinomio()
# polinomio = "33x^1 + 5x^2 - 2x^0 -3x^2 -3x^3 + 1x^1"
# listas = ordenar.dividir_polinomio(polinomio)

# # Imprimir el polinomio sin ordenar
# for grado, lista in listas.items():
#     print(f"Lista grado {grado}:")
#     lista.imprimir()

# # Organizar cada lista por coeficiente
# for lista in listas.values():
#     lista.organizar_heap()

# # Reconstruir el polinomio completo
# polinomio_ordenado = ordenar.reconstruir_polinomio(listas)
# print("\nPolinomio ordenado:")
# polinomio_ordenado.imprimir()