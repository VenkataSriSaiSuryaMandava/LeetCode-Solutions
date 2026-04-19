class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        maxArray = [0] * n
        minArray = [float("inf")] * n

        maxVal = 0
        for i in range(n):
            maxVal = max(maxVal, nums[i])
            maxArray[i] = maxVal

        minVal = float("inf")
        for i in range(n - 1, -1, -1):
            minVal = min(minVal, nums[i])
            minArray[i] = minVal

        for i in range(n):
            if maxArray[i] - minArray[i] <= k:
                return i

        return -1