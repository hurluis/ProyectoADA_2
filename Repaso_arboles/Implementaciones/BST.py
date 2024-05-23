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


class Queue:

    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.queue]
        return ' '.join(result)

    def is_empty(self):
        return self.linkedlist.head == None

    def enqueue(self, e):
        new_node = Node(e)
        if self.linkedlist.head is None:
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

    def insert(self, value):
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
                else:
                    self.leftchild.insert(value)
                    self.length += 1
            else:
                if self.rightchild is None:
                    self.rightchild = BST(value)
                    self.rightchild.parent = self
                    self.length += 1
                else:
                    self.rightchild.insert(value)
                    self.length += 1

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

# Example of usage:
bt = BST()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(13)
bt.insert(7)
bt.insert(44)
bt.insert(2)
bt.insert(1)
bt.insert(3)

# Print the tree
bt.printTree()


print("\n")
# Delete a node
bt.deleteNode(10)
bt.printTree()