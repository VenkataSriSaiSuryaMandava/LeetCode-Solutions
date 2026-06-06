class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        leftSum = [0] * n
        rightSum = [0] * n

        prefix = 0
        for i in range(n):
            leftSum[i] = prefix
            prefix += nums[i]

        suffix = 0
        for i in range(n - 1, -1, -1):
            rightSum[i] = suffix
            suffix += nums[i]
        
        res = []
        for i in range(n):
            res.append(abs(leftSum[i] - rightSum[i]))
        
        return res