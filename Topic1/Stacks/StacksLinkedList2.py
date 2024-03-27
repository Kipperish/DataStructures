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
        self.top = None
        self.size = size
        self.length = 0
    def isEmpty(self): #checks if stack is empty
        if self.top == None:
            return True
        else:
            return False
    def isFull(self): #checks if stack is full
        if self.length == self.size:
            return True
        else:
            return False
    def push(self, data):
        newNode = Node(data)
        if self.isFull(): #checks if full
            print("Stack is full")
        else:
            if self.isEmpty():
                self.top = newNode #adds new node to the top
            else:
                newNode.setNext(self.top) #new node points to previous top
                self.top = newNode
            self.length += 1
    def pop(self):
        if self.isEmpty(): #checks if empty
            print("Stack is empty")
        else:
            popped = self.top.getData() #takes from the top of the stack
            self.top = self.top.getNext() #next item becomes top
            self.length -= 1
            print(popped)
            return popped
    def peek(self):
        if self.isEmpty(): #checks if empty
            print("Stack is empty")
        else:
            print(self.top.getData()) #takes data from top
            return self.top.getData()
    def printStack(self):
        current = self.top
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

stack.peek()
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