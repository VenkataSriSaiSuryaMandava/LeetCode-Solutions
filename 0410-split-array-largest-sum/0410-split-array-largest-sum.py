class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(largest):
            curSum = 0
            subArrays = 1

            for n in nums:
                curSum += n
                if curSum > largest:
                    subArrays += 1
                    curSum = n
            
            return subArrays <= k
        
        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            m = (l + r) // 2

            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res