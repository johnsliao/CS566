# John Liao
# HW 2-1

class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data, node):
        if data < node.data:
            if node.left is not None:
                self.insert(data, node.left)
            else:
                node.left = Node(data)
                node.left.parent = node

        if data > node.data:
            if node.right is not None:
                self.insert(data, node.right)
            else:
                node.right = Node(data)
                node.right.parent = node

    def find(self, data, node):
        # Recursive find
        if node.data is data:
            return node

        if node.left is not None:
            return self.find(data, node.left)
        if node.right is not None:
            return self.find(data, node.right)

        return None

    def iterative_find(self, data):
        # Iterative find
        node = self.root

        while node is not None:
            if node.data is data:
                return node

            if data < node.data:
                node = node.left
            else:
                node = node.right

        return None

binarySearchTree = BinarySearchTree(1)

binarySearchTree.insert(2, binarySearchTree.root)
binarySearchTree.insert(3, binarySearchTree.root)
binarySearchTree.insert(4, binarySearchTree.root)
binarySearchTree.insert(5, binarySearchTree.root)
binarySearchTree.insert(6, binarySearchTree.root)

print 'Recursive Search'
print binarySearchTree.find(4, binarySearchTree.root) is not None # search for 4
print binarySearchTree.find(10, binarySearchTree.root) is not None # search for 10
print

print 'Iterative Search'
print binarySearchTree.iterative_find(4) is not None # search for 4
print binarySearchTree.iterative_find(99) is not None # search for 99

