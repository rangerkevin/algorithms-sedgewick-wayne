import random
import time
import insertionSort
import exercise_17

class Quick:

    def __init__(self, M):
        self.CUT_OFF = M
        print("Quick sorting: ")

    def sort(self, alist):
        insert = insertionSort.Insertion()
        self.sortHelper(alist, 0, len(alist) - 1, insert)

    def sortHelper(self, alist, lo, hi, insert):
        if hi <= lo:
            return 
        if hi - lo + 1 < self.CUT_OFF:
            insert.sort(alist, lo, hi)
            return
        splitPoint = self.partition(alist, lo, hi)
        self.sortHelper(alist, lo, splitPoint - 1, insert)
        self.sortHelper(alist, splitPoint + 1, hi, insert)
        
    def partition(self, alist, lo, hi):
        pivot = alist[lo]
        left, right = lo + 1, hi
        
        done = False
        while not done:
            while alist[left] < pivot:
                left += 1
                if left > hi:
                    done = True
                    break
            while alist[right] > pivot:
                right -= 1
            if left >= right:
                break
            self.exch(alist, left, right)

        self.exch(alist, lo, right)
        return right

    def exch(self, alist, i, j):
        alist[i], alist[j] = alist[j], alist[i]



n = 10000
execTime_a = []
execTime_b = []
quick = Quick(5)
quick17 = exercise_17.Quick()
for i in range(10):
    alist = []
    for i in range(n):
        alist.append(i)
    random.shuffle(alist)
    blist = list(alist)
    start = time.time()
    quick.sort(alist)
    end = time.time()
    execTime_a.append(end - start)
    start = time.time()
    quick17.sort(blist)
    end = time.time()
    execTime_b.append(end - start)
    #print(alist)
    
print("Execution time average for quick sort with insertion sort: " + str(sum(execTime_a) / len(execTime_a)) + " seconds.")
print("Execution time average for quick sort: " + str(sum(execTime_b) / len(execTime_b)) + " seconds.")

