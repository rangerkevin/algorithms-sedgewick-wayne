import random
import time
import sys
import quickSort

class Quick:

    def __init__(self):
        print("Quick sorting: ")

    def sortWithSentinels(self, alist):
        maxItem = alist[0]
        maxIndex = 0
        for i in range(len(alist)):
            if alist[i] > maxItem:
                maxItem = alist[i]
                maxIndex = i
        self.exch(alist, maxIndex, len(alist) - 1)

        self.sortHelperWithSentinels(alist, 0, len(alist) - 1)

    def sort(self, alist):
        self.sortHelper(alist, 0, len(alist) - 1)

    def sortHelper(self, alist, lo, hi):
        if hi <= lo:
            return 
        splitPoint = self.partition(alist, lo, hi)
        self.sortHelper(alist, lo, splitPoint - 1)
        self.sortHelper(alist, splitPoint + 1, hi)
        
    def sortHelperWithSentinels(self, alist, lo, hi):
        if hi <= lo:
            return 
        splitPoint = self.partitionWithSentinels(alist, lo, hi)
        self.sortHelperWithSentinels(alist, lo, splitPoint - 1)
        self.sortHelperWithSentinels(alist, splitPoint + 1, hi)

    def partitionWithSentinels(self, alist, lo, hi):
        pivot = alist[lo]
        left, right = lo + 1, hi
        
        while True:
            # No boundary check with the help of sentinels
            # Thus the running time is the smallest among the three
            while alist[left] < pivot:
                left += 1
            while alist[right] > pivot:
                right -= 1
            if left >= right:
                break
            self.exch(alist, left, right)

        self.exch(alist, lo, right)
        return right

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
execTime_c = []
quick = Quick()
pquick = quickSort.Quick
for i in range(10):
    alist = []
    for i in range(n):
        alist.append(i)
    #print(alist)
    random.shuffle(alist)
    blist = list(alist)
    clist = list(alist)
    start = time.time()
    quick.sort(alist)
    end = time.time()
    execTime_a.append(end - start)
    start = time.time()
    quick.sortWithSentinels(blist)
    end = time.time()
    execTime_b.append(end - start)
    start = time.time()
    pquick.sort(clist)
    end = time.time()
    execTime_c.append(end - start)
    #print(alist)
    
print("Execution time average for normal quick sort: " + str(sum(execTime_a) / len(execTime_a)) + " seconds.")
print("Execution time average for quick sort with sentinels: " + str(sum(execTime_b) / len(execTime_b)) + " seconds.")
print("Execution time average for python quick sort: " + str(sum(execTime_c) / len(execTime_c)) + " seconds.")
