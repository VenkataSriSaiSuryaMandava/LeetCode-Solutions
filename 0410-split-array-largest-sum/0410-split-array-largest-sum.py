class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(largest):
            subarrays = 1
            curSum = 0

            for n in nums:
                curSum += n

                if curSum > largest:
                    subarrays += 1
                    curSum = n
            
            return subarrays <= k

        l = max(nums)
        r = sum(nums)
        res = sum(nums)
        
        while l <= r:
            m = (l + r) // 2

            if canSplit(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res