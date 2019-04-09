from BST import *

class BST(BinarySearchTree):
    """The general APIs for binary search tree"""
    # Iterative min
    def min(self):
        return self.__min__(self.root)

    def __min__(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    def max(self):
        return self.__max__(self.root)

    def __max__(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node

    def floor(self, key):
        node = self.__floor__(self.root, key)
        return node

    def __floor__(self, node, key):
        if node is None:
            return None
        while node:
            if node.key == key:
                return node
            elif node.key > key:
                node = node.left
            else:
                tmp = node
                node = node.right
        return tmp

    def ceiling(self, key):
        node = self.__ceiling__(self.root, key)
        return node

    def __ceiling__(self, node, key):
        if node is None:
            return None
        while node:
            if node.key == key:
                return node
            elif node.key < key:
                node = node.right
            else:
                tmp = node
                node = node.left
        return tmp

    def rank(self, key):
        return self.__rank__(self.root, key)

    def __rank__(self, node, key):
        if node is None:
            return 0
        rank = 0
        while node:
            if node.key == key:
                return rank + self.__size__(node.left)
            elif node.key > key:
                node = node.left
            else:
                rank = rank + 1 + self.__size__(node.left)
                node = node.right
        return rank

    def select(self, k):
        return self.__select__(self.root, k)

    def __select__(self, node, k):
        if node is None:
            return None
        while node:
            t = self.__size__(node.left)
            if t == k:
                return node
            elif t > k:
                node = node.left
            else:
                node = node.right
                k = k - t - 1
        return node
