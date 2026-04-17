class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(num):
            revNum = 0

            while num:
                digit = num % 10
                revNum = revNum * 10 + digit
                num = num // 10
            
            return revNum
        
        res = float("inf")
        revMap = {}

        for i, num in enumerate(nums):
            if num in revMap:
                res = min(res, i - revMap[num])
            
            revNum = reverse(num)
            revMap[revNum] = i
        
        return res if res != float("inf") else -1