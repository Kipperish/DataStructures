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
    print(current)
    return current

def add(linkedList, item):


traverse(linkedList)