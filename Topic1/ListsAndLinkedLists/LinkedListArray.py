linkedList = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Sharon", None],
    ["Roberto", 1],
    [None, None],
    [None, None]
]

def traverse(linkedList):
    head = 0
    data = 0
    pointer = 1
    current = head
    if linkedList[head] == None:
        print("Empty List")
    else:
        while linkedList[current][pointer] != None:
            print(linkedList[current][data])
            current = linkedList[current][pointer]
    print(linkedList[current][data])
    return current

def traverseNoPrint(linkedList):
    head = 0
    data = 0
    pointer = 1
    current = head
    while linkedList[current][pointer] != None:
        current = linkedList[current][pointer]
    return current

def freeSpaces(linkedList):
    spaces = [] #Stores the free spaces in the list
    data = 0
    for i in range(len(linkedList)):
        if linkedList[i][data] == None:
            spaces.append(i)
    return spaces

def add(linkedList, item):
    lastItem = traverseNoPrint(linkedList)
    dataIndex = 0
    nextIndex = 1
    notFull = freeSpaces(linkedList) #if the list from the free spaces function is empty its set to false meaning the list is full but if it isnt full it allows to use the list of free spaces to put new items
    if notFull:
        linkedList[notFull[0]][dataIndex] = item
        linkedList[notFull[0]][nextIndex] = None #creates the new item with data of item and pointer to null
        linkedList[lastItem][nextIndex] = notFull[0] #changes last items pointer to the new item to be the new last item
    else:
        print("list is full")

def remove(linkedList, deleted):
    head = 0
    data = 0
    pointer = 1
    current = head
    inList = False
    while linkedList[current][pointer] != None:
        if linkedList[current][data] == deleted:
            inList = True
        current = linkedList[current][pointer]
    current = head
    if inList == True:
        while linkedList[(linkedList[current][pointer])][data] != deleted: #checks to see if the next item is the one being removed
            current = linkedList[current][pointer]
        deletedIndex = linkedList[current][pointer] #stores the index of the item to be deleted
        linkedList[current][pointer] = linkedList[linkedList[current][pointer]][pointer] #updates the current items pointer to copy the deleted items pointer
        linkedList[deletedIndex][data] = None
        linkedList[deletedIndex][pointer] = None #sets deleted data and pointer to null to be reused
    else:
        print(f"Item ({deleted}) not in list")

traverse(linkedList)
print()
add(linkedList,"Boris")
traverse(linkedList)
print()
remove(linkedList, "Sarah")
traverse(linkedList)
remove(linkedList, "alfredo")
print()
print(freeSpaces(linkedList))