class Node:
    def __init__(self, key, value, n):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    """The general APIs for binary search tree"""
    def __init__(self):
        self.root = None
        self.capacity = 0

    def size(self):
        return self.capacity

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
            self.capacity += 1
            return Node(key, value, 1)
        if node.key < key:
            node.right = self.__put__(node.right, key, value)
        elif node.key > key:
            node.left = self.__put__(node.left, key, value)
        else:
            node.value = value
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

    def deleteMin(self):
        self.root = self.__deleteMin__(self.root)

    def __deleteMin__(self, node):
        if node is None:
            return None
        if node.left is None:
            self.capacity -= 1
            return node.right
        node.left = self.__deleteMin__(node.left)
        return node

    def deleteMax(self):
        self.root = self.__deleteMax__(self.root)

    def __deleteMax__(self, node):
        if node is None:
            return None
        if node.right is None:
            self.capacity -= 1
            return node.left
        node.right = self.__deleteMax__(node.right)
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
