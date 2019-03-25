class MaxPQ:
    """Define a method to construct a max priority queue from an array of integers"""
    def __init__(self, nums):
        self.pq = [None] * (len(nums) + 1)
        self.pq[0] = 0
        for i in range(len(nums)):
            self.pq[i + 1] = nums[i]

    def constructor_swim(self):
        size = len(self.pq)
        for i in range(size):
            self.swim(i)

    def constructor_sink(self):
        size = len(self.pq)
        for k in range(int(size / 2), 0, -1):
            self.sink(k, size)

    def swim(self, k):
        while k > 1 and self.less(int(k / 2), k):
            self.exch(k, int(k / 2))
            k = int(k / 2)

    def sink(self, k, n):
        while 2 * k < n:
            j = 2 * k
            if j < n and self.less(j, j + 1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def print(self):
        print(self.pq)
