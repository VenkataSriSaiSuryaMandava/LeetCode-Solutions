class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        res = float("inf")

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            if nums[m] <= nums[l]:
                r = m - 1
            else:
                l = m + 1
        
        return res