from BST import *
import random

class BST(BinarySearchTree):
    def delete(self, key):
        self.root = self.__delete__(self.root, key)

    # Hibbard delete plus randomized node selection
    def __delete__(self, node, key):
        if node is None:
            return None
        if node.key > key:
            node.left = self.__delete__(node.left, key)
        elif node.key < key:
            node.right = self.__delete__(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node
            # Randomly selecting its predecessor or successor as its replacement
            # Which would improve the tree's balance
            rand = random.randint(0, 1)
            node = self.__min__(t.right) if rand == 0 else self.__max__(t.left)
            if rand == 0:
                node.right = self.__deleteMin__(t.right)
                node.left = t.left
            else:
                node.left = self.__deleteMax__(t.left)
                node.right = t.right
        node.N = self.__size__(node.left) + self.__size__(node.right) + 1
        return node
