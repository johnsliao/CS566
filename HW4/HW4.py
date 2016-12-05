# John Liao
# CS 566, HW 4
# Email: jsmiao@bu.edu
# BU ID: U47-74-9883

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
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
        if node.data is data:
            return node

        if node.left is not None:
            return self.find(data, node.left)
        if node.right is not None:
            return self.find(data, node.right)

        return None

    def print_in_order_traversal(self, node):
        if node.left is not None:
            self.print_in_order_traversal(node.left)

        print node.data

        if node.right is not None:
            self.print_in_order_traversal(node.right)

if __name__ == '__main__':
    # Set number of values, range
    n = 10  # number of values
    i = 1   # lower bound, inclusive
    j = 50  # upper bound, inclusive
    array = []

    print 'n=%s, i=%s, j=%s' % (n, i, j)

    # Randomly generate distinct values to be stored in BST
    assert n <= j-i+1, 'Cannot generate distinct values for this range.'

    while len(array) < n:
        value = random.randint(i, j)

        if value in array:
            continue

        array.append(value)

    print 'Array:', array

    # Store into BST
    for i, value in enumerate(array):
        if i == 0:
            binarySearchTree = BinarySearchTree(value)
            continue

        binarySearchTree.insert(value, binarySearchTree.root)

    # Print BST (in-order traversal)
    print
    print 'In-Order Traversal'
    binarySearchTree.print_in_order_traversal(binarySearchTree.root)