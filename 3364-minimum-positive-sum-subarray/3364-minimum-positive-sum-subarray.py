class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = float("inf")
        n = len(nums)

        for i in range(n):
            curSum = 0

            for j in range(i, n):
                curSum += nums[j]

                if l <= j - i + 1 <= r and curSum > 0:
                    res = min(res, curSum)
        
        return res if res != float("inf") else -1