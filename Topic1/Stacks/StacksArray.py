stack = []
top = -1
length = 0
size = 5
def isFull():
    global length
    global size
    if length == size:
        return True
    else:
        return False
def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False
def push(data):
    global stack
    global top
    global stack
    global length
    if isFull():
        print("stack is full")
    else:
        stack.append(data)
        top += 1
        length += 1
def pop():
    global stack
    global length
    global top
    if isEmpty():
        print("Stack is empty")
    else:
        popped = stack[top]
        stack.remove(stack[top])
        top -= 1
        length -= 1
        return popped
    
push("A")
print(stack)
push("L")
print(stack)
push("F")
print(stack)
push("R")
print(stack)
push("E")
print(stack)
push("D")
print(stack)
push("O")
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)