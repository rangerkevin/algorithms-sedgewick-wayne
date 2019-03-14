import random
import time

class MergeSort:

    def __init__(self):
        print("Merge sorting: ")

    def merge(self, alist, lo, mid, hi, aux):
        i, j = lo, mid + 1
        
        # We still need to assign the values to this aux array since the values here in alist are changing after each merge
        for k in range(lo, hi + 1):
            aux[k] = alist[k]

        for k in range(lo, hi + 1):
            if i > mid:
                alist[k] = aux[j]
                j += 1
            elif j > hi:
                alist[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                alist[k] = aux[i]
                i += 1
            else:
                alist[k] = aux[j]
                j += 1

    def sort(self, alist):
        # Create the aux array here and pass it into the sort_helper method
        # This avoids creating the same aux array every time in sort_helper method
        aux = [None] * len(alist)
        self.sort_helper(alist, 0, len(alist) - 1, aux)

    def sort_helper(self, alist, lo, hi, aux):
        if hi <= lo:
            return
        mid = int((lo + hi) / 2)
        self.sort_helper(alist, lo, mid, aux)
        self.sort_helper(alist, mid + 1, hi, aux)
        self.merge(alist, lo, mid, hi, aux)


n = 10
alist = []
for i in range(n):
    alist.append(random.randint(0, n))
#alist = [3,2,1,0]
start = time.time()
test = MergeSort()
test.sort(alist)
end = time.time()
print(alist)
print("Execution time: " + str(end - start) + " seconds.")

   
