from BST import *

class BST(BinarySearchTree):
    def height(self):
        return self.__height__(self.root)

    def __height__(self, node):
        if node is None:
            return 0
        height_left = self.__height__(node.left)
        height_right = self.__height__(node.right)

        return max(height_left, height_right) + 1
