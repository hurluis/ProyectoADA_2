class Nodo:
    def __init__(self, coef, grado):
        self.coef = coef
        self.grado = grado
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None

    def insertar(self, coef, grado):
        nuevo_nodo = Nodo(coef, grado)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        resultado = []
        while actual:
            resultado.append(f"{actual.coef}x^{actual.grado}")
            actual = actual.siguiente
        print(" + ".join(resultado))

    def organizar_heap(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append((actual.coef, actual.grado))
            actual = actual.siguiente

        self._heap_sort(elementos)

        # Reconstruir la lista enlazada con los elementos ordenados
        self.cabeza = None
        for coef, grado in elementos:
            self.insertar(coef, grado)

    def _heap_sort(self, arr):
        n = len(arr)

        # Construir el heap (Max-Heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)

        # Extraer elementos del heap uno por uno
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Intercambiar
            self._heapify(arr, i, 0)

    def _heapify(self, arr, n, i):
        mayor = i  # Inicializar mayor como raíz
        izquierda = 2 * i + 1  # Hijo izquierdo
        derecha = 2 * i + 2    # Hijo derecho

        # Verificar si el hijo izquierdo es mayor que la raíz
        if izquierda < n and arr[izquierda][0] > arr[mayor][0]:
            mayor = izquierda

        # Verificar si el hijo derecho es mayor que el mayor actual
        if derecha < n and arr[derecha][0] > arr[mayor][0]:
            mayor = derecha

        # Cambiar la raíz si es necesario
        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            self._heapify(arr, n, mayor)

# Función para dividir el polinomio en listas enlazadas
def dividir_polinomio(polinomio):
    import re
    terminos = re.findall(r'[+-]?\d*x\^\d+', polinomio)
    lista_por_grado = {}

    for termino in terminos:
        coef, grado = map(int, re.findall(r'-?\d+', termino))
        if grado not in lista_por_grado:
            lista_por_grado[grado] = Polinomio()
        lista_por_grado[grado].insertar(coef, grado)

    return lista_por_grado

# Función para reconstruir el polinomio completo
def reconstruir_polinomio(lista_por_grado):
    polinomio_final = Polinomio()

    # Conectar cada lista de grados
    for grado in sorted(lista_por_grado.keys()):
        actual = lista_por_grado[grado].cabeza
        while actual:
            polinomio_final.insertar(actual.coef, actual.grado)
            actual = actual.siguiente

    return polinomio_final

