class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(largest):
            subArrays = 1
            curSum = 0

            for n in nums:
                curSum += n

                if curSum > largest:
                    curSum = n
                    subArrays += 1
            
            return subArrays <= k
        
        l = max(nums)
        r = sum(nums)
        res = sum(nums)

        while l <= r:
            m = (l + r) // 2

            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res