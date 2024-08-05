class Nodo:
    #constructor es O(1)
    def __init__(self, numero=None, letra=None):
        self.numero = numero
        self.letra = letra
        self.next = None

#Primer metodo es O(n)
def crear_lista(elementos, indice=0):
    if indice >= len(elementos):
        return None
    numero, letra = elementos[indice]
    nodo = Nodo(numero, letra)
    nodo.next = crear_lista(elementos, indice + 1)
    return nodo

#Segundo metodo es O(n)
def insertar_en_posicion(head, letra, posicion, contador=0):
    if head is None or contador == posicion:
        nuevo_nodo = Nodo(None, letra)
        nuevo_nodo.next = head
        return nuevo_nodo
    head.next = insertar_en_posicion(head.next, letra, posicion, contador + 1)
    return head

#tercer metodo es O(n)
def longitud_lista(head):
    if head is None:
        return 0
    return 1 + longitud_lista(head.next)

#cuarto metodo es O(n)
def insertar_medio(head, letra):
    longitud = longitud_lista(head)
    posicion_medio = longitud // 2
    return insertar_en_posicion(head, letra, posicion_medio)

#quinto metodo es O(n)
def insertar_numero(head, numero, posicion, contador=0):
    if head is None:
        return None
    if contador == posicion:
        head.numero = numero
        return head
    head.next = insertar_numero(head.next, numero, posicion, contador + 1)
    return head

#sexto metodo es O(n)
def actualizar_indices(head, contador=0):
    if head is None:
        return
    head.numero = contador
    actualizar_indices(head.next, contador + 1)

#septimo metodo es O(n log n)
def organizar_lista(head):
    def a_lista(head):
        if head is None:
            return []
        return [(head.numero, head.letra)] + a_lista(head.next)
    
    def de_lista(elementos, indice=0):
        if indice >= len(elementos):
            return None
        numero, letra = elementos[indice]
        nodo = Nodo(numero, letra)
        nodo.next = de_lista(elementos, indice + 1)
        return nodo
    
    elementos = [elemento for elemento in a_lista(head) if elemento[0] is not None]
    elementos.sort()
    return de_lista(elementos)

#octavo metodo es O(n)
def imprimir_lista(head):
    if head is None:
        print("")
        return
    print(f"{head.numero} {head.letra}", end=" -> " if head.next else "\n")
    imprimir_lista(head.next)

# Crear lista inicial
elementos_iniciales = [(5, 'L'), (2, 'M'), (7, 'K'), (4, 'U')]
head = crear_lista(elementos_iniciales)

# Imprimir lista antes de la modificación
print("Lista antes de la modificación:")
imprimir_lista(head)

# Organizar lista
head = organizar_lista(head)
print("Lista después de organizar:")
imprimir_lista(head)

# Datos ingresados por el usuario
numero_usuario = int(input("ingrese el numero: ")) 
print("\n")
letra_usuario = input("ingrese una letra en mayuscula: ")
print("\n")

# Insertar letra en la posición media
head = insertar_medio(head, letra_usuario)
print("Lista después de insertar la letra en el medio:")
imprimir_lista(head)

# Insertar número en la posición especificada por el usuario
head = insertar_numero(head, numero_usuario, numero_usuario)

# Actualizar los índices correctamente antes de organizar
actualizar_indices(head)

# Reorganizar la lista para reflejar el nuevo índice del número ingresado
head = organizar_lista(head)

# Imprimir lista después de la modificación
print("Lista después de la modificación:")
imprimir_lista(head)