class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        maxArray = [float("-inf")] * n
        minArray = [float("inf")] * n

        curMax = float("-inf")
        curMin = float("inf")

        for i in range(n):
            curMax = max(curMax, nums[i])
            maxArray[i] = curMax

        for i in range(n - 1, -1, -1):
            curMin = min(curMin, nums[i])
            minArray[i] = curMin
        
        for i in range(n):
            if maxArray[i] - minArray[i] <= k:
                return i
        
        return -1