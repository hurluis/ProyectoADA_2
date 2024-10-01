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
        if not self.cabeza or grado > self.cabeza.grado:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.grado >= grado:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def sumar_terminos(self):
        actual = self.cabeza
        while actual and actual.siguiente:
            if actual.grado == actual.siguiente.grado:
                actual.coeficiente += actual.siguiente.coeficiente
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

class Polinomio:
    def __init__(self):
        self.listas_por_grado = {}
        self.polinomio_actual = ""

    def esta_vacio(self):
        return len(self.listas_por_grado) == 0

    def dividir_polinomio(self, polinomio):
        self.listas_por_grado.clear()  # Limpiar las listas existentes
        terminos = polinomio.replace(" ", "").replace("-", "+-").split("+")
        for termino in terminos:
            if termino:
                if 'x^' in termino:
                    coef, grado = termino.split('x^')
                elif 'x' in termino:
                    coef, grado = termino.split('x')
                    grado = '1'
                else:
                    coef, grado = termino, '0'
                
                coef = int(coef) if coef else 1
                grado = int(grado)
                
                if grado not in self.listas_por_grado:
                    self.listas_por_grado[grado] = ListaEnlazada()
                self.listas_por_grado[grado].agregar(coef, grado)
        self.actualizar_polinomio_actual()
        return self.listas_por_grado

    def reconstruir_polinomio(self):
        resultado = ""
        for grado in sorted(self.listas_por_grado.keys(), reverse=True):
            lista = self.listas_por_grado[grado]
            actual = lista.cabeza
            while actual:
                if actual.coeficiente != 0:
                    if resultado and actual.coeficiente > 0:
                        resultado += " + "
                    elif actual.coeficiente < 0:
                        resultado += " - "
                    
                    coef_abs = abs(actual.coeficiente)
                    if coef_abs != 1 or grado == 0:
                        resultado += str(coef_abs)
                    
                    if grado > 0:
                        resultado += "x"
                        if grado > 1:
                            resultado += f"^{grado}"
                
                actual = actual.siguiente
        return resultado.strip() if resultado else "0"

    def actualizar_polinomio_actual(self):
        self.polinomio_actual = self.reconstruir_polinomio()

    def agregar_al_final(self, polinomio):
        self.dividir_polinomio(polinomio)
        self.actualizar_polinomio_actual()

    def organizar_heap(self):
        for lista in self.listas_por_grado.values():
            lista.sumar_terminos()
        self.actualizar_polinomio_actual()

    def imprimir_actual(self):
        print(self.polinomio_actual)

    def sumar_mismos_grados(self):
        for lista in self.listas_por_grado.values():
            lista.sumar_terminos()
        self.actualizar_polinomio_actual()

    def __str__(self):
        return self.polinomio_actual


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