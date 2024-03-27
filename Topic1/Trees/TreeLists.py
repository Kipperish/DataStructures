left = 0
right = 2
data = 1

tree = [
    [1, "M", 2],
    [3, "H", 4],
    [5, "T", 6],
    [-1, "D", -1],
    [-1, "K", -1],
    [-1, "R", -1],
    [-1, "X", -1]
]

def inOrderTraverse(tree, pos):
    global left
    global right
    global data
    if tree[pos][left] != -1:
        inOrderTraverse(tree, tree[pos][left])
    print(tree[pos][data])
    if tree[pos][right] != -1:
        inOrderTraverse(tree, tree[pos][right])    

def preOrderTraverse(tree, pos):
    global left
    global right
    global data
    print(tree[pos][data])
    if tree[pos][left] != -1:
        inOrderTraverse(tree, tree[pos][left])
    if tree[pos][right] != -1:
        inOrderTraverse(tree, tree[pos][right])

def postOrderTraverse(tree,pos):
    global left
    global right
    global data
    if tree[pos][left] != -1:
        inOrderTraverse(tree, tree[pos][left])
    if tree[pos][right] != -1:
        inOrderTraverse(tree, tree[pos][right])
    print(tree[pos][data])


inOrderTraverse(tree, 0)
print()
preOrderTraverse(tree,0)
print()
postOrderTraverse(tree,0)