class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        res = float('-inf')

        l = 0
        for r in range(len(nums)):
            total += nums[r]

            if (r - l + 1) == k:
                res = max(res, float(total / k))
                total -= nums[l]
                l += 1
        
        return res