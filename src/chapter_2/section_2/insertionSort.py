import random
import time

class Insertion:

    def __init__(self):
        print("Insertion sorting: ")

    def sort(self, alist, start, end):
        n = end - start + 1
        for i in range(start, end + 1):
            j = i
            while j > start:
                if self.less(alist[j], alist[j - 1]):
                    self.exch(alist, j, j - 1)
                j -= 1

    def less(self, a, b):
        return a < b

    def exch(self, alist, i, j):
        alist[i], alist[j] = alist[j], alist[i]

n = 20
alist = []
for i in range(n):
    alist.append(random.randint(0, n))
start = time.time()
test = Insertion()
test.sort(alist, 0, len(alist) - 1)
end = time.time()
print("Execution time: " + str(end - start) + " seconds.")
print(alist)

