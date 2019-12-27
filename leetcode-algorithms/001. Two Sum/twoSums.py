class Solution:
    def twoSums(self, nums, target):
        res = {}
        for i, num in enumerate(nums):
            if num in res:
                return (res[num], i)
            else:
                res[target - num] = i


A = [1, 3, 5, 7, 4, 9, 10, 13]
target = 7

X = Solution()
print(X.twoSums(A, target))
