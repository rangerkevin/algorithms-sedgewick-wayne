import random

class QuickBest:

    def __init__(self, n):
        self.n = n
        print("Quick sorting: ")

    def best(self):
        alist = [None] * self.n
        for i in range(n):
            alist[i] = i
        self.best_helper(alist, 0, self.n - 1)
        return alist

    def best_helper(self, alist, lo, hi):
        # Base case, no duplicate elements
        for i in range(lo, hi + 1):
            assert alist[i] == i
        if hi <= lo:
            return 
        mid = int(lo + (hi - lo) / 2)
        self.best_helper(alist, lo, mid - 1)
        self.best_helper(alist, mid + 1, hi)

        self.exch(alist, lo, mid)
        
    def exch(self, alist, i, j):
        alist[i], alist[j] = alist[j], alist[i]
    


n = 7
best = QuickBest(n)
alist = best.best()
print(alist)
