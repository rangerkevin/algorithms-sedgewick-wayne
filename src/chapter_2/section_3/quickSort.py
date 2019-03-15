import random

class Quick:

    def __init__(self):
        print("Quick sorting: ")

    def sort(self, alist):
        self.sort_helper(alist, 0, len(alist) - 1)

    def sort_helper(self, alist, lo, hi):
        if hi <= lo:
            return 
        splitPoint = self.partition(alist, lo, hi)
        self.sort_helper(alist, lo, splitPoint)
        self.sort_helper(alist, splitPoint + 1, hi)

    def partition(self, alist, lo, hi):
        pivot = alist[lo]
        left, right = lo + 1, hi
        
        while left <= right:
            while left <= right and alist[left] < pivot:
                left += 1

            while left <= right and alist[right] > pivot:
                right -= 1

            if left <= right:
                alist[left], alist[right] = alist[right], alist[left]

        alist[lo], alist[right] = alist[right], alist[lo]
        return right


n = 100
alist = []
for i in range(n):
    alist.append(i)
random.shuffle(alist)
print(alist)
Quick = Quick()
Quick.sort(alist)
print(alist)
