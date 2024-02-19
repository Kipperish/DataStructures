class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.length = 0
        self.top = -1
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def isFull(self):
        if self.length == self.size:
            return True
        else:
            return False
    def push(self, item):
        if not self.isFull():
            self.stack.append(item)
            self.length += 1
            self.top += 1
        else:
            print("list is full")
    def pop(self):
        if not self.isEmpty():
            item = self.stack[self.top]
            self.stack.remove(item)
            self.length -= 1
            self.top -= 1
            return(item)
        else:
            print("List is empty")
    def printStack(self):
        print(self.stack)

carStack = Stack(6)
carStack.push("Mondeo")
carStack.printStack()
carStack.push("Golf")
carStack.printStack()
print(carStack.isEmpty())
carStack.push("Fiesta")
carStack.printStack()
carStack.push("Punto")
carStack.printStack()
print(carStack.pop())
carStack.printStack()
carStack.push("Civic")
carStack.printStack()
print(carStack.isFull())
print(carStack.pop())
carStack.printStack()
print(carStack.pop())
carStack.printStack()