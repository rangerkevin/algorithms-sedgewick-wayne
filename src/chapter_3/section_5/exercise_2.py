class SequentialSearchSET:

    def __init__(self):
        self.head = None
        self.capacity = 0

    class Node:
        def __init__(self, key, next = None):
            self.key = key
            self.next = next

    def contains(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return True
            node = node.next
        return False

    def add(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return
            node = node.next
        newNode = Node(key, self.head)
        self.head = newNode
        self.capacity += 1

    def remove(self, key):
        node = self.head
        prev = node
        if node.key == key:
            self.head = self.head.next
            self.capacity -= 1
            return
        while node != None:
            if node.key == key:
                prev.next = node.next
                self.capacity -= 1
                return
            prev = node
            node = node.next

    def size(self):
        return self.capacity

    def keys(self):
        # Return a list of keys
        node = self.head
        keys = []
        while node != None:
            keys.append(node.key)
            node = node.next
        return keys

