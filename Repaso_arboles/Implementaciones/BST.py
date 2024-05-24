class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return ' '.join(result)


class queue:

  def __init__(self):
    self.linkedlist = LinkedList()

  def __str__(self):
    result = [str(x.value) for x in self.queue]
    return ' '.join(result)

  def is_empty(self):
    return self.linkedlist.head == None

  def enqueue(self, e):
    new_node = Node(e)
    if self.linkedlist.head == None:
      self.linkedlist.head = new_node
      self.linkedlist.tail = new_node
    else:
      new_node.next = None
      self.linkedlist.tail.next = new_node
      self.linkedlist.tail = new_node

  def dequeue(self):
    if self.is_empty():
      return "No hay elementos en la lista"
    else:
      popped_node = self.linkedlist.head
      if self.linkedlist.head == self.linkedlist.tail:
        self.linkedlist.head = None
        self.linkedlist.tail = None
      else:
        self.linkedlist.head = self.linkedlist.head.next
      popped_node.next = None
      return popped_node

class BST:
    def __init__(self, value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.parent = None
        self.length = 0 
        self.NodosArbol=[]
        self.queue = queue()
        self.Node = Node(value)  

    def insert(self, value):
        NodosArbol=[]
        if value is None:
            return

        if self.value is None:
            self.value = value
            self.length = 1
        else:
            if value < self.value:
                if self.leftchild is None:
                    self.leftchild = BST(value)
                    self.leftchild.parent = self
                    self.length += 1
                    self.queue.enqueue(self.leftchild)
                    self.NodosArbol.append(self.leftchild)
                else:
                    self.leftchild.insert(value)
                    self.length += 1
            else:
                if self.rightchild is None:
                    self.rightchild = BST(value)
                    self.rightchild.parent = self
                    self.length += 1
                    self.queue.enqueue(self.rightchild)
                    self.NodosArbol.append(self.rightchild)
                else:
                    self.rightchild.insert(value)
                    self.length += 1


    def MostrarHojas(self):
        Hojas = []
        self.ObtenerHojas(self, Hojas)
        return Hojas
    

    def searchNode(self, value):
        if self.value is None:
            return "El nodo con valor {} NO fue encontrado".format(value)

        if self.value == value:
            return "El nodo con valor {} SI fue encontrado".format(value)

        if value < self.value and self.leftchild is not None:
            return self.leftchild.searchNode(value)

        if value > self.value and self.rightchild is not None:
            return self.rightchild.searchNode(value)

        return "El nodo con valor {} NO fue encontrado".format(value)

    def printTree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self

        if not node:
            return

        if node.rightchild:
            self.printTree(node.rightchild, prefix + ("│    " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        if node.leftchild:
            self.printTree(node.leftchild, prefix + ("     " if is_left else "│   "), True)

    def deleteNode(self, value):
        if self.value == value:
            # Case 1: No children
            if self.leftchild is None and self.rightchild is None:
                return None
            # Case 2: Two children
            elif self.leftchild is not None and self.rightchild is not None:
                tempNode = self.rightchild
                while tempNode.leftchild is not None:
                    tempNode = tempNode.leftchild
                self.value = tempNode.value
                self.rightchild = self.rightchild.deleteNode(tempNode.value)
            # Case 3: One child
            elif self.leftchild is not None:
                return self.leftchild
            else:
                return self.rightchild
        else:
            if value < self.value and self.leftchild is not None:
                self.leftchild = self.leftchild.deleteNode(value)
            elif value > self.value and self.rightchild is not None:
                self.rightchild = self.rightchild.deleteNode(value)

        return self


    def ObtenerHojas(self, node, Hojas):
        if node is None:
            return

        if node.leftchild is None and node.rightchild is None:
            Hojas.append(node.value)

        if node.leftchild:
            self.ObtenerHojas(node.leftchild, Hojas)

        if node.rightchild:
            self.ObtenerHojas(node.rightchild, Hojas)

    def encontrarEnHojas(self, numero):
        Current=[]
        for elemento in self.MostrarHojas():
            if elemento ==numero:
                Current.append(elemento)
        return print(len(Current))
    

    def CantidadNumeros(self, elemento):
        if self is None:
            return 0
        almacenador = 1 if self.value == elemento else 0
        contadorIzquiuera = self.leftchild.CantidadNumeros(elemento) if self.leftchild else 0
        condadorDerecha = self.rightchild.CantidadNumeros(elemento) if self.rightchild else 0

        return almacenador +    contadorIzquiuera + condadorDerecha
    
    def mostrarElementosArbol(self):
        elements = []
        if self.leftchild:
            elements.extend(self.leftchild.mostrarElementosArbol())
        elements.append(self.value)
        if self.rightchild:
            elements.extend(self.rightchild.mostrarElementosArbol())
        return elements
    

    def levelOrderTraversal(self):
        if not self:
            return []

        elements = []
        customqueue = queue()
        customqueue.enqueue(self)

        while not customqueue.is_empty():
            current = customqueue.dequeue()
            elements.append(current.value.value)  
            if current.value.leftchild:
                customqueue.enqueue(current.value.leftchild)

            if current.value.rightchild:
                customqueue.enqueue(current.value.rightchild)

        return print(elements)
    
    
    def deepestLeftChild(self):
        if not self:
            return None
        
        while self.leftchild:
            self = self.leftchild
        return self

    def deepestRightChild(self):
        if not self:
            return None
        
        while self.rightchild:
            self = self.rightchild
        return self
    
    def deepestValue(self):
        deepest_left = self.deepestLeftChild()
        deepest_right = self.deepestRightChild()

        if deepest_left and deepest_right:
            return deepest_left.value if deepest_left.value > deepest_right.value else deepest_right.value
        elif deepest_left:
            return deepest_left.value
        elif deepest_right:
            return deepest_right.value
        else:
            return self.value

    def DiferenciaAbsolutaMinima(self):
        values = self.mostrarElementosArbol()
        
        minima = float('inf')
        for elemento in range(1, len(values)):
            diferencia = abs(values[elemento] - values[elemento-1])
            if diferencia < minima:
                minima = diferencia
        
        return minima

    def valor_mayor(self):
        current=[]
        iteraciones=0
        while len(self.mostrarElementosArbol()) != iteraciones:
            mayor=float('-inf')
            for elemento in self.mostrarElementosArbol():
                mayor=max(mayor, elemento)
                iteraciones+=1
            current.append(mayor)
        return current

    def calcular_altura(self):
        if not self:
            return 0
        if self.leftchild:
            altura_izquierda = self.leftchild.calcular_altura()
        else:
            altura_izquierda = 0
        if self.rightchild:
            altura_derecha = self.rightchild.calcular_altura()
        else:
            altura_derecha = 0
        return max(altura_izquierda, altura_derecha) + 1
    
    def cantidad_nodos(self):
        current=self.mostrarElementosArbol()
        return len(current)

    def calcsuma_arbol(self):
        suma_total = self.value
    
        if self.leftchild:
            suma_total += self.leftchild.calcsuma_arbol()
        
        if self.rightchild:
            suma_total += self.rightchild.calcsuma_arbol()
        
        return suma_total
    
    def invertirArbol(self):
        if self is None:
            return None

        self.leftchild, self.rightchild = self.rightchild, self.leftchild

        if self.leftchild:
            self.leftchild.invertirArbol()
        if self.rightchild:
            self.rightchild.invertirArbol()

    def encontrarNivelValor(self, valor, nivel=1):
        if self.value == valor:
            return nivel
        
        nivel_izquierdo = self.leftchild.encontrarNivelValor(valor, nivel + 1) if self.leftchild else 0
        nivel_derecho = self.rightchild.encontrarNivelValor(valor, nivel + 1) if self.rightchild else 0
            
        return max(nivel_izquierdo, nivel_derecho)
    
    def operacion_arbol(self):
        resultado_izquierdo = 0
        resultado_derecho = 0

        if self.leftchild:
            if self.leftchild.leftchild and self.leftchild.rightchild:
                suma_hijos_izquierdo = self.leftchild.leftchild.calcsuma_arbol() + self.leftchild.rightchild.calcsuma_arbol()
                resultado_izquierdo = suma_hijos_izquierdo * self.leftchild.value
        if self.rightchild:
            if self.rightchild.leftchild and self.rightchild.rightchild:
                suma_hijos_derecho = self.rightchild.leftchild.calcsuma_arbol() + self.rightchild.rightchild.calcsuma_arbol()
                resultado_derecho = suma_hijos_derecho * self.rightchild.value

        resultado = resultado_izquierdo - resultado_derecho
        return resultado
    

bt = BST()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(13)
bt.insert(7)
bt.insert(44)
bt.insert(2)
bt.insert(1)
bt.insert(4)


# Print the tree
bt.printTree()


Hojas = bt.MostrarHojas()
print("\nHojas:", Hojas)

# Print the tree after getting Hojas
print("\nTree after getting Hojas (should be unchanged):")
bt.printTree()

bt.encontrarEnHojas(4)

print(bt.CantidadNumeros(4))

nodos=bt.mostrarElementosArbol()
print("\nNodos del arbol: ", nodos)

(bt.levelOrderTraversal())

print(bt.deepestRightChild().value)

print(bt.calcsuma_arbol())

print("Árbol original:")
bt.printTree()

# Invertir el árbol
bt.invertirArbol()

print("\nÁrbol invertido:")
bt.printTree()

