class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext

class Stack():
    def __init__(self, size):
        self.head = None
        self.size = size
        self.length = 0
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def isFull(self):
        if self.length == self.size:
            return True
        else:
            return False
    def push(self, data):
        newNode = Node(data)
        current = self.head
        if self.isFull():
            print("List is full")
        else:
            if current == None:
                self.head = newNode
            else:
                while current.getNext() != None:
                    current = current.getNext()
                current.setNext(newNode)
            self.length += 1
    def pop(self):
        current = self.head
        if self.isEmpty():
            print("Stack is empty")
        else:
            if current.getNext() == None:
                print(self.head.getData())
                self.head = None
            else:
                while current.getNext().getNext() != None:
                    current = current.getNext()
                print(current.getNext().getData())
                current.setNext(current.getNext().getNext())
            self.length -= 1
    def printStack(self):
        current = self.head
        stack = []
        if self.isEmpty():
            print("Stack is empty")
        else:
            while current != None:
                stack.append(current.data)
                current = current.getNext()
            print(stack)

stack = Stack(5)

stack.push("alfredo")
stack.printStack()
print()

stack.push("alf")
stack.printStack()
print()

stack.push("redo")
stack.printStack()
print()

stack.pop()
print()
stack.printStack()
print()

stack.push("A")
stack.printStack()
print()

stack.push("L")
stack.printStack()
print()

stack.push("F")
stack.printStack()
print()

stack.push("R")
stack.printStack()
print()

stack.push("E")
stack.printStack()
print()

stack.push("D")
stack.printStack()
print()

stack.push("O")
stack.printStack()
print()

stack.pop()
stack.printStack()
print()

stack.pop()
stack.printStack()
print()

stack.pop()
stack.printStack()
print()

stack.pop()
stack.printStack()
print()

stack.pop()
stack.printStack()
print()

stack.pop()
