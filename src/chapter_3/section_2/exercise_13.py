from BST import *

class BST(BinarySearchTree):
    """The general APIs for binary search tree"""
    # Iterative get
    def get(self, key):
        return self.__get__(self.root, key)

    def __get__(self, node, key):
        while node is not None:
            if node.key == key:
                return node.value
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        return None

    # Iterative put
    def put(self, key, value):
        self.root = self.__put__(self.root, key, value)

    def __put__(self, node, key, value):
        root = node
        if node is None:
            return Node(key, value, 1)
        while node is not None:
            if node.key == key:
                node.value = value
                break
            elif node.key > key:
                t = node
                node = node.left
            else:
                t = node
                node = node.right
        if t.key > key:
            t.left = Node(key, value, 1)
        else:
            t.right = Node(key, value, 1)
        
        # Traverse the path and increment the N
        node = root
        while node.key != key:
            node.N += 1
            if node.key > key:
                node = node.left
            else:
                node = node.right
        # Always return the original root node
        return root
        
   
