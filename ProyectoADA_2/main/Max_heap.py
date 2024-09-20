class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Maxheap:
    def __init__(self, value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.parent = None
        self.length = 0 
        self.Node = Node(value)  
        self.arbol=[]
    
    
    def insert(self, value):
        if value is None:
            return  

        if self.value is None:
            self.value = value
            self.length = 1 
        else:
            if self.leftchild is None:
                nuevo_nodo = Maxheap(value)
                nuevo_nodo.parent = self
                self.leftchild = nuevo_nodo
                self.length += 1  
                self.arbol.append(nuevo_nodo)
            elif self.rightchild is None:
                nuevo_nodo = Maxheap(value)
                nuevo_nodo.parent = self
                self.rightchild = nuevo_nodo
                self.length += 1  
                self.arbol.append(nuevo_nodo)   
            else:
                if self.leftchild.length <= self.rightchild.length:
                    self.leftchild.insert(value)
                    self.length +=1
                else:
                    self.rightchild.insert(value)
                    self.length +=1

        self.verificarMaxHeap()





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



    def verificarMaxHeap(self):
        if self.leftchild and self.value > self.leftchild.value:
            self.value, self.leftchild.value = self.leftchild.value, self.value
            self.leftchild.verificarMaxHeap()
        if self.rightchild and self.value > self.rightchild.value:
            self.value, self.rightchild.value = self.rightchild.value, self.value
            self.rightchild.verificarMaxHeap()