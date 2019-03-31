class SequentialSearchST:

    def __init__(self):
        self.head = None
        self.capacity = 0

    class Node:
        def __init__(self, key, value, next = None):
            self.key = key
            self.value = value
            self.next = next

    def get(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def put(self, key, value):
        node = self.head
        while node != None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        newNode = self.Node(key, value, self.head)
        self.head = newNode
        self.capacity += 1

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

    def delete(self, key):
        node = self.head
        prev = node
        if node.key == key:
            self.head = self.head.next
            self.capacity -= 1
            return self.head.value
        while node != None:
            if node.key == key:
                prev.next = node.next
                self.capacity -= 1
                return node.value
            prev = node
            node = node.next
            

st = SequentialSearchST()
print(st.get(1))
print(st.put(1, 'a'))
print(st.put(2, 'b'))
print(st.put(3, 'c'))
print(st.size())
print(st.keys())
print(st.delete(4))
print(st.delete(2))
print(st.size())
