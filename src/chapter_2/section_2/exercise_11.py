import random
import time
import insertionSort

class MergeSort:

    def __init__(self, cut_off):
        self.CUT_OFF = cut_off
        print("Merge sorting: ")

    def merge(self, alist, aux, lo, mid, hi):
        i, j = lo, mid + 1
        
        for k in range(lo, hi + 1):
            if i > mid:
                aux[k] = alist[j]
                j += 1
            elif j > hi:
                aux[k] = alist[i]
                i += 1
            elif alist[i] < alist[j]:
                aux[k] = alist[i]
                i += 1
            else:
                aux[k] = alist[j]
                j += 1

    def sort(self, alist):
        # Improvement 3: Create the aux array here and pass it into the sort_helper method
        # This eliminates the copy to aux array during merge
        # 10~12% improvement is seen when n equals 10000
        aux = list(alist)
        insert = insertionSort.Insertion()
        self.sort_helper(aux, alist, 0, len(alist) - 1, insert)

    def sort_helper(self, alist, aux, lo, hi, insert):
        if hi <= lo:
            return
        if hi - lo + 1 < self.CUT_OFF:
            # Improment 1: Apply insertion sort if subarray is shorter than 15 items
            # Only 1~2% improvement is seen when n equals 10000 and cut_off equals 15
            insert.sort(aux, lo, hi)
        else:
            mid = int((lo + hi) / 2)
            self.sort_helper(aux, alist, lo, mid, insert)
            self.sort_helper(aux, alist, mid + 1, hi, insert)
            if alist[mid] <= alist[mid + 1]:
                # Improvement 2: return when last item of first subarray is less than or equal to the first item of second subarray, so that merge can be skipped
                return
            self.merge(alist, aux, lo, mid, hi)


n = 10000
execTime = []
for i in range(10):
    alist = []
    for i in range(n):
        alist.append(random.randint(0, n))
    start = time.time()
    test = MergeSort(15)
    test.sort(alist)
    end = time.time()
    execTime.append(end - start)
    #print(alist)

print("Execution time average: " + str(sum(execTime) / len(execTime)) + " seconds.")

   
