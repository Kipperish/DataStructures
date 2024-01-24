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
                current = current.getNext
            newNode.setNext(current.getNext())
            current.setNext(newNode)

myList = LinkedList()
myList.insertAtFront("bartholomew")
myList.insertAtFront("tarquin")
myList.traverse()