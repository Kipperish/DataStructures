'''
queue to add students
'''
queue = ["","","","",""]
front = 0
rear = -1
size = 0

def isFull():
    global rear
    if rear == 4:
        return True
    
def isEmpty():
    global size
    if size == 0:
        return True
    
def enQueue(student):
    global queue
    global rear
    global size
    if not isFull():
        rear += 1
        size += 1
        queue[rear] = student
    else:
        print("Queue is full")

def deQueue():
    global front
    global size
    global queue
    if not isEmpty():
        print(queue[front])
        front += 1
        size -= 1
    else:
        print("Queue is empty")



# TEST CASES
    
# Test Case 1: Enqueue elements
enQueue("A")
enQueue("B")
enQueue("C")
enQueue("D")
enQueue("E")

print(queue)
print("Q Size: ", size)

# Test Case 2: Attempt to enqueue when the queue is full
enQueue("F")
print(queue)
print("Q Size: ", size)


# Test Case 3: Dequeue elements
deQueue()  # Output should be "A"
deQueue()   # Output should be "B"
print(queue)
print("Q Size: ", size)


# Test Case 4: Attempt to dequeue when the queue is empty
deQueue()  
deQueue() 
deQueue() 
deQueue() # Output should be "Error: Queue Empty"
print(queue)
print("Q Size: ", size)


# Test Case 5: Enqueue after dequeue
enQueue("F")
enQueue("G")
print(queue)
print("Q Size: ", size)


# Test Case 6: Attempt to enqueue when the queue is full
enQueue("H")  # Output should be "Error: Queue Full"

print(queue)
print("Q Size: ", size)