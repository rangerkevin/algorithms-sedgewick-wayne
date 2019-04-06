class Node:
    def __init__(self, key, value, n):
        self.key = key
        self.value = value
        self.N = n
        self.left = None
        self.right = None

class BST:
    """The general APIs for binary search tree"""
    def __init__(self):
        self.root = None

    def size(self):
        return self.__size__(self.root)

    def __size__(self, node):
        if node is None:
            return 0
        return node.N

    def get(self, key):
        return self.__get__(self.root, key)

    def __get__(self, node, key):
        if node is None:
            return None
        if node.key < key:
            return self.get(node.right, key)
        elif node.key > key:
            return self.get(node.left, key)
        else:
            return node.value

    def put(self, key, value):
        self.root = self.__put__(self.root, key, value)

    def __put__(self, node, key, value):
        if node is None:
            return Node(key, value, 1)
        if node.key < key:
            node.right = self.__put__(node.right, key, value)
        elif node.key > key:
            node.left = self.__put__(node.left, key, value)
        else:
            node.value = value
        node.N = self.__size__(node.left) + self.__size__(node.right) + 1
        return node

    def min(self):
        return self.__min__(self.root).key

    def __min__(self, node):
        if node.left is None:
            return node
        return self.__min__(node.left)

    def max(self):
        return self.__max__(self.root).key

    def __max__(self, node):
        if node.right is None:
            return node
        return self.__max__(node.right)

    def floor(self, key):
        node = self.__floor__(self.root, key)
        if node is None:
            return None
        return node.key

    def __floor__(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key > key:
            return self.__floor__(node.left, key)
        node_t = self.__floor__(node.right, key)
        if node_t is not None:
            return node_t
        return node

    def ceiling(self, key):
        node = self.__ceiling__(self.root, key)
        if node is None:
            return None
        return node.key

    def __ceiling__(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key < key:
            return self.__ceiling__(node.right, key)
        node_t = self.__ceiling__(node.left, key)
        if node_t is not None:
            return node_t
        return node

    def select(self, k):
        return self.__select__(self.root, k)

    def __select__(self, node, k):
        if node is None:
            return None
        t = self.__size__(node.left)
        if t > k:
            return self.__select__(node.left, k)
        elif t < k:
            return self.__select__(node.right, k - t - 1)
        else:
            return node

    def rank(self, key):
        return self.__rank__(self.root, key)

    def __rank__(self, node, key):
        if node is None:
            return 0
        if node.key > key:
            return self.__rank__(node.left, key)
        elif node.key < key:
            return 1 + self.__size__(node.left) + self.__rank__(node.right, key)
        else:
            return self.__size__(node.left)

    def deleteMin(self):
        self.root = self.__deleteMin__(self.root)

    def __deleteMin__(self, node):
        if node.left is None:
            return node.right
        node.left = self.__deleteMin__(node.left)
        node.N = self.__size__(node.left) + self.__size__(node.right) + 1
        return node

    def delete(self, key):
        self.root = self.__delete__(self.root, key)

    # Hibbard delete
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
            # Selecting its successor as its replacement
            # Can randomly select its predecessor or successor as its replacement
            # Which would improve the tree's balance
            node = self.__min__(t.right) 
            node.right = self.__deleteMin__(t.right)
            node.left = t.left
        node.N = self.__size__(node.left) + self.__size__(node.right) + 1
        return node
