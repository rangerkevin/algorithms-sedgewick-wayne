"""In this implementation of max priority queue, I'll be using unsorted array, sorted array and linked list to represent a max pq"""
class MaxPQ_unsortedArray:

    def __init__(self):
        self.nums = []

    def insert(self, n):
        self.nums.append(n)

    def delMax(self):
        size = len(self.nums)
        assert (size != 0), "Priority Queue is empty!"
        maxNum = self.nums[0]
        maxIndex = 0
        for i in range(1, size):
            if self.nums[i] > maxNum:
                maxNum = self.nums[i]
                maxIndex = i
        self.swap(maxIndex, size - 1)
        return self.nums.pop()

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


class MaxPQ_sortedArray:
    
    def __init__(self):
        self.nums = []
    
    def insert(self, n):
        size = len(self.nums)
        index = 0
        number = n
        for i in range(size):
            if n < self.nums[i]:
                number = self.nums[i]
                self.nums[i] = n
                index = i
                break
            index = i
        for j in range(index + 1, size):
            tmp = self.nums[j]
            self.nums[j] = number
            number = tmp
        self.nums.append(number)

    def delMax(self):
        size = len(self.nums)
        assert (size != 0), "Empty priority queue!"
        return self.nums.pop()
    

class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MaxPQ_unsortedLinkedList:
        
    def __init__(self):
        self.head = DoublyLinkedListNode(-1)
        self.tail = self.head
        
    def insert(self, n):
        newNode = DoublyLinkedListNode(n)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def delMax(self):
        node = self.head.next
        assert (node is not None), "Empty priority queue!"
        maxNode = node
        print(maxNode.value)
        node = node.next
        while node is not None:
            if node.value > maxNode.value:
                maxNode = node
            node = node.next
        maxNode.prev.next = maxNode.next
        if maxNode.next is not None:
            maxNode.next.prev = maxNode.prev
        else:
            self.tail = maxNode.prev 
        return maxNode.value


class SinglyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class MaxPQ_sortedLinkedList:

    def __init__(self):
        self.head = SinglyLinkedListNode(-1)

    def insert(self, n):
        newNode = SinglyLinkedListNode(n)
        prev = self.head
        node = self.head.next
        while node is not None:
            if node.value > n:
                prev = node
                node = node.next
            else:
                break
        prev.next = newNode
        newNode.next = node

    def delMax(self):
        node = self.head.next
        assert (node is not None), "Empty priority queue!"

        self.head.next = self.head.next.next
        return node.value

