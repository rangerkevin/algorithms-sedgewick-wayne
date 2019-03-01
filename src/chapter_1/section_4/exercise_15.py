class ThreeSum:
    """Exercise 1.4.15 of Algorithms Fourth Edition"""

    def __init__(self, nums, target):
        self.nums = sorted(nums)
        self.target = target

    def getResults(self):
        results = []
        combo = []
        for i in range(len(self.nums) - 2):
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue
            item = self.nums[i]
            self.get2Sum(i + 1, len(self.nums) - 1, combo + [item], results, target - item)
            
    def get2Sum(self, start, end, combo, results, target):
        while start < end:
            sum = self.nums[start] + self.nums[end]
            if sum == target:
                results.append(list(combo + [self.nums[start], self.nums[end]]))
                start += 1
                end -= 1
                while start < end and self.nums[start] == self.nums[start - 1]:
                    start += 1
                while start < end and self.nums[end] == self.nums[end + 1]:
                    end -= 1
            elif sum > target:
                end -= 1
            else:
                start += 1
    


