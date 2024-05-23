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


class MinHeap:
    def __init__(self, value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.parent = None
        self.length = 0 
        self.queue = queue()
        self.Node = Node(value)  



    def insert(self, value):
        if value is None:
            return  

        if self.value is None:
            self.value = value
            self.length = 1 
        else:
            if self.leftchild is None:
                new_node = MinHeap(value)
                new_node.parent = self
                self.leftchild = new_node
                self.length += 1  
                self.queue.enqueue(new_node)
            elif self.rightchild is None:
                new_node = MinHeap(value)
                new_node.parent = self
                self.rightchild = new_node
                self.length += 1  
                self.queue.enqueue(new_node)
            else:
                if self.leftchild.length <= self.rightchild.length:
                    self.leftchild.insert(value)
                    self.length +=1
                else:
                    self.rightchild.insert(value)
                    self.length +=1

        self.verificarMinHeap()

    
        
    

    def searchNode(self, value):
        if self.value is None:
            return "El nodo con valor {} NO fue encontrado".format(value)
                    
        if self.value == value:
            return "El nodo con valor {} SI fue encontrado".format(value)
                    
        if self.leftchild is not None:
            left_result = self.leftchild.searchNode(value)
            if left_result != "El nodo con valor {} NO fue encontrado".format(value):
                return left_result
        
        if self.rightchild is not None:
            right_result = self.rightchild.searchNode(value)
            if right_result != "El nodo con valor {} NO fue encontrado".format(value):
                return right_result
                
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
            # Caso 1: No tiene hijos
            if self.leftchild is None and self.rightchild is None:
                self.value = None
                self.length -= 1
                return None
            # Caso 2: Tiene ambos hijos
            elif self.leftchild is not None and self.rightchild is not None:
                # Elegir el sucesor inmediato (podría ser también el predecesor inmediato)
                tempNode = self.rightchild
                while tempNode.leftchild is not None:
                    tempNode = tempNode.leftchild
                self.value = tempNode.value
                self.rightchild = self.rightchild.deleteNode(tempNode.value)
                self.verificarMinHeap()
            # Caso 3: Tiene solo un hijo
            elif self.leftchild is not None:
                self.value = self.leftchild.value
                self.leftchild = None
                self.length -= 1
            else:
                self.value = self.rightchild.value
                self.rightchild = None
                self.length -= 1
        else:
            if self.leftchild is not None:
                self.leftchild = self.leftchild.deleteNode(value)
            if self.rightchild is not None:
                self.rightchild = self.rightchild.deleteNode(value)

        return self

    

    def removeMin(self):
        if self.leftchild is None and self.rightchild is None:
            if self.parent is not None:
                if self.parent.leftchild == self:
                    self.parent.leftchild = None
                else:
                    self.parent.rightchild = None
            min_value = self.value
            self.value = None
            self.length -= 1
            return min_value
                
        min_value = self.value
        last_node = self.LastNode(self)
        self.value = last_node.value
        
        if last_node.parent:
            if last_node.parent.leftchild == last_node:
                last_node.parent.leftchild = None
            else:
                last_node.parent.rightchild = None
            self.length -= 1
        else:
            self.value = None
            self.length -= 1
        
        self.verificarMinHeap()
        return min_value


    def LastNode(self, rootNode):
        if rootNode is None:
            return None
        
        queue = [rootNode]
        while queue:
            current = queue.pop(0)
            if current.leftchild is not None:
                queue.append(current.leftchild)
            if current.rightchild is not None:
                queue.append(current.rightchild)
        
        return current



    def verificarMinHeap(self):
        if self.leftchild and self.value > self.leftchild.value:
            self.value, self.leftchild.value = self.leftchild.value, self.value
            self.leftchild.verificarMinHeap()
        if self.rightchild and self.value > self.rightchild.value:
            self.value, self.rightchild.value = self.rightchild.value, self.value
            self.rightchild.verificarMinHeap()

            
min_heap = MinHeap()
min_heap.insert(4)
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(1)
min_heap.insert(5)
min_heap.insert(6)
min_heap.insert(12)



print("Árbol de min-heap:")
min_heap.printTree()



min_heap.removeMin()
min_heap.printTree()

min_heap.deleteNode(4)
min_heap.printTree()