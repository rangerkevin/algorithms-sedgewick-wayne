class BinarySearch:
    """Exercise 1.4.10 of Algorithms Fourth Edition"""

    def __init__(self, nums, target):
        self.nums = sorted(nums)
        self.target = target

    def findFirstIndex(self):
        start, end = 0, len(self.nums) - 1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if self.nums[mid] >= self.target:
                end = mid 
            else:
                start = mid

        if self.nums[start] == self.target:
            return start
        if self.nums[end] == self.target:
            return end


nums = [1,2,3,3,5,6,7,8]
target = 3
bs = BinarySearch(nums, target)
print(bs.findFirstIndex())

