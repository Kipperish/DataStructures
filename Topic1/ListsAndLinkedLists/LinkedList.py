class Node():
    def __init__(self, givenData):
        self.data = givenData
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext

class LinkedList():
    def __init__(self):
        self.head = None
    def traverse(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = (current.getNext())
    def insertAtFront(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def insertInOrder(self, data):
        newNode = Node(data)
        current = self.head
        if current == None:
            self.head = newNode
        elif newNode.getData() < current.getData():
            newNode.setNext(self.head)
            self.head = newNode
        else:
            while current.getNext() != None and current.getNext().getData() < newNode.getData():
                current = current.getNext()
            newNode.setNext(current.getNext())
            current.setNext(newNode)
    def delete(self, data):
        current = self.head
        if current.getData() == data:
            self.head = current.getNext()
        else:
            while current.getNext().getData() != data:
                current = current.getNext()
            current.setNext(current.getNext().getNext()) 
            

myList = LinkedList()
myList.insertInOrder("Bartholomew")
myList.insertInOrder("Tarquin")
myList.insertInOrder("Alfredo")
myList.insertInOrder("Reginald")
myList.insertInOrder("Clarence")
myList.traverse()
print()

myList.delete("Bartholomew")
myList.traverse()
print()

myList.delete("Tarquin")
myList.traverse()