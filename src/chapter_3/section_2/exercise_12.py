from BST import *

class Node(Node):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST(BinarySearchTree):
    """The general APIs for binary search tree"""
    def __init__(self):
        BinarySearchTree.__init__(self)
        self.capacity = 0

    def size(self):
        return self.capacity

    def __put__(self, node, key, value):
        if node is None:
            self.capacity += 1
            return Node(key, value)
        if node.key < key:
            node.right = self.__put__(node.right, key, value)
        elif node.key > key:
            node.left = self.__put__(node.left, key, value)
        else:
            node.value = value
        return node

    def __deleteMin__(self, node):
        if node is None:
            return None
        if node.left is None:
            self.capacity -= 1
            return node.right
        node.left = self.__deleteMin__(node.left)
        return node

    def __deleteMax__(self, node):
        if node is None:
            return None
        if node.right is None:
            self.capacity -= 1
            return node.left
        node.right = self.__deleteMax__(node.right)
        return node

    # Hibbard delete
    def __delete__(self, node, key):
        if node is None:
            return None
        if node.key > key:
            node.left = self.__delete__(node.left, key)
        elif node.key < key:
            node.right = self.__delete__(node.right, key)
        else:
            self.capacity -= 1
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node
            # Selecting its successor as its replacement
            # Can randomly select its predecessor or successor as its replacement
            # Which would improve the tree's balance
            node = self.__min__(t.right) 
            node.right = self.__deleteMin__(t.right)
            node.left = t.left
        return node

    def height(self):
        return self.__height__(self.root)

    def __height__(self, node):
        if node is None:
            return 0
        height_left = self.__height__(node.left)
        height_right = self.__height__(node.right)

        return max(height_left, height_right) + 1
