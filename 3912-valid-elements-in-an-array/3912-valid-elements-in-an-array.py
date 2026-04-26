class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [float("-inf")] * len(nums)
        leftMax = float("-inf")

        for i in range(len(nums)):
            left[i] = leftMax
            leftMax = max(nums[i], leftMax)

        right = [float("-inf")] * len(nums)
        rightMax = float("-inf")
        
        for i in range(len(nums) - 1, -1, -1):
            right[i] = rightMax
            rightMax = max(nums[i], rightMax)

        res = []

        for i, n in enumerate(nums):
            if left[i] < n or right[i] < n:
                res.append(n)

        return res