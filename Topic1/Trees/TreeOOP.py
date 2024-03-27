class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    def add(self, data):
        newNode = Node(data)
        current = self.root
        positionFound = False
        if self.isEmpty():
            self.root = newNode
        else:
            while not positionFound:
                if newNode.data >= current.data:
                    if current.right == None:
                        current.right = newNode
                        positionFound = True
                    else:
                        current = current.right
                else:
                    if current.left == None:
                        current.left = newNode
                        positionFound = True
                    else:
                        current = current.left

    def inOrderTraverse(self):
        if self.isEmpty():
            print("Tree is empty")
        else:
            def traverse(current):
                if current.left != None:
                    traverse(current.left)
                print(current.data)
                if current.right != None:
                    traverse(current.right)
            traverse(self.root)

    def postOrderTraverse(self):
        if self.isEmpty():
            print("Tree is empty")
        else:
            def traverse(current):
                if current.left != None:
                    traverse(current.left)
                if current.right != None:
                    traverse(current.right)
                print(current.data)
            traverse(self.root)

    def preOrderTraverse(self):
        if self.isEmpty():
            print("Tree is empty")
        else:
            def traverse(current):
                print(current.data)
                if current.left != None:
                    traverse(current.left)
                if current.right != None:
                    traverse(current.right)
            traverse(self.root)

tree = Tree()
tree.add(1)
tree.add(5)
tree.add(21)
tree.add(3)
tree.add(12)
tree.add(6)
tree.add(18)
tree.add(4)
tree.add(32)

tree.inOrderTraverse()
print()
tree.preOrderTraverse()
print()
tree.postOrderTraverse()