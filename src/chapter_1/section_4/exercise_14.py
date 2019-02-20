class FourSum:
    """Exercise 1.4.14 of Algorithms Fourth Edition"""

    def __init__(self, nums, N, target):
        self.nums = sorted(nums)
        self.N = N
        self.target = target

    def getResults(self):
        results = []
        combo = []
        index = 0
        N = self.N
        target = self.target
        self.helper(N, index, combo, results, target)
        return results
            
    def helper(self, N, index, combo, results, target):
        if N > 2:
            for i in range(index, len(self.nums) - N + 1):
                if i > 0 and self.nums[i] == self.nums[i - 1]:
                    continue
                item = self.nums[i]
                self.helper(N - 1, i + 1, combo + [item], results, target - item)
        else:
            self.get2Sum(index, len(self.nums) - 1, combo, results, target)

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


nums = [-5, -3, -1, 0, 1, 2, 3, 3, 4, 5, 8, 8]
test = FourSum(nums, 4, 0)
print(test.getResults())
